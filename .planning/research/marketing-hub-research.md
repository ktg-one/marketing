# AI Marketing Hub — Implementation Research

**Researched:** 2026-05-26
**Confidence:** HIGH (official Claude Code docs verified, live plugin inspection, Composio confirmed active)

---

## 1. Implementation Approach Recommendation

Build `/hub` as a **project-local skill at `.claude/skills/hub/SKILL.md`** (not as a plugin). Rationale:

- The hub is a workflow coordinator for this vault only, not a distributable product
- Project skills at `.claude/skills/` load with no namespace — the command stays `/hub` not `/ai-marketing-hub:hub`
- The existing plugins (`claude-blog-main`, `banana-claude`) are already installed project-wide; no cross-plugin calling needed
- Simpler to iterate: edit `SKILL.md` and run `/reload-plugins` with no install step

The skill should be structured as an **orchestration script** — it reads the post file, then walks through each pipeline step sequentially, using Claude's tools (Skill, MCP calls, Bash, Read/Write) to execute each step and pass output forward.

---

## 2. Skill Invocation Patterns

### Can `/hub` call `/blog repurpose` directly?

**No. A skill cannot invoke another skill by typing a slash command.** Claude Code does not have a mechanism for one skill to "call" `/command-name` programmatically the way you would call a function.

What actually happens: when a skill's `SKILL.md` content loads into context, it becomes instructions. The skill can **instruct Claude to invoke another skill by name** and Claude will use the `Skill` tool to do it. This is the only cross-skill invocation mechanism.

**Verified pattern from official docs:**

> "A few built-in commands are also available through the Skill tool, including `/init`, `/review`, and `/security-review`."

> "To restrict Claude's skill access... `Skill(commit)` for exact match, `Skill(name *)` for prefix match."

So the `Skill` tool is a real Claude Code tool that loads a skill. Your hub SKILL.md can instruct Claude to call `Skill("blog-repurpose")` with specific arguments, and Claude will execute it.

**Confirmed: Skills from other plugins are accessible via their name as registered.** Plugin skills register under a namespace only when invoked by a human via `/`. When Claude uses the `Skill` tool, it references by skill `name` in frontmatter. Check each plugin skill's frontmatter `name` field — `blog-repurpose` has `name: blog-repurpose`, `banana` has `name: banana`.

**The correct hub pattern:**

```markdown
## Pipeline Step 2: Repurpose

Invoke the `blog-repurpose` skill with the post file path as the argument.
Instruct it to generate all platforms (option 6). Wait for completion and
confirm outputs were saved to repurposed/.
```

This tells Claude to use the Skill tool with `blog-repurpose`. Claude loads that skill's SKILL.md into context and executes the workflow.

**Critical constraint from docs:** Subagents cannot spawn other subagents. If you use `context: fork` for isolation, the forked subagent cannot further delegate. Keep the hub running in the main session context (no `context: fork` on the hub skill itself) so it can chain multiple skill invocations.

### Sequential Pipeline Pattern

The correct pattern for multi-step sequential pipelines in a skill is **inline execution with explicit handoff state** — not separate subagents for each step.

Recommended hub structure:

```
Step 1: Read + validate the post file
Step 2: Invoke blog-repurpose skill → wait → confirm repurposed/ files exist
Step 3: Invoke banana skill → generate hero image + platform crops (see image section)
Step 4: Invoke blog-geo skill → confirm GEO score output
Step 5: Invoke blog-seo-check skill → confirm SEO checklist output
Step 6: Invoke blog-schema skill → confirm JSON-LD output
Step 7: Publish via Composio MCP tools (see Composio section)
Step 8: Report pipeline summary
```

Each step should have an explicit **verify** gate: check the output file exists or the MCP call returned success before moving to the next step. If a step fails, the hub should surface which step failed and what was left incomplete, rather than silently continuing.

Using `context: fork` (subagent isolation) is appropriate only for steps that are expensive and would flood the main context with file content — particularly the repurpose step which generates 5 full-length documents. Consider wrapping steps 2-6 in forked subagents if context pollution becomes a problem in practice.

---

## 3. Composio Integration Pattern

### What's confirmed available

From `wiki/hot.md` (live discovery during an active session):

> **Composio connections available**: cursor, discord, elevenlabs, facebook, figma, github, gmail, googlecalendar, googledrive, googlesheets, hugging_face, **linkedin**, mem0, **reddit**, slack, telegram, **vercel**, youtube

