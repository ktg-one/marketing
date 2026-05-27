---
type: playbook
title: "Runtime Configuration"
created: 2026-05-26
updated: 2026-05-26
tags: [playbook, runtime, mcp, configuration]
---

# Runtime Configuration

## Active Runtime: OpenCode
All plugins loaded as skills in OpenCode. wp-mcp-ultimate configured to Claude Code sidecar.

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
