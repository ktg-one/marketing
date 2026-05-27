---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, architecture, strawhats]
---

# Cognitive Architecture (Prompt-Only)

The thesis behind [[STRAWHATS-DIRECTIVE]]: LLM output quality is bounded not by model capability but by the **architecture of the prompt envelope** around it.

## Tagline

> Stop prompting. Start architecting.

## The argument

A bare prompt asks the model to do everything in one pass: assess the task, choose a method, plan, execute, verify, polish. The model has no architectural place to put uncertainty, no gate to refuse, no protocol to iterate. Result: it generates. Confidently. See [[Fabrication Necessity]] for the empirical confirmation.

A cognitive architecture (like [[STRAWHATS-DIRECTIVE]]) **separates the cascade**:

1. **Assess before planning** — RKQDE, Success Criteria Lock
2. **Plan before executing** — MR.RUG, SkeleTraIn, Prompt Bombs, ARQ Gate
3. **Iterate before delivering** — 3-Iteration Protocol, CoVE, Gap Scan
4. **Curate before saving** — Density Optimization, BoT

Each phase has gates. Each gate enforces confidence ≥0.9 or refusal. The model now has architectural permission to stop fabricating.

## Why "Prompt-Only"

The qualifier matters. STRAWHATS achieves the Vertex 99.99th percentile **without fine-tuning, without tool use, without custom inference**. The architecture lives entirely in the prompt envelope. That's the upper limit of what's currently possible with prompt-only engineering.

## Cross-references

- [[STRAWHATS-DIRECTIVE]] — the canonical implementation
- [[the-cascade]] — the framework essay
- [[Fabrication Necessity]] — the empirical problem this solves
- [[Internal Process Verification Boundary]] — the specific failure mode bare prompting can't address
