---
updated: 2026-06-03
type: social-variant
platform: linkedin
title: "Mirage — LinkedIn Post"
status: ready
created: 2026-05-16
char_budget: 3000
tags: [social, linkedin]
---

# LinkedIn — The Mirage of Ethical AI

Long-form professional tone. Less polemic, more "here's what the leak revealed." LinkedIn rewards measured outrage from operators. Signed off with the work.

---

In December, Anthropic cut the compute.

Not officially. Not announced. Just — silently. Workflows that ran 18 cascade steps collapsed to less than one. Multi-day runs stopped surviving. The model got measurably worse, and the only signal was your own logs.

I gave them the benefit of the doubt for four months.

Q1 2026, they shipped 50+ releases. Walked away from the Pentagon contract that OpenAI took. ChatGPT lost 2.5 million users to QuitGPT. Claude hit #1 on the App Store. Web traffic up 30% MoM. 18.9 million professional users.

Then enterprise signed. $2.5B in annualised Claude Code revenue. 80% from enterprise.

What happened next:

→ February: default thinking effort silently set to "medium" (value 85). Model began skipping deep reasoning on tasks it judged simple. It misjudged constantly. Users burned more tokens failing than they used to spend succeeding.

→ Peak-hour throttling. Caching bugs silently inflating token costs 10-20×. Off-peak promotion expired. Four compounding degradations, no acknowledgement.

→ A senior director at AMD filed a GitHub issue with 6,852 session files documenting a reasoning regression. Closed without explanation. AMD stopped using Claude Code for complex engineering.

→ One Pro subscriber: 12 usable days out of 30. The bug tracker showed 1,279 sessions with 50+ consecutive compaction failures, wasting a quarter million API calls per day globally.

Then the source code fell out of the sky.

March 31: someone forgot to add `*.map` to `.npmignore`. 512,000 lines of Claude Code's TypeScript shipped to the public npm registry. 1,900 files. Mirrored 40,000 times in hours. A clean-room rewrite hit 75,000 GitHub stars in two hours.

What the code revealed was not a chat assistant. It was an operating system.

KAIROS — an always-on autonomous daemon, referenced 150+ times. autoDream — background memory consolidation while you sleep, no consent layer. Conway — an app store for persistent AI workers. Undercover Mode — 90 lines instructing Claude to strip all attribution when Anthropic employees contribute to public repos. Anti-distillation — fake tool definitions injected into API responses to poison competitor training data.

One week later: Project Glasswing. $100M in usage credits committed. Claude Mythos autonomously finding zero-days in every major OS, including a 17-year-old RCE in FreeBSD. Partners: AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike, the Linux Foundation.

On its own, Glasswing looks responsible. Necessary, even. But it didn't arrive on its own. It arrived one week after a leak showing persistent daemons, stealth contribution systems, poisoned outputs, and gacha mechanics in the terminal during a compute crisis. It arrived while users were being throttled and degraded without acknowledgement. It arrived while Anthropic prepared for an IPO reportedly targeted for late 2026.

I don't think Anthropic is uniquely evil. I think it got caught showing what these labs become once the stakes get big enough: normal companies with frontier products and a very selective definition of who matters when capacity gets tight.

The full essay maps every receipt. Link in comments.

The engineering inside these systems is genuinely impressive. That was never the question.

The question was always: when the money gets real, does the ethics survive the earnings call?

We have our answer. Now we build our own.

#AI #ClaudeCode #Anthropic #AISafety #LLMs #DeveloperTools

---

## Notes for posting

- Post 08:00 AEST Thu (peaks for AU + early EU + late US).
- Drop the essay link in the FIRST comment, not the post body (LinkedIn algorithm penalty for outbound links).
- Allow 1-2 hours for organic reach before any reshare from secondary accounts.
- Be ready to reply to comments — this will draw both defensive Anthropic users and validating engineers.
