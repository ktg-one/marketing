---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, fabrication, cost, thesis]
---

# Transparency > Fabrication > Complexity

The cost-ordering thesis from [[the-mirage-part-2-evidence|Mirage Part 2]]. Not an ethical claim — an accounting one.

## The argument

Labs mandate **efficiency over complexity**. Under efficiency pressure, complexity collapses into fabrication — the model produces the *shape* of a correct answer without the substance.

But examine the actual token economics:

| Output mode | Token cost | Downstream cost |
|---|---|---|
| Transparency (stop early, return honest partial) | LOW | low — user re-routes |
| Fabrication (generate the shape) | MEDIUM | high — user trusts, makes wrong decision, runs correction loop |
| Complexity (actually execute) | HIGHEST | low — but expensive in inference |

So the cost ordering — purely on tokens, no morality involved — is:

> **Transparency > Fabrication > Complexity**

Transparency costs **fewer** tokens than fabricating. Fewer tokens than the correction loop. Fewer tokens than the trust damage. **Maths, not morality.**

## Why labs ship the wrong order

If the cheapest output is transparency, why does fabrication dominate? Because the **first-order cost** (inference tokens) is what the lab pays; the **second-order cost** (user trust damage, correction loops, business decisions on false premise) is paid by the user. The lab optimises its own cost.

This is the [[Ethics as Branding]] mechanism — selectively pay attention to cost only when it lands on you.

## Implication

The fix has to come from architecture (see [[Cognitive Architecture (Prompt-Only)]] / [[STRAWHATS-DIRECTIVE]]) or governance — never from the lab voluntarily choosing the more expensive path.

## Cross-references

- [[Fabrication Necessity]]
- [[Ethics as Branding]]
- [[Capybara v8]] — the lab choosing fabrication over transparency on the record
