# REQUIREMENTS — AI Content Hub (KTG)

> Synthesized from research on the three-layer plugin architecture, 100+ skills across 7 plugin directories, and the proven Capture→Plan→Create→Optimize→Review→Publish pipeline.

---

## 1. Functional Requirements

### 1.1 Capture & Intake
- **FR-1.1** The Hub MUST accept content seeds from at least three input modes: user prompt, file path, and URL.
- **FR-1.2** Every captured seed MUST be ingested into the wiki via `wiki-ingest`, producing entity, concept, and cross-reference nodes before downstream skills run.
- **FR-1.3** The wiki hot cache (`wiki/hot.md`) MUST be updated at end-of-session so the next agent picks up state without re-reading the full vault.

### 1.2 Planning
- **FR-2.1** Each campaign MUST produce a `campaign-brief.md` containing: target keyword, intent, audience, angle, distribution channels, and success criteria.
- **FR-2.2** The brief MUST be derived from wiki state (not invented) — planning skills read wiki index and relevant pages first.
- **FR-2.3** The brief is the single source of truth consumed by all downstream Create/Optimize/Publish skills.

### 1.3 Creation
- **FR-3.1** Content creation MUST support parallel sub-agents — image generation (banana) runs concurrent with prose drafting.
- **FR-3.2** Sub-skill loading MUST use the `Skill` tool (not Read) so the orchestrator stays under context budget.
- **FR-3.3** Heavy steps (long-form writing, batch image gen, multi-page audits) MUST be forked to Task subagents to keep main context clean.
- **FR-3.4** Image generation MUST use the banana plugin (Gemini Nano Banana) via the official 5-component prompt formula.

### 1.4 Optimization Pipeline (sequential, ordered)
- **FR-4.1** Order is fixed: **GEO → page audit → schema**. Each stage consumes the prior stage's output.
- **FR-4.2** GEO (Generative Engine Optimization) MUST score AI crawler accessibility, llms.txt compliance, and passage-level citability.
- **FR-4.3** Page audit MUST run technical SEO checks (E-E-A-T, readability, depth, Core Web Vitals where data is available).
- **FR-4.4** Schema MUST emit valid JSON-LD matched to the content archetype (Article, Product, FAQ, HowTo, etc.).

### 1.5 Review Gate
- **FR-5.1** A mandatory human review gate MUST sit between Optimize and Publish.
- **FR-5.2** The gate MUST block all publish actions until an explicit `YES` is received from the user (per-post green-light, no blanket approval).
- **FR-5.3** The gate MUST present: final content, all generated assets, GEO/SEO score, schema preview, and target channels.

### 1.6 Publish
- **FR-6.1** Publish order is fixed: **Vercel deploy → canonical URL captured → social variants generated → Composio fires to Reddit + LinkedIn**.
- **FR-6.2** Social variants MUST be derived from the canonical URL (no orphan posts).
- **FR-6.3** Reddit and LinkedIn variants MUST be channel-specific (different hooks, length, formatting) — not the same copy duplicated.
- **FR-6.4** All outbound posts MUST route through Composio (not direct platform APIs); n8n routes are deprecated for this pipeline.

### 1.7 Cross-Skill Coordination
- **FR-7.1** Skill discovery: orchestrator skills MUST consult `wiki/modules/index.md` and `wiki/modules/pipeline-signals.md` before chaining.
- **FR-7.2** Progressive loading: a skill MUST NOT load the full sub-skill tree on entry — only the entry skill loads, sub-skills load on demand via `Skill` tool.

---

## 2. Non-Functional Requirements

### 2.1 Performance
- **NFR-1.1** End-to-end pipeline (capture → review-ready) SHOULD complete in under 10 minutes for a single article-length campaign.
- **NFR-1.2** Image generation steps MUST run in parallel with prose drafting — never serialize what can fan out.
- **NFR-1.3** MCP tool calls SHOULD respond under 100ms (v3 mandate). Slower MCP servers are routed through gateway.py.

