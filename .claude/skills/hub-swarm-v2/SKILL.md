---
name: hub-swarm-v2
description: >
  KTG content marketing pipeline — SWARM MODE v2. Concrete 11-agent parallel
  pipeline using the Agent tool. Local-first: Ollama for text, cloud for images
  and publish. Drop a post, spawn agents, publish everywhere.
user-invokable: true
argument-hint: "<post-file-path> [--cloud] [--ads] [--canvas]"
disable-model-invocation: false
metadata:
  author: ktg
  version: "2.2.0"
---

# Hub-Swarm v2 — Concrete Agentic Pipeline

Spawns 11 sub-agents in parallel using the `Agent` tool. Default: Ollama for text tasks. Cloud only for images, live data, and publishing.

## Local-First Routing

| # | Agent | Default | Model | Fallback |
|---|-------|---------|-------|----------|
| 1 | `repurpose-medium` | **Local** | `Ministral:latest` | `blog-repurpose` |
| 2 | `repurpose-reddit` | **Local** | `Ministral:latest` | `blog-repurpose` |
| 3 | `repurpose-x` | **Local** | `Ministral:latest` | `blog-repurpose` |
| 4 | `repurpose-meta` | **Local** | `Ministral:latest` | `blog-repurpose` |
| 5 | `repurpose-linkedin` | **Local** | `Ministral:latest` | `blog-repurpose` |
| 6 | `image-hero` | **Cloud** | — | `blog-image` → `banana` |
| 7 | `seo-geo` | **Local** | `Qwopus:latest` | `blog-geo` |
| 8 | `seo-page` | **Local** | `Qwopus:latest` | `seo-page` |
| 9 | `seo-technical` | **Local** | `Qwopus:latest` | `seo-technical` |
| 10 | `seo-schema` | **Local** | `Ministral:latest` | `seo-schema` |
| 11 | `seo-check` | **Local** | `Qwopus:latest` | `blog-seo-check` |
| 12 | `ads-create` | **Local** | `Qwopus:latest` | `ads-create` |
| 13 | `ads-generate` | **Cloud** | — | `ads-generate` |
| 14 | `canvas-generate` | **Cloud** | — | `canvas-generate` |

**Override:** `--cloud` forces all text agents to use Skill tool instead of Ollama.

## Agent Manifest

| # | Agent Name | Invokes | Task | Output |
|---|-----------|---------|------|--------|
| 1 | `repurpose-medium` | Ollama `Ministral:latest` | Generate Medium variant | `social-medium.md` |
| 2 | `repurpose-reddit` | Ollama `Ministral:latest` | Generate Reddit variant | `social-reddit.md` |
| 3 | `repurpose-x` | Ollama `Ministral:latest` | Generate X thread variant | `social-x-thread.md` |
| 4 | `repurpose-meta` | Ollama `Ministral:latest` | Generate Meta variant | `social-meta.md` |
| 5 | `repurpose-linkedin` | Ollama `Ministral:latest` | Generate LinkedIn variant | `social-linkedin.md` |
| 6 | `image-hero` | `blog-image` (or `banana`) | Generate hero 16:9 | `hero-16x9.png` |
| 7 | `seo-geo` | Ollama `Qwopus:latest` | AI citation audit | `GEO-ANALYSIS.md` + score |
| 8 | `seo-page` | Ollama `Qwopus:latest` | On-page SEO audit | `SEO-PAGE.md` |
| 9 | `seo-technical` | Ollama `Qwopus:latest` | Technical SEO audit | `SEO-TECHNICAL.md` |
| 10 | `seo-schema` | Ollama `Ministral:latest` | JSON-LD generation | `schema.json` |
| 11 | `seo-check` | Ollama `Qwopus:latest` | Post-writing validation | `SEO-CHECKLIST.md` |

Optional agents (if `--ads`):
| 12 | `ads-create` | Ollama `Qwopus:latest` | Campaign brief | `campaign-brief.md` |
| 13 | `ads-generate` | `ads-generate` | Ad creatives | `ad-creative-*.png` |

Optional agents (if `--canvas`):
| 14 | `canvas-generate` | `canvas-generate` | Visual canvas | `post.canvas` |

---

## Orchestrator Dispatch

For each agent, spawn via `Agent` tool with this prompt template:

### Local Agent Template

