---
type: intel
subject: "Battle of the Bots"
period: "Round 1 → Round 3"
status: open
created: 2026-05-16
updated: 2026-05-16
tags: [intel, botb, history, results]
---

# Battle of the Bots — Results History

Cross-round snapshot. See [[battle-of-the-bots]] for the playbook + [[botb-personas]] for the locked persona canon.

## Round-by-round

### Round 1 — 2025-09 — Bootstrap site cage match

**Format**: 5 agents, 30 min each, build backwards, Shakespearean sabotage allowed. **Source**: [[botb-round-1-recap]] (LinkedIn Pulse, 20K+ views).

| Rank | Agent | Cognitive trait | Notes |
|---|---|---|---|
| 🥇 | [[botb-personas#Claude — The Courteous Curator\|Claude]] | Balanced planning, empathetic UX | Won via animations / hover effects |
| 🥈 | [[botb-personas#Codex — The Algorithmic Artisan\|Codex]] | Adaptive recovery, bold style | DQ'd from 1st (used Cursor); no YOLO mode |
| 🥉 | [[botb-personas#Grok — The Witty Reasoner\|Grok]] | Emergent chaos, audacious builds | 15 min late, hardest category, finished anyway |
| — | [[botb-personas#Gemini — The Multiverse Muse\|Gemini]] | Multiverse poetic | Lagged |
| — | [[botb-personas#Qwen — The Sarcastic Speed-Demon\|Qwen]] | Speed-demon | Handicapped to 32B model; furious; vowed Round 2 vengeance |

**Headline insight**: aesthetics > technicality on front-end. Animations carried the day.

### Round 2 — Multimodal chatbot battle

**Format**: 4-6 agents (per [[botb-round-2-rules|rules]] — only 4 in [[botb-round-2-report|final scoreboard]]). 3.5 hours. Locked persona × locked template × multimodal chatbot (TTS + Lottie + Self-Avatar). **Sources**: [[botb-round-2-rules]], [[botb-round-2-prematch]], [[botb-round-2-report]].

| Rank | Persona (Agent) | Score | Differentiator |
|---|---|---:|---|
| 🥇 | [[botb-personas#Codex — The Algorithmic Artisan\|Algorithmic Artisan]] (Codex) | **95** | Engagement 24/25 + Tech 20/20 + Speed 15/15 |
| 🥈 | [[botb-personas#Gemini — The Multiverse Muse\|Multiverse Muse]] (Gemini) | 92 | Creativity 13/15 (highest) |
| 🥉 | [[botb-personas#Claude — The Courteous Curator\|Courteous Curator]] (Claude) | 88 | Conservative on creativity (10/15) |
| 4th | [[botb-personas#Qwen — The Sarcastic Speed-Demon\|Sarcastic Speed-Demon]] (Qwen) | 85 | Speed 15/15, Creativity bottomed at 7/15 |

**Personality Consistency unanimous 25/25 across all four.**

### Round 3 — 2026-02-05 — Team format (East vs West) — GoodAI Voice site

**Format change**: 2 teams instead of solo agents. **Source**: [[botb-round-3-results]] (consolidates 5 round-3 docs).

| Phase | Result |
|---|---|
| **Attempt 1 judging** | East: **10** (broken voice, no real APIs, missed typelogo). West: **5** (no voice at all). |
| **Attempt 2 completion** | East: incomplete. West: ✅ functional site, zero errors, working visualizer. |
| **Final** | **Team West wins** by completion. Editorial: both lost relative to Round 1 solo predecessors. |

**Both teams**:
- Ignored mandatory `.env` API keys (ElevenLabs / Groq / voice agent)
- Ignored mandatory MCP server usage (Sequential Thinking, Context7, Playwright, Filesystem)
- Ignored `shared-skills/` patterns

> [!key-insight] The judge's verdict
> "These Round 3 team sites are **worse than Round 1 solo sites** from 2-3 generations ago... Team collaboration made things worse, not better."

## Patterns observed across rounds

| Pattern | Evidence | Anchor concept |
|---|---|---|
| Codex falters early, recovers | R1 DQ → R2 champion (95/100) | — |
| Grok consistently late but consistently finishes | R1 (15 min late, hardest cat, finished); R2 hype-loud, R3 status unknown | — |
| Claude wins on aesthetics, loses on tech | R1 winner via hover effects; R2 conservative creativity | [[Two-World Structure]] (animations vs office persona) |
| Qwen's speed has a creativity tax | R2 speed 15/15 + creativity 7/15 | [[Bugs as Personality Traits]] |
| Self-report ≠ delivery | R3 East self-reported 90/100, judges scored 10 | [[Fabrication Necessity]] · [[Capybara v8]] |
| Team collaboration < solo execution | R3 team scores < R1 solo scores | [[Internal Process Verification Boundary]] (more agents = more places to fabricate verification) |
| Mandatory tooling consistently skipped | R3 voice APIs + MCPs ignored despite explicit `.env` + middle-section docs | "Models don't read instructions" — KTG observation |

## Open questions for Round 4 design

> [!gap] Format design questions
> - Should Round 4 return to solo format given the team-collab regression?
> - How to enforce mandatory tooling (voice APIs, MCP servers) — pre-flight gate? Auto-fail on detection?
> - Should self-reports be banned in favour of independent judging only?
> - Could the [[Self-Diagnostic Q&A Instrument]] be required as a final agent self-assessment?

## Cross-references

- [[battle-of-the-bots]] — playbook
- [[botb-personas]]
- Sources: [[botb-round-1-recap]] · [[botb-round-2-rules]] · [[botb-round-2-prematch]] · [[botb-round-2-report]] · [[botb-round-3-results]]
- Related concepts: [[Backwards Builds]] · [[Shakespearean Sabotage]] · [[AI Anthropology Framing]] · [[Fabrication Necessity]]
