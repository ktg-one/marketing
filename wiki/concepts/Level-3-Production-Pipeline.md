---
type: concept
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [concept, production, pipeline, team-llm, automation]
---

# Level 3 Production Pipeline

The industrialized AI animation pipeline for [[team-llm-production-bible|The Prompt Zone]]. Defined in [[prompt-zone-strategic-briefing]].

## The Level model

| Level | Description |
|---|---|
| Level 1 | Manual creation — human does everything |
| Level 2 | Individual AI tools assist at specific steps |
| **Level 3** | **Integrated systems scale entire departments via automated handoffs** |

The goal is Level 3: orchestrated tools that hand off to each other without human intervention between phases, achieving "industrial-grade output with minimal human overhead."

## The four phases

### Phase 1 — Creative Development

- **Tools**: Gemini / Claude (screenplay formatting, brand voice), LTX Studio (script → scene conversion)
- **Output**: Formatted scripts, scene breakdowns, brand-consistent dialogue

### Phase 2 — Character Engineering

- **Tools**: LTX Studio "Elements" hub or local SwarmUI
- **Method**: Reference images (frontal view, neutral lighting) lock facial landmarks for character persistence across scenes
- **Output**: Locked character identity assets that survive scene-to-scene generation

### Phase 3 — High-Fidelity Generation

| Tool | Function |
|---|---|
| [[LTX-Video]] (LTX-2) | 4K cinematic delivery; directorial control (camera angles, motion paths) |
| Krea.ai | Real-time interaction; "Motion Transfer" to apply movement to characters |

### Phase 4 — Automated Post-Production

| Tool | Function |
|---|---|
| Filmora | Smart Scene Cut · Auto Reframe (4K → vertical) · Auto Beat Sync |
| ElevenLabs | Emotive voice generation per character (Stability/Clarity per arc) |

ElevenLabs Stability/Clarity settings are character-specific — e.g., [[Kimi]]'s glow-up arc requires reduced Stability + boosted Clarity post-upgrade.

## Automation glues

Four automation patterns that connect phases without manual handoff:

| Glue | Tool | What it does |
|---|---|---|
| Script monitoring | n8n / Zapier | Detects script changes → triggers AI video API generation |
| Asset handoff | JetStream Watch Folders | Local SwarmUI renders → auto-transfer to Filmora / Canva cloud |
| Lip-sync | [[Hedra]] / Krea.ai Live Portrait | Auto-syncs character faces to ElevenLabs audio output |
| Social reframe | Filmora Auto Reframe | 4K horizontal → vertical TikTok/Reel |

## Technical specifications ([[LTX-Video]])

- Resolution: must be multiples of 32
- Frame counts: follow **8n+1 formula**
- Sampling steps: exceed 100 for final renders
- CFG scale: 2–5
- Hardware: 12GB VRAM minimum, 24GB recommended for smooth local processing

## 2026 strategic direction

From [[prompt-zone-strategic-briefing]]:
- **Centralize**: LTX-2 as unified storyboarding + character management (replace fragmented tools like Boords)
- **Directorial control**: Prefer Runway Gen-4 or LTX-2 path-painting over random generation
- **Ethical**: Watermark per Digital Replica Rights Act
- **Industrialize**: API Playgrounds over browser — integrate video gen into internal production apps

## Relationship to orchestration

The [[Team LLM Orchestration Roster]] defines which LLM agents do which cognitive tasks (Claude as spine, Gemini for research). Level 3 Pipeline defines which production tools handle which creative execution tasks. They operate in parallel: the orchestration layer produces content; the pipeline produces video.

## Cross-references

- [[prompt-zone-strategic-briefing]] — source
- [[LTX-Video]] · [[Hedra]] — key tool entities
- [[Team LLM Orchestration Roster]] — cognitive orchestration layer (distinct from this pipeline)
- [[team-llm-production-bible]] — what this pipeline produces
- [[Kimi]] — example of Stability/Clarity per-character ElevenLabs settings
