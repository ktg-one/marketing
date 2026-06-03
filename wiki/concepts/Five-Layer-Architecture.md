---
status: developing
updated: 2026-06-03
type: concept
title: "Five-Layer Architecture"
aliases: ["5-layer stack", "ktg-one stack", "Layer 1-5"]
created: 2026-05-27
tags: [concept, architecture, pipeline, orchestration, design-pattern]
---

# Five-Layer Architecture

The [[ktg-one]] stack model introduced (or formalised) in the rewritten `CLAUDE.md`. Five clearly separated layers from persistent state at the bottom to publishing at the top, with a non-bypassable [[Review-Gate]] at the Layer 5 boundary.

## The Stack

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

## Layer Descriptions

### Layer 1 — State (wiki/)

The knowledge graph. Persistent, append-only state that survives `/clear` and session resets. The Karpathy LLM Wiki Pattern makes this load-bearing: agents without the wiki have no user context.

Key files: `hot.md` (session cache), `index.md` (catalog), `sources/`, `entities/`, `concepts/`, `log.md` (append-only).

### Layer 2 — Plugins

The skill library. 7 plugins, ~80 skills. Skills are loaded on-demand by AI CLIs; never via `Read`. Each plugin has a `SKILL.md` with YAML frontmatter for discovery.

Plugins: `claude-blog`, `claude-seo`, `claude-ads`, `banana-claude`, `claude-canvas`, `best-practices`, `wp-mcp-ultimate`.

See [[Skill-Progressive-Disclosure]] for the loading discipline.

### Layer 3 — Orchestration

The brain of the pipeline. The `/hub <slug>` skill in `.claude/skills/hub/` is the primary entry point — it coordinates all plugins for a given post. Per-domain sub-orchestrators: `/blog`, `/ads`, `/seo`, `/canvas`.

Cross-plugin coordination is documented in `wiki/modules/pipeline-signals.md`.

### Layer 4 — Runtime

Where content is actually generated:
- `pipeline/run.sh` — working production (2s, bash templates, $0)
- `pipeline/ktg_pipeline/` — Python AI framework (~70% complete, 4 LLM providers, untested)
- `pipeline/publish-kit/<slug>/` — the [[Publish-Kit-Pattern]] output

### Layer 5 — Publishing

Outbound execution: Vercel deployment + [[Composio]] social firing. **Non-bypassable [[Review-Gate]]** sits at this boundary — no agent can cross without explicit per-post human `YES`.

## Cross-Cutting Concerns

Two systems span all layers:
- `.planning/` — [[GSD-Methodology]] (6-phase roadmap, phase verification criteria)
- `sccd/` — [[SCCD-Model]] (functional self-model, 1,600+ lines math + Python)

## Design Rationale

The separation matters because each layer has different change risk:
- Layer 1 (wiki) changes are additive, safe
- Layer 2 (plugins) changes affect all downstream orchestration
- Layer 5 changes have real-world side effects (posts fired, deploys triggered)

The [[Review-Gate]] at Layer 5 is the blast-radius containment mechanism.

## Cross-References
- [[ktg-one]] — the project this describes
- [[Review-Gate]] — the Layer 5 gate
- [[Publish-Kit-Pattern]] — Layer 4 output
- [[Skill-Progressive-Disclosure]] — Layer 2 loading discipline
- [[GSD-Methodology]] — cross-cutting planning layer
- [[SCCD-Model]] — cross-cutting functional model
- [[Composio]] — Layer 5 publishing connector
- [[claude-md-ktg-one]] — where this architecture is formally stated
