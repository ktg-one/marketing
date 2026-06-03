---
name: publish
description: Publishes an approved KTG publish kit — deploys to Vercel and posts the LinkedIn and Reddit variants via Composio — but only if the per-post review gate has been approved for that slug. Use when the user says "publish <slug>", "/publish", "post the approved kit", or "ship this post".
argument-hint: "<slug>"
---

# publish — fire the publish, only if approved

Publish the content kit for the slug the user names (`$ARGUMENTS`).

## Hard gate — check approval first

Only proceed if the review gate has been approved for this slug, signalled by the marker file:

```
${CLAUDE_PROJECT_DIR}/pipeline/output/$ARGUMENTS/.approved
```

1. **Verify the marker exists.** Check `${CLAUDE_PROJECT_DIR}/pipeline/output/$ARGUMENTS/.approved`.
   - If it does **NOT** exist: STOP. Tell the user the slug has not passed the review gate, and that they must run the `hub` skill and give an explicit per-post `YES` to the reviewer first. Do not publish anything.
   - Approval is **per-post only** — never treat a prior approval of one slug as approval of another, and never accept a session-wide blanket approval.

2. **If approved, publish:**
   - **Vercel** — deploy the site/content via the Vercel deploy tool.
   - **LinkedIn** — post the LinkedIn variant via the Composio MCP (`linkedin`) route.
   - **Reddit** — post the Reddit variant via the Composio MCP (`reddit`) route.

   Note: a `PreToolUse` hook independently re-checks the `.approved` marker and will hard-block any Composio/Vercel publish call if it is missing (fail-closed). Do not attempt to bypass it.

3. **Manual channels — say so explicitly.** **X (Twitter), Meta (Facebook/Instagram), and Medium do NOT support reliable auto-posting** — their platform APIs block it. Hand the user the prepared variants and tell them to post these three manually.

4. **Report** what was published where, with links/IDs, and which channels still need a manual paste.
