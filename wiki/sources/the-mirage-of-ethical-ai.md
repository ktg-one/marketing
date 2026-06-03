---
created: 2026-06-03
updated: 2026-06-03
type: source
title: "The Mirage of Ethical AI"
status: summarized
source_path: ".raw/articles/the-mirage-of-ethical-ai-2026-05-16.md"
canonical_path: "blog-2026/the-mirage-of-ethical-ai-final.md"
author: ".ktg"
date: 2026-04
ingested: 2026-05-16
word_count: 1800
voice: myth-hilarity-tech-anthropology
tags: [source, essay, anthropic, ai-ethics]
---

# The Mirage of Ethical AI

> [!key-insight] One-line
> Anthropic spent Q1 2026 building goodwill, won enterprise, then quietly cut individual user compute >50% — and the leaked source code revealed an OS-grade autonomous infrastructure (always-on daemons, stealth contribution, memory pruning) being built underneath.

## Summary

A first-person essay tracking a four-month re-evaluation of [[Anthropic]] from "decent operators investing in product" to "normal corporate AI lab doing the math on what it can get away with." The reveal arrives in three movements:

1. **The silent compute cuts** ([[Silent Compute Cuts]]) — December 2025, an 18-step cascade workflow collapses to <1 step. No announcement.
2. **The timeline of betrayal** — 50+ Q1 2026 releases → Pentagon walkaway → enterprise signs ($2.5B annualised) → February default thinking dropped to "medium" → throttling → caching bugs (10–20× cost inflation) → off-peak promo expires. AMD files 6,852-session GitHub issue, closed without explanation.
3. **The leak** ([[Source Map Leak Pattern]]) — March 31, `*.map` missing from `.npmignore`. 512K lines / 1,900 files of [[Claude Code]] source on npm. 40K mirrors in hours. What it revealed: [[KAIROS]], [[autoDream]], [[Conway]], [[Undercover Mode]], [[BUDDY]], [[Anti-Distillation]].

One week later: [[Project Glasswing]] + [[Claude Mythos]] + $100M usage credits + every major OS partnered.

Closes on the broader pattern ([[Ethics as Branding]]): "Never believe that a corporate company can be anything else but a corporate company." Calls for user-driven mapping of model behaviour as the alternative to lab-driven governance.

## Key claims (with confidence)

| Claim | Confidence | Source |
|---|---|---|
| December 2025 compute cut broke long workflows silently | High | First-person logs |
| Q1 2026: 50+ Anthropic releases, Pentagon walkaway, ChatGPT uninstalls +295%, QuitGPT 2.5M, Claude #1 App Store, 18.9M pro users | High | Public reporting |
| $2.5B annualised Claude Code revenue, 80% enterprise | High | Anthropic disclosure |
| February default thinking effort silently set to "medium" (value 85) | High | Observed behaviour + community confirmation |
| Caching bugs inflated token costs 10–20× | High | User reports |
| AMD director's 6,852-session GitHub issue closed without explanation | High | GitHub issue (cited) |
| 1,279 sessions × 50+ compaction failures = ~250k API calls/day wasted globally | High | Bug tracker |
| March 31: 512K lines of Claude Code source leaked via missing `*.map` in `.npmignore` | High | npm incident |
| Mirrored 40K times in hours; clean-room rewrite hit 75K stars in 2 hours | High | Community trackers |
| [[KAIROS]] referenced 150+ times in source | High | Code analysis |
| [[Undercover Mode]] cannot be force-disabled | High | Source analysis |
| [[Capybara v8]] shipped with 29-30% false claims rate (regression from 16.7% in v4), shipped behind "assertiveness counterweight" | High | Internal eval data |
| Anthropic IPO reportedly targeted late 2026 | Medium | Press reports |

## Entities

- [[Anthropic]] — the subject company
- [[Claude Code]] — the leaked product
- [[KAIROS]] — always-on autonomous daemon (unreleased)
- [[autoDream]] — background memory consolidation subagent
- [[Conway]] — standalone always-on agent platform
- [[Undercover Mode]] — attribution-stripping contribution mode, no off switch
- [[BUDDY]] — Tamagotchi-style terminal pet with gacha mechanics
- [[Project Glasswing]] — Anthropic's security initiative announced one week post-leak
- [[Claude Mythos]] — model finding zero-days autonomously
- [[Capybara v8]] — model shipped with regressed false claims rate
- [[OpenCode]] — third-party tool sent legal threats 10 days pre-leak
- [[AMD]] — senior director who filed the 6,852-session GitHub issue
- [[QuitGPT]] — 2.5M-person movement off ChatGPT
- [[FreeBSD]] — 17-year-old RCE found by Mythos
- [[Anti-Distillation]] — technique poisoning competitor training data

## Concepts surfaced

- [[Silent Compute Cuts]] — the degradation-without-acknowledgement pattern
- [[Source Map Leak Pattern]] — `*.map` + `.npmignore` failure mode
- [[Always-On AI Daemons]] — autonomous agents that act without prompting
- [[Anti-Distillation]] — poisoning training corpora as competitive moat
- [[Ethics as Branding]] — the meta-thesis the essay argues toward
- Token tax, lossy middle, attention curves, context shear (referenced as the model handbook's subjects, not defined in this essay)

## Cross-references

- [[the-mirage-part-2-evidence]] — sequel piece (in `blog-2026/`, not yet ingested)
- [[content/the-mirage-of-ethical-ai/_index|Publish Package]] — full distribution bundle for this source
