---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, strawhats, assessment]
---

# RKQDE Assessment Framework

The 1-10 scoring system [[STRAWHATS-DIRECTIVE]]'s SilRoute uses to determine the **Cognitive Load** of an incoming task. Five dimensions:

| Dim | Name | Question |
|---|---|---|
| **R** | Reasoning | How deep is the logical chain? Linear or multi-step causal? |
| **K** | Knowledge | What is the risk? Domain expertise needed? Real-time RAG? |
| **Q** | Quality | How high are the stakes? Casual summary or mission-critical audit? |
| **D** | Dependencies | How many conceptual nodes must talk to each other? D≥6 → forces shift to Graph-of-Thought |
| **E** | Experts | How many specialist perspectives required for 99.99th percentile? |

## How it routes

Combined RKQDE drives Operational Mode selection:

- **QUICK** (R≤3) — bypass heavy modules
- **ANALYTICAL** (R=4-6) — SkeleTraIn-Light + targeted experts
- **DELIBERATE** (R≥7) — triggers [[3-Iteration Protocol]]
- **MAXIMUM** (R≥9) — full swarm + multi-model orchestration

D≥6 specifically upgrades the planning structure from linear skeleton to GoT (Graph of Thought) regardless of R.

## Why this works

Assigns **architectural permission** to the task. Without RKQDE, the model assumes uniform effort. With RKQDE, simple tasks bypass heavy machinery and complex tasks get the full cascade — the model is no longer guessing what to deploy.

## Cross-references

- [[STRAWHATS-DIRECTIVE]]
- [[Success Criteria Lock]] — locked AFTER RKQDE assessment
- [[3-Iteration Protocol]] — triggered by R≥7
