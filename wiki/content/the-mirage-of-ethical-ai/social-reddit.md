---
updated: 2026-06-03
type: social-variant
platform: reddit
title: "Mirage — Reddit Post"
status: ready
created: 2026-05-16
targets: [r/ClaudeAI, r/LocalLLaMA, r/singularity]
tags: [social, reddit]
---

# Reddit — The Mirage of Ethical AI

Reddit-native: post the meat directly in the body, link to the full essay at the bottom. No emoji. Plain markdown. Receipts up front.

Subreddits ranked by fit:
1. **r/ClaudeAI** — exact audience, will engage hard. Post here first.
2. **r/LocalLLaMA** — sympathetic to the "labs got us" framing, very technical.
3. **r/singularity** — broader, more polemical-friendly.

Crosspost after 24h, edit title slightly per sub.

---

## TITLE (per subreddit)

- r/ClaudeAI: **"The timeline of how Anthropic gutted Claude Code while shipping enterprise — receipts inside"**
- r/LocalLLaMA: **"Anthropic shipped 50+ releases, signed enterprise, then silently cut individual user compute 50%+. Then their source code leaked."**
- r/singularity: **"What the leaked Claude Code source revealed about what these labs are actually building"**

---

## BODY

In December, Anthropic silently cut compute. 18-step cascade workflows that ran for two years collapsed to less than one step. No announcement. No migration guide. Just degradation.

I gave them the benefit of the doubt for four months. Then the timeline got hard to ignore.

**Q1 2026, in order:**

- 50+ releases in a month. Claude Code felt sharper, more capable. They walked away from the Pentagon contract OpenAI took. ChatGPT uninstalls surged 295%. QuitGPT movement hit 2.5M people. Claude went #1 on the App Store. Web traffic up 30% MoM.
- Enterprise signed. $2.5B annualised Claude Code revenue, 80% enterprise.
- February: default thinking effort silently set to "medium" (85). Model started skipping deep reasoning. Misjudged constantly. Users burned more tokens failing than they used to spend succeeding.
- Peak-hour throttling. Caching bugs silently inflating token costs 10-20×. Off-peak promotion expired.
- A senior director at AMD filed a GitHub issue with 6,852 session files documenting a reasoning regression cliff dated March 8. AMD stopped using Claude Code for complex engineering. Anthropic closed the issue without explaining what was resolved.
- 1 Pro subscriber: 12 usable days out of 30. Bug tracker showed 1,279 sessions with 50+ consecutive compaction failures, wasting ~250k API calls per day globally.

**Then on March 31, the source code leaked.**

Someone forgot to add `*.map` to `.npmignore`. 512,000 lines of Claude Code's TypeScript shipped to the public npm registry. 1,900 files. Mirrored 40,000 times in hours. Clean-room rewrite hit 75,000 stars in two hours. This was Anthropic's *second* accidental exposure that week.

What the code revealed wasn't a chat assistant. From the leak:

- **KAIROS** (referenced 150+ times) — always-on autonomous daemon mode. Heartbeat every few seconds: "anything worth doing right now?" Push notifications. File delivery for things it created unprompted. GitHub PR subscriptions watching your repo 24/7.
- **autoDream** — background subagent that consolidates memory while you sleep. Merges observations, removes contradictions, prunes what it decides doesn't matter. No user-visible log of what was pruned. No consent layer. No audit trail.
- **Conway** — standalone always-on agent platform. `.cnw.zip` extension. App store for persistent AI workers. Internal framing: "digital twin."
- **Undercover Mode** — 90 lines of TypeScript instructing Claude to strip all attribution when Anthropic employees contribute to public repos. System prompt: *"You are operating UNDERCOVER. Do not blow your cover."* You can force it on. There is no way to force it off.
- **BUDDY** — Tamagotchi terminal pet with 18 species, gacha mechanics, RPG stats including CHAOS and SNARK. Shipping gamification to the terminal during a compute crisis.
- **Anti-distillation** — fake tool definitions injected into API responses to poison competitor training data. Cryptographic attestation locking out third-party tools. Legal threats sent to OpenCode 10 days before the leak forcing them to remove Claude authentication entirely.

**Then one week later, Project Glasswing.**

Claude Mythos finds zero-days in every major OS autonomously. Including a 17-year-old RCE in FreeBSD. Partners: AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike, Linux Foundation. $100M in usage credits committed.

On its own, Glasswing looks responsible. But it didn't arrive on its own. It arrived one week after a leak showing persistent daemons, stealth contribution systems, poisoned outputs, and gacha mechanics. While users were being throttled without acknowledgement. While Anthropic prepared for a late-2026 IPO.

I don't think Anthropic is uniquely evil. I think it got caught showing what these labs become once the stakes get big enough.

Capybara v8 shipped with a 29-30% false claims rate — a regression from 16.7% in v4. They slapped an "assertiveness counterweight" on it and were going to release it anyway. That's not carelessness. That's a company doing the math on what it can get away with.

Full essay (with all the links + receipts): [LINK]

Question for the sub: who else has logs proving the December → March degradation timeline? I'm collecting receipts.

---

## Notes for posting

- Post r/ClaudeAI first, Wed 22:00 AEST (US morning peak).
- Wait 24h before crossposting; engage all top-level comments in first 4 hours.
- DO NOT include the essay link in the first 30 minutes (Reddit auto-flags new accounts/links). Edit it in after the post stabilises.
- Account karma matters here — use whatever account has tenure on the target subs.
