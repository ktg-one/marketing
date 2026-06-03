---
name: hub-swarm
description: >
  KTG content marketing pipeline — SWARM MODE. Orchestrates 7 plugins
  via parallel agent dispatch. Drop a post, get it published everywhere
  with maximum parallelism. Local-first: Ollama for text, cloud for images
  and live data. Agents run simultaneously, not sequentially.
user-invokable: true
argument-hint: "<post-file-path> [--cloud] [--ads] [--canvas]"
disable-model-invocation: false
metadata:
  author: ktg
  version: "2.2.0"
---

# Hub-Swarm: Parallel Content Pipeline

Drop a post. Spawn agents. Publish everywhere.

## Local-First Routing

All text agents default to Ollama. Image + publish agents use cloud.

| Swarm | Local (Ollama) | Cloud (Skill tool) | Default |
|-------|---------------|-------------------|---------|
| Content | `Ministral:latest` (13.5B) | `blog-repurpose` | **Local** |
| SEO (5 agents) | `Qwopus:latest` (9B) | `blog-geo`, `seo-page`, etc. | **Local** |
| Ads brief | `Qwopus:latest` (9B) | `ads-create` | **Local** |
| Image hero | — | `blog-image` → `banana` | **Cloud** |
| Image crops | ImageMagick (local binary) | — | **Local** |
| Publish | — | Composio MCP | **Cloud** |

**Override:** `--cloud` skips Ollama, uses Skill tool for all text tasks.

## Architecture

```
PHASE 0: VALIDATE (Sequential — fast)
  └─ Validate input file exists, extract title/slug
  └─ Check Ollama: curl http://localhost:11434/api/tags

PHASE 1: SWARM DISPATCH (Parallel — all agents at once)
  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
  │ CONTENT     │ │ IMAGES      │ │ SEO         │
  │ ollama-     │ │ blog-image  │ │ ollama-geo  │
  │ repurpose   │ │ or banana   │ │ ollama-seo  │
  │ (5 agents)  │ │             │ │ (5 agents)  │
  └─────────────┘ └─────────────┘ └─────────────┘
  ┌─────────────┐ ┌─────────────┐
  │ ADS         │ │ CANVAS      │
  │ ollama-ads  │ │ canvas-     │
  │ (optional)  │ │ generate    │
  │             │ │ (optional)  │
  └─────────────┘ └─────────────┘

PHASE 2: GATHER (Sequential — collect results)
  └─ Wait for all agents. Assemble artifact manifest.

PHASE 3: REVIEW GATE (Sequential — human checkpoint)
  └─ Show manifest. Wait for explicit YES per channel.

PHASE 4: PUBLISH SWARM (Parallel — all channels at once)
  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
  │ VERCEL      │ │ WORDPRESS   │ │ SOCIAL      │
  │ deploy      │ │ publish     │ │ Reddit      │
  │             │ │             │ │ LinkedIn    │
  │             │ │             │ │ X           │
  └─────────────┘ └─────────────┘ └─────────────┘
  ┌─────────────┐
  │ ADS         │
  │ Google Ads  │
  │ Meta Ads    │
  │ LinkedIn    │
  │ TikTok      │
  └─────────────┘
```

---

## Plugin → Skill Mapping

| Swarm Agent | Actual Skill Name | Scope | Invocation |
|-------------|------------------|-------|------------|
| `blog-repurpose` | `blog-repurpose` | User (`~/.agents/skills/`) | `Skill` tool, prompt with file path + all platforms |
| `blog-image` | `blog-image` | User (`~/.agents/skills/`) | `Skill` tool, `generate <topic>` |
| `banana` | `banana` | Project (`.claude/skills/`) | `Skill` tool, `generate <prompt>` |
| `blog-geo` | `blog-geo` | User (`~/.agents/skills/`) | `Skill` tool, prompt with file path |
| `seo-page` | `seo-page` | User (`~/.agents/skills/`) | `Skill` tool, `<url>` or file path |
| `seo-technical` | `seo-technical` | User (`~/.agents/skills/`) | `Skill` tool, `<url>` or file path |
| `seo-schema` | `seo-schema` | User (`~/.agents/skills/`) | `Skill` tool, `<url>` or file path |
| `blog-seo-check` | `blog-seo-check` | User (`~/.agents/skills/`) | `Skill` tool, prompt with file path |
| `ads-create` | `ads-create` | User (`~/.agents/skills/`) | `Skill` tool, prompt with brand + post |
| `ads-generate` | `ads-generate` | User (`~/.agents/skills/`) | `Skill` tool, prompt with campaign brief |
| `canvas-generate` | `canvas-generate` | Project (`.claude/skills/`) | `Skill` tool, prompt with post content |

