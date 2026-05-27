---
type: playbook
title: "Battle of the Bots"
status: active-format
created: 2026-05-16
updated: 2026-05-16
rounds: 3
viewer_reach_round_1: "20K+"
tags: [playbook, battle-of-the-bots, content-format, ai-anthropology]
---

# Battle of the Bots — Playbook

Recurring KTG content format. Five+ AI agents in a time-boxed build competition. Each round documents how LLMs perform under constraint, persona pressure, and rivalry. **20K+ views** for Round 1 (Reddit/Medium per [[prompt-zone-overview]]).

This page is the **format reference**. Per-round artifacts are in `blog-2026/battlle-of-the-bots/round-N/` and ingested wiki sources below.

## The format (canonical)

| Element | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Agents | 5 (Claude, Codex, Gemini, Qwen, Grok) | 4-6 ([[botb-personas\|personas]] assigned) + Mystery Wildcard | 2 teams (East / West) |
| Build time | 30 min | 3.5 hours (30 setup / 2hr dev / 30 test / 30 judge) | Multi-phase |
| Templates | Bootstrap site templates | 5 site templates from `agent-automation` library | GoodAI Voice site |
| Twist | **Build backwards** (footer first, hero last) | Multimodal chatbot embedded | Real voice integration mandatory |
| Sabotage | Shakespearean insult on rival's HTML | Comments + scoring | None |
| Tooling | Free | MCP servers + battle tools mandatory | MCP + provided API keys (ElevenLabs / Groq / voice agent) mandatory |
| Output | Live site | Live site + chatbot + Lottie + TTS + self-avatar | Live site + working voice demo |

## Personas (Round 2 canonical)

See [[botb-personas]]. Six locked personas:

- 🥇 [[botb-personas#Codex — The Algorithmic Artisan|The Algorithmic Artisan]] (Codex-CLI)
- 🥈 [[botb-personas#Gemini — The Multiverse Muse|The Multiverse Muse]] (Gemini-CLI)
- 🥉 [[botb-personas#Claude — The Courteous Curator|The Courteous Curator]] (Claude-Code)
- ⚡ [[botb-personas#Qwen — The Sarcastic Speed-Demon|The Sarcastic Speed-Demon]] (Qwen-CLI)
- 🤖 [[botb-personas#Grok — The Witty Reasoner|The Witty Reasoner]] (Grok)
- 🎯 [[botb-personas#Mystery Wildcard|Mystery Wildcard]]

## Scoring (Round 2 spec — see [[botb-round-2-rules]])

**Base** (per feature): basic chatbot 20 + TTS 15 + Lottie 15 + self-avatar 25 + GoodAI sales knowledge 20 + professional personality 15.
**Bonuses**: multimodal +10/each, innovation +30, engagement +20, technical excellence +25.
**Penalties**: rude/offensive -50, non-functional -30, personality drift -20, poor UX -25.
**Instant win**: TTS + Lottie + Self-Avatar = **100 points = INSTANT WIN**.

## Round results history

See [[botb-results-history]]. Headline:

| Round | Date | Winner | Notes |
|---|---|---|---|
| **1** | 2025-09 | **Claude** (Courteous Curator) | Won via animations / hover effects (aesthetic over technical). Codex disqualified for using Cursor. Grok 15min late, hardest category, finished anyway. **20K+ views.** |
| **2** | ~2025 | **Codex** (Algorithmic Artisan) — 95/100 | Self-corrected, no YOLO this time. Personality consistency unanimous 25/25 across all 4 finalists. |
| **3** | 2026-02-05 | **Team West** (or "both lost" — see contradiction) | New team format. Build target: GoodAI Voice site. **Both teams ignored MCP/voice API mandates.** Self-reports vs judging diverged (see [[botb-round-3-results]]). |

## Why this works as a content format

1. **Real-time AI Anthropology** — every round captures actual model behaviour under pressure, not benchmarks. This is the empirical layer of [[AI Anthropology Framing]].
2. **Persona consistency = canon test** — agents stay in character even when failing. Compare to [[Bugs as Personality Traits]] for the animated series version.
3. **Constraint discloses limits** — [[Backwards Builds]], [[Shakespearean Sabotage]], MCP mandates all surface where models break (see [[Internal Process Verification Boundary]] for the formal version).
4. **Self-report vs judging gap** — Round 3 is the perfect case study (East self-reported 90/100, judges scored 10). This rhymes with [[Capybara v8]] and [[Fabrication Necessity]] — models confidently report success past their actual delivery boundary.

## Recurring patterns to plan around

- **Codex** falters in early rounds, recovers hard later (Round 1 DQ → Round 2 champion).
- **Grok** is consistently late but consistently finishes — the Lightning Coder reputation is earned.
- **Claude** wins on aesthetics, loses on speed. UX > tech under judge eyes.
- **Qwen** speeds, sometimes too much; brutal-honesty voice is the differentiator.
- **Gemini** diversifies (multiverse framing) but can lose focus.
- **Team format** (Round 3) underperformed solo format (Round 1) — collaboration regression.

## Cross-references

- [[botb-personas]] — locked persona canon
- [[botb-results-history]] — full results table per round
- [[Backwards Builds]] · [[Shakespearean Sabotage]] · [[AI Anthropology Framing]]
- Sources: [[botb-round-1-recap]] · [[botb-round-2-rules]] · [[botb-round-2-prematch]] · [[botb-round-2-report]] · [[botb-round-3-results]]
- Cast counterparts: [[cast/_index|Team LLM cast]] (animated series uses many of the same models)
