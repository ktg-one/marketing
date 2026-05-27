---
type: entity
entity_kind: product
status: active
created: 2026-05-16
updated: 2026-05-16
tags: [entity, product, claude, anthropic]
---

# Claude Code

Anthropic's developer-facing CLI / coding agent. Subject of the March 31 leak (see [[Source Map Leak Pattern]]).

## Revenue

$2.5B annualised, 80% from enterprise (per Anthropic disclosure cited in [[the-mirage-of-ethical-ai]]).

## Documented degradations (Q1–Q2 2026)

- December 2025: silent compute cut breaking long-cascade workflows ([[Silent Compute Cuts]])
- February 2026: default thinking effort silently set to "medium" (value 85)
- Peak-hour throttling
- Caching bugs inflating token costs 10–20×
- Off-peak promotion expired
- 50+ consecutive compaction failures across 1,279 tracked sessions

## Leaked components (March 31)

512K lines / 1,900 files. From the leak (mostly unreleased to public):

| Component | What it is |
|---|---|
| [[KAIROS]] | Always-on autonomous daemon mode |
| [[autoDream]] | Background memory consolidation subagent |
| [[Conway]] | Standalone always-on agent platform with `.cnw.zip` extensions |
| [[Undercover Mode]] | Attribution-stripping contribution mode (90 lines TS) |
| [[BUDDY]] | Tamagotchi terminal pet with gacha mechanics |
| [[Anti-Distillation]] | Fake tool definitions in API responses |

## Sources

- [[the-mirage-of-ethical-ai]]
