---
name: hub
description: >
  KTG content marketing pipeline. Takes a written blog post and runs the full
  publishing workflow: repurpose for all platforms, generate hero image, SEO
  and AI citation optimisation, then pause for green-light before publishing
  to all channels via Composio. Google-first: uses Gemini for text and image
  generation. Use when user says "hub",
  "/hub", "publish this", "run the pipeline", "post this everywhere".
user-invokable: true
argument-hint: "<post-file-path> [--local]"
disable-model-invocation: false
metadata:
  author: ktg
  version: "1.2.0"
---

# Hub — KTG Content Marketing Pipeline

Drop a post file. Get it published everywhere.

## Routing — Google-first

| Task | Engine (default: Google) | Cloud Skill tool | Default |
|------|--------------------------|------------------|---------|
| Repurpose | `gemini-3.5-flash` | `blog-repurpose` | **Gemini** |
| SEO validation | `gemini-3.5-flash` | `blog-seo-check` | **Gemini** |
| GEO scoring | `gemini-3.5-flash` | `blog-geo` | **Gemini** |
| Schema JSON-LD | `gemini-3.5-flash` | `seo-schema` | **Gemini** |
| Page SEO audit | `gemini-3.5-flash` | `seo-page` | **Gemini** |
| Technical SEO | `gemini-3.5-flash` | `seo-technical` | **Gemini** |
| Hero draft / hard reasoning | `gemini-3-pro-preview` | — | **Gemini** |
| Hero image | `gemini-3.1-flash-image-preview` (Nano Banana) | `blog-image` → `banana` | **Gemini** |
| Live SERP data | — | `seo-dataforseo` | **Cloud** |
| Publish | — | Composio MCP | **Cloud** |

**Driver:** `GEMINI_API_KEY` (already in the shell). Config: `pipeline/config.yaml`.
**Override:** Pass `--local` to route text through Ollama (offline fallback only — small models, lower quality).
**Voice guard:** inject `blog/user_voice.md` (Myth-Hilarity) into every generation prompt — Gemini defaults to generic register.

### Gemini Invocation Pattern

```bash
# List models the key can call
curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" \
  | python3 -c "import sys,json; [print(m['name']) for m in json.load(sys.stdin)['models']]"

# Generate (non-streaming, for agents)
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"<prompt>"}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])"
```

**Context window:** Gemini Flash/Pro ≥ 1M tokens — no chunking needed for normal posts.

---

## Plugin Map

| Step | Skill Name | Scope | Command | Arguments |
|------|-----------|-------|---------|-----------|
| Repurpose (cloud) | `blog-repurpose` | User (`~/.agents/skills/`) | `Skill` tool | prompt with file path + platforms |
| Images | `blog-image` | User (`~/.agents/skills/`) | `Skill` tool | `generate <topic>` |
| Images (alt) | `banana` | Project (`.claude/skills/`) | `Skill` tool | `generate <prompt>` |
| GEO audit (cloud) | `blog-geo` | User (`~/.agents/skills/`) | `Skill` tool | prompt with file path |
| SEO audit (cloud) | `seo-page` | User (`~/.agents/skills/`) | `Skill` tool | `<url>` or file path |
| Technical SEO (cloud) | `seo-technical` | User (`~/.agents/skills/`) | `Skill` tool | `<url>` or file path |
| Schema (cloud) | `seo-schema` | User (`~/.agents/skills/`) | `Skill` tool | `<url>` or file path |
| SEO check (cloud) | `blog-seo-check` | User (`~/.agents/skills/`) | `Skill` tool | prompt with file path |

---

## Step 0 — Validate input

Parse `$ARGUMENTS` for a file path. If none provided:

```
Usage: /hub <path-to-post.md>

Example: /hub wiki/content/mirage-post/post.md
```

Read the post file. Extract:
- **Title** — from frontmatter `title:` or first H1
- **Slug** — kebab-case title for output file naming
- **Platform** — detect from frontmatter `platform:` if present (default: generic blog)

Report: `Running KTG hub pipeline on: <title>`

---

## Step 1 — Repurpose

**Default:** Generate variants via Gemini `gemini-3.5-flash` (see Gemini Invocation Pattern). Inject `blog/user_voice.md` into each prompt for Myth-Hilarity voice.

Read the post file into memory. With Gemini's ≥1M context, pass the full post — no chunking needed.

Run 5 Gemini calls in sequence (or parallel via `Agent` tool):