---

## Swarm Agent Definitions

### Content Swarm

**Default (local):** 5 parallel Ollama agents, one per platform.

```yaml
agent: ollama-repurpose-medium
model: Ministral:latest
parallel: true
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Ministral:latest","prompt":"Write a Medium article (800-1200 words,
  professional tone, discussion prompt) based on this post:\n<post-content-or-summary>\n
  Output only the article.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > social-medium.md
output: social-medium.md

agent: ollama-repurpose-reddit
model: Ministral:latest
parallel: true
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Ministral:latest","prompt":"Write a Reddit discussion post
  (authentic tone, r/ClaudeAI format, discussion starter) based on this post:\n<post-content-or-summary>\n
  Output only the post.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > social-reddit.md
output: social-reddit.md

agent: ollama-repurpose-x
model: Ministral:latest
parallel: true
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Ministral:latest","prompt":"Write an X thread (hook + 8-15 tweets,
  engagement CTA) based on this post:\n<post-content-or-summary>\n
  Output only the thread, one tweet per line.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > social-x-thread.md
output: social-x-thread.md

agent: ollama-repurpose-meta
model: Ministral:latest
parallel: true
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Ministral:latest","prompt":"Write a Facebook/Meta post
  (scannable, key takeaways, CTA) based on this post:\n<post-content-or-summary>\n
  Output only the post.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > social-meta.md
output: social-meta.md

agent: ollama-repurpose-linkedin
model: Ministral:latest
parallel: true
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Ministral:latest","prompt":"Write a LinkedIn article (professional,
  data-forward, 800-1200 words, discussion prompt) based on this post:\n<post-content-or-summary>\n
  Output only the article.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > social-linkedin.md
output: social-linkedin.md
```

**Cloud fallback (`--cloud`):**
```yaml
agent: blog-repurpose
skill_name: blog-repurpose
scope: user
parallel: true
task: >
  Use the Skill tool with name="blog-repurpose". Prompt:
  "Read the blog post at <file-path>. Repurpose it for ALL platforms:
  Medium, Reddit, X, Meta, LinkedIn. Generate all five variants."
output: social-*.md (5 files)
```

### Image Swarm

```yaml
agent: blog-image
skill_name: blog-image
scope: user
parallel: true
dependency: validate_complete
task: >
  Use the Skill tool with name="blog-image". Prompt:
  "Generate a hero image for a blog post titled '<title>'.
  Topic: <one-sentence summary>. Style: editorial, AI/tech theme, no text overlay.
  Aspect ratio: 16:9. Save to hero-16x9.png in the post directory."
fallback: >
  If blog-image MCP unavailable, use Skill tool with name="banana".
  Prompt: "Generate a hero image for '<title>'. <summary>. Style: editorial, AI/tech.
  Aspect ratio: 16:9. Size: 2K. Save to hero-16x9.png."
output: hero-16x9.png

agent: image-crop
skill_name: bash (ImageMagick)
scope: local
parallel: true
dependency: hero_generated
task: >
  Run ImageMagick crops via Bash:
  magick hero-16x9.png -resize 1200x627^ -gravity Center -extent 1200x627 hero-linkedin.png
  magick hero-16x9.png -resize 1200x675^ -gravity Center -extent 1200x675 hero-x.png
  magick hero-16x9.png -resize 1080x1080^ -gravity Center -extent 1080x1080 hero-square.png
output: hero-*.png (3 files)
```

### SEO Swarm

**Default (local):** 5 parallel Ollama agents.

