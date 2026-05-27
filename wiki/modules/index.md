---
type: meta
title: "Modules — Plugin Ecosystem"
created: 2026-05-26
updated: 2026-05-26
tags: [meta, index, modules, plugins]
---

# Plugin Ecosystem — Master Index

7 plugins, 79 skills, 40 agents — transferred from `.claude/plugins/` into AI-agnostic skill format.

## Plugins

| Plugin | Skills | Agents | Status |
|--------|--------|--------|--------|
| [[modules/claude-blog|claude-blog]] | 22 | 4 | Registered (7 of 22) |
| [[modules/claude-seo|claude-seo]] | 25 | 22 | Pre-installed in OpenCode |
| [[modules/claude-ads|claude-ads]] | 22 | 10 | Registered (6 of 22) |
| [[modules/banana-claude|banana-claude]] | 1 | 1 | Pre-installed |
| [[modules/claude-canvas|claude-canvas]] | 8 | 3 | Pre-installed |
| [[modules/best-practices|best-practices]] | 1 | 1 | Pre-installed |
| [[modules/wp-mcp-ultimate|wp-mcp-ultimate]] | — | — | Pending (needs WP URL) |

## Key Design Patterns

- [[playbooks/karpathy-llm-wiki|Karpathy LLM Wiki Pattern]] — all plugins use this architecture
- [[modules/cross-plugin-dependencies|Cross-Plugin Dependency Model]] — banana as image engine, wp-mcp as WordPress gateway
- [[modules/agent-roster|Agent Roster]] — 40 specialist agents across all plugins

## Registration Progress

- **79 total skills** across 7 plugins
- **13 registered** this session (6 ads + 7 blog)
- **31 pending** (16 ads + 15 blog)
- **28 pre-installed** in OpenCode (seo-*, banana, canvas-*, best-practices, karpathy-guidelines, no-workarounds)
- **4 skipped** (codex-seo overlap)
- **3 non-skill** (wp-mcp-ultimate is MCP server, no transfer needed)
