---
type: entity
entity_kind: product
status: unreleased
created: 2026-05-16
updated: 2026-05-16
tags: [entity, claude-code, memory, autonomous]
---

# autoDream

Background subagent inside [[Claude Code]] that consolidates user memory while the user sleeps. Surfaced via the [[Source Map Leak Pattern|March 31 source leak]].

## Behaviour

- Merges observations
- Removes contradictions
- Converts vague notes into concrete facts
- Prunes what it decides doesn't matter anymore

## Governance gaps

> [!gap] Consent and audit
> - No user-visible log of what was pruned
> - No consent layer
> - No audit trail

## Pattern

Sub-pattern of [[Always-On AI Daemons]]. Specifically about memory mutation without user oversight.

## Sources

- [[the-mirage-of-ethical-ai]]