```yaml
agent: ollama-geo
model: Qwopus:latest
parallel: true
dependency: validate_complete
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Qwopus:latest","prompt":"You are a GEO analyst. Score this post
  for AI citation readiness (ChatGPT, Perplexity, Google AIO).\n<post-frontmatter + first 2000 words + headings>\n
  Rate 0-100 on: Passage Citability, Structural Readability, Authority Signals,
  Technical Accessibility, Freshness. Output GEO Readiness Score: XX/100
  with platform breakdown and top 5 changes.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > GEO-ANALYSIS.md
output: GEO-ANALYSIS.md

agent: ollama-seo-page
model: Qwopus:latest
parallel: true
dependency: validate_complete
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Qwopus:latest","prompt":"You are an SEO auditor. Analyze this post
  for on-page SEO and content quality.\n<post-frontmatter + first 2000 words + headings>\n
  Score 0-100 per: On-Page SEO, Content Quality, Technical Meta, Images.
  Output overall score with category breakdown and prioritized fixes.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > SEO-PAGE.md
output: SEO-PAGE.md

agent: ollama-seo-technical
model: Qwopus:latest
parallel: true
dependency: validate_complete
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Qwopus:latest","prompt":"You are a technical SEO auditor.
  This is a static Markdown file (not a live site). Audit:\n<post-frontmatter + headings + links + image refs>\n
  Check: heading hierarchy, internal links (3+), external links (2+),
  image alt text, URL slug, canonical, OG hints, mobile readiness.
  Output Technical Score: XX/100 with fixes.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > SEO-TECHNICAL.md
output: SEO-TECHNICAL.md

agent: ollama-schema
model: Ministral:latest
parallel: true
dependency: validate_complete
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Ministral:latest","prompt":"Generate valid JSON-LD schema.org
  for this blog post.\nFrontmatter: <frontmatter>\nTitle: <title>\nAuthor: <author>\nPublished: <date>\nModified: <date>\nURL: <canonical>\n
  Required: Article/BlogPosting, Organization, Person, BreadcrumbList.
  Output ONLY valid JSON-LD inside ```json ... ``` blocks.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > schema.json
output: schema.json

agent: ollama-seo-check
model: Qwopus:latest
parallel: true
dependency: validate_complete
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Qwopus:latest","prompt":"Run post-writing SEO validation checklist.\n<full post>\n
  Check: title (40-60 chars), meta (150-160), H1 (exactly one), hierarchy (no skips),
  internal links (3+), external links (2+), canonical, OG, Twitter Cards,
  URL slug, image alt text. Output pass/fail per item with fixes.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > SEO-CHECKLIST.md
output: SEO-CHECKLIST.md
```

**Cloud fallback (`--cloud`):**
```yaml
agent: blog-geo
skill_name: blog-geo
scope: user
parallel: true
task: >
  Use Skill tool with name="blog-geo". Prompt: "Score <file-path> for AI citation readiness."
output: GEO-ANALYSIS.md

agent: seo-page
skill_name: seo-page
scope: user
parallel: true
task: >
  Use Skill tool with name="seo-page". Prompt: "Run on-page SEO analysis on <file-path>."
output: SEO score card

agent: seo-technical
skill_name: seo-technical
scope: user
parallel: true
task: >
  Use Skill tool with name="seo-technical". Prompt: "Run technical SEO audit on <file-path>."
output: Technical score card

agent: seo-schema
skill_name: seo-schema
scope: user
parallel: true
task: >
  Use Skill tool with name="seo-schema". Prompt: "Generate JSON-LD for <file-path>."
output: schema.json

agent: blog-seo-check
skill_name: blog-seo-check
scope: user
parallel: true
task: >
  Use Skill tool with name="blog-seo-check". Prompt: "Run SEO validation on <file-path>."
output: Pass/fail checklist
```

### Ads Swarm (Optional)

**Default (local):**
```yaml
agent: ollama-ads-create
model: Qwopus:latest
parallel: true
condition: user_requested_ads
dependency: validate_complete
task: >
  curl -s http://localhost:11434/api/generate
  -d '{"model":"Qwopus:latest","prompt":"You are an ad strategist. Read this blog post
  and create a campaign brief.\n<post-content-or-summary>\n
  Output: campaign concept, messaging pillars, target audience, 3 headline options,
  2 CTA options, recommended platforms. Save as campaign-brief.md.","stream":false}'
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'])"
  > campaign-brief.md
output: campaign-brief.md
```

Ad creatives use cloud (`blog-image` or `banana`) — no local image gen model.

**Cloud fallback (`--cloud`):**
```yaml
agent: ads-create
skill_name: ads-create
scope: user
parallel: true
task: >
  Use Skill tool with name="ads-create". Prompt:
  "Read brand-profile.json and <file-path>. Produce campaign brief."
output: campaign-brief.md

agent: ads-generate
skill_name: ads-generate
scope: user
parallel: true
dependency: campaign-brief_complete
task: >
  Use Skill tool with name="ads-generate". Prompt:
  "Read campaign-brief.md and brand-profile.json. Produce ad creatives."
output: ad-creative-*.png
```

