---
status: developing
type: playbook
title: "Runtime Configuration"
created: 2026-05-26
updated: 2026-05-26
tags: [playbook, runtime, mcp, configuration]
---

# Runtime Configuration

> [!contradiction] 2026-06-03 — Runtime is Claude Code, not OpenCode
> The "Active Runtime: OpenCode" line below is **superseded**. The runtime is **Claude Code**, with `/hub` orchestration (Layer 3 of the [[Five-Layer-Architecture]]) and the [[ktg-hub-Plugin]] packaged as both a Claude Code plugin and a Claude Cowork `.plugin`. Orchestration + publish use the Claude Agent SDK ([[Agent-SDK-Orchestration]]). Treat references to "OpenCode" below as historical. The plugin → runtime mapping should be read as Claude Code, not OpenCode.

## Active Runtime: ~~OpenCode~~ Claude Code
~~All plugins loaded as skills in OpenCode.~~ Plugins load as skills/agents in **Claude Code** via `/hub` orchestration. wp-mcp-ultimate configured to Claude Code sidecar.

## Plugin → Runtime Mapping

| Plugin | Runtime | Status |
|--------|---------|--------|
| claude-blog | OpenCode | Skills registered (7/22) |
| claude-ads | OpenCode | Skills registered (6/22) |
| claude-seo | OpenCode | Pre-installed (seo-* skills) |
| banana-claude | OpenCode | Pre-installed |
| claude-canvas | OpenCode | Pre-installed |
| best-practices | OpenCode | Pre-installed |
| wp-mcp-ultimate | Claude Code (sidecar) | Configured — needs WP URL |

## MCP Servers Used

| Server | Plugin Consumer | Purpose |
|--------|----------------|---------|
| nanobanana-mcp | banana-claude | Gemini image generation |
| wp-mcp-ultimate | blog (planned) | WordPress REST API |
| DataForSEO | seo (extension) | Live SERP/keyword data |
| Firecrawl | seo (extension) | Full-site crawling |
| chrome-devtools | seo | Screenshots, rendering checks |
