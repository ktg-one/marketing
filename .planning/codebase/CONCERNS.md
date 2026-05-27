# Codebase Concerns

**Analysis Date:** 2026-05-27

This is not a traditional software repository — it is an agent-orchestrated content production workspace. "Concerns" here means: security exposure, blocked integrations, untested code paths, state-coupling risks, cross-vault drift, and paused workstreams. Per `AGENTS.md` §6 there is **no automated test suite**; per `PROJECT_STATE.md` the Python AI pipeline is ~70% built and never run against a real LLM. Several issues below are documented elsewhere in the repo — this file consolidates them and adds the ones that are only implicit.

---

## Security Considerations

### WordPress credential stored in `README.md.txt` (not `.env`)

- **Risk:** WP `wp-mcp-ultimate` Basic auth (base64) lives in `README.md.txt` — a plain `.txt` file at repo root.
- **Files:** `README.md.txt` (12 lines), referenced by `AGENTS.md` §7 ("WordPress MCP auth is stored in `README.md.txt`").
- **Why dangerous:**
  - There is **no `.gitignore` at the repo root** (verified — file does not exist). Nothing prevents `README.md.txt` from being staged and committed.
  - The `.txt` extension means most secret-scanners and editor `.env`-hiding patterns will not catch it.
  - `AGENTS.md` §7 explicitly notes: *"Sensitive files are NOT in `.gitignore` by default — be careful what you commit."* This is the operational gap.
- **Current mitigation:** User discipline only. No pre-commit hook, no secret scanner, no `.gitignore` rule.
- **Recommendations:**
  1. Create `.gitignore` and add `README.md.txt`, `.env*`, `*.secret*`, `*credentials*`.
  2. Move WP Basic auth to a real `.env` file (or to OS keyring / MCP env injection).
  3. Rotate the WP Basic auth credential once moved (treat current as potentially exposed).

### Composio publish path — review gate is the *only* guardrail

- **Risk:** Composio MCP connectors for `reddit`, `linkedin`, `vercel`, `gmail`, `discord`, `slack`, `youtube`, `facebook`, `googledrive` are all wired and can fire from any AI session.
- **Files:** `CLAUDE.md` ("Publishing & security"), `AGENTS.md` §7 ("Review Gate Security"), `.planning/ROADMAP.md` Phase 4.0.
- **Why dangerous:** The Composio gateway has no per-action consent prompt of its own. The only thing standing between a hallucinated `/hub` invocation and a real post going live is the **Review Gate skill** in Phase 4 of the roadmap — which is itself listed as in-progress.
- **Current mitigation:**
  - Per-post `YES` requirement documented in `CLAUDE.md` and `AGENTS.md`.
  - Gate state written to wiki (survives `/clear`) — see `AGENTS.md` §7.
- **Recommendations:**
  - Until Phase 4.0 ships, treat the Composio connection list as "permission to use the route, not permission to post" (already canonised in `CLAUDE.md`).
  - Add a dry-run mode to `pipeline/run.sh` and `/hub` (Phase 6.0 already lists this — accelerate it).
  - Never grant blanket per-session approval. Per-post `YES` is non-negotiable.

### MCP gateway is a single trust boundary

- **Risk:** `.claude/config.json` proxies all MCP tool calls through `D:\projects\.mcp\gateway.py`, a file **outside this repo**.
- **Files:** `.claude/config.json`, referenced from `AGENTS.md` §7.
- **Why fragile:** A compromise or misconfiguration of `gateway.py` would silently affect every Composio, WordPress, and Vercel call made from this workspace. The gateway lives on a separate drive (`D:`) with its own change control.
- **Current mitigation:** None visible from this repo.
- **Recommendations:** Document the gateway version pinning and audit policy somewhere in `wiki/playbooks/runtime-config.md`. Treat any change to `gateway.py` as a security-review event.

### No `.gitignore` at repo root

- **Risk:** `data/state_store.db/`, `.venv/`, `__pycache__/`, `pipeline/logs/`, `in-memoria.db`, and the credential-bearing `README.md.txt` are all currently un-ignored.
- **Files:** Verified absence of `C:/Users/kevin/Pictures/ktg-one/.gitignore`.
- **Recommendations:** Author a minimal `.gitignore` covering: secrets (`*.env`, `README.md.txt`, `*credentials*`), runtime state (`data/`, `pipeline/logs/`, `pipeline/output/`), Python (`.venv/`, `__pycache__/`, `*.pyc`), local DBs (`*.db`, `in-memoria.db`).

---

## Blocked / Impossible Integrations

These are not bugs to fix — they are platform reality. Documented in `pipeline/REALITY_CHECK.md` and `PROJECT_STATE.md`. Restated here so future agents do not waste cycles trying to "fix" them.

