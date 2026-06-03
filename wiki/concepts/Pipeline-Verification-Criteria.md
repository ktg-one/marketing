---
status: developing
updated: 2026-06-03
type: concept
title: "Pipeline Verification Criteria"
aliases: ["phase verification", "pipeline gates", "verification criteria", "quality gates"]
created: 2026-05-27
tags: [concept, pipeline, quality, testing, verification, gsd]
---

# Pipeline Verification Criteria

Phase-by-phase verification gates used in [[ktg-one]] instead of a traditional automated test suite. The alternative to pytest/jest/CI in an agent-orchestrated content pipeline. Defined in `.planning/ROADMAP.md`.

> "This project has **no traditional build system** and **no test suite** in the conventional software engineering sense. The 'build' is skill orchestration; the 'tests' are pipeline verification criteria." — [[agents-md-ktg-one|AGENTS.md]]

## Why Verification Criteria Instead of Unit Tests

A content pipeline produces human-evaluated outputs (drafts, social posts, images, SEO scores). Automated unit tests cannot verify whether a LinkedIn post "sounds right" or whether a GEO score is meaningful. Phase verification criteria test the pipeline's end-to-end output properties at the level where quality actually lives.

This is the "evidence over intuition" principle from the [[Best-Practices-Kernel]] applied at pipeline scope.

## The Six Phase Gates ([[GSD-Methodology]])

| Phase | Verification Criterion |
|---|---|
| **1.0 Foundation** | 3 seeds → 3 briefs generated; `wiki/hot.md` reflects current state on a fresh session start |
| **2.0 Creation** | 1 brief → 1 draft + 3 images in one orchestration run; main context stays under 30% budget |
| **3.0 Optimization** | 3 drafts through optimization pipeline → valid JSON-LD schema each; GEO score present |
| **4.0 Review Gate** | Autonomous publish attempt is blocked; per-post `YES` required before anything fires |
| **5.0 Publish** | Deploy → URL captured → 2 social variants → 2 fires → wiki log entry written |
| **6.0 Hardening** | Full pipeline completes end-to-end in <10 minutes; `/wiki-lint` returns zero orphans |

## Supplementary Quality Checks

Beyond the phase gates, quality is also verified by:

1. **Wiki lint** — `/wiki-lint` to detect orphans, dead links, frontmatter gaps
2. **Voice audit** — sample drafts against `[[user-voice]]` (Myth-Hilarity ruleset)
3. **Schema validation** — verify JSON-LD output against Schema.org using `seo-schema` skill
4. **Token audit** — ensure orchestrator skills stay under 4k tokens after loading (see [[Skill-Progressive-Disclosure]])

## Manual Test: Full Pipeline

```
1. Create test post in wiki/content/test-post/post.md
2. Run /hub wiki/content/test-post/post.md
3. Verify: 4 social variants, hero + 3 crops, GEO score, schema.json
4. Verify: Review gate stops and waits for YES
5. Type STOP to cancel (do not publish test content)
6. Run /wiki-lint — confirm zero orphans
```

## Relationship to AGENTS.md

This concept is defined in AGENTS.md section 4 (Build and Test Commands) and section 6 (Testing Instructions). The source of truth for phase criteria is `.planning/ROADMAP.md`.

## Cross-References
- [[GSD-Methodology]] — the framework these criteria belong to
- [[Review-Gate]] — Phase 4.0 gate
- [[Best-Practices-Kernel]] — "evidence over intuition" upstream principle
- [[Skill-Progressive-Disclosure]] — token audit gate
- [[ktg-one]] — the pipeline being verified
- [[agents-md-ktg-one]] — where these criteria are formally listed
