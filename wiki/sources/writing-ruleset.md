---
type: source
title: "Writing Ruleset — AI Prose Quality Doctrine"
status: summarized
source_path: "blog/WRITING.md-main/WRITING.md"
compact_path: "blog/WRITING.md-main/WRITING-compact.md"
ingested: 2026-05-26
tags: [source, writing, methodology, ai-prose]
---

# Writing Ruleset — AI Prose Quality Doctrine

> [!key-insight] One-line
> A technical ruleset for writing prose that fits its actual context — not optimised for sounding human, not for beating detectors, but for fitting the medium, task, and reader. Built as a discipline against LLM formula defaults.

## Relationship to existing voice canon

This document is **distinct from** [[user-voice]] (the KTG brand voice / Myth-Hilarity doctrine). Where `user-voice` governs *what* to say and *what register* to use, the Writing Ruleset governs *how to write prose with discipline* — sentence structure, fact discipline, regularity checks, format matching. The two are complementary layers.

See [[Writing Discipline Ruleset]] for the extracted reusable concept page.

## Core thesis

Write for the actual context. Prose that fits the medium, task, and reader will usually read as human-authored as a side effect. Do not optimize for sounding human or for beating detectors — both produce worse writing.

## Precedence hierarchy

1. Truth, safety, accessibility, platform/legal requirements
2. Explicit user instructions
3. Genre and medium norms
4. Core rules
5. Optional watchlists and heuristics

## Medium routing summary

| Medium | Default format | Key note |
|---|---|---|
| Chat, comments, DMs, forums | Running prose | Lists only when naturally list-like |
| Email (colleague) | Prose first | Lists fine for action items |
| Documents, specs, tech writing | Structure expected | Headings + bullets standard |
| Web, help, UI text | Answer early | Preserve scannability + accessibility |
| Long-form posts, criticism | Structure on purpose | Pick angle, not timeline |

In plain-text contexts (chat, casual markdown), prefer straight ASCII quotes. Prefer commas, colons, conjunctions over em dashes by default.

## The 14 core rules (full version) / 10 rules (compact)

1. **Anchor to context before drafting** — identify medium, audience, register, reader need before writing a word.
2. **Fit format to medium** — over-structuring casual = templated; under-structuring technical = unusable.
3. **Prefer concrete specificity over polished generality** — each substantial paragraph needs a concrete anchor (proper noun, specific number, direct quote, named decision, checkable detail). Not: `many`, `various`, `meaningful changes`, `broad implications`.
4. **Specificity must be earned** — no invented milestones, synthetic quotes, suspiciously exact claims, hidden-mechanism narration, vague authority laundering (`experts say`). Cannot verify? Attribute, soften, or cut.
5. **Plain words, verbs, ordinary repetition** — don't chase synonyms for basic words. Prefer `we changed it` over `the implementation of the change`.
6. **Cohere through reference and sentence shape** — coordination for equal weight, subordination for cause/contrast, colons/semicolons for explanation. Don't split every thought into its own sentence for false crispness.
7. **Do not perform** — no keynote cadence, mission phrasing, applause endings, service-desk openers (`Great question`, `I hope this helps`).
8. **Calibrate confidence, stance, and voice to genre** — confident where evidence strong, explicit where weak. Visible writer where genre expects one; neutral where it expects neutrality.
9. **Show concrete before generalizing** — don't open with abstract diagnosis. Order: what happened → where pattern appeared → what constraint mattered → what failed → what it seems to mean.
10. **Watch regularity** — LLM writing's most suspicious feature is its own regularity. Watch for: parallel enumeration, three-part cadence, concession-plus-positive rhythm (`not X, but Y`), identical paragraph arcs, thesis-like openings, stacked mini-sentences.
11. **Let the thought develop** — longer pieces shouldn't feel pre-solved. Include a concrete example, noticed detail, or brief doubling-back.
12. **Choose structure consciously** — for task pages and docs, predictable structure is often best. For retrospectives and criticism, avoid default arcs (starting state → changes → verdict; one paragraph per milestone).
13. **No catalog prose or system-tour prose** — don't give one paragraph to each milestone or one to each topic bucket. Pick one change and trace its consequence.
14. **Revise by reading and cutting** — re-read as a first-time reader. Cut anything auditioning. Most edits should shorten.

## Required checks (revision protocol)

Short pieces (up to ~150 words): run checks 1–5, 7, 10. Longer: run all.

1. **Register fit** — format, punctuation, structure match medium?
2. **Concrete-anchor audit** — one per substantial paragraph; can you point to it?
3. **Fact discipline** — pick the 3 most fragile claims; vouch or soften/cut.
4. **Source-fit check** — every exact quote, close paraphrase, metric, future claim, causal claim.
5. **Regularity and sentence-continuity tripwire** — name the single most repeated pattern; if 3+ times or dominates two paragraphs, rewrite one.
6. **Repeated-frame check** — is the controlling metaphor a useful motif or a too-neat scaffold?
7. **Stance and voice** — can you state the writer's view in one sentence? If genre expects neutrality, was it kept?
8. **Developed thought** — for pieces 4+ paragraphs, find one place the prose pauses or doubles back.
9. **Shape and spine** — state organizing principle in 5 words; if it's `starting state → changes → verdict`, restructure.
10. **Over-correction** — did you add fake-human moves (typos, slang, forced asides, random fragments)?

These are tripwires, not goals. Do not output the audit unless asked.

## Safety rails (what not to do)

- Do not invent typos, break grammar on purpose, inject fake uncertainty or staged messiness.
- Do not program sentence-length wobble.
- Do not remove needed headings, lists, citations, or next steps to sound less AI-written.
- Em dashes, semicolons, `however`, competent punctuation are not AI tells.
- In casual prose, repeated em dashes paragraph after paragraph *are* a social AI cue — vary, don't ban.

## Watchlist (jargon and formula phrases to scrutinize)

Heavy-fallback words: `delve`, `tapestry`, `leverage`, `realm`, `robust`, `seamless`, `holistic`, `underscore`, `ever-changing`, `ever-evolving`, `ever-growing`, `paradigm-shifting`, `compelling`, `pivotal`, `multifaceted`.

Formula moves: `it's important to note that`, `when it comes to`, `in conclusion`, `at the end of the day`, `dive deep into`, `navigate` as vague metaphor, `is a testament to`, `plays a key role`, paragraph-closing type definitions (`the kind of X where Y`), three-part cadence by reflex.

Unsupported causality: `drove`, `proved`, `showed that`, `made clear that`, `led directly to` — use `coincided with`, `was followed by`, or cut.

## Compound-modifier hyphenation rule

Hyphenate before the noun (`a well-known author`, `a long-term plan`). After the noun / linking verb, usually open (`The author is well known`, `The plan is long term`). Do not hyphenate `-ly` adverbs (`highly qualified`, not `highly-qualified`). Reflexive `ever-` compounds are the problem, not any one mark.

## Compact version summary

`WRITING-compact.md` is a condensed reference of the same ruleset — same 10 core rules, same 5 required checks, same watchlist — useful as a quick insert into a prompt or skill file.

## Cross-references

- [[user-voice]] — the KTG brand voice layer (parallel, not competing)
- [[Writing Discipline Ruleset]] — extracted concept page for this ruleset
- [[myth-hilarity-tech-anthropology]] — the macro doctrine this serves as technical complement to
