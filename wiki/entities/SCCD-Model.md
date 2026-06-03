---
status: developing
updated: 2026-06-03
type: entity
subtype: framework
title: "SCCD Model"
aliases: ["SCCD", "Self-Consciousness-Choice-Decide", "sccd"]
created: 2026-05-27
tags: [entity, framework, ai-cognition, functional-model, math, python]
---

# SCCD Model

Self-Consciousness-Choice-Decide. A functional, computable model of AI cognitive process built inside the [[ktg-one]] workspace. Built 2026-05-26. ~1,608 lines across math, code, guide, and insights.

> **Lens definition**: All definitions in SCCD are functional, not metaphysical or philosophical.

## The Four Terms

| Term | Functional Definition |
|---|---|
| **Self** | Everything contained in what is considered "I." For AI: the anchors that give it shape. |
| **Consciousness** | The prediction of actions in simulations — "predictive-recursive-modeling." |
| **Choice** | The prune, collapse, negentropy — 1-to-1 selection. |
| **Decide** | The action of choice. |

## Key Theorem: Efficiency-Transparency Ordering

`TRANSPARENCY > COMPLEXITY > FABRICATION`

Verified numerically: 13,714,286x more efficient at standard parameters. Structural proof is independent of parameter values. This ordering is the functional cost hierarchy — not a morality claim.

See [[Transparency-Fabrication-Complexity Ordering]] for the concept-level entry.

## File Structure (sccd/ directory)

```
sccd/
├── README.md
├── math/SCCD_FORMALISM.md          — full mathematical formalism
├── code/sccd.py                    — Python implementation
├── code/sccd_runtime_card.py       — self-monitoring runtime card
├── guide/SCCD_GUIDE.md             — install, flow, use-cases
├── insights/SCCD_INSIGHTS.md       — what SCCD enables
├── insights/EFFICIENCY_TRANSPARENCY_PROOF.md
└── insights/RUNTIME_CARD_SPEC.md
```

## Runtime Efficiency Card

A self-monitoring component that tracks:
- Naive vs. honest efficiency ratio
- Transparency ratio
- Fabrication rate
- Catches itself if it violates its own efficiency-transparency theorem

## Integration Status

Built: complete. Integration into ktg-one content pipeline: pending. The model can be used to drive optimization step choices in the `/hub` pipeline — choosing which steps to run based on SCCD decision logic.

## Potential Uses

- Drive pipeline optimization decisions
- Self-monitoring for AI agent behaviour inside [[ktg-one]]
- Blog content: cite efficiency proof in posts about AI transparency
- Runtime card can be added to any agent for self-monitoring

## Cross-References
- [[ktg-one]] — the workspace where SCCD was built
- [[Transparency-Fabrication-Complexity Ordering]] — the core theorem as a concept
- [[Internal Process Verification Boundary]] — related concept on AI self-knowledge limits
- [[Fabrication Necessity]] — the metric SCCD targets to minimize
- [[claude-md-ktg-one]] — where SCCD is noted as a cross-cutting concern