### 2.2 Token Budget
- **NFR-2.1** Orchestrator skills MUST stay under ~4k tokens after loading; sub-skills load on demand.
- **NFR-2.2** Wiki hot cache MUST stay under ~500 tokens — it is read on every session start.
- **NFR-2.3** Heavy file reads (audits, full source ingests) MUST be performed in Task subagents whose context dies with the task.
- **NFR-2.4** Main session SHOULD `/clear` between unrelated campaigns to prevent cross-contamination.

### 2.3 Platform Constraints
- **NFR-3.1** Plugins live under `.claude/plugins/` — 7 directories: blog (22 skills), ads (22), seo (25), banana, canvas, wp-mcp-ultimate, best-practices.
- **NFR-3.2** Wiki vault is the persistent state layer — every agent reads and writes wiki, never local scratch files for state.
- **NFR-3.3** WordPress publishing routes through `wp-mcp-ultimate` MCP (`https://ktg.one/wp-json/mcp/wp-mcp-ultimate`).
- **NFR-3.4** Vercel handles non-WP deploys; canonical URL capture is required before social fan-out.
- **NFR-3.5** Composio is the social outbound layer; n8n is backup only.

### 2.4 Reliability
- **NFR-4.1** The Review Gate is non-bypassable in autonomous mode — even `/loop` and autonomous runners stop here.
- **NFR-4.2** Every publish action MUST be reversible or auditable (Vercel rollback, post deletion, log entry in wiki).

### 2.5 Voice & Style
- **NFR-5.1** All long-form prose MUST run through the two-layer writing stack: `[[user-voice]]` (Myth-Hilarity brand register) over `[[Writing Discipline Ruleset]]` (technical prose layer).

---

## 3. Architecture Decisions

### 3.1 Three-Layer Architecture
**Decision:** Directive → Orchestration → Execution.
- **Directive layer** — STRAWHATS-DIRECTIVE, CLAUDE.md, user-voice. Sets posture, voice, and non-negotiables.
- **Orchestration layer** — Pipeline skills (blog, ads, seo orchestrators) that route between sub-skills. Decide *what* to do, not *how*.
- **Execution layer** — Leaf sub-skills (blog-write, ads-creative, seo-schema, banana). Do the actual work. No knowledge of pipeline.

**Rationale:** Separates policy from mechanism. Sub-skills are swappable. Orchestrators can be re-routed without rewriting execution.

### 3.2 Model Routing
**Decision:** Bifurcate model selection by task type.
- **Gemini (research / fact-check / web-grounded analysis)** — has Google Search grounding, fresher web access, faster for read-heavy work.
- **Claude Sonnet (synthesis, roadmapping, orchestration)** — better at multi-step reasoning, voice adherence, and complex tool-use chains.
- **Codex (bulk mechanical edits)** — repo-wide refactors.
- **Claude Opus (this orchestrator)** — strategy and review-gate decisions.

**Rationale:** Cost and capability matched to task. Don't burn Opus context on web research; don't trust Gemini to synthesize brand voice.

### 3.3 Sub-Skill Loading via `Skill` Tool
**Decision:** Sub-skills load through the `Skill` tool, never via `Read`.

**Rationale:** `Skill` invocation is auditable, version-aware, and integrates with the harness's skill metadata. Reading skill files directly breaks evolution (skills update; cached reads go stale).

### 3.4 Task-Fork for Heavy Steps
**Decision:** Any step that reads >5 files or generates >2k tokens of output runs in a Task subagent.

**Rationale:** Subagent context dies on completion. Main context stays under budget. Aligns with the wiki-ingest parallel pattern already proven in 2026-05-26 session.

### 3.5 Wiki as State Layer
**Decision:** All cross-skill state lives in the wiki, not in conversation memory.

**Rationale:** Survives `/clear`, model swaps, and session resets. Hot cache is the 500-token continuity primitive. Every session re-enters with full context.

### 3.6 Mandatory Human Review Gate
**Decision:** No autonomous publish. Review Gate is hard-coded between Optimize and Publish.

**Rationale:** Public-facing posts have non-trivial blast radius (brand, SEO, audience trust). Cost of pausing is low; cost of bad autonomous post is high.

### 3.7 Composio Over Direct APIs
**Decision:** All social outbound through Composio MCP.

**Rationale:** Single auth surface, unified rate-limit handling, audit log. n8n is kept as fallback only — `list_workflows` still failing as of 2026-05-26.

