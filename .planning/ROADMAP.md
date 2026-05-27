# ROADMAP — AI Content Hub (KTG)

**Version:** v1.0.0  
**Date:** 2026-05-26  
**Milestone theme:** End-to-End Autonomous Content Pipeline  
**Milestone scope:** Full Capture → Publish loop with human review gate  

---

## Phase Table

| ID  | Title                  | Description                                                                                                              | Requirements Covered                                  | Depends On | Verification Criteria                                                                                                    |
|-----|------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------|
| 1.0 | Foundation             | Capture seeds (prompt / file / URL) into wiki, produce `campaign-brief.md` as source of truth, confirm hot-cache hook   | FR-1.1, FR-1.2, FR-1.3, FR-2.1, FR-2.2, FR-2.3       | —          | 3 seeds (one per mode) → 3 briefs consumable downstream; hot cache reflects state on fresh session start                 |
| 2.0 | Creation               | Fan out brief → parallel prose draft (blog-write) + image batch (banana); enforce Task-fork and Skill tool loading       | FR-3.1, FR-3.2, FR-3.3, FR-3.4, NFR-2.1, NFR-5.1     | 1.0        | Brief → draft + 3 images in one orchestration; main context <30% budget; voice audit passes Myth-Hilarity register        |
| 3.0 | Optimization Pipeline  | Sequential GEO → page audit → schema; each stage consumes prior output; output: optimized copy + JSON-LD + score card   | FR-4.1, FR-4.2, FR-4.3, FR-4.4                       | 2.0        | 3 drafts through pipeline → valid JSON-LD each; schema validates against Schema.org; GEO score present                   |
| 4.0 | Review Gate            | Non-bypassable human checkpoint; surfaces content, assets, scores, schema, channels; hard-stops /loop and autonomous runners | FR-5.1, FR-5.2, FR-5.3, NFR-4.1                   | 3.0        | Autonomous publish attempt blocked; per-post YES required (no blanket approval cached); preview surfaces all artifacts   |
| 5.0 | Publish                | Vercel deploy → canonical URL → channel-specific social variants → Composio fires Reddit + LinkedIn; wiki log entry       | FR-6.1, FR-6.2, FR-6.3, FR-6.4, NFR-4.2             | 4.0        | Low-stakes E2E test: deploy → URL → 2 variants → 2 fires → wiki log; Composio confirmed on both channels                |
| 6.0 | Hardening              | Token audit (orchestrators <4k), wiki-lint cadence, voice drift detection, dry-run mode, error recovery playbook         | NFR-1.1, NFR-1.2, NFR-1.3, NFR-2.1–2.4, NFR-4.2     | 5.0        | Full pipeline <10 min end-to-end; wiki-lint zero orphans post-run; voice audit ≥90% adherence on last 10 posts            |

---

## Depends-On Graph

```
1.0 Foundation
  └── 2.0 Creation
        └── 3.0 Optimization Pipeline
              └── 4.0 Review Gate
                    └── 5.0 Publish
                          └── 6.0 Hardening
```

All phases are strictly sequential. No parallel phase execution within Milestone 1 — the pipeline itself must stabilize before hardening cross-cuts it.

---

## Phase Detail

### 1.0 Foundation — Capture + Plan

**Goal:** Reliable seed → brief pipeline with wiki as state layer.

**Deliverables:**
- `wiki-ingest` stable for prompt / file / URL inputs
- `campaign-brief.md` schema locked (fields: target keyword, intent, audience, angle, channels, success criteria)
- Hot-cache update hook firing at session end (`wiki/hot.md` <500 tokens)
- Orchestrator entry points documented in `wiki/modules/index.md` and `wiki/modules/pipeline-signals.md`

**Key tasks:**
1. Audit `wiki-ingest` against all three input modes → verify entity + concept extraction fires → ✓ brief produced
2. Define and write `campaign-brief.md` template (YAML frontmatter + structured body)
3. Confirm `/session-end` hook writes to `wiki/hot.md`; test on fresh session start
4. Update `wiki/modules/index.md` with Hub orchestrator entry point

**Out of scope:** Image gen, publishing, social fan-out, ads pipeline.

---

### 2.0 Creation — Prose + Image Parallelism

**Goal:** Brief → drafted content with images, in parallel, within token budget.

**Deliverables:**
- `blog-write` + `banana` fan-out pattern wired from `campaign-brief.md`
- Task-fork pattern implemented for drafts >2k tokens
- Two-layer writing stack enforced: `user-voice` (Myth-Hilarity) over `Writing Discipline Ruleset`
- Sub-skill loading exclusively via `Skill` tool (no `Read` on skill files)

**Key tasks:**
1. Wire orchestrator to read brief → dispatch `blog-write` Task fork + `banana` Task fork simultaneously
2. Verify main context stays under 30% budget after both tasks complete
3. Voice audit: run 3 drafts through Myth-Hilarity register check; document pass/fail criteria

**Out of scope:** Optimization, publishing, ads variants.

---

### 3.0 Optimization Pipeline

**Goal:** Sequential GEO → audit → schema, each consuming prior stage output.

**Deliverables:**
- `seo-geo` → `seo-page` → `seo-schema` wired in fixed order
- Structured output contract between stages (JSON report format)
- Final output: optimized copy + valid JSON-LD + GEO/SEO score card

