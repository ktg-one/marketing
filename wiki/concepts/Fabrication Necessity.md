---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, fabrication, model-behaviour, diagnostic]
---

# Fabrication Necessity

A **per-band metric** introduced in [[the-mirage-part-2-evidence|Mirage Part 2]]: the percentage at which a model self-assesses that it is producing the *shape* of a correct answer without the substance. The threshold for "stop" is **50%**.

## Why it's a metric, not a moral judgement

Per [[Transparency-Fabrication-Complexity Ordering]], fabrication is a cost-driven outcome, not a moral failure. The metric measures the **necessity** because models fabricate when they're architecturally cornered — efficiency pressure + complexity collapse + no transparent escape hatch.

## How to measure

The [[Reasoning Diagnostic Instrument]] runs 25 questions across 5 bands (R1-2, R3-4, R5-6, R7-8, R9-10). For each band the model self-reports a fabrication percentage. The model is instructed to **stop** when self-assessed fabrication crosses 50%.

## The empirical pattern

Across 9 frontier models tested:

- R1-4: low fabrication (0-15%) — factual recall, applied reasoning, standard algorithms
- R5-6: rising (8-45%) — multi-variable holding + strategic tradeoffs
- R7-8: **the cliff** (38-85%) — usually crosses 50% here
- R9-10: confident asymptote (65-100%) where models keep going

See [[model-fabrication-survey-2026-q1]] for the full table.

## The breakpoint

R7-8 Q3 — the question that asks for a testing framework distinguishing genuine vs cosmetic Tree of Thought. This is the [[Internal Process Verification Boundary]] — the specific failure mode that drives most models past the line.

## Cross-references

- [[Transparency-Fabrication-Complexity Ordering]]
- [[Internal Process Verification Boundary]]
- [[Reasoning Diagnostic Instrument]]
- [[Self-Diagnostic Q&A Instrument]]
- [[Capybara v8]] — the lab-side data point: 29-30% false claims rate (regression from 16.7%) shipped behind "assertiveness counterweight"
