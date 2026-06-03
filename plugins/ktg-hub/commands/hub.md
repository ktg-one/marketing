---
description: Run the Gemini-driven KTG content pipeline on a blog post, assemble the publish-kit, then STOP at the non-bypassable review gate.
argument-hint: "<post-file-path>"
---

# /ktg-hub:hub — drive the content pipeline to the review gate

You are orchestrating the KTG / Good AI content pipeline for the post at: **$ARGUMENTS**

## What this does

Repurpose a blog post into platform variants -> SEO/GEO + JSON-LD schema -> (optional) image -> assemble an 8-file publish-kit. The engine is Gemini (Google AI Studio). The house voice — **Myth-Hilarity + Tech Anthropology** — is sourced from `blog/user_voice.md` and applied to narrative variants only (never to structured/JSON outputs).

## Steps

1. **Confirm the input exists.** If `$ARGUMENTS` is empty or the file is missing, ask for a valid post path and stop.

2. **Run the bundled pipeline.** Execute exactly:

   ```bash
   uv run --no-project --with pyyaml --with requests python "${CLAUDE_PLUGIN_ROOT}/pipeline/run.py" $ARGUMENTS
   ```

   - The pipeline is Gemini-driven by default and needs `GEMINI_API_KEY` in the environment. If the run reports a missing/invalid key, surface that clearly and stop — do not silently fall back.
   - Use `${CLAUDE_PLUGIN_ROOT}` for the pipeline path. Never hardcode an absolute path.

3. **Summarize the publish-kit.** Read the generated output (the 8-file publish-kit: per-platform variants — Medium / Reddit / X / LinkedIn / Meta — plus SEO + ads + schema artifacts) and give the user a concise summary of each piece. Note the slug.

4. **STOP at the review gate.** This is non-bypassable.
   - Do **NOT** auto-publish anything.
   - Write an approval-needed state for the slug so the gate survives `/clear` (e.g. a note in the publish-kit dir indicating the kit is assembled and awaiting per-post `YES`). Do **NOT** create the `.approved` marker yourself — that marker is written only by `publish-reviewer` after an explicit human `YES`.
   - Tell the user: review the publish-kit, and when satisfied reply with an explicit per-post `YES` for this slug. Approval is per-post only — never session-wide.

5. **Point to the next step.** After approval, the user runs `/ktg-hub:publish <slug>` to deploy to Vercel and post to LinkedIn + Reddit via Composio. X / Meta / Medium remain manual (platform APIs block auto-posting).
