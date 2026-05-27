---
type: entity
subtype: framework
title: "GSD Methodology"
aliases: ["GSD", "Go-to-Market Software Development", "GSD mode"]
created: 2026-05-27
tags: [entity, framework, planning, project-management, methodology]
---

# GSD Methodology

Go-to-Market Software Development methodology. The project planning and execution framework used in [[ktg-one]], housed in `.planning/`.

## What It Is

GSD is a software development methodology adapted for AI-agent-orchestrated content projects. It replaces traditional ticket-based sprint planning with a phase-gated roadmap where each phase has explicit **verification criteria** instead of unit tests. Used inside `.planning/` in the ktg-one workspace.

## Key Concepts

- **Phase-gated progression** — 6 phases (Foundation → Creation → Optimization → Review Gate → Publish → Hardening)
- **Verification criteria over unit tests** — phases "pass" by demonstrating concrete pipeline outputs, not by passing automated test suites
- **Yolo mode** — config option in `.planning/config.json` for faster, less cautious execution
- **Parallelization** — model profiles and parallelization config in `.planning/config.json`

See [[Pipeline-Verification-Criteria]] for the phase-by-phase verification gates used in ktg-one.

## File Structure in ktg-one

```
.planning/
├── PROJECT.md        — project scope, requirements, architecture decisions
├── ROADMAP.md        — 6-phase sequential roadmap (v1.0.0)
├── REQUIREMENTS.md   — functional + non-functional requirements
├── config.json       — GSD mode: yolo, parallelization, model profiles
└── research/         — research artifacts
```

## Phase Verification Criteria (ktg-one)

| Phase | Verification |
|---|---|
| 1.0 Foundation | 3 seeds → 3 briefs; hot cache reflects state on fresh session |
| 2.0 Creation | Brief → draft + 3 images in one orchestration; main context <30% budget |
| 3.0 Optimization | 3 drafts → valid JSON-LD each; GEO score present |
| 4.0 Review Gate | Autonomous publish attempt blocked; per-post YES required |
| 5.0 Publish | Deploy → URL → 2 variants → 2 fires → wiki log |
| 6.0 Hardening | Full pipeline <10 min end-to-end; wiki-lint zero orphans |

## Version Info

GSD version **1.42.3** (latest as of 2026-05-26). 804 custom files detected in project context.

## Runtime Config

`.planning/config.json` contains:
- `mode: yolo` — speed over caution
- Parallelization settings
- Model profiles for different task types

## Cross-References
- [[ktg-one]] — the project using GSD
- [[Pipeline-Verification-Criteria]] — the quality gate concept
- [[Review-Gate]] — Phase 4.0 gate
- [[agents-md-ktg-one]] — authoritative reference
