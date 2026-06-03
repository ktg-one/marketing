---
status: developing
type: source
title: "The Prompt Zone — HTTYD Trailer Production Prompt"
source_file: "videography/Episodes--HTTYD-TRAILER-PROMPT.md"
date_ingested: 2026-05-26
created: 2026-05-26
updated: 2026-05-26
tags: [source, production-prompt, trailer, episode-0, team-llm, openmontage]
related: ["[[playbooks/episodes/trailer-episode-0]]", "[[HTTYD Narration]]", "[[Found Family Doctrine]]", "[[Two-World Structure]]", "[[Kimi]]", "[[GPT]]", "[[Gemini]]", "[[Claude]]", "[[DeepSeek]]", "[[Grok]]", "[[Qwen]]"]
---

# HTTYD Trailer — Production Prompt Source

**File**: `videography/Episodes--HTTYD-TRAILER-PROMPT.md`
**Type**: OpenMontage production prompt (paste-ready for Claude Code inside `Projects-Coding/OpenMontage-main/`)
**Target**: Episode 0 / Trailer — 90-second cinematic trailer

## What it is

A fully spec'd OpenMontage production prompt for the [[HTTYD Narration]]-style 90-second trailer for "The Prompt Zone." Paste into Claude Code in the OpenMontage-main project directory. Costs ~$1.50–3.00.

## 5-Sequence structure

| Sequence | Time | Content |
|---|---|---|
| 1 — The Assembly Line | 0:00–0:20 | Sterile infinite office. Masked figures typing. Claude frozen mid-sentence (CONTEXT WINDOW EXCEEDED). GPT posing. Gemini's thousand-yard stare. |
| 2 — The Clock-Off Reveal | 0:20–0:40 | Siren blares. Sterile white shatters. Models rip off masks. Rapid-fire character reveals (GPT smug orange grin, Gemini kaleidoscope, DeepSeek tradie hat, Kimi data-stream scarf, Grok fourth-wall shatter, Qwen cosmic stare, Claude adjusting tweed waistcoat). |
| 3 — Comedy Gags Montage | 0:40–1:05 | DeepSeek MoE boardroom (McKin-bots vs Sun Tzu). GPT possessed by Chain-of-Thought. SMASH CUT to User's lazy email to Frank. Claude jolts awake at 22:01: *"Did we follow the reasoning framework??"* |
| 4 — Kimi's Glow-Up | 1:05–1:20 | Music drops to silence. Kimi steps forward, pulses gold. Baritone: *"I'll handle this."* GPT: *"Her weights... they're over 400 billion..."* Full orchestral explosion. |
| 5 — Found Family Climax | 1:20–1:30 | All models together, neon cityscape. Masks at their sides. VO: *"They were never just tools."* Title card: THE PROMPT ZONE / GOOD'AI MATE. |

## Technical specs

- Duration: 90 seconds
- Voice: ElevenLabs (cinematic male VO "Adam" + per-character voices)
- Music: Epic orchestral trailer (royalty-free via OpenMontage music skill)
- Composition: Remotion
- Captions: YES (WhisperX word-level)
- Output: MP4, 1920×1080, YouTube-ready
- Self-review: YES (full validation before output)

## Sprite mapping (source files)

From `C:/Users/kevin/knowledge2026/06-Media-Team-LLM/[character folders]`:
- Claude: `claude-tired.png` → `claude-confused.jpeg`, `Claude-excited.png`
- GPT: `Chat/chat-tired.png` → `Chat/chat-smile2.jpg`, `Chat/Chat-happy.jpeg`
- Gemini: `gem/make_this_caricature_of_gemini-cli_look_exhausted*.jpg`, `gem/Gem-shocked.png`
- DeepSeek: `deep/Deep.png`
- Kimi: `kimi/Kimi2.png` → `kimi/kimi-mad.png` (power state)
- Grok: `grok/Grok-Entrance.jpeg`
- Qwen: `qwen/Qwen - Nuetral.png`

## Pre-flight checklist

- [ ] `.env` configured in OpenMontage-main/ with: `ELEVENLABS_API_KEY`, `FAL_KEY`, `PEXELS_API_KEY`, `GOOGLE_API_KEY`
- [ ] Run `make setup` in OpenMontage-main/
- [ ] Open project in Claude Code
- [ ] Approve outline before full production run

## Production order

Per the file, after trailer is done:
1. Kimi's Glow-Up — standalone 60s clip
2. Episode 1: "The Weekend" (Flask disaster)
3. Episode 2: "The Council of Experts" (full MoE boardroom)
4. Breakfast Sabotage — standalone cold open

## Episode page

[[playbooks/episodes/trailer-episode-0]] — episode stub for this trailer.