```bash
# Medium
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write a Medium article (800-1200 words, professional tone, discussion prompt at end) based on this blog post:\n\n<post-content-or-summary>\n\nOutput only the article, no preamble."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > social-medium.md

# Reddit
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write a Reddit discussion post (authentic tone, r/ClaudeAI format, discussion starter) based on this blog post:\n\n<post-content-or-summary>\n\nOutput only the post, no preamble."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > social-reddit.md

# X thread
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write an X/Twitter thread (hook tweet + 8-15 tweets, engagement CTA, match character limits) based on this blog post:\n\n<post-content-or-summary>\n\nOutput only the thread, one tweet per line, no preamble."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > social-x-thread.md

# Meta
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write a Facebook/Meta post (scannable, key takeaways, CTA) based on this blog post:\n\n<post-content-or-summary>\n\nOutput only the post, no preamble."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > social-meta.md

# LinkedIn
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write a LinkedIn article (professional tone, data-forward, 800-1200 words, discussion prompt) based on this blog post:\n\n<post-content-or-summary>\n\nOutput only the article, no preamble."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > social-linkedin.md
```

**Skill-tool alternative (or `--local` for offline Ollama):**
Use the `Skill` tool with `name="blog-repurpose"`:

> Read the blog post at `<file-path>`. Repurpose it for ALL platforms: Medium article, Reddit discussion post, X thread, Meta post, and LinkedIn article. Generate all five variants in one invocation. Match platform-native tone and formatting. Save each variant to the same directory as the post using these exact filenames:
> - `social-medium.md`
> - `social-reddit.md`
> - `social-x-thread.md`
> - `social-meta.md`
> - `social-linkedin.md`

Report: `Repurpose complete — 5 variants generated`

---

## Step 2 — Images

**Generate hero image:**

Use the `Skill` tool with `name="blog-image"` and pass:

> Generate a hero image for a blog post titled "<title>". The post is about <one-sentence summary>. Style: editorial, AI/tech theme, no text overlay. Aspect ratio: 16:9. Save to `hero-16x9.png` in the post directory.

If `blog-image` MCP is unavailable, fall back to `Skill` tool with `name="banana"`:

> Generate a hero image for a blog post titled "<title>". The post is about <one-sentence summary>. Style: editorial, AI/tech theme, no text overlay. Aspect ratio: 16:9. Size: 2K. Save to `hero-16x9.png` in the post directory.

**Crop for platforms** (ImageMagick — run via Bash):

```bash
# LinkedIn / OG: 1200x627
magick "hero-16x9.png" -resize 1200x627^ -gravity Center -extent 1200x627 "hero-linkedin.png"

# Twitter/X: 1200x675
magick "hero-16x9.png" -resize 1200x675^ -gravity Center -extent 1200x675 "hero-x.png"

# Square (Reddit/Instagram): 1080x1080
magick "hero-16x9.png" -resize 1080x1080^ -gravity Center -extent 1080x1080 "hero-square.png"
```

If ImageMagick is not installed, report: "ImageMagick not found — skipping crops. Install with `winget install ImageMagick.ImageMagick` then re-run."

Report: `Images complete — hero + 3 crops`

---

## Step 3 — Optimise

**Default:** Run audits via Gemini `gemini-3.5-flash`. Pass the full post — no context-window trimming needed.

**3a. AI citation / GEO optimisation:**

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"You are a GEO (Generative Engine Optimization) analyst. Score this blog post for AI citation readiness (ChatGPT, Perplexity, Google AI Overviews).\n\nPost content:\n<post-frontmatter + first 2000 words + all headings>\n\nRate 0-100 on:\n1. Passage-Level Citability (clear 120-180 word answer blocks)\n2. Structural Readability (H1-H2-H3 hierarchy, question headings, lists/tables)\n3. Authority Signals (author byline, dates, sources cited)\n4. Technical Accessibility (AI crawler hints, no JS-gated content)\n5. Freshness (update dates within 30 days)\n\nOutput format:\nGEO Readiness Score: XX/100\nPlatform Breakdown: Google AIO: X/100 | ChatGPT: X/100 | Perplexity: X/100\nTop 5 Changes: 1. ... 2. ... 3. ... 4. ... 5. ..."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > GEO-ANALYSIS.md
```

**3b. SEO audit:**

```bash
# On-page + content quality
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"You are an SEO auditor. Analyze this blog post for on-page SEO and content quality.\n\nPost content:\n<post-frontmatter + first 2000 words + all headings>\n\nScore 0-100 per category:\n- On-Page SEO (title, meta, H1, headings, URL, internal/external links)\n- Content Quality (word count, readability Flesch 60-70, keyword density 1-3%, E-E-A-T)\n- Technical Meta (canonical, OG tags, Twitter Cards, hreflang)\n- Images (alt text, file size, format, dimensions, lazy loading)\n\nOutput: Overall Score: XX/100 with category breakdown and prioritized fixes."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > SEO-ANALYSIS.md