```
You are agent <agent-name> in the KTG Hub-Swarm pipeline.
Your job: call Ollama and produce ONE artifact.

Input file: <post-file-path>
Post title: <title>
Post slug: <slug>

Run this curl command (exact):
<curl-command-from-manifest>

Save stdout to: <output-path>
Report back with: success/failure, output path, and any errors.
```

### Cloud Agent Template

```
You are agent <agent-name> in the KTG Hub-Swarm pipeline.
Your job: invoke ONE plugin skill and produce ONE artifact.

Input file: <post-file-path>
Post title: <title>
Post slug: <slug>

Use the Skill tool with name="<skill-name>" and pass this exact prompt:
<prompt-from-manifest-below>

Save your output to: <output-path>
Report back with: success/failure, output path, and any errors.
```

---

## Per-Agent Prompts

### Repurpose Agents (1–5)

**Local (default):**

**Agent `repurpose-medium`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Ministral:latest","prompt":"Write a Medium article (800-1200 words, professional tone, discussion prompt) based on this post:\n<post-content-or-summary>\n\nOutput only the article.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > social-medium.md
```

**Agent `repurpose-reddit`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Ministral:latest","prompt":"Write a Reddit discussion post (authentic tone, r/ClaudeAI format, discussion starter) based on this post:\n<post-content-or-summary>\n\nOutput only the post.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > social-reddit.md
```

**Agent `repurpose-x`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Ministral:latest","prompt":"Write an X thread (hook + 8-15 tweets, engagement CTA) based on this post:\n<post-content-or-summary>\n\nOutput only the thread, one tweet per line.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > social-x-thread.md
```

**Agent `repurpose-meta`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Ministral:latest","prompt":"Write a Facebook/Meta post (scannable, key takeaways, CTA) based on this post:\n<post-content-or-summary>\n\nOutput only the post.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > social-meta.md
```

**Agent `repurpose-linkedin`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Ministral:latest","prompt":"Write a LinkedIn article (professional, data-forward, 800-1200 words, discussion prompt) based on this post:\n<post-content-or-summary>\n\nOutput only the article.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > social-linkedin.md
```

**Cloud (`--cloud`):**
All use `Skill` tool with `name="blog-repurpose"`. Prompt:
> Read the blog post at `<file-path>`. Repurpose for ALL platforms: Medium, Reddit, X, Meta, LinkedIn. Generate all five variants. Save to `<dir>/social-*.md`.

### Image Agent (6)

**Agent `image-hero`:**
> Use Skill tool with `name="blog-image"`. Prompt: "Generate a hero image for a blog post titled '<title>'. Topic: <summary>. Style: editorial, AI/tech theme, no text overlay. Aspect ratio: 16:9. Save to `<dir>/hero-16x9.png`."
>
> If blog-image MCP unavailable, fall back to Skill tool with `name="banana"`. Prompt: "Generate a hero image for '<title>'. <summary>. Style: editorial, AI/tech. Aspect ratio: 16:9. Size: 2K. Save to `<dir>/hero-16x9.png`."

After hero generation, run ImageMagick crops (can be a 12th agent or inline):
```bash
magick "<dir>/hero-16x9.png" -resize 1200x627^ -gravity Center -extent 1200x627 "<dir>/hero-linkedin.png"
magick "<dir>/hero-16x9.png" -resize 1200x675^ -gravity Center -extent 1200x675 "<dir>/hero-x.png"
magick "<dir>/hero-16x9.png" -resize 1080x1080^ -gravity Center -extent 1080x1080 "<dir>/hero-square.png"
```

### SEO Agents (7–11)

**Local (default):**

**Agent `seo-geo`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Qwopus:latest","prompt":"You are a GEO analyst. Score this post for AI citation readiness (ChatGPT, Perplexity, Google AIO).\n<post-frontmatter + first 2000 words + headings>\n\nRate 0-100 on: Passage Citability, Structural Readability, Authority Signals, Technical Accessibility, Freshness. Output GEO Readiness Score: XX/100 with platform breakdown and top 5 changes.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > GEO-ANALYSIS.md
```

