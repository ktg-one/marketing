# Testing Patterns

**Analysis Date:** 2026-05-27

## There Is No Automated Test Suite

This is explicit and intentional. From `AGENTS.md` §6 and `CLAUDE.md`:

> There is **no automated test suite** (no pytest, no jest, no CI). Quality is ensured through pipeline verification criteria defined in `.planning/ROADMAP.md`.

There is **no `pytest`, no `jest`, no `make test`, no GitHub Actions workflow** at the repo root. The Python `main.py` is a stub (`print("Hello from ktg-one!")`). `pyproject.toml` declares no test dependencies. Quality gates are pipeline verification criteria, wiki state integrity checks, voice audits, schema validation, and token budget audits.

This is a deliberate decision. The "code" here is skill orchestration + wiki state + content — none of which is meaningfully tested by unit tests. The verifiable assertions live one level up: did the pipeline produce a valid 8-file publish-kit? Does the wiki still pass lint? Does the draft hit the voice register?

(Note: individual skill plugins shipped from upstream — e.g. `claude-blog-main`, `claude-seo` — contain their own `tests/` directories with pytest. Those are upstream-author tests, not part of ktg-one's quality loop. Do not extend them here.)

## Quality Mechanisms (the actual "tests")

There are six quality mechanisms in active use. Each is invoked manually or as part of a phase verification.

### 1. Phase Verification Criteria (`.planning/ROADMAP.md`)

Each of the six pipeline phases has explicit pass/fail criteria. These are the closest thing to acceptance tests in this repo.

| Phase | Verification Criteria |
|-------|----------------------|
| **1.0 Foundation** | 3 seeds (one per input mode: prompt / file / URL) → 3 briefs consumable downstream; hot cache reflects state on fresh session start |
| **2.0 Creation** | Brief → draft + 3 images in one orchestration; main context <30% budget; voice audit passes Myth-Hilarity register |
| **3.0 Optimization** | 3 drafts through pipeline → valid JSON-LD each; schema validates against Schema.org; GEO score present |
| **4.0 Review Gate** | Autonomous publish attempt blocked; per-post `YES` required (no blanket approval cached); preview surfaces all artifacts |
| **5.0 Publish** | Low-stakes E2E: deploy → URL → 2 variants → 2 fires → wiki log entry; Composio confirmed on both Reddit and LinkedIn |
| **6.0 Hardening** | Full pipeline <10 min end-to-end; wiki-lint zero orphans post-run; voice audit ≥90% adherence on last 10 posts |

A phase is "tested" by running the deliverable end-to-end and verifying each criterion was hit. Failure means the phase regressed, not that a unit test went red.

**Milestone success criteria** (ROADMAP.md §"Milestone Success Criteria") aggregate these:
1. Single `/hub` invocation produces a published post via Vercel + Reddit + LinkedIn without manual intervention beyond Review Gate `YES`
2. No orchestrator skill exceeds 4k tokens; hot cache stays under 500 tokens
3. End-to-end <10 minutes for a single article
4. Image generation and prose drafting fan out concurrently — never serialized
5. No publish path bypasses the Review Gate; per-post approval required
6. ≥90% of published posts pass Myth-Hilarity register audit
7. Every publish has a wiki log entry; every error has a documented recovery path
8. All published posts carry Schema.org-valid JSON-LD matched to content archetype

### 2. `/wiki-lint` — State Integrity Check

The structural test for the wiki state layer.

**What it catches:**
- Orphans (pages with no inbound `[[wikilinks]]`)
- Dead links (wikilinks pointing to non-existent pages)
- Frontmatter gaps (missing `type`, `tags`, `created`, `updated`)
- Index drift (pages not registered in `wiki/index.md`)

**When to run:**
- After every `/wiki-ingest` (cadence target: every 5 ingests or weekly per Phase 6.0)
- Before closing a session
- As part of Phase 6.0 hardening criteria (must report **zero orphans**)

**Invocation:** `/wiki-lint`

### 3. Voice Audit — `[[user-voice]]` Ruleset

The content-quality test. Drafts that don't pass the Myth-Hilarity register are not allowed through the Review Gate.

**Two-layer stack** (NFR-5.1):
1. `[[user-voice]]` — Myth-Hilarity + Tech Anthropology brand register
2. `[[Writing Discipline Ruleset]]` — technical prose layer that prevents collapse into formula

**Source-of-truth files:**
- `wiki/voice/myth-hilarity-tech-anthropology.md`
- `blog/user_voice.md`
- `blog/WRITING.md-main/WRITING.md`

**How to run:**
- During Phase 2.0: sample 3 drafts → manual check against register
- During Phase 6.0: voice drift detector samples last 10 published posts → score ≥90% adherence
- During `/hub`: voice check is implicit in the `blog-write` skill output

**Pass criterion:** the draft sounds like Kevin Tan writing under the Myth-Hilarity register, not like generic LLM prose.

### 4. Schema Validation — `seo-schema` Skill

The structured-data test for every published post.

**What it validates:**
- JSON-LD output is valid JSON
- Schema validates against Schema.org spec
- Archetype matches content (Article / HowTo / FAQ / Product / etc. per FR-4.4)

**Invocation:** `/seo schema <url>` or as the final stage of the Optimization pipeline (`seo-geo → seo-page → seo-schema`, FR-4.1)

**Pass criterion (Phase 3.0):** 3 drafts through pipeline → each emerges with valid JSON-LD that validates against Schema.org.

**Hook enforcement:** `.claude/plugins/claude-seo/hooks/hooks.json` registers a `PostToolUse` schema validation hook.

### 5. Token Budget Audit

The performance test for the orchestration layer.

**What it measures:**
- Every orchestrator skill's loaded token count (must be <4k per NFR-2.1)
- `wiki/hot.md` token count (must be <500 per NFR-2.2)
- Main session context utilization during a `/hub` run (target <30% per Phase 2.0 verification)
- Per-skill token consumption during a full pipeline run (Phase 6.0 deliverable)

**When to run:**
- Phase 6.0 hardening: instrument the pipeline, log token counts per skill invocation, identify largest consumers
- Whenever an orchestrator SKILL.md is modified — re-measure before merging
- After every wiki session end — confirm `hot.md` still fits

**Pass criterion:** No orchestrator over 4k. Hot cache under 500. Main context under 30% after a full creation run.

### 6. Manual End-to-End — `bash pipeline/run.sh` on a Test Post

The integration test. Run the working production pipeline on a known-good test post and inspect outputs.

**The script:** `pipeline/run.sh` — ~2-second bash pipeline that produces the 8-file `pipeline/publish-kit/<slug>/` directory. This is the proven path; the Python `pipeline/ktg_pipeline/` AI layer is ~70% untested per `PROJECT_STATE.md`.

**The procedure (from AGENTS.md §6):**

```
1. Create a test post at wiki/content/test-post/post.md
2. Run `/hub wiki/content/test-post/post.md`
3. Verify: 4 social variants generated (Reddit, LinkedIn, X-thread, Medium/IG caption)
4. Verify: hero image + 3 crops produced
5. Verify: GEO score attached
6. Verify: schema.json present and valid
7. Verify: Review Gate stops and waits for YES
8. Type STOP to cancel (do not publish test content to live channels)
9. Run `/wiki-lint` — confirm zero orphans
```

**Pass criterion:** All eight steps complete in order. The Review Gate must hard-stop. `/wiki-lint` must report clean.

**Alternative E2E (Phase 5.0):** Low-stakes published test — deploy a real low-stakes post to Vercel, fire Reddit + LinkedIn variants via Composio, confirm wiki log entry written. Used to validate Phase 5 deliverable, not for routine testing.

## Test Files / Test Data

**No `tests/` directory at the repo root.** The closest equivalents:

- `wiki/content/<slug>/` — every campaign is its own test fixture. Past campaigns serve as regression samples.
- `pipeline/publish-kit/<slug>/` — generated output fixtures from past `pipeline/run.sh` runs
- `blog/battlle-of-the-bots/round-N/battle-logs/` — raw CLI transcripts of past battle runs (`<agent>-<timestamp>.log`)
- `.planning/research/` — research artifacts that anchor planning decisions

**Test posts** (when needed for E2E): create under `wiki/content/test-post/` and **never** approve at the Review Gate. Cancel with `STOP`.

## Mocking

**Not applicable.** There are no Python unit tests to mock for. The integration surface area (Composio, Vercel, MCP gateway) is exercised live in low-stakes test posts during Phase 5 verification, not mocked.

For Phase 6.0 deliverable `hub --dry-run`: runs all pipeline steps but **skips publish and Composio calls**. This is the closest thing to a mocked test mode in the project — it isolates orchestration logic from outbound side-effects.

## Coverage

**No coverage tooling. No coverage target.** The pipeline is "covered" when:
- All six phases hit their ROADMAP verification criteria
- `/wiki-lint` reports zero orphans
- The voice drift detector scores ≥90% on the last 10 published posts (Phase 6.0)
- The full pipeline completes end-to-end in <10 minutes (milestone success criterion 3)

## Common Patterns

**Verification before trust** (user's global rule, applied here):
- Always run `/wiki-lint` after structural wiki changes
- Always re-measure token budget after editing an orchestrator SKILL.md
- Always run `bash pipeline/run.sh` on a test post before claiming the pipeline still works
- Never trust a publish completed without a wiki log entry

**Failure recovery:**
- Wiki-ingest fails → fall back to manual page creation; capture failure mode in `wiki/playbooks/hub-recovery.md`
- Composio times out → retry once, then surface to user; do not silently fail
- Vercel deploy errors → use `vercel rollback <deploymentId>`; document in wiki log
- Voice audit <90% → reroute draft through `blog-write` with explicit voice constraints

**Async testing:** N/A — the pipeline is sequential at the phase boundary, parallel within Phase 2.0 (image + prose fan-out). Concurrency is verified by checking that main context stays under 30% budget while both Task subagents run (Phase 2.0 criterion).

**Error testing:** Manually attempt to bypass the Review Gate (e.g. `/loop hub`) — gate MUST block (Phase 4.0 criterion).

---

*Testing analysis: 2026-05-27*