| Channel | Status | Blocker | Workaround |
|---------|--------|---------|------------|
| **X (Twitter)** | Impossible to automate | Write access requires $5,000/month enterprise tier; v2 basic ($100/mo) is read-mostly with 3,000-tweet/month limit | Manual copy-paste from `pipeline/publish-kit/<slug>/x-thread.txt` |
| **Meta (Facebook / Instagram)** | Restricted | Requires Business Verification; personal accounts blocked; 25 posts/day cap on approved apps; spam detection aggressive | Buffer, Creator Studio, or Meta Business Suite (manual) |
| **Medium** | Hard / read-only for most | API v1 write access is gated; most accounts get read-only OAuth | Manual import of `pipeline/publish-kit/<slug>/medium.md` via "Import story" |
| **LinkedIn** | Possible | OAuth + `w_member_social`, 150 req/day | Composio wiring exists in principle; posts marked "via [app]" — slightly less organic |
| **Reddit** | Possible | OAuth, 60 req/min, subreddit anti-bot rules | Composio route active; risk of ban if spammy |
| **n8n** | Auth broken | `list_workflows` MCP call fails intermittently — flagged in `CLAUDE.md` and `.planning/ROADMAP.md` Backlog | Composio is the default route; n8n listed only as backup |

**Operational implication:** Copy-paste is the canonical reality for X, Meta, and Medium. The `publish-kit/<slug>/` pattern (8 ready-to-paste files per post) is the working solution — not a stopgap. Do not propose "auto-post everywhere" architectures.

---

## Untested Code

### Python AI pipeline — framework only, never run end-to-end

- **Files:** `pipeline/ktg_pipeline/pipeline.py`, `pipeline/ktg_pipeline/config.py`, `pipeline/ktg_pipeline/providers/`, `pipeline/ktg_pipeline/agents/`, `pipeline/run.py`.
- **Per `PROJECT_STATE.md`:** ~70% complete, ~2,000 lines across 10 modules. Providers implemented for Ollama, LM Studio, Google AI Studio, OpenRouter.
- **What is NOT verified:** actual LLM calls, prompt quality, error handling, output formatting.
- **What IS verified:** config loading; 4 providers exist as code.
- **Impact:** If an agent assumes `python pipeline/run.py` is production-ready (because the code exists and looks clean), it will silently produce bad output or crash on first contact with a real LLM.
- **Fix approach:** Run `pip install pyyaml requests`, start Ollama with a small model, run `python pipeline/run.py pipeline/input/test-post.md --provider ollama`, capture output, then iterate. Until then, treat `pipeline/run.sh` (bash, 2-second, working) as the only production path.

### Pipeline verification = manual checklists, not tests

- **Files:** `.planning/ROADMAP.md` Phase 1.0–6.0 (verification criteria are prose, not assertions).
- **What is asserted instead:** "3 seeds → 3 briefs", "main context <30% budget", "valid JSON-LD", "wiki-lint zero orphans", "voice audit ≥90%". These are useful operational gates but **none of them run automatically**.
- **Risk:** Regression detection depends entirely on the human operator running `/wiki-lint` and re-executing the pipeline. No CI exists.

### Battle-of-the-Bots `deploy.sh` scripts have real side-effects

- **Files:** `blog/battlle-of-the-bots/round-N/<project>/deploy.sh` (mentioned in parent `CLAUDE.md` and `wiki/` working conventions).
- **Risk:** Each `deploy.sh` runs `gh repo create` against the hardcoded user `kevin` and publishes a public repo to GitHub Pages. No dry-run flag. No confirmation prompt.
- **Mitigation:** Documented in `CLAUDE.md` ("confirm before running") — but this is user discipline, not a code guardrail.

---

## Architecture Risks

### Plugin registration is incomplete (13 of 79 skills)

- **Source:** `wiki/modules/index.md` — "79 total skills across 7 plugins · 13 registered this session (6 ads + 7 blog) · 31 pending · 28 pre-installed in OpenCode · 4 skipped · 3 non-skill."
- **Risk:** Orchestrators that reference unregistered skills will silently fail to load them or fall back to lower-quality defaults. `claude-blog` shows "Registered (7 of 22)"; `claude-ads` shows "Registered (6 of 22)".
- **Impact:** Phases 2.0 (Creation) and 3.0 (Optimization) in `.planning/ROADMAP.md` depend on these plugins. A skill that is documented but not registered is invisible to the runtime.
- **Fix approach:** Continue the registration pass tracked in `AGENTS.md` §10 ("Plugin registration — 13 of 79 skills registered — Continue registering blog + ads sub-skills").

### `wiki/` is load-bearing — the Karpathy mandate is the system's spine