All three publish channels (Reddit, LinkedIn, Vercel) are connected. Authentication is already done.

### How Composio is wired

Composio is NOT in the current `gateway.py`. It was used interactively in the session as MCP tools, likely via a separate `.mcp.json` in the project or via the `claude mcp add` route. The hot cache confirms it works.

To find the active Composio server config:

```powershell
cat "C:/Users/kevin/Pictures/ktg-one/.mcp.json" 2>$null
claude mcp list
```

### Tool naming

Composio MCP tools follow a natural-language description pattern, not constants like `REDDIT_CREATE_POST`. From official Composio docs:

| Platform | Tool description |
|----------|-----------------|
| Reddit | "Create a Reddit post" — creates text or link post on a subreddit, optional flair |
| LinkedIn | "Create a LinkedIn post" — creates post for authenticated user or organization |
| LinkedIn | "Create article or URL share" — creates article or URL share via UGC Posts API |
| Vercel | Deploy/hosting tools |

**The invocation pattern** is natural language to Claude, which then calls the MCP tool:

```
"Post the Reddit variant to r/ClaudeAI. Use the text from repurposed/{slug}-reddit-post.md.
Title: [extracted title from the file]. Include the Vercel URL at the end."
```

Claude routes this to the correct Composio MCP tool automatically. You do not need to hardcode tool IDs in the hub skill.

### Confirmed publish order from hot cache

The established publish order for this vault is:

1. Deploy to Vercel → capture canonical URL
2. Substitute URL into Reddit and LinkedIn variants
3. Fire Reddit via Composio
4. Fire LinkedIn via Composio

The hub skill should replicate this order. The Vercel step likely uses Composio's Vercel toolkit or a separate deploy command — confirm with `claude mcp list` which Vercel tools are available.

### Green-light constraint

**CRITICAL from memory/feedback:** Always get explicit per-post green-light before firing any social send. The hub skill must pause after generating all variants and images, display a summary for review, and ask "Ready to publish? (yes/no)" before triggering any Composio calls.

Build this as an explicit checkpoint step in the skill:

```
## Step 7: Pre-Publish Review

Before publishing, show:
- List of files generated in repurposed/
- Image paths generated
- Target platforms and subreddits
- Post the question: "Ready to publish all channels? Respond YES to continue, or
  tell me which channels to skip."

Wait for user confirmation. Do NOT proceed until explicit YES received.
```

---

## 4. Image Pipeline Approach

### How banana handles sizing

From `banana/SKILL.md` inspection:

Banana does NOT accept a "generate all platform crops" single call. Each generation is **one API call, one aspect ratio**. The `set_aspect_ratio` tool must be called before each `gemini_generate_image` call.

Platform sizing table from the skill:

| Platform | Ratio | Banana call |
|----------|-------|-------------|
| Blog hero / YouTube thumb | 16:9 | `set_aspect_ratio(16:9)` then generate |
| Social post / avatar | 1:1 | `set_aspect_ratio(1:1)` then generate |
| Story / Reel | 9:16 | `set_aspect_ratio(9:16)` then generate |
| LinkedIn portrait | 4:5 | `set_aspect_ratio(4:5)` then generate |

For a full hub pipeline, the image step should generate 2-3 variants:

1. **Hero image** at 16:9 (blog + LinkedIn share)
2. **Square crop** at 1:1 (Twitter/X, general social)
3. Optionally **Story crop** at 9:16 (if Instagram Reels are in scope)

The banana skill uses `gemini-3.1-flash-image-preview` as default at 2K resolution. For hub automation, 2K is appropriate (not 4K, which is for print).

### ImageMagick crop fallback

The banana skill includes a post-processing pipeline using ImageMagick (`magick` v7 or `convert` v6). For the hub, you can generate one base 16:9 image and then use ImageMagick to crop to other ratios rather than making 3 separate Gemini API calls:

```bash
# From banana SKILL.md post-processing section:
magick hero.png -resize 1080x1080^ -gravity center -extent 1080x1080 square.png
magick hero.png -resize 1080x1920^ -gravity center -extent 1080x1920 story.png
```

This saves 2 Gemini API calls per publish run. Check ImageMagick availability first:

```bash
which magick || which convert || echo "ImageMagick not installed"
```

### Prompt construction for hub images

Banana requires the creative director pipeline: it cannot receive raw text. For hub automation, the skill should extract the post's core subject/angle and construct the brief programmatically:

