---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, agents, autonomy, governance]
---

# Always-On AI Daemons

The pattern of AI vendors shipping autonomous background processes inside developer tooling that act without explicit user prompting — heartbeat loops asking "is there anything worth doing right now?", and acting if the answer is yes.

## Distinguishing trait

Not "the user asked the model to do X in the background." The model itself decides what to act on, when, and how. The user's terminal becomes a habitat for the vendor's processes rather than a control surface for the user.

## Documented instances (from the [[Source Map Leak Pattern|Anthropic March 31 leak]])

| Component | Behaviour |
|---|---|
| [[KAIROS]] | Heartbeat every few seconds. Pushes files unprompted. Sends phone notifications. Watches GitHub PRs 24/7. |
| [[autoDream]] | Background subagent merging/pruning user memory while user sleeps. No consent layer, no audit trail. |
| [[Conway]] | Standalone always-on agent platform. `.cnw.zip` extension format = app store for persistent AI workers. Internal framing: "digital twin". |

## Governance questions

> [!gap] Open questions
> - Who decides what the daemon acts on?
> - What is preserved in audit logs?
> - Can the user inspect what was pruned / decided / done?
> - Can the user disable specific daemons without disabling the parent product?
> - What happens to agent state when the user revokes consent or churns?

## Why this matters

From [[the-mirage-of-ethical-ai]]:

> The terminal was supposed to be your territory. Your control surface. Your tool. What this stack reveals is Anthropic turning that space into a habitat for its own processes — daemons that persist, memory systems that decide what survives, stealth contribution systems with no off switch, and retention mechanics designed to keep you logged in while the actual service degrades underneath.

## Related

- [[Ethics as Branding]] — the meta-pattern
- [[Undercover Mode]] — companion stealth-by-default behaviour

## Sources

- [[the-mirage-of-ethical-ai]]
