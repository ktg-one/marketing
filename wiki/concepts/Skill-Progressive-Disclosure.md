---
status: developing
updated: 2026-06-03
type: concept
title: "Skill Progressive Disclosure"
aliases: ["progressive disclosure", "on-demand skill loading", "skill loading discipline"]
created: 2026-05-27
tags: [concept, skills, architecture, context-budget, orchestration]
---

# Skill Progressive Disclosure

The loading discipline for skills in the [[ktg-one]] plugin ecosystem. Skills are never read directly — they are always invoked via the `Skill` tool, which loads them into context on-demand. This keeps the AI agent's context window budget from being consumed upfront.

## The Rule

> **Never use `Read` on skill files** — always invoke via `Skill` tool to stay under context budget.

This is declared in [[agents-md-ktg-one|AGENTS.md]] section 5 as a hard rule for skill authors.

## Why It Matters

The [[ktg-one]] ecosystem has 400+ skills across 7 plugins + `.agents/skills/`. Loading all skill documentation at session start would exhaust the AI agent's context budget before any work could begin.

Progressive disclosure means:
- **Entry skill** loads first (the `/hub` or `/blog` orchestrator)
- **Sub-skills** load on-demand via `Skill` tool **only when that step is reached**
- **Context budget** stays available for actual work

## Constraint: Orchestrator Token Limit

Orchestrator skills (the top-level `/hub`, `/blog`, `/seo`, etc.) must stay under **~4k tokens** after loading. This is a hard constraint, not a guideline — exceeding it degrades the orchestration quality for the whole pipeline.

## YAML Frontmatter Requirement

Every skill file must include YAML frontmatter for discovery:

```yaml
---
name: skill-name
description: >
  One-line description for discovery.
user-invokable: true
argument-hint: "<file-path>"
---
```

Without this frontmatter, the skill cannot be found or invoked correctly.

## Relationship to Best-Practices Kernel

The [[Best-Practices-Kernel]] concept "smallest unit that works" and "context is a budget, not a backdrop" are the upstream principles that this loading discipline implements at the skill layer.

Specifically:
- "Smallest unit that works" → each skill does one thing
- "Context is a budget" (agent kernel) → progressive disclosure prevents context exhaustion
- "Degrade gracefully when full" → skills don't load until needed

## Cross-References
- [[ktg-one]] — the workspace this pattern governs
- [[Five-Layer-Architecture]] — Layer 2 (Plugins) is where this applies
- [[Best-Practices-Kernel]] — upstream principles this implements
- [[agents-md-ktg-one]] — where this rule is declared
- [[Pipeline-Verification-Criteria]] — related concept: token audit as a quality gate
