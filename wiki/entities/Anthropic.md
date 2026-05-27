---
type: entity
entity_kind: organization
status: active
created: 2026-05-16
updated: 2026-05-16
tags: [entity, organization, ai-lab, anthropic]
---

# Anthropic

AI lab. Ships [[Claude Code]] and the Claude model family. Subject of [[the-mirage-of-ethical-ai|The Mirage of Ethical AI]].

## Q1 2026 trajectory

- 50+ releases in a single month
- Walked away from a Pentagon contract that OpenAI took
- Beneficiary of the [[QuitGPT]] migration (2.5M people moved off ChatGPT after the Pentagon news)
- Claude hit #1 on the App Store; web traffic +30% MoM; 18.9M professional users
- Enterprise signed: $2.5B annualised [[Claude Code]] revenue, 80% from enterprise

## The degradation timeline

See [[anthropic-2026-q1-degradation]] for the full intel snapshot. Headlines:

- **December 2025**: silent compute cut. 18-step cascade workflows collapse to <1 step ([[Silent Compute Cuts]]).
- **February 2026**: default thinking effort silently set to "medium" (value 85). Model skips deep reasoning on tasks it judges simple. Misjudges constantly.
- **Compounding**: peak-hour throttling, caching bugs inflating token costs 10–20×, off-peak promo expired.
- **AMD GitHub issue** with 6,852 session files documenting reasoning regression cliff dated 2026-03-08 — closed without explanation. AMD stopped using [[Claude Code]] for complex engineering.
- **Bug tracker**: 1,279 sessions × 50+ compaction failures = ~250k API calls/day wasted globally.

## March 31 source leak

`*.map` missing from `.npmignore`. 512,000 lines / 1,900 files of [[Claude Code]] source shipped to npm. Mirrored 40,000 times in hours. Clean-room rewrite hit 75,000 GitHub stars in 2 hours. Second accidental exposure that week (the first was a draft blog about an unreleased model called "Mythos" left publicly accessible). See [[Source Map Leak Pattern]].

What the leak revealed (all unreleased / non-public):
- [[KAIROS]] — always-on autonomous daemon
- [[autoDream]] — background memory consolidation
- [[Conway]] — app store for persistent AI workers
- [[Undercover Mode]] — attribution-stripping contribution mode
- [[BUDDY]] — gacha terminal pet
- [[Anti-Distillation]] — fake tool definitions in API responses to poison competitor training

## Project Glasswing (one week post-leak)

See [[Project Glasswing]]. AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike, Linux Foundation as partners. $100M in usage credits. [[Claude Mythos]] autonomously finding zero-days in every major OS, including a 17-year-old RCE in [[FreeBSD]].

## Other receipts cited in source

- [[Capybara v8]] shipped with 29-30% false claims rate (regression from 16.7% in v4), behind an "assertiveness counterweight"
- Legal threats sent to [[OpenCode]] 10 days before the leak, forcing removal of Claude authentication
- IPO reportedly targeted for late 2026

## Pattern read

Per the source author: not uniquely evil, but illustrative of [[Ethics as Branding]] — a normal corporate company with a frontier product and a selective definition of who matters when capacity gets tight.

## Sources

- [[the-mirage-of-ethical-ai]] (2026-04, .ktg)
