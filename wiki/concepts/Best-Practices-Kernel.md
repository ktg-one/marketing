---
type: concept
title: "Best-Practices Kernel"
aliases: ["best-practices", "engineering kernel", "agent kernel", "six-cut kernel"]
created: 2026-05-27
tags: [concept, engineering, best-practices, agent-discipline, plugin]
---

# Best-Practices Kernel

The upstream canonical engineering and agent discipline principles, packaged as the `best-practices-main` plugin in [[ktg-one]]. Source: `github.com/AgriciDaniel/best-practices`. Loaded via `/best-practices` skill invocation.

> **This is the canonical definition.** The behavioral rules in [[agents-md-ktg-one|AGENTS.md]] section 5 ("Think Before Coding", "Simplicity First", "Surgical Changes", "Goal-Driven Execution") are a project-scope re-statement of this upstream kernel. When the two conflict or diverge in detail, this plugin is the authoritative source.

## The Stance

> Context over text. Calibrated confidence. Evidence over vibes. No agreement theater. Confidence is earned, not asserted. Skepticism is not new information. Accountability is non-transferable: you read because you sign.

Without the stance, the kernel becomes ceremony.

## Engineering Kernel (Six Cuts)

### Before
- **Read before write.** Code you do not understand, you cannot change. Open call sites, tests, schema, consumers. Removals break assumptions as often as additions.
- **Name like the next reader is hostile.** Good names carry context, bad names hide bugs. Cannot name it cleanly = do not understand it yet.

### During
- **Smallest unit that works.** One purpose per unit, well-defined edges, testable in isolation. Complexity is earned, not anticipated. No abstraction without three real callers.
- **Delete more than you add.** Code is liability. Carry only what earns its weight every week.

### After
- **Evidence over intuition.** Measure before optimizing. Trust nothing unverified. If a task has no verification path, refuse it until it does.
- **Failure is the spec.** Before a fix, find the root cause; symptoms patched at the surface come back. Include the security failure path. An undo plan is not optional.

## Agent Kernel

Shipping with help (teammate, agent, swarm) nests rigor inside coordination.

- **One chair.** Every change has one human who owns the call.
- **Bounded slices.** No overlapping write scopes.
- **Explorers map, workers implement, verifiers gate.** Different read/write contracts.
- **Acceptance criteria written before execution.**
- **Per-change rigor inside every slice.** Orchestration amplifies the engineering kernel, does not exempt it.
- **Closeout has five parts.** Integrated result, verification summary, commit IDs per slice, notes current, next slice with rationale.

**Extra agent constraint**: Context is a budget, not a backdrop. Clear when poisoned. Dispatch fresh-context reviewers, not the same head twice.

## The Loop

Every diff:
1. Understand intent before touching keys
2. Enumerate blast radius before changing a public surface
3. Ship the smallest viable change
4. Prove it with tests, prove it again after every fix
5. Write the undo plan or do not ship

Guessing on any one means stop and investigate.

## Composition

- Needs enforcement for adversarial agents → add `obra/superpowers`
- Needs iron-law TDD → add `superpowers:test-driven-development`
- Needs debugging discipline → add `superpowers:systematic-debugging`
- Needs parallel-agent SOP → add `superpowers:dispatching-parallel-agents`

## Relationship to AGENTS.md

[[agents-md-ktg-one|AGENTS.md]] re-states four of these principles in section 5 under the project's own framing. That is a downstream re-statement. Per the user instruction: treat this plugin as the upstream canonical source, AGENTS.md as project-scope encoding. If section 5 of AGENTS.md ever contradicts this kernel, flag it — it should not.

## Relationship to Skill Loading

The agent kernel's "context is a budget" principle is directly implemented by [[Skill-Progressive-Disclosure]] in the plugin layer.

## Cross-References
- [[ktg-one]] — project using this plugin (`best-practices-main`)
- [[Skill-Progressive-Disclosure]] — implements the "context is a budget" agent kernel rule
- [[Pipeline-Verification-Criteria]] — implements "evidence over intuition" at pipeline scope
- [[agents-md-ktg-one]] — downstream re-statement of these principles
