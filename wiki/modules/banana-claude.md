---
status: developing
type: entity
title: "banana-claude plugin"
created: 2026-05-26
updated: 2026-05-26
tags: [plugin, image-generation, gemini, skills]
---

# banana-claude Plugin

AI image generation engine — Gemini Nano Banana models via nanobanana-mcp. Central image provider for the entire ecosystem.

## Stats
- Version: 1.4.1
- Skills: 1 (`banana`)
- Agents: 1 (`brief-constructor`)
- Entry: `skills/banana/SKILL.md`

## Consumed By (6 dependents)
| Dependent | Plugin | Dependency |
|-----------|--------|------------|
| ads-generate | claude-ads | Hard |
| ads-photoshoot | claude-ads | Hard |
| visual-designer | claude-ads | Hard (MCP) |
| blog-image | claude-blog | Soft |
| seo-image-gen | claude-seo | Soft |
| canvas-generate | claude-canvas | Soft |

## Role in Ecosystem
Acts as the image generation backend for the entire plugin suite. Skills that need visuals (ads creative, blog hero images, canvas nodes, SEO images) all dispatch through banana.
