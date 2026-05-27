---
type: decision
title: "Claude Code Config — KTG-one Project Setup"
created: 2026-05-26
updated: 2026-05-26
decision_date: 2026-05-26
status: active
tags:
  - meta
  - claude-code
  - config
  - hooks
related:
  - "[[2026-05-16-vault-bootstrap-session]]"
---

# Claude Code Config — KTG-one Project Setup

## What was decided

`.claude/settings.json` was created for this project. Previously, hook definitions existed in `.claude/hooks/hooks.json` and `.claude/hooks/hooks-claude-canvas.json` but were never activated — Claude Code only reads hooks from `settings.json`, not standalone JSON files.

## Hook structure (live as of 2026-05-26)

| Hook | Trigger | What it does |
|---|---|---|
| `SessionStart` | Every session open | Loads `wiki/hot.md` into context; prompts Claude to read it silently |
| `PreCompact` | Before context compaction | Prompts Claude to write current session state to `wiki/hot.md` |
| `PostCompact` | After context compaction | Prompts Claude to re-read `wiki/hot.md` (restores context lost in compaction) |
| `PostToolUse Write\|Edit` | After any file write or edit | Auto-commits `wiki/`, `.raw/`, `.vault-meta/` to git (no-ops if no git repo) + validates `.canvas` files |
| `Stop` | When Claude stops | Outputs `systemMessage` reminding to update `hot.md` if wiki pages changed |

## The PreCompact → PostCompact loop

The key insight: hook-injected context does **not** survive compaction. The loop is:

1. `PreCompact` → Claude writes fresh state to `wiki/hot.md`
2. Compaction runs (context is summarised, old turns dropped)
3. `PostCompact` → Claude re-reads `wiki/hot.md`

Result: continuity survives the compaction boundary.

## agentmemory

First use of `mcp__agentmemory__memory_save` confirmed working. Three memories saved to the agentmemory MCP server this session:
- KTG-one project architecture (vault structure, four streams)
- Settings.json hook structure
- Plugin/agent/command inventory

agentmemory persists across sessions independently of `hot.md` — more robust for structural facts that don't change session to session.

## Plugin configuration

`claude-obsidian` and `canvas` plugins are enabled **globally** in `~/.claude/settings.json` — no project-level enablement needed. Project-level `.claude/` provides:
- `commands/` — slash commands: `/canvas`, `/wiki`, `/autoresearch`, `/save`
- `agents/` — subagents: `brief-constructor`, `canvas-composer`, `canvas-layout`, `canvas-media`, `wiki-ingest`, `wiki-lint`
- `skills/` — project-local skills (currently empty; skills come from global plugin install)

## Known issue

`.claude/config.json` has broken JSON syntax (missing closing bracket and brace). It is not a valid Claude Code config filename and does nothing — ignore it. `settings.json` is the canonical config.
