---
status: developing
type: entity
title: "claude-ads plugin"
created: 2026-05-26
updated: 2026-05-26
tags: [plugin, ads, marketing, skills]
---

# claude-ads Plugin

Multi-platform ad auditing and creation suite. 80 Google Ads checks, 50 Meta Ads checks.

## Stats
- Version: 1.7.0
- Skills: 22 (6 registered)
- Agents: 10
- Entry: `skills/ads/SKILL.md`

## Agents
- **audit-google** — Google Ads audit (80 checks)
- **audit-meta** — Meta Ads audit (50 checks)
- **audit-creative** — LinkedIn/TikTok/Microsoft creative
- **audit-tracking** — Conversion tracking audit
- **audit-budget** — Budget analysis
- **audit-compliance** — Compliance verification
- **creative-strategist** — Campaign concept strategy
- **visual-designer** — AI image generation (banana MCP)
- **copy-writer** — Headlines, CTAs, primary text
- **format-adapter** — Asset dimension validation

## Registered Skills (6/22)
- `ads` — orchestrator
- `ads-google`, `ads-meta`, `ads-audit`, `ads-youtube`, `ads-creative`

## Hard Dependencies
- `ads-generate`, `ads-photoshoot`, `visual-designer` → banana-claude (required)
