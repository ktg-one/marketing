# Hub Pipeline — Operations Manual

The `/hub` pipeline takes a blog post and produces a publish-ready kit: 5 platform variants, a hero image, and a full SEO/GEO/schema package — before handing off to you for a final review.

---

## What it produces

One run on a post (`blog/your-post.md`) creates `pipeline/publish-kit/<slug>/`:

| File | What it is |
|------|-----------|
| `social-medium.md` | 800–1200 word Medium article |
| `social-reddit.md` | Reddit discussion post (r/ClaudeAI format) |
| `social-x-thread.md` | Hook tweet + 8–12 thread tweets |
| `social-meta.md` | Facebook/Meta scannable post |
| `social-linkedin.md` | 800–1200 word LinkedIn article |
| `hero-16x9.png` | Hero image at 16:9 |
| `hero-linkedin.png` | Cropped 1200×627 |
| `hero-x.png` | Cropped 1200×675 |
| `hero-square.png` | Cropped 1080×1080 |
| `GEO-ANALYSIS.md` | AI citation readiness score (0–100) + platform breakdown |
| `SEO-ANALYSIS.md` | On-page SEO audit + content quality score |
| `SEO-CHECKLIST.md` | Pass/fail checklist for 11 SEO items |
| `schema.json` | Valid JSON-LD (BlogPosting, Organization, Person, BreadcrumbList) |

---

## How to run it

```
/hub blog/your-post.md
```

That's it. The pipeline runs Steps 1–3 (repurpose → image → optimize), presents a review gate, then waits for your `YES` before doing anything with publish.

To force the offline local models instead of Gemini:
```
/hub blog/your-post.md --local
```

---

## Text generation — Google-first

All text tasks route through **Gemini** by default. Driver: `GEMINI_API_KEY` (already in your shell).

| Task | Model | What it does |
|------|-------|-------------|
| 5× repurpose | `gemini-3.5-flash` | Medium, Reddit, X, Meta, LinkedIn variants |
| GEO analysis | `gemini-3.5-flash` | AI citation readiness score |
| SEO audit | `gemini-3.5-flash` | On-page + content quality |
| Technical SEO | `gemini-3.5-flash` | Heading structure, links, meta |
| Schema JSON-LD | `gemini-3.5-flash` | Valid structured data |
| SEO checklist | `gemini-3.5-flash` | 11-item pass/fail |
| Hero draft / hard reasoning | `gemini-3-pro-preview` | escalate when Flash isn't enough |

Cost per post: **fractions of a cent** (Flash). **Voice:** inject `blog/user_voice.md` into every prompt or output drifts generic.

Verify the key before `/hub`:
```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" | head -c 200
```

Offline fallback only: `/hub <post> --local` routes text through Ollama (small local models, lower quality).

---

## Image generation — three options

### Option A: Gemini (Nano Banana 2) — recommended
**Cost:** ~$0.13/hero at 2K · **Quality:** excellent editorial/cinematic

1. Get an API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Set it in your shell profile (e.g. PowerShell `$PROFILE`) as `$env:GEMINI_API_KEY`
3. The pipeline calls it automatically

The banana-claude plugin has an MCP install path for deeper integration:
```bash
bash .claude/plugins/banana-claude/install.sh
```
After install, `/banana generate <prompt>` works as a standalone command.

### Option B: Grok (xAI Aurora)
**Cost:** included in Grok subscription or via API · **Quality:** strong photorealistic

Grok's Aurora model generates images via the xAI API. To wire it:

1. Get API key from [console.x.ai](https://console.x.ai)
2. Set `$env:XAI_API_KEY` in your shell profile
3. The hub skill can call it via the xAI REST endpoint:
   ```
   POST https://api.x.ai/v1/images/generations
   model: grok-2-image-1212
   prompt: <your prompt>
   ```

At the moment the hub defaults to Gemini for images. To use Grok: call it manually with the crafted prompt from the hub output, or wire a `_run_image_grok.py` script (same pattern as `_run_repurpose.py`).

### Option C: Local (ComfyUI / Automatic1111 on your 5070)
**Cost:** $0 · **Quality:** depends on workflow/model · **Speed:** fast with NVFP4

ComfyUI (recommended):
1. Start ComfyUI: open it on `localhost:8188`
2. Load your NVFP4 workflow
3. Use the image prompt from the hub output as your positive prompt
4. Save output as `hero-16x9.png` to `pipeline/publish-kit/<slug>/`

Automatic1111:
1. Start with `--api` flag: `webui.bat --api`
2. POST to `http://localhost:7860/sdapi/v1/txt2img`
3. Same prompt → save to the publish-kit directory

The hub's image prompt is designed to work across all three backends — it's a visual brief, not model-specific syntax.

---

## Reading the outputs

**GEO-ANALYSIS.md** — check the score and platform breakdown. A score of 60+ means AI search engines can cite your post. Common fix: add more direct-answer paragraphs (120–180 words each with a clear claim).

**SEO-ANALYSIS.md** — overall score + category breakdown. Anything under 60 in a category has prioritized fixes listed.

**SEO-CHECKLIST.md** — 11 binary items. Fix every `[FAIL]` before publishing. Takes 10 minutes.

**schema.json** — paste into your post's `<head>` inside `<script type="application/ld+json">`. Validates at [validator.schema.org](https://validator.schema.org).

**Social variants** — read each one before copy-pasting. Ministral is good but occasionally produces filler openers ("In today's..."). Edit those out.

---

## The review gate

After Steps 1–3, the pipeline stops and shows a full summary:

```
═══════════════════════════════════════
  KTG HUB — READY TO PUBLISH
═══════════════════════════════════════
  ✓ 5 variants        ✓ images
  ✓ GEO score: 72     ✓ SEO score: 68
  ✓ schema.json
═══════════════════════════════════════
```

Type `YES` to continue to Vercel deploy + Composio social posts.
Type `STOP` to cancel — all generated files are kept.

**This gate cannot be bypassed.** Even `/loop` stops here.

---

## Cost summary

| Task | Cost |
|------|------|
| 5 platform repurpose variants | ~$0.00X (Gemini Flash) |
| GEO + SEO + schema + checklist | ~$0.00X (Gemini Flash) |
| Hero image (Gemini 2K) | ~$0.13 |
| Hero image (Grok) | API rate or subscription |
| Hero image (local 5070) | ~$0.01 electricity |
| Social publishing (Composio) | Free tier / subscription |
| **Total per post (text only)** | **~$0.01** |
| **Total per post (with Gemini image)** | **~$0.14** |

---

## Quick troubleshoot

| Problem | Fix |
|---------|-----|
| GEMINI_API_KEY unset | Set it in your shell profile; verify with the model-list curl above |
| Gemini 429 rate limit | Back off; retry failed step; drop to `gemini-3.5-flash-lite` if sustained |
| Output sounds generic | Voice ruleset not injected — pass `blog/user_voice.md` into the prompt |
| Gemini 403 key leaked | Generate new key at aistudio.google.com/apikey |
| ImageMagick missing (no crops) | `winget install ImageMagick.ImageMagick` |
| Composio timeout | Retry the publish step; all generated files survive the timeout |