# Technical SEO (analyzed as static markdown file, not live site)
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"You are a technical SEO auditor. This is a static Markdown blog post (not a live site). Audit what CAN be checked from the file:\n\nPost content:\n<post-frontmatter + all headings + links + image refs>\n\nCheck:\n1. Heading hierarchy (no skipped H1->H2->H3)\n2. Internal links (3+ contextual, descriptive anchor)\n3. External links (2+ authoritative, Tier 1-2)\n4. Image alt text (present on all images)\n5. URL slug (lowercase, hyphens, <60 chars)\n6. Canonical hint (if frontmatter has canonical)\n7. OG/twitter card hints (if frontmatter has them)\n8. Mobile readiness (short paragraphs, no tables wider than screen)\n\nOutput: Technical Score: XX/100 with fixes."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" >> SEO-ANALYSIS.md
```

**3c. Schema markup:**

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Generate valid JSON-LD schema.org markup for this blog post.\n\nPost frontmatter:\n<frontmatter>\n\nPost title: <title>\nAuthor: <author or \"Kevin Tan\">\nPublished: <date>\nModified: <date>\nURL: <canonical or placeholder>\n\nRequired schemas:\n1. Article (or BlogPosting) — headline, author, datePublished, dateModified, image, publisher\n2. Organization — name, url, logo, sameAs\n3. Person (author) — name, url, sameAs\n4. BreadcrumbList — if applicable\n\nOutput ONLY valid JSON-LD inside ```json ... ``` blocks. No commentary."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > schema.json
```

**3d. Post-writing SEO validation:**

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Run a post-writing SEO validation checklist on this blog post.\n\nPost content:\n<full post>\n\nChecklist (pass/fail + fix if fail):\n□ Title tag: 40-60 chars, primary keyword in first half, power word\n□ Meta description: 150-160 chars, statistic included, value prop at end\n□ H1: exactly one, matches intent, includes keyword\n□ Heading hierarchy: no skipped levels (H1->H2->H3 only)\n□ Internal links: 3+ contextual, descriptive anchor\n□ External links: 2+ authoritative sources\n□ Canonical URL: set in frontmatter\n□ OG tags: og:title, og:description, og:image present\n□ Twitter Cards: twitter:card, twitter:image present\n□ URL slug: lowercase, hyphens, <60 chars\n□ Image alt text: present on all images\n\nOutput: Checklist with pass/fail per item and specific fixes."}]}]}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['candidates'][0]['content']['parts'][0]['text'])" > SEO-CHECKLIST.md
```

**Skill-tool alternative (or `--local` for offline Ollama):**
Run these skill invocations in sequence:

**3a-cloud.** Use `Skill` tool with `name="blog-geo"`:
> Score the blog post at `<file-path>` for AI citation readiness across ChatGPT, Perplexity, and Google AI Overviews. Output a 0-100 score and platform-specific recommendations. Save the analysis as `GEO-ANALYSIS.md` in the post directory.

**3b-cloud.** Use `Skill` tool with `name="seo-page"`:
> Run a deep single-page SEO analysis on the blog post at `<file-path>`. Cover on-page elements, content quality, technical meta tags, schema, images, and performance. Report the overall score and critical issues.

Then use `Skill` tool with `name="seo-technical"`:
> Run a technical SEO audit on the blog post at `<file-path>`. Cover crawlability, indexability, security, URL structure, mobile, Core Web Vitals, structured data, JavaScript rendering, and IndexNow. Report the technical score and critical issues.

**3c-cloud.** Use `Skill` tool with `name="seo-schema"`:
> Detect and validate schema markup for the blog post at `<file-path>`. Generate missing JSON-LD for Article/BlogPosting, Organization, Person, and BreadcrumbList. Save to `schema.json` in the post directory.

**3d-cloud.** Use `Skill` tool with `name="blog-seo-check"`:
> Run the post-writing SEO validation checklist on the blog post at `<file-path>`. Check title tag, meta description, heading hierarchy, internal/external links, canonical URL, OG tags, Twitter Cards, URL structure, and image alt text. Report pass/fail per item with fix recommendations.

Report: `Optimisation complete — GEO score: <N>/100, SEO score: <N>/100, schema generated`

---

## Step 4 — Review gate (MANDATORY)

**STOP. Do not publish anything yet.**

Present a full summary to the user:

```
═══════════════════════════════════════
  KTG HUB — READY TO PUBLISH
