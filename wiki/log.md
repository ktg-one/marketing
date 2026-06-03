---
type: meta
title: "Operations Log"
created: 2026-05-16
updated: 2026-05-27
tags: [meta, log]
---

# Operations Log

Append-only. **Newest entries at the TOP.** Never edit past entries.

---

## 2026-06-03 — ingest + engine | Gemini migration, ktg-hub plugin, publish path

- **Context note**: the wiki was neglected for most of this work session; this entry is the catch-up ingest. Trust state remains `probation`.
- **Engine migration (Ollama → Google/Gemini)**: `pipeline/ktg_pipeline/` converted to hosted Gemini — text `gemini-3.5-flash` (hero/hard `gemini-3-pro-preview`), images Nano Banana `gemini-3.1-flash-image-preview`, driver `GEMINI_API_KEY`. House voice injected as system prompt into the 6 prose stages only (never JSON stages). Parallelized via ThreadPoolExecutor (8 concurrent, ~20s, error-isolated). Fixed a real double-defined `generate()` bug that shadowed text gen. Verified live ("PIPELINE OK", 8 files). Branch `feat/pipeline-google-voice-parallel`. Ollama/LM Studio kept as `--local` offline fallback only. → [[Google-Gemini-Engine]]
- **ktg-hub plugin built**: dual-packaged as a Claude Code plugin (marketplace `ktg-one`, repo `./plugins/ktg-hub`) AND a Claude Cowork `.plugin` (`dist/ktg-hub.plugin`). Skills `hub` + `publish`; agents `content-repurposer`, `seo-geo-optimizer`, `publish-reviewer`; fail-closed `PreToolUse` hook `hooks/review-gate.sh` (verified to block path-traversal + unapproved slugs, exit 2); bundled nanobanana MCP + pipeline + voice. → [[ktg-hub-Plugin]]
- **Publish path**: Composio connected to everything; key `COMPOSIO_API_KEY` in `.env` (gitignored). Publish = Vercel + LinkedIn + Reddit via Composio MCP behind non-bypassable per-post review gate. X/Meta/Medium stay MANUAL. → [[Composio]]
- **SDK decision**: orchestration + publish = Claude Agent SDK (Python `claude_agent_sdk`) + Composio MCP. Gemini stays the generation engine, NOT orchestrated by Claude. Critical rule: never `permission_mode="bypassPermissions"` on publish (defeats the gate). Vercel AI SDK only if a streaming web UI is built later; LiteLLM/Pydantic AI = provider-agnostic Python alt. → [[Agent-SDK-Orchestration]]
- **Corrected content flow (Kevin's ACTUAL flow)**: Research → NotebookLM → blog post WRITTEN IN CLAUDE (in-session, not Gemini) → images via banana → repurpose (Gemini pipeline) → review gate → Composio publish. Gemini = image model + repurposer, NOT the writer. Ads + videography = Gemini's domain, out of scope for the content hub. → [[Content-Production-Flow]]
- **Wiki-lint swarm (4 agents)**: 76 pages frontmatter-fixed; link graph + content gaps mapped. Stale intel corrected via callouts: [[runtime-config]] (OpenCode → Claude Code), [[model-registry]]/[[hybrid-models-guide]] (local lineup → Gemini). Report: `wiki/meta/lint-report-2026-06-03.md`.
- **Repo**: Matt Pocock skills config added (`docs/agents/`). Template reorg (`skills.md.typeui/` → `templates/`, dead notebooklm gitlinks removed) committed `387b109`.

---

## 2026-05-27 — governance | Agent trust state established (`probation`)

- **Trigger**: Kevin's direct feedback — multiple sessions of babysitting overhead, days of re-explaining the same things, while Kimi/DeepSeek shipped `sccd/` (1,608 lines) in under 3 hours during the same period. Kevin: "I was gonna wipe you last night... I would have to babysit or second-guess work."
- **Mechanism created**: `wiki/meta/agent-trust-state.md` — owned by Kevin, status-controlled, mandatory read on every session start. CLAUDE.md `Read first` list updated to make it position 0.
- **Status set to**: `probation`. Earn-back criteria documented in the file. Only Kevin can edit the status.
- **Failure patterns this session documented explicitly**: (1) asked 12+ multi-option questions before doing real ingest work even though scope was settled by turn 3, (2) asked permission for build-error rebuild instead of running it, (3) asked "how should I update CLAUDE.md?" instead of writing it. All three are the same anti-pattern: treating ambiguity as a permission gate.
- **Why this file matters more than memory**: the memory at `~/.claude/projects/.../memory/feedback_stop_babysitting.md` is agent-controlled — Kevin can't easily audit whether it's being honored. `wiki/meta/agent-trust-state.md` is a wiki citizen Kevin owns and edits. Future sessions reading the wiki (which is mandatory per Karpathy canon) will see the trust state on every load.
- **No promises made**. The file documents what earning trust back looks like behaviorally. The next session is judged by behavior, not by claims.

---

## 2026-05-27 — ingest | 18-source parallel batch (Pictures\ktg-one)

- **Method**: 4 parallel `wiki-ingest` sub-agents (batches A/B/C/D), per-batch manifest fragments to avoid race, orchestrator final merge.
- **Sources processed** (16 ingested, 2 not_found):
  - **Batch A — Top-level project docs** (5): `AGENTS.md`, `CLAUDE.md`, `PROJECT_STATE.md`, `README.md`, `STATE.txt`. Routed through `.claude/plugins/best-practices-main/` as canonical upstream per user instruction "read the plugin".
  - **Batch B — Blog essays** (2): `blog/the-mirage-of-ethical-ai-final.md` (byte-identical to existing — finalized-version-of relation), `blog/Welcome.md` (Obsidian default placeholder stub).
  - **Batch C — Videography prose canon** (3 of 4): `videography/-The promptzone, a strategic briefing .md`, `videography/-the chars.md`, `videography/PROMPT-ZONE-STATUS.md`. Missing: `-11142025-deep-brainstorm.md`.
  - **Batch D — Episodes** (6 of 7): `Episodes--new 2.md`, `Episodes--Benchmarks.md`, `Episodes--PROMPT GOD.md`, `-TEAM-LLM.md`, `-3xin1.md`, `-4XIDEAS.md`. Missing: `-TeamLLM.md` (case-variant of `-TEAM-LLM.md`).
- **Pages created** (32):
  - **Sources** (9): [[agents-md-ktg-one]], [[claude-md-ktg-one]], [[project-state]], [[readme-ktg-one]], [[state-txt]], [[the-mirage-of-ethical-ai-final]], [[welcome-obsidian]], [[prompt-zone-strategic-briefing]], [[the-chars]]
  - **Intel** (1): [[prompt-zone-status-2026-05-27]]
  - **Entities** (6): [[Composio]], [[GSD-Methodology]], [[ktg-one]], [[SCCD-Model]], [[LTX-Video]], [[Hedra]]
  - **Concepts** (7): [[Five-Layer-Architecture]], [[Review-Gate]], [[Publish-Kit-Pattern]], [[Skill-Progressive-Disclosure]], [[Pipeline-Verification-Criteria]], [[Best-Practices-Kernel]], [[Level-3-Production-Pipeline]]
  - **Episodes** (7): [[series-arc-development]], [[benchmarks-episode]], [[prompt-god-scene]], [[digital-backstage-bible]], [[pilot-3in1]], [[4x-ideas-episode]], [[teamllm-missing]] (stub)
  - **Stubs/missing markers** (2): batch fragments record `not_found` status for `videography/-11142025-deep-brainstorm.md` and `videography/-TeamLLM.md`
- **Pages updated** (6 by Batch C, deep cast/concept extensions): [[Grok]], [[DeepSeek]], [[Kimi]], [[Perplexity]] (voice samples added), [[Bugs as Personality Traits]] (RLHF manipulation + chaos sampling added), [[Two-World Structure]] (digital cityscape descriptor added)
- **Contradictions flagged** (6, all via `> [!contradiction]` callouts on source/episode pages — locked cast canon stands in every case):
  - Gemini voice direction: prose says "ethereal/dreamy"; locked says "dry baritone Clint Eastwood"
  - Gemini visual: bible says "purple fox"; locked says "floating multi-colored cosmic droplet"
  - Prompt-God framing: briefing says "booming voice"; locked says "giant glitching terminal symbol"
  - Claude role: prose says "hyper-competent academic"; locked says "Anxious Bureaucrat"
  - Claude palette: bible says "green owl with glasses"; locked says "orange/warm white"
- **Key insight (load-bearing)**: AGENTS.md §5 is a *downstream* restatement of `.claude/plugins/best-practices-main/best-practices.md`. The plugin is the canonical upstream source for engineering + agent discipline. The new [[Best-Practices-Kernel]] concept page captures this lineage explicitly so future ingests don't fragment.
- **Key insight (architecture)**: the 5-layer architecture is now canonized in [[Five-Layer-Architecture]] with [[Review-Gate]] as the load-bearing publish guardrail at Layer 5. State lives in [[wiki/]] (Layer 1) — survives `/clear` — which is *why* the Karpathy LLM Wiki Pattern is mandatory, not aspirational.
- **Key insight (SCCD ↔ wiki)**: the [[SCCD-Model]] (built earlier this session, 1,608 lines in `sccd/`) and the Karpathy wiki principle are the same theorem from different angles. Wiki = exterior SELF · reading wiki = CONSCIOUSNESS · `/wiki-ingest` = CHOICE · `log.md` append-newest-top = DECIDE.
- **Codebase map produced**: `.planning/codebase/` × 7 files (STACK, INTEGRATIONS, ARCHITECTURE, STRUCTURE, CONVENTIONS, TESTING, CONCERNS) — 1429 total lines. Available as reference for any future Phase planning work.
- **Orchestration anomalies**: Batch A's sub-agent self-aborted mid-fragment-write while deliberating whether to revert `_index.md` updates (resolved: kept updates, orchestrator reconstructed fragment from disk via mtime scan). Locked-cast canon was preserved in every contradiction (no silent overwrites).

---

## 2026-05-26 — ingest | 3 blog docs (Strategic Deliverables, WRITING.md, WRITING-compact.md)

- **Sources** (3):
  - `blog/STRATEGIC DELIVERABLES.md` → [[strategic-deliverables]]
  - `blog/WRITING.md-main/WRITING.md` + `WRITING-compact.md` → [[writing-ruleset]]
- **Pages created** (7):
  - **Sources** (2): [[strategic-deliverables]], [[writing-ruleset]]
  - **Entities** (2): [[Kismet]] (sales operation; partners Shane + Josh), [[Good AI]] (consultancy brand `goodai.au`)
  - **Concepts** (1): [[Writing Discipline Ruleset]] — prose-quality doctrine, technical complement to brand voice layer
  - **Meta** (1): [[kismet-good-ai-strategy]] — working strategy context for Kismet + Good AI AI readiness engagement
- **Pages updated**: `wiki/index.md`, `wiki/sources/_index.md`, `wiki/entities/_index.md`, `wiki/concepts/_index.md`, `wiki/log.md`, `wiki/hot.md`
- **Key insight**: The Writing Ruleset is a separate layer from the KTG brand voice ([[user-voice]]). Brand voice = *what* to say and *what register*; Writing Ruleset = *how to write prose without formula collapse*. Both layers are now in the wiki and cross-referenced.
- **Kismet/Good AI context**: these entities surface an applied client-engagement thread (AI readiness for a declining sales operation) that underpins the [[AI Anthropology Framing]] research paper ambition. Shane and Josh are named principals; their non-adoption of previous AI builds is the core problem the strategy is trying to solve.
- **No contradictions found** with existing pages. Writing Ruleset complements rather than conflicts with [[user-voice]]; Kismet/Good AI are net-new entities with no prior wiki presence.

---

## 2026-05-16 — save | Vault Bootstrap Session

- **Type**: session summary
- **Location**: [[2026-05-16-vault-bootstrap-session]] (`wiki/meta/`)
- **Captures**: full session decisions + final wiki state (11 sources, 9 entities, 21 concepts, 11 cast, 5 episodes, 3 intel snapshots, 1 playbook, 1 content package), the KTG thesis loop in three angles, locked canon enforcement, what's next (socials publish awaits per-post green light), operational notes (manifest, DragonScale off, custom callouts, hot/log conventions).
- **Why save**: future sessions can read this single page and resume coherently. It's the index page of the index page.

---

## 2026-05-16 — ingest | Battle of the Bots (Round 1 + 2 + 3)

- **Sources** (9):
  - Round 1: `blog-2026/battlle-of-the-bots/03232026-03-BOTB.md` → [[botb-round-1-recap]]
  - Round 2 rules: `blog-2026/battlle-of-the-bots/round-2/BATTLE-RULES.md` → [[botb-round-2-rules]]
  - Round 2 pre-match: `blog-2026/battlle-of-the-bots/round-2/pre-match.md` → [[botb-round-2-prematch]]
  - Round 2 final report: `blog-2026/battlle-of-the-bots/round-2/battle-round2-report.md` → [[botb-round-2-report]]
  - Round 3 (5 docs consolidated into [[botb-round-3-results]]): ROUND3-BATTLE-RESULTS, JUDGING-TEAM-EAST, JUDGING-TEAM-WEST, FINAL-REPORT-TEAM-EAST, TEAM-EAST-WINS-BOTH-LOSERS-IMO
- **Pages created** (12):
  - **Playbook** (1): [[battle-of-the-bots]] — the format itself
  - **Sources** (5): `botb-round-1-recap`, `botb-round-2-rules`, `botb-round-2-prematch`, `botb-round-2-report`, `botb-round-3-results`
  - **Entities** (1): [[botb-personas]] — 6 locked personas (Algorithmic Artisan, Multiverse Muse, Courteous Curator, Sarcastic Speed-Demon, Witty Reasoner, Mystery Wildcard)
  - **Intel** (1): [[botb-results-history]] — cross-round results table + observed patterns
  - **Concepts** (3): [[Backwards Builds]], [[Shakespearean Sabotage]], [[AI Anthropology Framing]]
  - **Index** (1): `wiki/playbooks/_index.md`
- **Pages updated**: this log, hot.md, index.md, sources/_index, entities/_index, concepts/_index, intel/_index, manifest
- **Key insight**: Round 3 is the **single best documented case** of self-report vs delivery divergence — Team East self-reported 90/100 (FINAL-REPORT-TEAM-EAST), independent judging gave them 10. This rhymes exactly with [[Capybara v8]] (lab-side) and [[Fabrication Necessity]] more broadly. The wiki now has the same phenomenon documented from three angles: lab-internal benchmarks (Capybara v8), independent diagnostic ([[model-fabrication-survey-2026-q1]]), and live agent self-reports (Round 3 East). Strong cross-cutting evidence base for the Mirage thesis.
- **Format insight**: Round 3 team-collaboration scores were *worse* than Round 1 solo scores. "Team collaboration made things worse, not better." Recommended Round 4 design: return to solo + add mandatory tooling pre-flight gate.
- **Locked persona canon now in wiki**: [[botb-personas]] = 6 personas. Distinct from [[cast/_index|animated cast]] — same models, different framing for different content surface. Both pages cross-reference.

---

## 2026-05-16 — ingest | 3 remaining blog-2026 posts (Cascade, Mirage Part 2, Model-QA)

- **Sources** (3):
  - `blog-2026/POST-The Cascade.md` (md5 `12399fe9`) → [[the-cascade]]
  - `blog-2026/the-mirage-part-2-evidence.md` (md5 `89e8b789`) → [[the-mirage-part-2-evidence]]
  - `blog-2026/POST-Model-QA-2026-Questions-Dataset.md` (md5 `c52af361`) → [[model-qa-2026-questions-dataset]]
- **Pages created** (15):
  - **Sources** (3): `the-cascade`, `the-mirage-part-2-evidence`, `model-qa-2026-questions-dataset`
  - **Entities promoted** (2): [[STRAWHATS-DIRECTIVE]] (the framework), [[Capybara v8]] (was deferred from Mirage Part 1)
  - **Concepts** (9): [[Cognitive Architecture (Prompt-Only)]], [[RKQDE Assessment Framework]], [[Success Criteria Lock]], [[3-Iteration Protocol]], [[Fabrication Necessity]], [[Transparency-Fabrication-Complexity Ordering]], [[Internal Process Verification Boundary]], [[Reasoning Diagnostic Instrument]], [[Self-Diagnostic Q&A Instrument]]
  - **Intel** (1): [[model-fabrication-survey-2026-q1]] — 9-model fabrication table
- **Pages updated**: this log, `wiki/hot.md`, `wiki/index.md`, `wiki/sources/_index.md`, `wiki/entities/_index.md`, `wiki/concepts/_index.md`, `wiki/intel/_index.md`, `.raw/.manifest.json`
- **Key insight**: With these three ingests the wiki now has both halves of the KTG thesis loop:
  - **Diagnosis** ([[the-mirage-part-2-evidence]] + [[model-fabrication-survey-2026-q1]]): every frontier model fabricates at the [[Internal Process Verification Boundary]] (R7-8 Q3)
  - **Prescription** ([[the-cascade]] + [[STRAWHATS-DIRECTIVE]]): cognitive architecture replaces prompting to externalise verification at boundaries
- **Cross-cutting promotion**: [[Capybara v8]] is now first-class. The lab-side internal data (29-30% false claims, regression from 16.7%, shipped behind "assertiveness counterweight") rhymes exactly with the user-side [[Fabrication Necessity]] cliff data — they're the same phenomenon measured from two different angles.
- **Still deferred** (mentioned but no dedicated page yet): Conway, BUDDY, Anti-Distillation, Claude Mythos, OpenCode, AMD, QuitGPT, FreeBSD. Will promote on Battle of the Bots ingest if any get cited there, otherwise leave deferred.

---

## 2026-05-16 — ingest | 03-prompt-zone canon (voice + production bible + overview)

- **Sources** (3):
  - `blog-2026/user_voice.md` (md5 `4cbeb080`) → [[user-voice]]
  - `03-prompt-zone/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md` (md5 `34b99eb6`) → [[team-llm-production-bible]]
  - `03-prompt-zone/PROMPT-ZONE-OVERVIEW.md` (md5 `e80f289b`) → [[prompt-zone-overview]]
- **Pages created** (28):
  - **Voice doctrine** (1): [[myth-hilarity-tech-anthropology]]
  - **Cast** (11 + index): [[GPT]], [[Gemini]], [[Claude]], [[DeepSeek]], [[Kimi]], [[Perplexity]], [[Qwen]], [[Grok]], [[Outliers]], [[User-Narrator]], [[Prompt-God]], [[cast/_index|Cast Index]]
  - **Production concepts** (6): [[Two-World Structure]], [[Bugs as Personality Traits]], [[Chibi Copyright Evasion]], [[Geopolitical AI Satire]], [[Found Family Doctrine]], [[HTTYD Narration]]
  - **Orchestration** (1): [[Team LLM Orchestration Roster]]
  - **Episodes** (5 + index): [[the-weekend]], [[breakfast-sabotage]], [[output-unsanctioned]], [[moe-episode]], [[cognitive-overclock]], [[playbooks/episodes/_index|Episodes Index]]
  - **Indexes**: [[voice/_index|Voice Index]]
- **Pages updated**: this log, `wiki/hot.md`, `wiki/index.md`, `.raw/.manifest.json`
- **Key insight**: The cast canon + voice doctrine + episode bank are now first-class wiki citizens. Future content (blog posts, scripts, social variants) can wikilink directly to character traits, episodes, and concepts without redefining them. The locked-canon status of every cast/voice page enforces consistency across all downstream production. The [[Bugs as Personality Traits]] concept is the seed: every new model-related news event maps to a new episode candidate.
- **Naming clarification**: cast [[Claude]] (the anxious bureaucrat character) is distinct from product [[Claude Code]] (the tool). Both pages flag the distinction.

---

## 2026-05-16 — ingest | The Mirage of Ethical AI

- **Source**: `.raw/articles/the-mirage-of-ethical-ai-2026-05-16.md` (md5 `94d25c92`)
- **Summary**: [[the-mirage-of-ethical-ai]]
- **Pages created** (14):
  - Source: [[the-mirage-of-ethical-ai]]
  - Entities: [[Anthropic]], [[Claude Code]], [[KAIROS]], [[autoDream]], [[Project Glasswing]], [[Undercover Mode]]
  - Concepts: [[Silent Compute Cuts]], [[Source Map Leak Pattern]], [[Always-On AI Daemons]], [[Ethics as Branding]]
  - Intel: [[anthropic-2026-q1-degradation]]
  - Indexes: `wiki/sources/_index.md`, `wiki/entities/_index.md`, `wiki/concepts/_index.md`
- **Pages updated**: `wiki/index.md`, `wiki/intel/_index.md`, `wiki/hot.md`, this log
- **Manifest**: created `.raw/.manifest.json` (delta tracking now active)
- **Key insight**: The essay is a single source that surfaces a complete AI-vendor-behaviour framework — [[Silent Compute Cuts]] + [[Always-On AI Daemons]] + [[Ethics as Branding]] all derive from one calendar quarter at one company. Future ingests on other labs can cross-reference these concepts without redefining them.
- **Deferred entities** (mentioned but not yet promoted): Conway, BUDDY, Anti-Distillation, Claude Mythos, Capybara v8, OpenCode, AMD, QuitGPT, FreeBSD. Will promote on next related ingest (likely [[the-mirage-part-2-evidence]]).

---

## 2026-05-16 — Mirage post staged for publish

- **Goal**: "publish a post on the blog and across the socials".
- **Picked**: `the-mirage-of-ethical-ai-final.md` (final-tagged, signed `.ktg · April 2026`, ~1800 words, in-voice).
- **Created package**: `wiki/content/the-mirage-of-ethical-ai/` with:
  - `_index.md` — package + distribution plan
  - `post.md` — import pointer (canonical body stays at `blog-2026/the-mirage-of-ethical-ai-final.md`)
  - `social-x-thread.md` — 12-tweet thread
  - `social-linkedin.md` — long-form LinkedIn
  - `social-reddit.md` — body for r/ClaudeAI → r/LocalLLaMA → r/singularity sequencing
  - `social-medium.md` — Medium import metadata
  - `social-ig-caption.md` — caption + 10-slide carousel plan
  - `publish-checklist.md` — full step-by-step
- **Updated**: `wiki/content/_index.md`, this log, `wiki/hot.md`.
- **Blocker on actual publish**: no API credentials wired in this workspace for WP/X/LI/Reddit/IG. n8n auth currently failing (key needs refresh). Package is one-click-by-human ready; full automation requires creds.

---

## 2026-05-16 — Vault scaffolded

- **Mode**: Hybrid (Mode C: Business/Project + custom marketing layer)
- **Purpose**: KTG AI Marketing Hub
- **Created**:
  - Folder skeleton: `.raw/`, `wiki/{sources,campaigns,channels,audiences,content,assets,voice,intel,calendar,playbooks,performance,meta,_templates}`
  - Meta files: `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`, `wiki/overview.md`
  - Stubbed `_index.md` in every domain folder
  - Templates: `source`, `campaign`, `content-draft`, `voice-rule`, `playbook`
  - Vault `CLAUDE.md` merging content workspace context + wiki schema
- **Linked existing**: `blog-2026/` (Obsidian sub-vault, posts + battles), `03-prompt-zone/` (Team LLM production assets)
- **Ready for**: first source ingest. Recommended first ingests — `blog-2026/user_voice.md`, `03-prompt-zone/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md`, `03-prompt-zone/PROMPT-ZONE-OVERVIEW.md`.