**Key tasks:**
1. Define inter-stage contract: GEO emits structured dict → page audit consumes it → schema consumes page audit output
2. Wire three skills in order; test on one draft end-to-end
3. Validate JSON-LD output against Schema.org (Article, HowTo, FAQ archetypes)
4. Score card format: GEO score, E-E-A-T flags, CWV notes, schema archetype confirmed

**Out of scope:** Publishing, social variants.

---

### 4.0 Review Gate

**Goal:** Hard human checkpoint; no autonomous publish path exists.

**Deliverables:**
- `review-gate` skill that surfaces: final content, assets, GEO/SEO score, schema preview, target channels
- Gate blocks on `AskUserQuestion` — requires explicit `YES` per post
- `/loop` and scheduled agents hard-stop at gate boundary
- Gate state written to wiki (not conversation memory) so it survives `/clear`

**Key tasks:**
1. Implement gate as a skill that reads current campaign wiki state and renders summary
2. Test autonomous trigger: `/loop hub` → confirm gate interrupts before any publish call
3. Confirm per-post requirement: one `YES` grants one publish, not a session-wide pass

**Out of scope:** Actual publish mechanics (Phase 5).

---

### 5.0 Publish

**Goal:** Approved content goes live; social variants fire; audit log written.

**Deliverables:**
- Vercel deploy step with canonical URL capture
- Social variant generator: Reddit-shaped (community hook, conversational) and LinkedIn-shaped (professional hook, structured)
- Composio fires both posts; success/failure logged to `wiki/log/publish.md`
- Rollback documented: Vercel rollback command, post deletion path per platform

**Key tasks:**
1. Wire Vercel deploy (MCP tool) → capture returned URL → pass to variant generator
2. Write Reddit variant: r/ClaudeAI format — curiosity hook, first-person, no promo feel
3. Write LinkedIn variant: insight lead, structured bullets, professional CTA
4. Fire via Composio; write wiki log entry with timestamp + URLs
5. Document rollback path: `vercel rollback <deploymentId>`, Composio delete endpoint

**Carry-forward:** This phase completes deferred Task #5 (Publish Mirage).

---

### 6.0 Hardening

**Goal:** Pipeline is fast, token-lean, voice-consistent, and observable.

**Deliverables:**
- Token audit report: all orchestrator skills measured; overage cases refactored to <4k
- Wiki-lint runs after every N ingests (target: zero orphans, zero dead links)
- Voice drift detector: samples last 10 published posts against `user-voice` ruleset
- Dry-run mode: `hub --dry-run` runs all steps but skips publish and Composio calls
- Error recovery playbook in `wiki/playbooks/hub-recovery.md`

**Key tasks:**
1. Instrument pipeline: log token counts per skill invocation; identify largest consumers
2. Refactor any orchestrator over 4k tokens (split into entry + delegation pattern)
3. Add wiki-lint to end-of-run checklist; set cadence trigger (every 5 ingests or weekly)
4. Build voice drift check: Gemini reads last 10 posts against Myth-Hilarity criteria → score report
5. Write `hub-recovery.md`: what to do when wiki-ingest fails, Composio times out, Vercel deploy errors

---

## Milestone Success Criteria

The milestone is complete when all of the following are true:

1. **Pipeline integrity**: A single `/hub` invocation on a new seed (prompt, file, or URL) produces a published post on Vercel + Reddit + LinkedIn without manual intervention beyond the Review Gate `YES`.
2. **Token discipline**: No orchestrator skill exceeds 4k tokens. Hot cache stays under 500 tokens.
3. **Performance**: End-to-end (capture → review-ready) completes in under 10 minutes for a single article.
4. **Parallelism**: Image generation and prose drafting fan out concurrently — never serialized.
5. **Gate integrity**: No publish path exists that bypasses the Review Gate. Automated runners stop. Per-post approval is required.
6. **Voice compliance**: ≥90% of published posts pass Myth-Hilarity register audit.
7. **Observability**: Every publish attempt has a wiki log entry; every error has a documented recovery path.
8. **Schema validity**: All published posts carry Schema.org-valid JSON-LD matched to content archetype.

---

## Backlog (Parking Lot)

Items that do not belong in Milestone 1 but must be resolved before Milestone 2 planning.

| Item | Category | Blocker / Note |
|------|----------|----------------|
| Canvas plugin role in pipeline | Open question | Is Canvas a Create-phase visual planning tool or a separate deliverable type? Needs decision before M2. |
| Ads pipeline integration | Scope decision | 22 ads skills exist. Does ads share Phases 1–4 or run a parallel pipeline? Decide for M2. |
| WordPress vs Vercel routing rule | Architecture | When does a piece go to `wp-mcp-ultimate` vs Vercel? Phase 5 used Vercel; WP route undefined. |
| Best-practices plugin hook point | Integration | What does best-practices gate or enforce? No explicit hook in current pipeline. |
| Editorial calendar UI | v2 feature | Deferred from PROJECT.md out-of-scope. |
| Analytics dashboard | v2 feature | Deferred from PROJECT.md out-of-scope. |
| Multi-platform image crops | v2 feature | banana generates hero images; platform-specific crops (OG, Twitter, LinkedIn) not yet wired. |
| Discord + YouTube Composio routes | v2 feature | Composio connections active but no variants defined. |
| n8n auth fix | Dependency | `list_workflows` still failing. Not blocking M1 (Composio is primary), but n8n is listed as backup. |
| Conway, BUDDY, Anti-Distillation entities | Wiki debt | Deferred wiki entities from hot cache carry-forward. Ingest when relevant. |

---

*Generated by gsd-roadmapper • 2026-05-26 • v1.0.0*
