---
name: hub-swarm
description: >
  KTG content marketing pipeline — SWARM MODE. Orchestrates 7 plugins
  via parallel agent dispatch. Drop a post, get it published everywhere
  with maximum parallelism. Agents run simultaneously, not sequentially.
user-invokable: true
argument-hint: "<post-file-path>"
disable-model-invocation: false
metadata:
  author: ktg
  version: "2.0.0"
---

# Hub-Swarm: Parallel Content Pipeline

Drop a post. Spawn agents. Publish everywhere.

## Architecture

```
PHASE 0: VALIDATE (Sequential — fast)
  └─ best-practices-main: shipping-rules check
  └─ Validate input file exists, extract title/slug

PHASE 1: SWARM DISPATCH (Parallel — all agents at once)
  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
  │ CONTENT     │ │ IMAGES      │ │ SEO         │
  │ blog-writer │ │ banana      │ │ seo-geo     │
  │ or          │ │ brief-      │ │ seo-page    │
  │ blog-       │ │ constructor │ │ seo-schema  │
  │ repurpose   │ │             │ │             │
  └─────────────┘ └─────────────┘ └─────────────┘
  ┌─────────────┐ ┌─────────────┐
  │ ADS         │ │ CANVAS      │
  │ creative-   │ │ canvas-     │
  │ strategist  │ │ composer    │
  │ copy-writer │ │             │
  │ visual-     │ │             │
  │ designer    │ │             │
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

## Swarm Agent Definitions

### Content Swarm

```yaml
agent: blog-writer
plugin: claude-blog-main
parallel: true
condition: draft_incomplete
task: Write blog post from brief. Follow Myth-Hilarity voice.
output: post.md

agent: blog-repurpose
plugin: claude-blog-main
parallel: true
condition: draft_complete
task: Repurpose post for ALL platforms: X, LinkedIn, Reddit, email.
output: social-*.md (4 files)
```

### Image Swarm

```yaml
agent: banana-brief
plugin: banana-claude
parallel: true
dependency: content_swarm_started
task: Generate hero image from post title + summary.
output: hero-16x9.png

agent: image-crop
plugin: banana-claude
parallel: true
dependency: hero_generated
task: Crop hero for platforms: LinkedIn, X, Square.
output: hero-*.png (4 files)
```

### SEO Swarm

```yaml
agent: seo-geo
plugin: claude-seo
parallel: true
dependency: content_complete
task: Optimize for AI citation: answer blocks, question H2s, llms.txt.
output: GEO-ANALYSIS.md

agent: seo-page
plugin: claude-seo
parallel: true
dependency: content_complete
task: On-page SEO audit: title, meta, headings, content quality.
output: SEO score

agent: seo-schema
plugin: claude-seo
parallel: true
dependency: content_complete
task: Generate JSON-LD schema: Article, Organization, BreadcrumbList.
output: schema.json
```

### Ads Swarm

```yaml
agent: creative-strategist
plugin: claude-ads
parallel: true
dependency: content_complete
task: Generate campaign concepts from brand profile + post content.
output: campaign-brief.md

agent: copy-writer
plugin: claude-ads
parallel: true
dependency: creative_strategy_complete
task: Write ad copy for Google, Meta, LinkedIn, TikTok.
output: ad-*.md (4 files)

agent: visual-designer
plugin: claude-ads
parallel: true
dependency: hero_generated
task: Design ad creatives from hero image + copy.
output: ad-creative-*.png
```

### Canvas Swarm (Optional)

```yaml
agent: canvas-composer
plugin: claude-canvas
parallel: true
condition: user_requested_visual_planning
task: Create visual canvas from post content.
output: post.canvas
```

---

## Dependency Graph

```
validate_input
    ├── blog_writer ──┐
    │                 ├──→ all_seo_agents (parallel)
    ├── blog_repurpose┤   ├──→ creative_strategist ──→ copy_writer
    │                 │   │
    └── banana_brief ─┼───┼──→ image_crop
                      │   │
                      └───┴──→ visual_designer
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
  Email: <word_count> words

IMAGES:
  Hero 16:9, LinkedIn crop, X crop, Square crop

SEO:
  GEO score: <N>/100
  SEO score: <N>/100
  Schema: <types>

ADS:
  Google Ads: <headline_count> headlines
  Meta Ads: <headline_count> headlines
  LinkedIn Ads: <headline_count> headlines
  TikTok Ads: <headline_count> headlines

CANVAS:
  <yes/no> Visual planning

CHANNELS:
  Vercel, WordPress, Reddit, LinkedIn, X, Google Ads, Meta Ads

Type YES to publish all, SKIP <channel> to exclude, STOP to cancel.
```

---

## Performance

| Phase | Sequential | Swarm | Speedup |
|-------|-----------|-------|---------|
| Validate | 1s | 1s | 1x |
| Content | 60s | 60s | 1x |
| Images | 30s | 30s | parallel |
| SEO | 45s | 15s | 3x |
| Ads | 60s | 20s | 3x |
| Canvas | 30s | 30s | optional |
| **Total** | **~226s** | **~90s** | **2.5x** |

---

## Error Handling

- Agent timeout: Report which agent timed out. Continue with others.
- Agent failure: Report failure. Offer to retry that agent only.
- Partial swarm: If 3 of 4 SEO agents succeed, use partial results.
- Dependency failure: If banana fails, image_crop and visual_designer skip gracefully.

---

## Notes

- Swarm uses Agent tool with subagent_type: general for parallel execution
- Each agent gets its own context budget — no shared state
- Results gathered via manifest, not conversation memory
- Review gate is the only sequential bottleneck (by design)
- Post-publish: wiki log entry, hot cache update
