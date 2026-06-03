#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# ktg-hub review-gate PreToolUse hook  (FAIL-CLOSED by design)
#
# The KTG review gate is NON-BYPASSABLE. This hook fires before any publish
# action (Composio reddit/linkedin sends, Vercel deploy) and blocks unless the
# active slug has an explicit human-written approval marker:
#
#     <project>/pipeline/publish-kit/<slug>/.approved
#
# FAIL-CLOSED PRINCIPLE: if we cannot positively confirm an approval marker for
# a definite slug, we BLOCK (exit 2). Ambiguity, missing slug, unreadable
# input, or any error all resolve to "blocked" — never to "allowed". A gate
# that opens when it is confused is not a gate. The only path to exit 0 is a
# real .approved file for a slug we could unambiguously resolve.
#
# Slug resolution order:
#   1. $KTG_PUBLISH_SLUG env var (set explicitly by the publish flow), else
#   2. the single slug under pipeline/publish-kit/ that already has .approved
#      (if exactly one exists — unambiguous), else
#   3. BLOCK.
#
# Exit codes: 0 = allow (approved). 2 = block (Claude Code treats stderr as the
# block reason for PreToolUse). Any other failure path also blocks.
# Host note: POSIX-ish bash; this machine runs cygwin bash.
# ---------------------------------------------------------------------------

set -u

# Read (and discard) the hook JSON from stdin so the producer never blocks on a
# full pipe. We don't strictly need fields from it, but we drain it safely.
STDIN_JSON="$(cat 2>/dev/null || true)"
: "${STDIN_JSON:=}"

# Determine the project root. CLAUDE_PROJECT_DIR is set by Claude Code; fall
# back to the current directory if it is somehow absent.
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
KIT_DIR="${PROJECT_DIR}/pipeline/publish-kit"

block() {
  echo "REVIEW GATE BLOCKED: $1" >&2
  echo "No per-post approval marker found. Run /ktg-hub:hub <post>, review the" >&2
  echo "publish-kit, and reply YES to the reviewer to approve THIS slug before" >&2
  echo "publishing. The gate is non-bypassable and fail-closed." >&2
  exit 2
}

SLUG=""

# 1. Explicit slug from environment.
if [ -n "${KTG_PUBLISH_SLUG:-}" ]; then
  SLUG="${KTG_PUBLISH_SLUG}"
fi

# 2. Otherwise, if exactly one slug under publish-kit is already approved, use it.
if [ -z "${SLUG}" ] && [ -d "${KIT_DIR}" ]; then
  approved_count=0
  approved_slug=""
  for d in "${KIT_DIR}"/*/; do
    [ -e "${d}" ] || continue
    if [ -f "${d}.approved" ]; then
      approved_count=$((approved_count + 1))
      approved_slug="$(basename "${d}")"
    fi
  done
  if [ "${approved_count}" -eq 1 ]; then
    SLUG="${approved_slug}"
  elif [ "${approved_count}" -gt 1 ]; then
    block "multiple approved slugs found — cannot determine which post this publish targets (set KTG_PUBLISH_SLUG)"
  fi
fi

# 3. Still no slug -> fail closed.
if [ -z "${SLUG}" ]; then
  block "could not determine the active publish slug"
fi

# Final check: the resolved slug must have an approval marker.
MARKER="${KIT_DIR}/${SLUG}/.approved"
if [ -f "${MARKER}" ]; then
  echo "ktg-hub review gate: slug '${SLUG}' is approved — allowing publish." >&2
  exit 0
fi

block "slug '${SLUG}' has no .approved marker at ${MARKER}"