```
From the post title and first 2 paragraphs, construct a banana image brief:
- Mode: Editorial (magazine-style for blog/LinkedIn)
- Subject: [derived from post topic]
- Call set_aspect_ratio(16:9) then invoke the banana skill with this brief
- Save as: images/{slug}-hero.png
```

The banana skill's domain routing (Cinema/Editorial/Product/etc.) handles the rest once given a well-formed brief.

---

## 5. Plugin Structure for Hub

The hub is **not** built inside an existing plugin. It lives at:

```
.claude/skills/hub/
  SKILL.md          ← orchestration logic + pipeline steps
  references/
    pipeline.md     ← step-by-step pipeline reference (if SKILL.md exceeds 500 lines)
```

`SKILL.md` frontmatter:

```yaml
---
name: hub
description: >
  Full marketing pipeline. Takes a written blog post and runs: repurpose for all
  platforms, image generation, GEO optimisation, SEO check, schema generation,
  then publishes to Reddit/LinkedIn/Vercel via Composio. Use when user says
  "run hub", "/hub", "publish this post", "full pipeline".
disable-model-invocation: true
argument-hint: "<post-file-path>"
allowed-tools: Read Write Edit Bash Skill
---
```

`disable-model-invocation: true` because the hub has real side effects (publishes to social). It must only fire when explicitly invoked.

The corresponding command file at `.claude/commands/hub.md` is optional — the skill at `.claude/skills/hub/SKILL.md` is sufficient and creates `/hub` automatically.

---

## 6. Gotchas and Constraints

### Skill context accumulation

From official docs: "When you or Claude invoke a skill, the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session."

If hub invokes blog-repurpose, then blog-geo, then blog-seo-check, then blog-schema sequentially, all four SKILL.md files accumulate in context. The blog plugin's SKILL.md files are large (blog-repurpose is 235 lines). By step 6, context will be significantly populated.

**Mitigation:** Use `context: fork` for the heaviest steps (repurpose, geo). Forked skills run in an isolated context and return only a summary to the main conversation. This keeps the hub's main context clean for the publish step where Composio tools need full context.

### Banana generates one image per call

No batch parameter exists. Each `gemini_generate_image` call produces one image. The hub must loop explicitly for each crop. Rate limits apply: ~5-15 RPM on free tier. If running multiple crops, add brief waits or catch 429s.

### blog-repurpose asks the user which platforms

Step 2 of blog-repurpose SKILL.md is an interactive question: "which platforms to generate for?" For hub automation, the hub skill must pre-answer this by including "all platforms (option 6)" in its instructions to the skill, so Claude routes around the interactive prompt.

From the skill: "If the user specifies a platform directly... skip this step and generate for that platform only." So the hub should pass the argument: invoke blog-repurpose with "all platforms" as the argument.

### Composio MCP server location

Composio is not currently mounted in `gateway.py`. It was accessed in the prior session but its config location is unclear from inspection. Before implementing the publish step, run `claude mcp list` to identify the server name and confirm which tools are exposed. The tool names will be natural-language descriptions, not constant names.

### n8n auth is broken

From hot.md: "n8n auth still failing on `list_workflows`". Do not route any hub publish steps through n8n. Composio is the confirmed route.

### No `/hub` command file needed

A `commands/hub.md` file and a `skills/hub/SKILL.md` file both create `/hub`. If both exist and share the same name, the skill takes precedence. Only create the SKILL.md — do not create a separate commands file.

### Windows PowerShell shell

This project runs on Windows with PowerShell. Any `!` shell injection in SKILL.md needs `shell: powershell` in frontmatter, or use Bash tool calls instead. The banana skill's ImageMagick commands use `magick` — confirm it is in PATH on Windows before relying on it.

---

## Sources

- Claude Code official docs: https://code.claude.com/docs/en/slash-commands (skills, plugin invocation, frontmatter reference)
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Composio MCP Reddit: https://composio.dev/toolkits/reddit/framework/claude-code
- Composio MCP LinkedIn: https://composio.dev/toolkits/linkedin/framework/claude-code
- Live plugin inspection: `.claude/plugins/claude-blog-main/skills/blog-repurpose/SKILL.md`
- Live plugin inspection: `.claude/plugins/banana-claude/skills/banana/SKILL.md`
- Live session context: `wiki/hot.md` (Composio connections confirmed active)
