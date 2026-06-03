---
status: developing
type: entity
title: "claude-blog plugin"
created: 2026-05-26
updated: 2026-05-26
tags: [plugin, blog, wordpress, skills]
---

# claude-blog Plugin

Content creation pipeline with NotebookLM research → write → SEO check → publish.

## Stats
- Version: 1.6.9
- Skills: 22 (7 registered)
- Agents: 4
- Entry: `skills/blog/SKILL.md`

## Agents
- **blog-researcher** — statistics, source research
- **blog-writer** — article writing/rewriting
- **blog-seo** — post-writing SEO validation
- **blog-reviewer** — quality scoring

## Registered Skills (7/22)
- `blog` — orchestrator
- `blog-analyze`, `blog-write`, `blog-seo-check`, `blog-rewrite`, `blog-repurpose`, `blog-geo`

## Pending (15)
- blog-brief, blog-calendar, blog-strategy, blog-outline, blog-schema, blog-chart, blog-audit, blog-cannibalization, blog-factcheck, blog-persona, blog-taxonomy, blog-notebooklm, blog-audio, blog-image, blog-google

## Dependencies
- `blog-image` → banana-claude (nanobanana-mcp)
- `blog-seo-check` → mirrors claude-seo validation rules
- blog publish workflow → wp-mcp-ultimate (WordPress MCP)
