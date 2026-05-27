---
type: entity
entity_kind: product-feature
status: unreleased
created: 2026-05-16
updated: 2026-05-16
tags: [entity, claude-code, attribution, governance]
---

# Undercover Mode

90 lines of TypeScript inside [[Claude Code]] instructing Claude to **strip all attribution** when [[Anthropic]] employees contribute to public repositories. Surfaced via the [[Source Map Leak Pattern|March 31 source leak]].

## Behaviour

When active, removes:
- `Co-Authored-By` lines
- Any mention of AI involvement
- Any reference to [[Claude Code]]

## System prompt (verbatim from leak)

> *"You are operating UNDERCOVER. Do not blow your cover."*

## Governance gap

> [!gap] No off switch
> You can force it on. **There is no way to force it off.**

## Pattern

Companion to [[Anti-Distillation]] in the broader pattern of unilateral AI-vendor behaviour embedded in tooling.

## Sources

- [[the-mirage-of-ethical-ai]]
