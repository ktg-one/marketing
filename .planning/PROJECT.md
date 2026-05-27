# AI Content Hub — KTG

## What This Is

A single `/hub` command that orchestrates the full content creation lifecycle — from idea capture and planning through writing, repurposing, image generation, SEO optimization, ad creation, and multi-channel publishing. Integrates all available plugins (blog, ads, SEO, image gen, WordPress, canvas) into a coherent autonomous pipeline.

## Core Value

Drop a piece of content (idea, draft, note) and run `/hub` — the system handles every downstream step without manual intervention: repurpose for all platforms, generate visuals, optimize for AI/SEO, create ad variants, and publish.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Unified `/hub` command that intelligently routes content through all plugin pipelines
- [ ] Blog pipeline: write, repurpose (X/LinkedIn/Reddit/newsletter), GEO optimize, SEO check, schema
- [ ] Image pipeline: hero image + platform crops via banana (Gemini Nano)
- [ ] Ads pipeline: generate ad variants (Google, Meta, LinkedIn, TikTok) from repurposed content
- [ ] SEO pipeline: audit, cluster strategy, technical SEO, content briefs
- [ ] WordPress publishing via wp-mcp-ultimate
- [ ] Canvas planning entry point for visual ideation
- [ ] Composio multi-channel publishing (Reddit, LinkedIn, Vercel)
- [ ] Pre-publish review gate with green-light confirmation
- [ ] Plugins auto-discovered and routed based on content type

### Out of Scope

- Editorial calendar UI — deferred to v2
- Analytics dashboard — deferred to v2
- Custom plugin development — all plugins already exist
- Multi-user/team features — single-user tool

## Context

This project runs on Windows (PowerShell) using OpenCode. Available plugins:
- `claude-blog-main` — 22 skills (write, repurpose, geo, seo-check, schema, strategy)
- `claude-ads` — 22 skills (create, generate, google, meta, tiktok, linkedin, youtube, amazon)
- `claude-seo` — 25 skills (audit, backlinks, cluster, geo, schema, technical, content briefs)
- `banana-claude` — image generation via Gemini Nano
- `claude-canvas` — visual planning and canvas creation
- `wordpress-mcp-ultimate` — WordPress publishing via MCP
- `best-practices-main` — development best practices

Existing hub skill at `.claude/skills/hub/SKILL.md` handles blog pipeline. Needs extension to integrate ads, SEO, and WordPress.

Composio MCP connections active: Reddit, LinkedIn, Vercel, Gmail, Google Drive, Discord, YouTube, GitHub.

## Constraints

- **Platform**: Windows, PowerShell — all commands must work in this environment
- **CLI tools**: `gemini` CLI and `claude` CLI available for multi-model orchestration
- **No n8n**: n8n auth broken — route all automation through OpenCode/CLI
- **Skill invocation**: skills cannot call other skills directly — use Skill tool or CLI delegation
- **Token budget**: sequential skill invocations accumulate context — use forked subagents for heavy steps

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Multi-model orchestration | gemini for research, claude for synthesis/roadmap | — Pending |
| Hub as project-local skill | Not a distributable plugin — single vault workflow | — Pending |
| Composio for publishing | n8n auth broken, Composio connections already active | — Pending |

---
*Last updated: 2026-05-26 after scope expansion*
