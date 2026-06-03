---
status: developing
type: concept
title: "Plugin Pipeline Signals"
created: 2026-05-26
updated: 2026-05-26
tags: [pipeline, signals, orchestration, architecture]
---

# Plugin Pipeline Signals — Sequential & Parallel Flows

## Runtime
All plugins built for **Claude Code** (Tier 4 Agent Skills). Loaded in OpenCode via skill registry. Cross-platform via AGENTS.md for Cursor/Gemini CLI.

## Blog Pipeline (claude-blog)
```
notebooklm (research source-grounded)
    ↓
brief (content brief + competitive analysis)
    ↓
outline (SERP-informed)
    ↓
write (template selection → draft → TL;DR → citations)
    ├── factcheck (parallel — verify statistics)
    └── image (parallel — hero + inline visuals via banana)
    ↓
seo-check (post-writing validation)
    ↓
schema (JSON-LD generation)
    ↓
geo (AI citation audit)
    ↓
repurpose (multi-platform distribution)
```

**Quality gate at analyze (0-100 score):** can be inserted between any steps.

## Ads Pipeline (claude-ads)
```
dna <url> → brand-profile.json
    ↓
create → campaign-brief.md (reads profile + optional audit)
    ↓
generate → ad-assets/ (reads brief + profile)
    ↓
photoshoot → product photos in 5 styles (standalone or via profile)
```

**Audit pipeline:**
```
context intake → detect industry/platform → spawn 6 parallel agents →
validate JSON scores → aggregate → Ads Health Score (0-100) → action plan with Quick Wins
```

## SEO Audit Pipeline (claude-seo)
```
detect business type → spawn 8+ parallel agents →
(technical, content, schema, sitemap, performance, visual, geo +
conditional: google, local, maps, backlinks, cluster, ecommerce, drift, sxo)
→ SEO Health Score (0-100) → prioritized action plan (Critical→High→Medium→Low)
→ optional PDF report
```

## Canvas Pipeline (claude-canvas)
```
create (blank or 12 template archetypes)
    ↓
populate (add nodes: image/text/banana/mermaid/svg/gif)
    ├── connect (edges between nodes)
    └── zone (group nodes with colors)
    ↓
layout (6 algorithms: grid/dagre/radial/force/linear/auto)
    ↓
export (PNG/SVG/PDF)
```

**Alternative:** `generate <description>` → full AI-orchestrated (all steps auto).

## Cross-Plugin Dependency Graph
```
banana-claude (image engine)
  ├── ads-generate (hard)
  ├── ads-photoshoot (hard)
  ├── ads/visual-designer agent (hard — MCP calls)
  ├── blog-image (soft — graceful fallback)
  ├── seo-image-gen (soft — install instructions)
  └── canvas-generate (soft — dispatches /banana)

wp-mcp-ultimate (WordPress gateway)
  └── blog-taxonomy (MCP integration)
  └── blog publish workflow (planned)

blog-seo-check ← mirrors claude-seo validation rules (conceptual)
```

## Key Design Patterns

1. **Orchestrator → Sub-skill routing** — All plugins use `/plugin command` syntax with operator sub-skill loaded based on first arg
2. **Parallel subagent delegation** — Audit commands spawn agents concurrently via Task tool with `context: fork`
3. **Sequential creative pipelines** — Content creation uses strict step ordering (output from step N feeds step N+1)
4. **Cross-plugin via MCP** — Banana provides image service, wp-mcp provides WordPress service
5. **Progressive disclosure** — SKILL.md is entry point, references/ loaded on-demand, never all at once
