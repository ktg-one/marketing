---
type: intel
subject: Anthropic
period: 2026-Q1
status: open
created: 2026-05-16
updated: 2026-05-16
tags: [intel, anthropic, claude-code, degradation]
---

# Anthropic — Q1 2026 Degradation Snapshot

Compiled from [[the-mirage-of-ethical-ai]]. Subject: [[Anthropic]] / [[Claude Code]].

## Headline

In the same calendar quarter that [[Anthropic]] shipped 50+ releases, walked away from a Pentagon contract, hit #1 on the App Store, and signed enterprise customers at $2.5B annualised revenue, individual user compute was silently cut by more than 50%.

## Pattern

Instance of [[Silent Compute Cuts]] and [[Ethics as Branding]].

## Timeline

| Date | Event |
|---|---|
| Dec 2025 | Silent compute cut. 18-step cascade workflows collapse to <1 step. No announcement. |
| Q1 2026 (early) | 50+ releases. Pentagon walkaway. ChatGPT uninstalls +295%. [[QuitGPT]] hits 2.5M. |
| Q1 2026 (mid) | Claude #1 App Store. Web traffic +30% MoM. 18.9M pro users. |
| Q1 2026 (late) | Enterprise signs. $2.5B annualised, 80% enterprise. |
| Feb 2026 | Default thinking effort silently set to "medium" (value 85). |
| Q1 ongoing | Peak-hour throttling. Caching bugs inflating token costs 10–20×. Off-peak promo expires. |
| 2026-03-08 | AMD-flagged reasoning regression cliff (per the AMD GitHub issue). |
| ~Mar 2026 | AMD director files GitHub issue with 6,852 session files. Closed without explanation. AMD stops using Claude Code for complex engineering. |
| ~Mar 2026 | Bug tracker shows 1,279 sessions × 50+ compaction failures = ~250k API calls/day wasted globally. |
| 2026-03-21 | Legal threats sent to [[OpenCode]] forcing removal of Claude authentication (10 days pre-leak). |
| 2026-03-31 | [[Source Map Leak Pattern|Source code leak]]. 512K lines / 1,900 files on npm. |
| 2026-04 (one week post-leak) | [[Project Glasswing]] announced + [[Claude Mythos]] Preview unveiled. |
| Late 2026 | Reportedly targeted IPO. |

## Receipts

| Receipt | Source signal |
|---|---|
| 50%+ user compute cut | First-person logs (cited author) |
| 12 usable days / 30 for one Pro subscriber | User report |
| ~250k wasted API calls/day | Bug tracker |
| 6,852-session AMD issue closed without explanation | GitHub |
| [[Capybara v8]] 29-30% false claims (regression from 16.7% in v4), shipped behind "assertiveness counterweight" | Internal eval data |

## Open questions

> [!gap] To investigate
> - Is the degradation reversible for individual-tier customers post-IPO, or has the new pricing/throughput floor been set?
> - Did any enterprise customer experience equivalent degradation, or were the cuts precisely targeted to non-enterprise plans?
> - Was the AMD issue closed because resolved, because de-prioritised, or because the engineer left?
> - What is the user-side surface for verifying the February thinking-effort default? Is there an API parameter to override?

## Related entities

- [[Anthropic]]
- [[Claude Code]]
- [[KAIROS]] / [[autoDream]] / [[Conway]] / [[Undercover Mode]] (leaked components)
- [[Project Glasswing]]
- [[Claude Mythos]]
- [[Capybara v8]]
- [[OpenCode]]

## Sources

- [[the-mirage-of-ethical-ai]] (2026-04, .ktg)
