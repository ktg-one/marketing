---
name: hub
description: Runs the KTG / Good AI content pipeline on a blog post — repurposes it for Medium, Reddit, X, LinkedIn and Meta in the Myth-Hilarity house voice, generates SEO/GEO and JSON-LD schema, assembles a publish kit, and stops at the non-bypassable review gate. Use when the user says "run the hub", "/hub", "run the content pipeline", "repurpose this post", or "prep this post for publishing".
argument-hint: "<post-file-path>"
---

# hub — drive the content pipeline to the review gate

Orchestrate the KTG / Good AI content pipeline for the post the user names (the path in `$ARGUMENTS`).

## What this does

Repurpose a blog post into platform variants → SEO/GEO + JSON-LD schema → (optional) image → assemble an 8-file publish kit. The engine is Gemini (Google AI Studio). The house voice — **Myth-Hilarity + Tech Anthropology** — is sourced from the bundled `voice/user_voice.md` and applied to narrative variants only (never to structured/JSON outputs).

## Steps

1. **Confirm the input exists.** If `$ARGUMENTS` is empty or the file is missing, ask for a valid post path and stop.

2. **Run the bundled pipeline.** Execute exactly (the leading env var makes the bundled house voice resolve regardless of CWD):

   ```bash
   KTG_VOICE_FILE="${CLAUDE_PLUGIN_ROOT}/voice/user_voice.md" uv run --no-project --with pyyaml --with requests python "${CLAUDE_PLUGIN_ROOT}/pipeline/run.py" "$ARGUMENTS" --config "${CLAUDE_PLUGIN_ROOT}/pipeline/config.yaml"
   ```

   - The pipeline is Gemini-driven and needs `GEMINI_API_KEY` in the environment. If the run reports a missing/invalid key, surface that clearly and stop — do not silently fall back.
   - Use `${CLAUDE_PLUGIN_ROOT}` for the pipeline path, bundled config, and bundled voice file. Never hardcode an absolute path.

3. **Summarize the publish kit.** Read the generated output under `pipeline/output/<slug>/` (per-platform variants — Medium / Reddit / X / LinkedIn / Meta — plus SEO + ads + schema artifacts) and give a concise summary of each piece. Note the slug.

4. **STOP at the review gate.** Non-bypassable.
   - Do **NOT** auto-publish anything.
   - Write an approval-needed note for the slug so the gate survives `/clear` (e.g. in `pipeline/output/<slug>/`). Do **NOT** create the `.approved` marker yourself — only `publish-reviewer` writes it, after an explicit human `YES`.
   - Tell the user: review the kit, and when satisfied reply with an explicit per-post `YES` for this slug. Approval is per-post only — never session-wide.

5. **Point to the next step.** After approval, run the `publish` skill on the slug to deploy to Vercel and post to LinkedIn + Reddit via Composio. X / Meta / Medium remain manual (platform APIs block auto-posting).