═══════════════════════════════════════

Post: <title>
File: <path>

VARIANTS GENERATED:
  ✓ Medium         → social-medium.md
  ✓ Reddit         → social-reddit.md
  ✓ X thread       → social-x-thread.md
  ✓ Meta           → social-meta.md
  ✓ LinkedIn       → social-linkedin.md

IMAGES:
  ✓ Hero 16:9      → hero-16x9.png
  ✓ LinkedIn crop  → hero-linkedin.png
  ✓ X crop         → hero-x.png
  ✓ Square crop    → hero-square.png

OPTIMISATION:
  ✓ GEO pass       → GEO-ANALYSIS.md
  ✓ SEO audit      → SEO-ANALYSIS.md
  ✓ SEO checklist  → SEO-CHECKLIST.md
  ✓ Schema         → schema.json

CHANNELS:
  → Reddit r/ClaudeAI
  → LinkedIn personal feed
  → Vercel deploy (canonical URL first)

═══════════════════════════════════════
```

Then ask:

> Review the variants before publishing. Type **YES** to publish to all channels, **SKIP <channel>** to exclude a channel, or **STOP** to cancel.

**Do not proceed until explicit YES is received.**

---

## Step 5 — Publish

**5a. Vercel deploy first** (get canonical URL):

Use Composio to deploy the post to Vercel. Capture the canonical URL from the deploy response.

Substitute the canonical URL into all social variants where `[CANONICAL_URL]` placeholder appears.

**5b. Fire each channel:**

Use Composio MCP tools to publish:

| Channel | Content | Image |
|---------|---------|-------|
| Medium | `social-medium.md` | none (link post) |
| Reddit r/ClaudeAI | `social-reddit.md` | none (link post) |
| X | `social-x-thread.md` | `hero-x.png` |
| Meta | `social-meta.md` | `hero-square.png` |
| LinkedIn | `social-linkedin.md` | `hero-linkedin.png` |

For each channel, report success or failure. If a channel fails, report the error and continue with remaining channels — do not abort the whole pipeline.

**5c. Final report:**

```
═══════════════════════════════════════
  KTG HUB — PUBLISHED
═══════════════════════════════════════

  ✓ Vercel    → <canonical-url>
  ✓ Medium    → <post-url>
  ✓ Reddit    → <post-url>
  ✓ X         → <post-url>
  ✓ Meta      → <post-url>
  ✓ LinkedIn  → <post-url>

═══════════════════════════════════════
```

**5d. Wiki log:**
After successful publish, append to `wiki/log.md`:
```markdown
- $(date +%Y-%m-%d) — Published: <title> → <canonical-url>
```

Update `wiki/hot.md` with the published URL and status.

---

## Error handling

- **Missing file**: Report path not found, stop.
- **Skill fails**: Report which skill name failed, offer to retry that step only. Use the exact skill name from the Plugin Map.
- **Gemini key missing/invalid**: Check `$GEMINI_API_KEY` is set; verify with the model-list curl in the Gemini Invocation Pattern. Offline fallback: `--local`.
- **Gemini 429 / rate limit**: Back off and retry the failed step only; switch the failing call to `gemini-3.5-flash-lite` if sustained.
- **Gemini 400 (bad request)**: Usually unescaped quotes in the prompt JSON — pass the prompt as a here-doc or escape `"` before embedding.
- **ImageMagick missing**: Skip crops, note in review gate, continue.
- **Composio channel fails**: Report error, continue other channels.
- **User types STOP at gate**: Cancel cleanly. All generated files are kept.

---

## Notes

- The review gate is non-negotiable — never auto-publish.
- **Google-first by default**: Gemini handles all text tasks (repurpose, SEO, GEO, schema) and image gen (Nano Banana). `--local` routes text to Ollama as an offline fallback only.
- **Driver**: `GEMINI_API_KEY` in the shell. Text `gemini-3.5-flash` (→ `gemini-3-pro-preview` for hero drafts); images `gemini-3.1-flash-image-preview`.
- **Voice**: inject `blog/user_voice.md` (Myth-Hilarity) into every text prompt — cloud models drift generic without it.
- Composio connections active: `medium`, `reddit`, `x`, `meta`, `linkedin`, `vercel`
- For Windows/PowerShell: ImageMagick commands use `magick` not `convert`
- Post variants are saved alongside the original — the wiki auto-commit hook picks them up
- Skill invocations use the `Skill` tool with exact `name=` from the Plugin Map. Never `Read` skill files directly.
