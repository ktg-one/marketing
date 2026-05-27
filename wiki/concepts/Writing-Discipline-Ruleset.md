---
type: concept
title: "Writing Discipline Ruleset"
tags: [concept, writing, prose, methodology, ai-writing]
created: 2026-05-26
---

# Writing Discipline Ruleset

> [!key-insight]
> A technical prose-quality discipline for AI-assisted writing — not optimising for "sounding human" but for fitting medium, task, and reader. The primary defence against LLM formula defaults.

## What this is (and isn't)

This ruleset operates at the *prose craft* layer. It is not [[user-voice]] (which governs the KTG brand register and Myth-Hilarity doctrine) — it is the technical complement. Where the brand voice says *what tone to use*, this ruleset says *how to write sentences that don't collapse into formula*.

It is also not a detector-evasion system. Optimising for sounding human or for beating AI detectors both produce worse writing.

## The core principle

Write for the actual context. Prose that fits the medium, task, and reader will usually read as human-authored as a side effect.

## The regularity problem

The single most common failure mode in LLM writing is **regularity** — not any individual word or move, but the predictable repetition of the same structural choices:

- Three-part cadence inside sentences by reflex
- Concession-plus-positive rhythm (`not X, but Y`) every few paragraphs
- One neat claim sentence per paragraph followed by orderly elaboration
- Same punctuation move (em dash, colon) doing the same job repeatedly
- Thesis-like openers on every paragraph
- Stacked mini-sentences for false crispness

The fix is not random variation. It is breaking the *pattern* where it dominates.

## Medium routing

Different media require different defaults:

- **Chat, comments, DMs**: running prose by default; lists only when naturally list-like; straight quotes in plain text; commas/colons/conjunctions over em dashes
- **Email**: prose first, lists for discrete action items
- **Documents, specs, technical writing**: structure is expected — use it
- **Web, help, UI text**: answer early; preserve scannability and accessibility
- **Long-form posts, criticism**: pick an angle, not a timeline; structure on purpose

## Concrete anchor requirement

Each substantial paragraph needs at least one concrete anchor:
- A proper noun the reader could look up
- A specific number (not just a date or version)
- A direct quote
- A named decision, moment, or thread
- A checkable detail

What does not count: `many`, `various`, `meaningful changes`, `broad implications`, bare milestone names.

## Fact discipline

Three categories of high-fragility claims require special care: exact quotes, public metrics, and causal claims. If `X caused Y` cannot be sourced directly, use `coincided with`, `was followed by`, or cut the causal relationship. Do not launder through `experts say`, `observers note`, `research suggests` without naming the source and confirming it supports the exact claim.

## Structure for longer pieces

Default genre shapes are fine for task pages, procedures, and news briefs. For retrospectives, criticism, and developmental writing, avoid:
- Starting state → changes → verdict
- One paragraph per named milestone
- One topic bucket per paragraph

Pick a through-line instead: one constraint that started biting, one mismatch between promise and reality, one shift in what people had to do. Cross-wire paragraphs so they depend on each other rather than sitting as labeled boxes.

## Required checks (five-point revision protocol)

1. **Register fit** — does format match medium and request?
2. **Concrete anchor** — one per substantial paragraph; if none, add or cut
3. **Regularity tripwire** — name the most repeated pattern; 3+ times = rewrite one
4. **Stance and shape** — can you state the organizing principle in 5 words?
5. **Over-correction** — added fake-human moves to break the pattern?

## Watchlist

Heavy-fallback words to scrutinize: `delve`, `tapestry`, `leverage`, `realm`, `robust`, `seamless`, `holistic`, `underscore`, `ever-evolving`, `paradigm-shifting`, `compelling`, `pivotal`.

Formula phrases: `it's important to note`, `when it comes to`, `in conclusion`, `is a testament to`, `plays a key role`, `the kind of X where Y`.

Unsupported causality: `drove`, `proved`, `showed that`, `led directly to` → replace with `coincided with`, `was followed by`, or cut.

## Relationship to KTG voice

| Layer | Source | Governs |
|---|---|---|
| Brand voice | [[user-voice]] | Register, tone, Myth-Hilarity doctrine |
| Prose discipline | [[writing-ruleset]] | Sentence structure, fact handling, regularity checks |
| Overall doctrine | [[myth-hilarity-tech-anthropology]] | The macro creative method |

## Cross-references

- [[writing-ruleset]] — full source page (both WRITING.md and WRITING-compact.md)
- [[user-voice]] — the KTG brand voice layer
- [[myth-hilarity-tech-anthropology]] — the macro doctrine this serves
