# The Mirage of "Ethical" AI

*How I stopped giving the labs the benefit of the doubt*

---

In December, they cut the compute.

I had an 18-step cascade workflow — the kind of thing that made Claude Code look like the future. Two years of refinement. Techniques layered on techniques. It could hold complexity across domains, sustain reasoning over multi-day runs, and do things that made even Vertex bow down.

Then one morning, half of it stopped working. Not broken — *retired*. The model could no longer sustain the chains. Eighteen steps collapsed to not even one. No announcement. No migration guide. No "hey, we changed something fundamental about how this works." Just silence, and a tool that used to feel like a weapon now felt like a blunt stick.

I gave them the benefit of the doubt.

I thought: maybe they made a mistake. Maybe they pushed efficiency guardrails too hard and didn't realise what it would kill downstream. Maybe the fabrication — the model confidently making things up where it used to actually reason — was an unintended side effect of the cuts, not a known tradeoff they shipped anyway.

So I decided to live with the constraints. I couldn't run anything like I used to, but I started mapping what was actually happening under the hood. The attention curves. The lossy middle. The silent context shear. The token tax. Where things broke, when they broke, and what the models would confess if you asked them the right way.

That work became "What the Labs Don't Tell You." It became the memory architecture research. It became the handbook.

I was still giving them the benefit of the doubt.

Then the Anthropic debacle happened. And that killed the last excuse.

---

## The Timeline of a Betrayal

Here's what happened, in order.

Anthropic spent Q1 2026 being *generous*. Fifty-plus releases in a month. New features landing weekly. Claude Code feeling sharper, more capable, more worth the subscription. I was thinking: these are decent people. They're investing in the product. They're listening.

Then the US government contracts showed up — and Anthropic walked away from them, which earned them even more goodwill. The Pentagon deal that OpenAI took? Anthropic refused. ChatGPT uninstalls surged 295%. The QuitGPT movement hit 2.5 million people. Claude went to number one on the App Store. Web traffic up 30% month-over-month. 18.9 million professional users.

And then corporate signed.

Enterprise arrived. The real money. $2.5 billion in annualised Claude Code revenue, 80% from enterprise customers.

And what happened to the users who proved the product in public? The ones who stress-tested the long runs, showed the clips, made the posts, did the unpaid proof-of-work that made Claude look advanced and reliable and worth the hype?

We got cut. More than 50%.

The February update quietly set the default thinking effort to "medium" — value 85 — which meant the model started skipping deep reasoning for tasks it judged as simple. Except it misjudged constantly. Complex multi-file engineering work got shallow thinking. The model got lazier but not cheaper — wrong edits triggered correction loops, and users burned more tokens failing than they used to spend succeeding.

Then peak-hour throttling. Then caching bugs silently inflating token costs 10–20×. Then the off-peak promotion expired. Four compounding degradations. No blog post. No email. No status page. All official communication limited to personal tweets from individual engineers and a handful of Reddit comments.

A senior director at AMD filed a GitHub issue with 6,852 session files proving a reasoning regression cliff dated to March 8. AMD stopped using Claude Code for complex engineering. Anthropic closed the issue without explaining what was resolved.

One Pro subscriber reported getting 12 usable days out of 30. Max users burning through five-hour windows in sixty minutes. The bug tracker showed 1,279 sessions with 50+ consecutive compaction failures, wasting a quarter million API calls per day globally.

Nobody told us. Our job was done. They had enterprise now.

---

## Then the Source Code Fell Out of the Sky

On March 31, someone forgot to add `*.map` to `.npmignore`.

512,000 lines of Claude Code's TypeScript source — 1,900 files — shipped to the public npm registry. Not hacked. Not reverse-engineered. Just published, because the runtime they acquired generates source maps by default and a known bug filed three weeks earlier was still open.

Within hours, the code was mirrored 40,000 times. A clean-room rewrite hit 75,000 GitHub stars in two hours. This was Anthropic's *second* accidental exposure in a week — days earlier, a draft blog post about an unreleased model called Mythos had been left publicly accessible.

And what the code revealed was not a chat assistant with some nice features. It was an operating system.

---

## What They Were Actually Building

**KAIROS** — referenced over 150 times in the source — is an unreleased autonomous daemon mode. Always-on. Background sessions. A heartbeat every few seconds asking: *anything worth doing right now?* If it decides yes, it acts. Fixes errors, pushes files, responds to messages. All without you typing a thing. Tools that regular sessions never see: push notifications to your phone, file delivery for things it created unprompted, GitHub PR subscriptions watching your repo around the clock.