- **Source:** `CLAUDE.md` ("Karpathy LLM Wiki Pattern (canon): agents that don't load the wiki have no user context. Reading the wiki INTO context is load-bearing, not optional.").
- **Risk:** Any agent that skips reading `wiki/hot.md` → `wiki/index.md` → `AGENTS.md` → `PROJECT_STATE.md` → `wiki/modules/index.md` operates blind. There is no runtime enforcement of the read-order — it is purely social contract.
- **Worse:** the Review Gate state itself lives in `wiki/` (intentional, so it survives `/clear` — see `AGENTS.md` §7). This means wiki corruption (accidental delete, bad merge, manual edit) could simultaneously erase project state *and* erase the gate's persistent approval ledger.
- **Mitigation:**
  - Run `/wiki-lint` on cadence (Phase 6.0 — "every 5 ingests or weekly").
  - Treat `wiki/log.md` as append-only (already convention).
  - Consider snapshotting `wiki/` before any bulk wiki operation.

### Hot cache (`wiki/hot.md`) staleness

- **Source:** `wiki/hot.md` last updated `2026-05-26T22:30:00+08:00`.
- **Risk:** `hot.md` is the first file every session reads. If a session ends without running the end-of-session hook (Phase 1.0 deliverable: "Hot-cache update hook firing at session end"), the next session starts with stale context and may re-do or contradict prior work.
- **Specific gaps in current `hot.md`:** the entries are session-fact dense (SCCD, model registry, publish kit) but the "Active Threads" list (Publish Mirage, Kismet/Good AI, Phase 1.0) does not carry state delta vs. the prior session — only status labels.
- **Fix approach:** Phase 1.0 explicitly tracks this as "Confirm `/session-end` hook writes to `wiki/hot.md`; test on fresh session start." Not yet verified.

### Quality enforcement = `/wiki-lint` + voice audit + user discipline

- **Source:** `AGENTS.md` §6 ("There is no automated test suite (no pytest, no jest, no CI).").
- **Means:** Every quality dimension — voice consistency, schema validity, wiki integrity, token budget, JSON-LD correctness — depends on a human invoking a skill (`/wiki-lint`, voice audit, `seo-schema`).
- **Risk:** Skipped lints silently accumulate. The roadmap's Phase 6.0 ("Hardening — Token audit, wiki-lint cadence, voice drift detection, dry-run mode, error recovery playbook") is the planned mitigation but is the *last* phase, not the first.

---

## State Coupling

### Review Gate state ↔ wiki survival are co-located

- Already covered above under "wiki/ is load-bearing" but worth restating: gate state surviving `/clear` is a feature; that same coupling means a single wiki incident takes out the gate.
- **Recommendation:** Periodic external backup of `wiki/` (git is fine — but git is not currently configured for safe credential handling per the `.gitignore` issue above).

### `pipeline/run.sh` output vs. `wiki/content/<slug>/` divergence

- `pipeline/run.sh` writes to `pipeline/output/` and `pipeline/publish-kit/<slug>/`.
- `wiki/content/<slug>/post.md` is the canonical content surface per parent `CLAUDE.md`.
- **Risk:** The two paths are not currently synchronized. The bash pipeline does not write back into `wiki/`. A publish kit can exist for a slug that has no corresponding wiki content entry, and vice versa.
- **Fix approach:** Document the canonical flow (wiki → pipeline → publish-kit) in `wiki/playbooks/`. Phase 5.0 partially addresses this (wiki log entry on publish) but the upstream direction is undefined.

---

## Cross-Vault Drift

### Parent vault `C:/Users/kevin/knowledge2026/` vs. this fork

- **Source:** `CLAUDE.md` ("Sister projects (outside this vault) — `C:/Users/kevin/knowledge2026/` — parent wiki vault. This fork (`Pictures/ktg-one`) is the marketing/content production fork.").
- **Risk:** Two vaults, no merge protocol. Concepts/entities created in this fork (e.g. SCCD, Kismet, Good AI strategy) are *not* automatically reflected in the parent. The parent's `MEMORY.md` packet index (`02232026-COP-R7-coding-kismet-n8n-calendar-errorlog`) references Kismet work that overlaps with `wiki/entities/` here.
- **Impact:** A future operator reading the parent vault will not see the content-production state. A future operator reading this fork will not see the parent's broader project context.
- **Fix approach:** Define a documented sync direction (parent ← this fork, or vice versa) and a cadence. Currently undefined.

### Next.js sites are separate repos

