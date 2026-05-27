# How to Use the KTG Content Pipeline

## Quick Start (30 seconds)

```bash
# 1. Add your blog post
cp your-post.md pipeline/input/

# 2. Run pipeline
bash pipeline/run.sh pipeline/input/your-post.md

# 3. Go to publish kit
cd pipeline/publish-kit/your-post-slug/

# 4. Follow README.md to publish
```

## Input Format

Your blog post needs YAML frontmatter:

```yaml
---
title: "Your Title Here"
slug: "your-url-slug"
topic: "AI, Technology"
tone: "professional"
target_audience: "tech professionals"
key_points:
  - Point one
  - Point two
call_to_action: "Subscribe for more"
---

# Your Content Here

Write in markdown.
```

## What Gets Generated

| Folder | Contents |
|--------|----------|
| `output/social/` | 5 platform variants |
| `output/seo/` | Meta tags, schema, keywords |
| `output/ads/` | Google, Meta, LinkedIn ads |
| `output/images/` | Image briefs (generate separately) |
| `publish-kit/{slug}/` | Copy-paste ready files |

## Publishing Order

1. **Review** — Check `review-checklist.md`
2. **Images** — Generate 4 images (Google AI Studio prompts provided)
3. **Blog** — Deploy to Vercel first (get canonical URL)
4. **Medium** — Import story, add canonical link
5. **LinkedIn** — Copy from `linkedin.txt`
6. **Reddit** — Copy from `reddit.txt`
7. **X** — Copy thread from `x-thread.txt` (post 1 by 1)
8. **Meta** — Copy from `meta.txt`

## Buffer Alternative

Upload `buffer.csv` to buffer.com for scheduled posting to X, Meta, LinkedIn.

## Current Limitations

- Images: Generate separately (prompts provided, not auto-generated yet)
- Publishing: Manual copy-paste (APIs block auto-post for X/Meta)
- Repurposing: Template-based (not AI-enhanced yet)