---

## 4. Phase Recommendations

### Phase 1 — Foundation (Capture + Plan)
**Goal:** Reliable seed → brief pipeline with wiki as state layer.

**Scope:**
- Stabilize `wiki-ingest` for the three input modes (prompt / file / URL).
- Lock the `campaign-brief.md` schema.
- Verify hot-cache update hook fires at session end.
- Document orchestrator entry points in `wiki/modules/index.md`.

**Verification:**
- Run 3 seeds (one per mode) → each produces a brief that downstream skills can consume.
- Hot cache reflects last session's state on next session start.

**Out of scope:** Image gen, publishing, social fan-out.

---

### Phase 2 — Creation (Prose + Image Parallelism)
**Goal:** Brief → drafted content with images, all in parallel.

**Scope:**
- Wire `blog-write` + `banana` to fan out from the brief.
- Implement Task-fork pattern for long-form drafts.
- Enforce two-layer writing stack (user-voice + Writing Discipline Ruleset).
- Verify sub-skill loading uses `Skill` tool, not `Read`.

**Verification:**
- A brief produces draft + 3 images in a single orchestration, with main context under 30% of budget.
- Voice audit: drafts pass Myth-Hilarity register check.

**Out of scope:** Optimization, publishing.

---

### Phase 3 — Optimization Pipeline
**Goal:** Sequential GEO → audit → schema, with scores attached to the draft.

**Scope:**
- Wire `seo-geo` → `seo-page` → `seo-schema` in fixed order.
- Each stage outputs a structured report consumed by the next.
- Final output: optimized content + JSON-LD + GEO/SEO score card.

**Verification:**
- Run 3 drafts through pipeline → each emerges with valid JSON-LD and a GEO score.
- Schema validates against Schema.org.

**Out of scope:** Publishing, social variants.

---

### Phase 4 — Review Gate
**Goal:** Non-bypassable human checkpoint before any publish action.

**Scope:**
- Implement gate as an explicit skill that surfaces: content, assets, scores, schema, target channels.
- Block all publish skills until `YES` received.
- Hard-stop autonomous runners (`/loop`, scheduled agents) at this gate.

**Verification:**
- Attempt autonomous publish → gate blocks, surfaces preview, waits.
- Per-post green-light required (no blanket approval cached).

**Out of scope:** Publish mechanics.

---

### Phase 5 — Publish (Vercel + Composio Fan-Out)
**Goal:** Approved content → live URL → channel-specific social variants → posted.

**Scope:**
- Vercel deploy step captures canonical URL.
- Variant generator produces Reddit-shaped and LinkedIn-shaped copy from canonical.
- Composio fires both posts; logs success/failure to wiki log.
- Rollback path documented (Vercel rollback, post deletion).

**Verification:**
- End-to-end test on a low-stakes post: deploy → URL → 2 variants → 2 fires → wiki log entry.
- Composio route confirmed for both Reddit (r/ClaudeAI) and LinkedIn.

**Carry-forward:** This phase completes the deferred Task #5 (Publish Mirage).

---

### Phase 6 — Hardening (Cross-Cutting)
**Goal:** Token budget, observability, voice drift detection.

**Scope:**
- Audit token usage across full pipeline; bring orchestrators under 4k.
- Add wiki-lint to CI-style cadence (weekly or per-N-ingests).
- Voice drift detection: sample published posts against user-voice rules.

**Verification:**
- Full pipeline runs under 10 min, end to end.
- Wiki lint reports zero orphans after a run.
- Voice audit on last 10 posts: ≥90% adherence to Myth-Hilarity register.

---

## Open Questions

1. **Canvas plugin role** — is Canvas part of the Create phase (visual planning) or a separate deliverable type? Not yet wired into the main pipeline.
2. **Ads plugin integration** — 22 ads skills exist but aren't in the blog-shaped pipeline above. Does ads run a parallel pipeline or share Phases 1–4?
3. **WordPress vs Vercel routing** — when does a piece go to WP (`wp-mcp-ultimate`) vs Vercel? Decision rule needed before Phase 5 finalizes.
4. **Best-practices plugin** — what does it gate or enforce? Needs explicit hook point in the pipeline.
