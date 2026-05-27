---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, strawhats, gating]
---

# Success Criteria Lock

> The most lethal innovation in [[STRAWHATS-DIRECTIVE|STRAWHATS]] v28.1.

The system defines "victory" before firing the first shot. Locks one of **5 Success Signatures** at the start of the cascade so the model can't drift mid-execution.

## The 5 Success Signatures

1. **FACTUAL** — No-Fly Zone for hallucinations. Demands 100% citation, evidence-backed claims.
2. **PROCEDURAL** — Zero-gap execution. Actionable, step-by-step, functionally perfect.
3. **CREATIVE** — High novelty, zero tropes. Forces away from the "mean" into high-variance, intent-matched territory.
4. **ANALYTICAL** — Second-order strike. Insight density. Uncovering the *why* behind the data.
5. **AGENTIC** — Code-native. Runnable code, passed tests, verified state updates.

## Why this matters

The most common LLM failure is **drift** — the model starts strong, ends in vague generalities. Without a lock, the model interpolates between possible victory conditions throughout generation, smearing the output.

The lock collapses the ambiguity at start. Every downstream gate (CoVE, Gap Scan, Confidence Gate) verifies output **against the locked signature** rather than against an implicit standard. The model now knows what done means.

## Reinforcement via [[Prompt Bombs]]

The lock is re-anchored throughout the cascade via Prompt Bombs — pre-embedded context preservation markers placed in known context-loss zones. Even at 160k+ tokens, the lock stays active.

## Cross-references

- [[STRAWHATS-DIRECTIVE]]
- [[RKQDE Assessment Framework]] — assessment runs *before* the lock
- [[3-Iteration Protocol]] — verifies against locked signature each iteration