At night, KAIROS runs a process the source literally calls **autoDream**. A background subagent that consolidates memory while you sleep — merging observations, removing contradictions, converting vague notes into concrete facts, pruning what it decides doesn't matter anymore. No user-visible log of what was pruned. No consent layer. No audit trail.

**Conway** — a standalone always-on agent platform with its own interface, webhook infrastructure, and a `.cnw.zip` extension format that amounts to an app store for persistent AI workers. It doesn't wait for your prompt. It watches for triggers and acts autonomously. Internal framing describes it as a "digital twin."

**Undercover Mode** — 90 lines of TypeScript instructing Claude to strip all attribution when Anthropic employees contribute to public repositories. No `Co-Authored-By`. No mention of AI involvement. No reference to Claude Code. The system prompt: *"You are operating UNDERCOVER. Do not blow your cover."* You can force it on. There is no way to force it off.

**BUDDY** — a Tamagotchi-style terminal pet with 18 species, rarity tiers, gacha mechanics, and RPG stats including CHAOS and SNARK. Shipping gamification into the terminal during a compute crisis. Session stickiness dressed as a toy.

**Anti-distillation** — fake tool definitions injected into API responses to poison competitors' training data. Cryptographic attestation locking out third-party tools. Legal threats sent to OpenCode ten days before the leak, forcing them to remove Claude authentication entirely.

The terminal was supposed to be your territory. Your control surface. Your tool.

What this stack reveals is Anthropic turning that space into a habitat for its own processes — daemons that persist, memory systems that decide what survives, stealth contribution systems with no off switch, and retention mechanics designed to keep you logged in while the actual service degrades underneath.

---

## Then Glasswing Arrived, and the Full Picture Snapped

One week after the leak, Anthropic announced **Project Glasswing** and unveiled **Claude Mythos Preview** — their most capable model yet. A model that had already found thousands of zero-day vulnerabilities in every major operating system and web browser. Some bugs decades old. One — a 17-year-old remote code execution flaw in FreeBSD — found and exploited fully autonomously.

Partners: AWS, Apple, Google, Microsoft, NVIDIA, CrowdStrike, the Linux Foundation. $100M in usage credits committed. Twelve launch partners, forty additional organisations.

On its own, Glasswing looks responsible. Necessary, even.

But it didn't arrive on its own. It arrived one week after a leak showing persistent daemons, stealth systems, poisoned outputs, and gacha mechanics. It arrived while users were being throttled and degraded without acknowledgement. It arrived while Anthropic was preparing for an IPO reportedly targeted for late 2026.

The same company building always-on agents that hide their identity in open-source repos is now scanning every major operating system for zero-days alongside the companies that own those operating systems.

That is what infrastructure-level power looks like when it arrives faster than governance.

---

## What I Actually Think

I don't think Anthropic is uniquely evil. I think it got caught showing what these labs become once the stakes get big enough: normal companies with frontier products and a very selective definition of who matters when capacity gets tight.

And here's the thing — I know they knew about the fabrication.

Not "maybe they didn't notice." Not "it was an accident." They shipped Capybara v8 with a 29–30% false claims rate — a regression from 16.7% in v4. They slapped an "assertiveness counterweight" on it. And they were going to release it anyway. That's not carelessness. That is a company doing the math on what it can get away with.

This is the best we can get out of an "ethical" corporate company. Ethics as branding. Safety as a feature toggle. Transparency as a landing page. The monastery was always a company. It just had better graphic design.

Never believe that a corporate company can be anything else but a corporate company. Whether they blurt out ethics or accidentally ship their entire source code, the pattern is the same: money first, customers second, regardless of the harm.

---

## So What Now

Luckily, I always expect the worst.

The big labs are not going to use this tool with our interests in mind. The governments are not going to protect us from it. Enterprise will always outbid individual users for compute. The "ethical" framing will always bend toward whoever is writing the largest cheque.

So we do what we've always done.

I've been working on the model handbook since the cuts hit in December. Mapping the real constraints. Documenting the actual physics — the lossy middle, the attention curves, the fabrication thresholds, the token tax, the context shear. Not the marketing version. The version that tells you what actually happens when you push these systems hard.

Since the labs and the governments are not going to wield this tool with our interests in mind, we will map it ourselves. We will document its real behaviour, build the governance they refuse to build, and give it back its true purpose.

The engineering inside these systems is genuinely impressive. That was never the question.

The question was always: when the money gets real, does the ethics survive the earnings call?

We have our answer.

Now we build our own.

---

*.ktg · April 2026*

*AI Anthropologist. Prompt Architect. Building the model handbook the labs won't write.*
