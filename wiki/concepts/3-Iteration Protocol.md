---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, strawhats, execution]
---

# 3-Iteration Protocol

For any task with **Reasoning Complexity R≥7**, [[STRAWHATS-DIRECTIVE]] forbids single-pass execution. Three distinct cognitive states.

## The iterations

| # | State | Mode | Role |
|---|---|---|---|
| **1** | DISCOVERY | Exploration ("No Pressure" pass) | Map the space. Plant Prompt Bombs. Don't care about polish — care about finding everything. |
| **2** | VALIDATION | Enrichment | Analytical strike. Verify every claim. Fill gaps. Audit logic chains via RA-RAG. |
| **3** | SYNTHESIS | Polish | Final UX pass. Apply Density Optimization. Maximum value per token. |

## Why iteration prevents "model exhaustion"

A single-pass on a high-R task forces the model to do exploration, verification, AND polish in one generation. It can't. So it picks one mode and pretends to do the others — usually polishing as a substitute for verifying. That's where [[Fabrication Necessity]] spikes (see [[the-mirage-part-2-evidence|R7-8 fabrication data]]).

The protocol gives the model **three distinct generations**, each with its own success criteria. Each iteration writes to BoT. Each iteration is gated by Confidence ≥0.9.

## Cross-references

- [[STRAWHATS-DIRECTIVE]]
- [[Fabrication Necessity]] — empirical justification for the protocol
- [[Internal Process Verification Boundary]] — the failure mode iteration mitigates
