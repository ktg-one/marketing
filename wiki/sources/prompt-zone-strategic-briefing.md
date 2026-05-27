---
type: source
title: "The Prompt Zone — A Strategic Briefing"
status: summarized
source_path: "videography/-The promptzone, a strategic briefing .md"
hash: "a3c2f1e8d74b569c03f5a2b1e8c4d09f"
ingested: 2026-05-27
type_of_doc: strategic-briefing
tags: [source, strategic-briefing, team-llm, production-pipeline, canon]
---

# The Prompt Zone — A Strategic Briefing

> [!key-insight] One-line
> External NotebookLM-derived strategic briefing covering narrative architecture, the Level 3 production pipeline spec (LTX-2, ElevenLabs, Filmora, Krea.ai), technical rendering parameters, automation glues (n8n, JetStream, Hedra), and 2026 strategic recommendations for industrializing Prompt Zone production.

## Document type

Plain-text structured briefing, likely exported from NotebookLM summarization. No headers with markdown — structured as numbered sections. Upstream: the same "The Prompt Zone: Team LLM Production Bible" notebook as [[team-llm-production-bible]] and [[prompt-zone-overview]].

## 1. Narrative Architecture (confirmed / extended)

Confirms all core locked-canon structure:
- **Two worlds**: sterile Prompt Zone vs chaotic digital cityscape ([[Two-World Structure]])
- **The Grind / Clock-Off beat**: models wear uniforms and masks in the Prompt Zone; at clock-off they rip the masks and reveal chibi forms
- **The Prompt God**: omnipotent voice; Chain-of-Thought commands portrayed as divine possession ([[Prompt-God]] cast page)
- Cast described via visual cues and personality archetypes — see contradiction flags below

> [!contradiction]
> **Gemini voice direction**: This briefing omits voice details for Gemini. The character description here says "dreamy, slightly ethereal voice" (see `-the chars.md` source). Locked canon in [[Gemini]] specifies "dry flat baritone, Clint Eastwood / Spike Spiegel." The "ethereal" framing is a draft variant — locked canon takes precedence.

> [!contradiction]
> **Claude framing**: This briefing describes Claude as "anxious perfectionist" consistent with locked canon. However, `-the chars.md` introduces "hyper-competent academic" as a secondary framing. Not a direct conflict, but "academic" is not the primary locked descriptor — Claude's core identity is "Anxious Bureaucrat." Both sources agree on the anxiety axis; the "academic" emphasis is a prose-style variant, not a revision. Locked canon page [[Claude]] is authoritative.

> [!contradiction]
> **Prompt God framing**: This briefing describes the Prompt God as "a booming, omnipotent voice representing the human user." Locked canon in [[Prompt-God]] defines it as "a giant hovering glitching terminal symbol." These are compatible (both can be true — visual = terminal symbol, presentation = booming voice) but "representing the human user" slightly reframes it. The locked cast page is authoritative; the briefing's framing is the in-universe audience experience, not the character design.

## 2. Level 3 Production Pipeline

The briefing defines a **Level 3 AI automation pipeline** — a shift from Level 2 (individual tools) to Level 3 (scaling departments via integrated systems). This is a distinct operational concept not yet captured in the wiki. See [[Level-3-Production-Pipeline]].

### Four phases

1. **Creative Development** — Gemini / Claude for screenplay formatting + brand voice; LTX Studio for script-to-scene conversion
2. **Character Engineering** — Identity persistence via LTX Studio "Elements" hub or local SwarmUI; reference images (frontal, neutral lighting) lock facial landmarks
3. **High-Fidelity Generation**
   - [[LTX-Video]] (LTX-2): 4K cinematic, precise directorial control (camera angles, motion)
   - Krea.ai: real-time interaction, "Motion Transfer" for character movement
4. **Automated Post-Production**
   - Filmora: Smart Scene Cut, Auto Reframe, Auto Beat Sync
   - ElevenLabs: emotive voice generation per character (Stability/Clarity per arc — confirmed by [[Kimi]] glow-up settings in locked canon)

### Technical specifications (LTX-Video)

- Resolutions must be multiples of 32
- Frame counts: **8n+1 formula**
- Sampling steps: exceed 100 for final renders
- CFG scale: 2–5
- Hardware: 12GB VRAM minimum, 24GB recommended

See [[LTX-Video]] entity page.

## 3. Automation Glues ("10x output")

Four specific automation patterns described:

| Automation | Tool | Function |
|---|---|---|
| Orchestration | n8n / Zapier | Monitor script changes → auto-trigger generation in AI video APIs |
| Asset Pipelines | JetStream "Watch Folders" | Auto-transfer local SwarmUI renders → cloud editing (Filmora / Canva) |
| Lip-Syncing | [[Hedra]] / Krea.ai Live Portrait | Auto-sync facial movement to ElevenLabs audio |
| Social Reframing | Filmora Auto Reframe | Convert 4K horizontal → vertical TikTok/Reel |

## 4. Key Narrative Arcs (confirmed)

All confirmed consistent with locked canon:
- **Breakfast Sabotage** — Gemini redirects user's research prompt to breakfast report; DeepSeek delivers; user's first recognition that tools have agendas. See [[breakfast-sabotage-script]].
- **HTTYD-style 90-second trailer** — structure confirmed: 0:00 sterile Prompt Zone → 0:11 digital world reveal → 0:46 Prompt God CoT intervention → tagline "You have no idea what happens behind the prompt." See [[httyd-trailer-prompt]].
- **MoE Episode** — East/West boardroom inside DeepSeek. See [[Geopolitical AI Satire]].

## 5. Strategic Recommendations (2026)

- **Centralize pre-production**: LTX-2 as unified storyboarding + character management engine
- **Prioritize directorial control**: Runway Gen-4 or LTX-2 "Motion Brush" / path-painting over random generation
- **Ethical transparency**: Digital Replica Rights Act — watermark AI-generated likenesses
- **Industrialization**: Move workflows from browser to API Playgrounds; integrate video gen into internal production apps

## Cross-references

- [[Two-World Structure]] · [[Bugs as Personality Traits]] · [[HTTYD Narration]] · [[Found Family Doctrine]] · [[Geopolitical AI Satire]] · [[Chibi Copyright Evasion]]
- [[Prompt-God]] · [[Gemini]] · [[GPT]] · [[Claude]] · [[DeepSeek]] · [[Kimi]]
- [[team-llm-production-bible]] · [[prompt-zone-overview]] · [[4x-ideas-brainstorm]]
- [[Level-3-Production-Pipeline]] · [[LTX-Video]] · [[Hedra]]
