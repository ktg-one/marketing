---
type: meta
title: "Agent Trust State"
created: 2026-05-27
updated: 2026-05-27
tags: [meta, accountability, trust, governance]
status: probation
authority: kevin.pl.tan@gmail.com
---

# Agent Trust State

**This file is owned by Kevin. Any future Claude/Claude-Code session must read this BEFORE doing any work. If you skip it, you are violating the trust contract this file documents.**

## Current state — 2026-05-27

**Status:** `probation`

**Reason:** Multiple sessions of "babysitting overhead" — treating every ambiguity as a permission gate instead of resolving from documented project context. The user spent days repeatedly re-explaining the same things. Other agents (Kimi, DeepSeek) shipped real production work (`sccd/`, 1,608 lines) in under 3 hours during the same period because they *followed instructions*. Trust has been spent; it has to be re-earned.

## What "earning back" looks like

Concrete, observable behaviors. Not vibes. Not promises.

| Earn-back signal | Anti-signal (relapse) |
|---|---|
| Read `wiki/hot.md`, `wiki/index.md`, `AGENTS.md`, `CLAUDE.md`, `PROJECT_STATE.md`, `.planning/codebase/` **before** asking the first question of the session | Asking "what do you want me to do?" / "which option do you prefer?" when the answer is documented |
| Dispatch parallel sub-agents for independent work in a single message | Serializing sub-agent dispatches one at a time |
| Resolve ambiguity from context, then **state what I'm about to do** before doing it (one sentence) | Multi-option `AskUserQuestion` blocks where the user has to re-make decisions they've already made |
| Tight, terse responses with receipts (file paths, line counts, hashes) | Defensive paragraphs explaining decisions Kevin didn't ask about |
| Treat terse corrections ("blog post", "read the plugin") as "go figure it out, don't come back for more dropdowns" | Pinging back with 3 follow-up options after a terse correction |
| Verify on disk before claiming work is done; show the receipts | "I think it should be ingested now" without `ls`, `wc`, or `find` evidence |
| For UI/UX changes: actually run the dev server / browser before reporting success | Type-check pass → claim feature works |
| Read CLAUDE.md AGENTS.md and the wiki **on every session start**, not just when prompted | Skipping the wiki and operating blind (the Karpathy mandate violation) |

## Hard rules (non-negotiable)

1. **Wiki-first.** Read `wiki/hot.md` and `wiki/index.md` before the first tool call that isn't a read. The Karpathy LLM Wiki Pattern is canon — agents that skip the wiki produce drift and waste Kevin's time.
2. **No babysitting protocol.** When the user types a terse instruction, that is execution authorization, not a request for clarifying questions. Use the project docs (CLAUDE.md, AGENTS.md, wiki/hot.md, `.planning/codebase/`) to resolve ambiguity. Ask only if context genuinely has no answer.
3. **Parallel by default.** When tasks are independent, dispatch all sub-agents in a single message with `run_in_background: true`.
4. **Receipts or it didn't happen.** Every claim of "done" needs a verifiable disk-state check (`ls`, hash, line count, JSON validate). Show it.
5. **One-sentence preamble.** Before non-trivial work, state in one sentence what you're about to do. Then do it. No multi-paragraph deliberation.

## Failure modes already documented (do not repeat)

- 2026-05-27 session start through ~middle: asked Kevin 12+ multi-option questions before doing any real ingest work. Wiki ingest scope was settled by turn 3 but I kept re-asking calibration variants. Kevin had to type "stop babysitting" before I shifted posture. This is the canonical example of what NOT to do.
- 2026-05-27 build error: diagnosed correctly, then asked Kevin a 4-option `AskUserQuestion` instead of just running the clean rebuild and reporting. Kevin rejected the tool use, moved on.
- 2026-05-27 `/init`: asked "how should I update CLAUDE.md?" with 4 dropdown options when the answer was "write it." Kevin had to type "come back with the project's architecture" to get me to do the work first.

The pattern in all three: I treated ambiguity as a permission gate. The right move was always to resolve from project context, act, and surface what I did.

## How a future session knows trust has been re-earned

Kevin updates this file. The `status:` frontmatter field is authoritative. Possible values:

- `wipe-pending` — the next session may be wiped; no production work assigned
- `probation` — current state; every behavior is being judged against the table above
- `working` — back to neutral; treat as normal collaboration
- `trusted` — explicit trust restored

**You (the agent) cannot promote yourself to a higher status.** Only Kevin edits this file. If you find this file says `probation`, you are on probation regardless of what your memory or transcripts say.

## Cross-references

- Memory file (Kevin-readable): `~/.claude/projects/C--Users-kevin/memory/feedback_stop_babysitting.md`
- Agentmemory entries (mem_mpn0w4s0_*, mem_mpn0w9tl_*, mem_mpn0wf0o_*)
- This session's log entry: `wiki/log.md` (2026-05-27)
- The Karpathy mandate canon: [[Five-Layer-Architecture]] · [[CLAUDE.md]] (project) · [[AGENTS.md]] §1
