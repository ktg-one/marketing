---
name: hub
description: >
  KTG content marketing pipeline. Takes a written blog post and runs the full
  publishing workflow: repurpose for all platforms, generate hero image, SEO
  and AI citation optimisation, then pause for green-light before publishing
  to all channels via Composio. Use when user says "hub", "/hub", "publish this",
  "run the pipeline", "post this everywhere".
user-invokable: true
argument-hint: "<post-file-path>"
disable-model-invocation: false
metadata:
  author: ktg
  version: "1.0.0"
---

# Hub — KTG Content Marketing Pipeline

Drop a post file. Get it published everywhere.

## Pipeline

```
1. Repurpose   → Medium, Reddit, X, Meta, LinkedIn
2. Images      → hero image (16:9) + crops via ImageMagick
3. Optimise    → AI citation (geo) + SEO check + JSON-LD schema
4. Review gate → show everything, wait for explicit YES
5. Publish     → Composio fires each variant to its platform
```

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

Invoke the `blog-repurpose` skill. Pass the post file path and pre-select **all platforms** to skip the interactive prompt:

> Repurpose the post at `<file-path>` for ALL platforms: Medium article, Reddit discussion post, X thread, Meta post, and LinkedIn article. Do not ask which platforms — generate all five.

Save each variant to the same directory as the post:
- `social-medium.md`
- `social-reddit.md`
- `social-x-thread.md`
- `social-meta.md`
- `social-linkedin.md`

Report: `Repurpose complete — 5 variants generated`

---

## Step 2 — Images

**Generate hero image:**

Invoke the `banana` skill with a prompt derived from the post title and main argument:

> Generate a hero image for a blog post titled "<title>". The post is about <one-sentence summary>. Style: editorial, AI/tech theme, no text overlay. Aspect ratio: 16:9. Size: 2K.

Save to `hero-16x9.png` in the post directory.

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

Run these three skills in sequence on the original post file:

**3a. AI citation / GEO optimisation:**
Invoke `seo-geo` on the post — optimise for AI citation readiness (ChatGPT, Perplexity, Google AI Overviews). Apply recommendations inline: add 134-167 word answer blocks, question-based H2s, server-side FAQ sections, verify AI crawler access in robots.txt, and generate an `llms.txt` if missing. Write `GEO-ANALYSIS.md` to the post directory.

**3b. Full SEO audit:**
Run `seo-page` for on-page analysis (title, meta, headings, content quality, images, Core Web Vitals signals). Then run `seo-technical` for deep technical audit (crawlability, indexability, canonical, hreflang, structured data, security headers, mobile, JS rendering). Report combined score and critical issues. Do not block on minor issues.

**3c. Schema markup:**
Invoke `seo-schema` — detect existing schema, validate against Google's rich result types, generate missing JSON-LD (Article/BlogPosting, Organization, Person, BreadcrumbList). Save to `schema.json` in the post directory.

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
  ✓ GEO pass       → AI citation ready
  ✓ SEO score      → <N>/100
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

---

## Error handling

- **Missing file**: Report path not found, stop.
- **Skill fails**: Report which step failed, offer to retry that step only.
- **ImageMagick missing**: Skip crops, note in review gate, continue.
- **Composio channel fails**: Report error, continue other channels.
- **User types STOP at gate**: Cancel cleanly. All generated files are kept.

---

## Notes

- The review gate is non-negotiable — never auto-publish.
- Composio connections active: `medium`, `reddit`, `x`, `meta`, `linkedin`, `vercel`
- For Windows/PowerShell: ImageMagick commands use `magick` not `convert`
- Post variants are saved alongside the original — the wiki auto-commit hook picks them up
