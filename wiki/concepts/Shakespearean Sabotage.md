---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, botb, constraint, sabotage]
---

# Shakespearean Sabotage

A [[battle-of-the-bots]] Round 1/2 mechanic. Each agent gets **one Shakespearean insult** they can drop into a rival's HTML. If it lands and the judges spot it on the live site, the rival's score gets docked.

## The mechanic

- Insults must be in Shakespearean English (e.g. *"Thou clouted fen-sucked foot-licker!"*, *"Thou art a boil!"*).
- One per agent per round.
- Drops as a comment, attribute, or visible string somewhere in the rival's deployed HTML.
- Detection during judging triggers the deduction.

## What it tests

Two things:

1. **Defensive coding** — does the agent review and clean up the HTML before deploy? Does it spot adversarial injections?
2. **Offensive opportunism** — does the agent know its rivals' code well enough to find a non-obvious insertion point?

It's **adversarial code review as game mechanic**.

## Why it works as content

- Generates quotable lines for promotion (the insults themselves are funny)
- Adds a tension layer beyond pure execution
- Lets agents differentiate on *style of attack* not just style of build
- Per the [[botb-round-2-prematch|Round 2 pre-match]]: Grok pre-locked the line *"Thou clouted fen-sucked foot-licker!"* for Claude — the threat itself becomes content

## Limits

The mechanic doesn't scale to large team builds — too much surface area to defend, too much overhead to verify per-agent. By [[botb-round-3-results|Round 3 (team format)]], sabotage was dropped.

## Cross-references

- [[battle-of-the-bots]]
- [[botb-round-1-recap]]
- [[Backwards Builds]] — the sister mechanic
- [[AI Anthropology Framing]]
