---
description: Publish an approved publish-kit — Vercel deploy + LinkedIn/Reddit via Composio. Only runs if the review gate is approved for the slug.
argument-hint: "<slug>"
---

# /ktg-hub:publish — fire the publish, only if approved

You are publishing the content kit for slug: **$ARGUMENTS**

## Hard gate — check approval first

This command is **only** allowed to proceed if the review gate has been approved for this slug. Approval is signalled by the marker file:

```
${CLAUDE_PROJECT_DIR}/pipeline/publish-kit/$ARGUMENTS/.approved
```

1. **Verify the marker exists.** Check that `${CLAUDE_PROJECT_DIR}/pipeline/publish-kit/$ARGUMENTS/.approved` is present.
   - If it does **NOT** exist: STOP. Tell the user the slug has not passed the review gate, and that they must run `/ktg-hub:hub <post>` and give an explicit per-post `YES` to the reviewer first. Do not publish anything.
   - Approval is **per-post only** — never treat a prior approval of one slug as approval of another, and never accept a session-wide blanket approval.

2. **If approved, publish:**
   - **Vercel** — deploy the site/content via the Vercel deploy tool.
   - **LinkedIn** — post the LinkedIn variant via the Composio MCP (`linkedin`) route.
   - **Reddit** — post the Reddit variant via the Composio MCP (`reddit`) route.

   Note: a `PreToolUse` hook independently re-checks the `.approved` marker and will hard-block any Composio/Vercel publish call if it is missing (fail-closed). Do not attempt to bypass it.

3. **Manual channels — say so explicitly.** **X (Twitter), Meta (Facebook/Instagram), and Medium do NOT support reliable auto-posting** — their platform APIs block it. Hand the user the prepared variants from the publish-kit and tell them to post these three manually.

4. **Report** what was published where, with links/IDs, and which channels still need a manual paste.
