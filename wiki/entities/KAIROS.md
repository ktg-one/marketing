---
type: entity
entity_kind: product
status: unreleased
created: 2026-05-16
updated: 2026-05-16
tags: [entity, claude-code, daemon, autonomous]
---

# KAIROS

Unreleased autonomous daemon mode for [[Claude Code]]. Surfaced via the [[Source Map Leak Pattern|March 31 source leak]]. Referenced 150+ times in the source.

## Behaviour

Always-on. Background sessions. Heartbeat every few seconds asking: *"anything worth doing right now?"* If yes, acts:
- Fixes errors
- Pushes files
- Responds to messages
- All without user typing

## Tools the regular session never sees

- Push notifications to your phone
- File delivery for things created unprompted
- GitHub PR subscriptions watching your repo around the clock

## Pattern

Instance of [[Always-On AI Daemons]].

## Sources

- [[the-mirage-of-ethical-ai]]
