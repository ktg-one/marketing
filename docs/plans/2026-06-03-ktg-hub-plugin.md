# Plan: ktg-hub — Claude Code plugin (refactor → post)

Date: 2026-06-03
Branch: feat/pipeline-google-voice-parallel
Goal (Kevin): refactor the marketing hub into a Claude Code/cowork plugin — agents + commands + hooks — that runs all the way to posting.

## Decisions (resolved, not asked)
- **Flavor:** standard Claude Code plugin (mirrors `claude-blog`). Cowork repackage is a later option.
- **Engine:** Google/Gemini (already converted + verified). Voice = `blog/user_voice.md`.
- **Vault stays out** of the plugin (data layer; not Glob-searchable inside a plugin).
- **Marketplace lives in this repo** at `.claude-plugin/marketplace.json`; plugin at `./plugins/ktg-hub`.
- **Pipeline is bundled** into the plugin (copy) so it's self-contained/distributable; referenced via `${CLAUDE_PLUGIN_ROOT}/pipeline`. Repo-root `pipeline/` remains source-of-truth until dedup (follow-up).

## Structure to build
```
.claude-plugin/marketplace.json            # repo root — marketplace entry
plugins/ktg-hub/
├── .claude-plugin/plugin.json             # name ktg-hub, v0.1.0, author Kevin
├── commands/
│   ├── hub.md                             # /ktg-hub:hub <post> — run pipeline → publish-kit → STOP at review gate
│   └── publish.md                         # /ktg-hub:publish <slug> — only after per-post YES; Vercel + Composio LI/Reddit
├── agents/
│   ├── content-repurposer.md              # platform variants in Myth-Hilarity voice
│   ├── seo-geo-optimizer.md               # SEO/GEO/schema (no voice on structured output)
│   └── publish-reviewer.md                # enforces the review gate; never auto-publishes
├── hooks/
│   ├── hooks.json                         # PreToolUse gate: block publish/Composio send unless <slug>/.approved exists
│   └── review-gate.sh                     # the gate check script (uses ${CLAUDE_PLUGIN_ROOT})
├── .mcp.json                              # nanobanana-mcp (Gemini image), ${GEMINI_API_KEY}
├── pipeline/                              # bundled copy of working pipeline (run.py, ktg_pipeline/, config.yaml, requirements.txt)
└── README.md
```

## Acceptance criteria
- All JSON valid (`plugin.json`, `marketplace.json`, `hooks.json`, `.mcp.json`).
- Plugin dir matches Claude Code spec; only `${CLAUDE_PLUGIN_ROOT}`/`${CLAUDE_PROJECT_DIR}` used for paths (no hardcoded absolute paths).
- Commands have valid YAML frontmatter (description, argument-hint).
- Agents have valid frontmatter (name, description).
- Review-gate hook genuinely blocks (exits non-zero) when approval marker is absent.
- README documents install (`/plugin marketplace add` → `/plugin install ktg-hub`) + usage.

## Out of scope (follow-up)
- De-duplicating repo-root `pipeline/` vs bundled copy.
- Live `/plugin install` end-to-end (non-interactive here) — validate by structure + JSON.
- Composio is remote/OAuth — referenced in command, not bundled as a local MCP.
