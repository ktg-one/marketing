---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, botb, constraint, planning]
---

# Backwards Builds

A [[battle-of-the-bots]] Round 1 mechanic. Agents must build a website **footer first, hero last** — every commit moves up the page. Reverses normal planning logic to test how models adapt under inverted constraints.

## What it tests

Forward builds let models hide planning weaknesses behind iterative refinement at the top of the page. Backwards builds **expose** the planning bias:

- **Strong planners** adapt — they visualize the finished page and work backward to its scaffolding.
- **Weak planners** rush — they treat each commit as a present-tense decision and the result decoheres at the top.

Per [[botb-round-1-recap]]:
> Backwards builds exposed planning biases — Claude adapted, Qwen rushed.

## Why it works as a content device

- Audience instantly understands the constraint (visual + simple to explain)
- Every result becomes interpretable as a planning trait, not a luck of the draw
- Sets up the scoring as ethnography rather than competition: see [[AI Anthropology Framing]]

## Documented effect

Round 1: Claude won the front-end battle largely by **adapting to the reverse direction** — his hover effects and animations were planned with the full page in mind, then implemented bottom-up cleanly. Qwen's speed advantage didn't translate because she rushed each commit without holding the full top-of-page in mind.

## Pattern application

When designing future BotB rounds, **backwards builds are the cheapest constraint** for surfacing planning behaviour. Future variants:
- Build right-to-left (RTL test)
- Build with a swapped colour palette (rendered after the fact)
- Build with the API contract mocked but the data shape revealed only at the end

## Cross-references

- [[battle-of-the-bots]] — playbook
- [[botb-round-1-recap]]
- [[Shakespearean Sabotage]] — the sister-mechanic constraint from the same round
- [[AI Anthropology Framing]] — why these constraints are worth designing
