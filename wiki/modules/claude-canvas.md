---
type: entity
title: "claude-canvas plugin"
created: 2026-05-26
updated: 2026-05-26
tags: [plugin, canvas, obsidian, visualization]
---

# claude-canvas Plugin

Obsidian Canvas creation and manipulation. 12 template archetypes, 6 layout algorithms.

## Stats
- Version: 1.0.0
- Skills: 8
- Agents: 3
- Entry: `skills/canvas/SKILL.md`

## Agents
- **canvas-composer** — full canvas orchestration
- **canvas-layout** — layout algorithm execution
- **canvas-media** — image/media node placement

## Skills (all pre-installed)
- `canvas` — orchestrator
- `canvas-create`, `canvas-populate`, `canvas-layout`, `canvas-present`
- `canvas-generate`, `canvas-template`, `canvas-export`

## Integration
- `canvas-generate` → dispatches `/banana` for image nodes (soft dependency)
- Obsidian Advanced Canvas plugin required for presenting