### Canvas Swarm (Optional)

```yaml
agent: canvas-generate
skill_name: canvas-generate
scope: project
parallel: true
condition: user_requested_visual_planning
dependency: validate_complete
task: >
  Use the Skill tool with name="canvas-generate". Prompt:
  "Create a visual canvas from the blog post at <file-path>. Detect the best
  archetype, generate content and visuals, instantiate template, apply layout,
  produce complete canvas. Save to post.canvas in post directory."
output: post.canvas
```

---

## Dependency Graph

```
validate_input
    ├── ollama-repurpose-* (5 agents) ──┐
    │                                   ├──→ ollama-seo-* (5 agents, parallel)
    ├── blog-image/banana               │   ├──→ ollama-ads-create
    │                                   │   │
    └── image-crop (ImageMagick)        ├───┼──→ (no dependency on ads)
                                        │   │
                                        └───┴──→ canvas-generate (optional)
```

---

## Review Gate Manifest

```
HUB-SWARM — READY TO PUBLISH

CONTENT:
  Post: <title>
  X thread: <word_count> words
  LinkedIn: <word_count> words
  Reddit: <word_count> words
  Medium: <word_count> words
  Meta: <word_count> words

IMAGES:
  Hero 16:9, LinkedIn crop, X crop, Square crop

SEO:
  GEO score: <N>/100
  SEO score: <N>/100
  Technical score: <N>/100
  Schema: <types>
  SEO check: <pass/fail count>

ADS (if requested):
  Google Ads: <headline_count> headlines
  Meta Ads: <headline_count> headlines
  LinkedIn Ads: <headline_count> headlines
  TikTok Ads: <headline_count> headlines

CANVAS (if requested):
  <yes/no> Visual planning

CHANNELS:
  Vercel, WordPress, Reddit, LinkedIn, X, Meta, Medium

Type YES to publish all, SKIP <channel> to exclude, STOP to cancel.
```

---

## Performance

Local Ollama runs at ~20-40 tokens/sec on RTX-class GPU. No API latency.

| Phase | Sequential (cloud) | Swarm (cloud) | Swarm (local) | Speedup |
|-------|-------------------|---------------|---------------|---------|
| Validate | 1s | 1s | 1s (+ Ollama check) | 1x |
| Content (5 variants) | 300s | 60s | 60s | 5x |
| Images | 30s | 30s | 30s | 1x |
| SEO (5 agents) | 225s | 45s | 45s | 5x |
| Ads | 60s | 20s | 20s | 3x |
| Canvas | 30s | 30s | 30s | optional |
| **Total** | **~646s** | **~186s** | **~186s** | **3.5x** |

**Cost:** Local = $0 in API calls. Cloud = ~$0.50-2.00 per run depending on post length.

---

## Error Handling

- Agent timeout: Report which agent/skill timed out. Continue with others.
- Agent failure: Report failure. Offer to retry that agent only.
- Partial swarm: If 4 of 5 SEO agents succeed, use partial results.
- **Ollama not running**: Check `curl http://localhost:11434/api/tags`. If fails, auto-fallback to `--cloud` mode.
- **Ollama model missing**: Auto-pull with `ollama pull <model>` or fallback to `--cloud`.
- **Context overflow**: If post >8k words, chunk into summaries before sending to Ollama.
- Dependency failure: If blog-image/banana fails, image-crop and ads-generate skip gracefully.
- ImageMagick missing: Skip crops, note in review gate, continue.

---

## Notes

- **Local-first by default**: Ollama for text, cloud for images + publish
- **Ollama models**: `Ministral:latest` (13.5B) for content/schema, `Qwopus:latest` (9B) for SEO/GEO/analysis
- Swarm uses the `Agent` tool with `subagent_type: general` for parallel execution
- Each agent gets its own context budget — no shared state
- Results gathered via manifest, not conversation memory
- Review gate is the only sequential bottleneck (by design)
- Post-publish: wiki log entry, hot cache update
- Cloud skill invocations use the `Skill` tool with exact `name=` from the Plugin Map
- Never `Read` skill files directly — invoke via `Skill` tool only
