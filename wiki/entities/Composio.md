---
type: entity
subtype: product
title: "Composio"
aliases: ["Composio MCP", "Composio connector"]
created: 2026-05-27
tags: [entity, product, publishing, mcp, social-media, automation]
---

# Composio

MCP-based publishing connector. The primary automated social outbound and deployment tool for the [[ktg-one]] pipeline. Replaces n8n as the default automation route (n8n `list_workflows` auth is currently broken).

## What It Does

Composio provides MCP tool connectors for major social and infrastructure platforms, enabling AI agents to fire content posts and deployments without requiring manual API setup per platform.

## Connected Channels (ktg-one)

| Channel | Purpose | Status |
|---|---|---|
| `reddit` | Community posts | Available |
| `linkedin` | Professional posts | Available |
| `vercel` | Site deployment | Available |
| `gmail` | Email campaigns | Available |
| `googledrive` | Asset storage | Available |
| `discord` | Community | Available |
| `slack` | Team | Available |
| `youtube` | Video | Available |
| `facebook` | Social | Available |

**Not available via Composio** (API-blocked):
- X (Twitter) — API $5K/month
- Meta (Instagram organic) — Business verification required
- Medium — API read-only for most users

## Usage Rules

- **Always get explicit per-post green-light from the user before firing any social send.** The channel list is permission to use the route, not permission to post.
- Composio is the **default** automation route — use instead of n8n
- n8n is wired but `list_workflows` auth is flaky — not reliable

## Deployment Flow (Vercel via Composio)

1. Post approved at [[Review-Gate]] → user types `YES`
2. Composio deploys to Vercel → captures canonical URL
3. Canonical URL injected into social variants
4. Composio fires Reddit + LinkedIn posts
5. Wiki log entry written

## MCP Gateway

Composio connections are managed via the MCP gateway at `D:\projects\.mcp\gateway.py`. Do not modify gateway config without understanding downstream effects.

## Relationship to n8n

n8n is wired into the [[ktg-one]] workspace but is not the default route. The `list_workflows` authentication has been broken since at least 2026-05. All automation should default to Composio.

## Cross-References
- [[ktg-one]] — the workspace using Composio
- [[Review-Gate]] — the gate before Composio fires
- [[Publish-Kit-Pattern]] — the content prepared for Composio to distribute
- [[Five-Layer-Architecture]] — Layer 5 (Publishing)
- [[project-state]] — current integration status
