---
type: entity
title: "wp-mcp-ultimate"
created: 2026-05-26
updated: 2026-05-26
tags: [plugin, wordpress, mcp, pending]
---

# wp-mcp-ultimate

WordPress MCP server — bridges WordPress REST API into any AI runtime via MCP protocol. Not a skill — a PHP-based MCP server.

## Stats
- Version: 1.0.0 (npm)
- 58 WordPress abilities
- PHP plugin + Playwright e2e tests

## Integration Points
- MCP server exposes WordPress WP-CLI commands
- blog plugin targets it for publishing workflows
- blog-taxonomy → WP taxonomy management

## Setup Status
- **BLOCKED** — needs WordPress site URL
- Requires MCP transport configuration in OpenCode
- No skill transfer needed (it's an MCP server, not a skill)

## Actions Needed
1. User provides WordPress site URL
2. Configure as MCP server in OpenCode
3. Test wp-cli integration
4. Connect blog skills to publishing workflow