- **Source:** `CLAUDE.md` references `C:/Users/kevin/Desktop/ktg-one/` and `C:/Users/kevin/projects2026/06-projects-code/goodai-mate/`.
- **Risk:** This vault produces content that ostensibly ships to those sites (via Vercel), but the deploy target repos are not under this vault's version control. Schema, route, and component changes in the Next.js repos can silently break the publish step.
- **Fix approach:** Document the deploy contract (what URL shape Vercel expects, what `frontmatter` fields must exist) in `wiki/playbooks/publish-vercel.md`. Not present today.

### `LEGIO/` and `Recursive-Council/` referenced but external

- Live under `C:/Users/kevin/knowledge2026/Projects-Coding/` per `CLAUDE.md`.
- **Risk:** Doc references can rot when the referenced repos move.

---

## Paused / Active Workstreams (per `wiki/hot.md`)

These are not bugs but unresolved state that future sessions will inherit. Tracked in `AGENTS.md` §10 and `wiki/hot.md`.

| Workstream | Status | Blocker |
|------------|--------|---------|
| **Publish "Mirage" post** | Awaiting green-light | Needs explicit user `YES` at Review Gate; Vercel → URL → Reddit + LinkedIn via Composio not yet fired |
| **Kismet / Good AI strategy — Phase 2** | Wikified, paused | Next phase ("Training + Dashboard") not defined |
| **Phase 1.0 Foundation** | In progress | Audit `wiki-ingest` for all 3 input modes (prompt / file / URL); confirm `/session-end` hook writes `wiki/hot.md` |
| **Plugin registration** | 13 of 79 skills registered | Continue registering blog + ads sub-skills (16 ads + 15 blog pending per `wiki/modules/index.md`) |
| **SCCD integration into pipeline** | Model complete, integration pending | Decide which pipeline steps use SCCD's choice/decide engine |
| **n8n `list_workflows` auth** | Broken | Not blocking Milestone 1 (Composio is primary); fix deferred to backlog |

---

## Test Coverage Gaps

There is no automated test coverage anywhere. The gaps that matter most:

| Untested area | Files | Risk | Priority |
|---------------|-------|------|----------|
| Python AI pipeline end-to-end | `pipeline/ktg_pipeline/pipeline.py`, `pipeline/run.py` | First real run will likely fail; no harness to catch regressions | High |
| Review Gate non-bypassability | Phase 4.0 deliverable (not yet built as named skill) | A bypass would mean unintended public posts | High |
| Wiki integrity post-edit | `wiki/` (any change) | Orphaned wikilinks degrade Karpathy pattern silently | High (run `/wiki-lint` after every ingest) |
| Voice drift on published posts | `blog/posted/`, `wiki/content/<slug>/post.md` | Brand-defining; drift is invisible without sampling | Medium (Phase 6.0 deliverable) |
| Token budget on orchestrators | `.claude/skills/hub/`, `.agents/skills/`, `.claude/plugins/*/SKILL.md` | Over-4k orchestrators degrade main context for downstream calls | Medium (Phase 6.0 deliverable) |
| JSON-LD schema validity | Output of `seo-schema` skill | Bad schema = no rich snippets | Medium (manual validate against schema.org) |
| Composio rate-limit handling | Composio MCP wrappers | Silent post failures could look like success | Low (until automation scales beyond per-post YES) |
| `deploy.sh` side-effects | `blog/battlle-of-the-bots/round-*/`/*/deploy.sh` | Creates public GitHub repos; no dry-run | Low (occasional manual use only) |

---

## Dependency Risks

- **`kimi-cli>=1.44.0`** (`pyproject.toml`): Single upstream for the Kimi CLI integration; no fallback. If the package goes silent the Kimi route in `wiki/intel/model-registry.md` breaks.
- **`tool>=0.8.0`** (`pyproject.toml`): Very generic name; risk of typosquat or version drift. Worth pinning exactly and auditing what it provides.
- **Composio MCP**: External SaaS — outage = no publishing. No fallback path documented.
- **MCP gateway (`D:\projects\.mcp\gateway.py`)**: Cross-drive dependency; not in this repo, not version-pinned here.

---

## Summary — What To Watch

1. **Add `.gitignore` before next commit.** Without it, `README.md.txt` (WP creds) is one `git add .` away from being public.
2. **Treat the Python pipeline as not-yet-real.** Use `pipeline/run.sh` (bash) until `pipeline/ktg_pipeline/` is validated against a live LLM.
3. **Never bypass the Review Gate.** It is currently the only thing between a hallucinated `/hub` call and a real Reddit / LinkedIn post.
4. **Read `wiki/hot.md` first, every session.** The Karpathy pattern is not enforced by runtime — only by discipline.
5. **Keep `wiki/` integrity sacred.** Project state, gate state, and pipeline state all live there. One bad merge erases all three.

---

*Concerns audit: 2026-05-27*
