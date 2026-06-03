---
status: developing
created: 2026-06-03
updated: 2026-06-03
type: source
title: "CLAUDE.md — ktg-one (5-Layer Architecture Reference)"
slug: claude-md-ktg-one
source_path: "CLAUDE.md"
source_type: project-config
ingested_at: 2026-05-27
tags: [source, project-config, architecture, pipeline, publishing, canon]
hash: md5:b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7
---

# CLAUDE.md — ktg-one

> Claude Code behavioral guide for ktg-one. Recently rewritten to encode the [[Five-Layer-Architecture]] explicitly. Declares itself subordinate to `AGENTS.md` when in conflict.

## Summary

CLAUDE.md is the Claude Code-specific orientation file for the ktg-one workspace. The latest revision introduced an explicit five-layer stack diagram as the primary architecture frame. It serves as the read-first doc for Claude Code sessions, points to the fuller AGENTS.md for deep context, and encodes the locked creative canon (cast, voice, orchestration roster).

## Five-Layer Architecture

```
Layer 5  PUBLISHING       Vercel · Composio (Reddit/LinkedIn) · WordPress
                          ⛔ Non-bypassable per-post REVIEW GATE
                             (state lives in wiki, survives /clear)
─────────────────────────────────────────────────────────────────────────
Layer 4  RUNTIME          pipeline/run.sh (2s bash, working production)
                          pipeline/ktg_pipeline/ (Python AI, ~70% untested)
                          pipeline/publish-kit/<slug>/ — 8 files per post
─────────────────────────────────────────────────────────────────────────
Layer 3  ORCHESTRATION    .claude/skills/hub/  →  /hub <slug>
                          Per-domain sub-orchestrators: /blog /ads /seo /canvas
─────────────────────────────────────────────────────────────────────────
Layer 2  PLUGINS          .claude/plugins/ — 7 plugins
                          claude-blog · claude-seo · claude-ads
                          banana-claude (image engine) · claude-canvas
                          best-practices · wp-mcp-ultimate (WP gateway)
─────────────────────────────────────────────────────────────────────────
Layer 1  STATE (wiki/)    hot.md → index.md → sources/entities/concepts/
                          intel/ playbooks/ modules/ log.md (append-only)
```

Cross-cutting concerns: `.planning/` ([[GSD-Methodology]] — 6-phase roadmap), `sccd/` ([[SCCD-Model]] — 1,600 lines math + Python), multi-CLI roster.

## Read-First Protocol

Session start order:
1. `wiki/hot.md` — rolling ~500-token context cache
2. `wiki/index.md` — master catalog
3. `AGENTS.md` — authoritative big-doc (overrides this file)
4. `PROJECT_STATE.md` — current pipeline status
5. `wiki/modules/index.md` — plugin ecosystem map

> **Karpathy LLM Wiki Pattern (canon):** reading the wiki INTO context is load-bearing, not optional. Ingesting new sources without first loading existing state breaks the graph.

## Plugin Pipeline Shapes

- **Blog**: sequential `brief → outline → write` + parallel factcheck + image at write step → `seo-check → schema → geo → repurpose`
- **SEO audit**: 8+ specialist agents in parallel → aggregated Health Score 0–100 → prioritised action plan
- **Ads**: `dna → create → generate`, `photoshoot` as branch
- **Canvas**: `create → populate → layout → export` or `/generate <desc>`

Cross-plugin: `banana-claude` is the image engine for ads/blog/seo/canvas. `wp-mcp-ultimate` is the WordPress gateway.

## Locked Canon

| Item | Source |
|---|---|
| Cast (11 characters) | `videography/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md` + `wiki/voice/cast/` |
| Creative engine | Technical LLM flaws = character flaws |
| Copyright evasion | Chibi designs, shape language, palettes — never logos ([[Chibi Copyright Evasion]]) |
| House voice | Myth-Hilarity + Tech Anthropology — `blog/user_voice.md` + `wiki/voice/myth-hilarity-tech-anthropology.md` |
| CLI orchestration roster | Claude=spine, Gemini=research, Codex=mechanical, Jules=async |

## Sister Projects

- `C:/Users/kevin/knowledge2026/` — parent wiki vault
- `C:/Users/kevin/Desktop/ktg-one/` + `goodai-mate/` — Next.js sites (separate repos)
- `LEGIO/`, `Recursive-Council/` — under `C:/Users/kevin/knowledge2026/Projects-Coding/`

## Duplication Note

The behavioral rules referenced at the end of AGENTS.md ("Think Before Coding", "Simplicity First", "Surgical Changes", "Goal-Driven Execution") originate from the upstream [[Best-Practices-Kernel]] plugin. CLAUDE.md does NOT re-list them explicitly — it relies on the plugin being loaded. This is cleaner than AGENTS.md which re-states them in section 5. Treat the plugin as the single definition point.

## Cross-References
- [[ktg-one]] — project entity
- [[Five-Layer-Architecture]] — the stack model documented here
- [[Review-Gate]] — layer 5 gate
- [[GSD-Methodology]] — cross-cutting planning layer
- [[SCCD-Model]] — cross-cutting functional model
- [[Best-Practices-Kernel]] — upstream plugin principles
- [[Composio]] — publishing connector
- [[Chibi Copyright Evasion]] — locked visual rule
- [[myth-hilarity-tech-anthropology]] — locked voice
- [[Team LLM Orchestration Roster]] — CLI roles
