---
type: entity
entity_type: product
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [entity, product, video-generation, production-tool, team-llm]
---

# LTX-Video (LTX-2)

AI video generation engine. Primary high-fidelity generation tool in the [[Level-3-Production-Pipeline]] for [[team-llm-production-bible|The Prompt Zone]].

## Role in pipeline

Phase 3 (High-Fidelity Generation) of the [[Level-3-Production-Pipeline]]. Handles 4K cinematic delivery with precise directorial control — camera angles, motion paths. Also used in Phase 2 (Character Engineering) via LTX Studio's "Elements" hub for facial landmark locking.

## Technical specifications

| Parameter | Value |
|---|---|
| Resolution | Must be multiples of 32 |
| Frame counts | 8n+1 formula |
| Sampling steps | Exceed 100 for final renders |
| CFG scale | 2–5 |
| VRAM (min) | 12GB |
| VRAM (recommended) | 24GB |

## Key capabilities

- **4K cinematic output** with directional control
- **LTX Studio "Elements" hub** — identity persistence; locks facial landmarks from a reference image (frontal, neutral lighting) across scenes
- **Motion Brush / path-painting** — preferred over random generation for directorial precision
- **Script → Scene**: LTX Studio converts scripts into discrete scenes and shots

## Positioning

Positioned as the unified pre-production and generation engine for 2026 — replacing fragmented tools (Boords for storyboarding, separate scene tools). Strategic recommendation is to centralize on LTX-2.

## Alternatives noted

- Krea.ai — real-time + Motion Transfer (used alongside LTX-2 in Phase 3)
- Runway Gen-4 — named as an alternative for directorial control (Motion Brush)

## Cross-references

- [[Level-3-Production-Pipeline]] — the pipeline this tool anchors
- [[prompt-zone-strategic-briefing]] — source document
- [[team-llm-production-bible]] — the production this tool serves