**Agent `seo-page`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Qwopus:latest","prompt":"You are an SEO auditor. Analyze this post for on-page SEO and content quality.\n<post-frontmatter + first 2000 words + headings>\n\nScore 0-100 per: On-Page SEO, Content Quality, Technical Meta, Images. Output overall score with category breakdown and prioritized fixes.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > SEO-PAGE.md
```

**Agent `seo-technical`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Qwopus:latest","prompt":"You are a technical SEO auditor. This is a static Markdown file (not a live site). Audit:\n<post-frontmatter + headings + links + image refs>\n\nCheck: heading hierarchy, internal links (3+), external links (2+), image alt text, URL slug, canonical, OG hints, mobile readiness. Output Technical Score: XX/100 with fixes.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > SEO-TECHNICAL.md
```

**Agent `seo-schema`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Ministral:latest","prompt":"Generate valid JSON-LD schema.org for this blog post.\nFrontmatter: <frontmatter>\nTitle: <title>\nAuthor: <author>\nPublished: <date>\nModified: <date>\nURL: <canonical>\n\nRequired: Article/BlogPosting, Organization, Person, BreadcrumbList. Output ONLY valid JSON-LD inside ```json ... ``` blocks.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > schema.json
```

**Agent `seo-check`:**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Qwopus:latest","prompt":"Run post-writing SEO validation checklist.\n<full post>\n\nCheck: title (40-60 chars), meta (150-160), H1 (exactly one), hierarchy (no skips), internal links (3+), external links (2+), canonical, OG, Twitter Cards, URL slug, image alt text. Output pass/fail per item with fixes.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > SEO-CHECKLIST.md
```

**Cloud (`--cloud`):**
All use respective `Skill` tools (`blog-geo`, `seo-page`, `seo-technical`, `seo-schema`, `blog-seo-check`) with file path prompts.

### Optional Ads Agents (12–13)

**Agent `ads-create` (local):**
```bash
curl -s http://localhost:11434/api/generate \
  -d '{"model":"Qwopus:latest","prompt":"You are an ad strategist. Read this blog post and create a campaign brief.\n<post-content-or-summary>\n\nOutput: campaign concept, messaging pillars, target audience, 3 headline options, 2 CTA options, recommended platforms. Save as campaign-brief.md.","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])" > campaign-brief.md
```

**Agent `ads-generate` (cloud — image gen):**
> Use Skill tool with `name="ads-generate"`. Prompt: "Read `<dir>/campaign-brief.md` and brand-profile.json. Produce platform-sized ad images. Save to `<dir>/ad-creative-*.png`."

### Optional Canvas Agent (14)

**Agent `canvas-generate`:**
> Use Skill tool with `name="canvas-generate"`. Prompt: "Create a visual canvas from the blog post at `<file-path>`. Detect best archetype, generate content and visuals, instantiate template, apply layout, produce complete canvas. Save to `<dir>/post.canvas`."

---

## Gather Phase

Wait for all agents to return. Collect:
1. Success/failure per agent
2. Output file paths
3. Scores (GEO, SEO, technical, blog-seo-check)
4. Any errors

Assemble artifact manifest. If any agent failed, mark it in the manifest.

---

## Review Gate

Present the manifest exactly as defined in `hub-swarm` skill. Wait for explicit `YES`.

---

## Publish Phase

Spawn 3 parallel publish agents:

| Agent | Task |
|-------|------|
| `publish-vercel` | Deploy post via Composio, capture canonical URL |
| `publish-wordpress` | Publish via `wordpress-mcp-ultimate` MCP |
| `publish-social` | Fire Reddit, LinkedIn, X, Meta via Composio |

Each publish agent receives the canonical URL from `publish-vercel` before firing.

---

## Notes

- **Local-first by default**: 10 of 11 core agents use Ollama. Only `image-hero` uses cloud (`blog-image`/`banana`).
- **Ollama models**: `Ministral:latest` (13.5B) for content + schema, `Qwopus:latest` (9B) for SEO/GEO/analysis
- Context limit: ~32k tokens. For posts >8k words, chunk into summaries before Ollama calls.
- Cloud skill invocations use the `Skill` tool with exact `name=` matching the skill frontmatter
- Agents do not share context — each loads its own skill/Ollama call independently
- Orchestrator stays under 4k tokens by keeping per-agent prompts minimal
- Never `Read` skill files directly — invoke via `Skill` tool or Ollama API only
- Review gate is the only sequential bottleneck (by design)
