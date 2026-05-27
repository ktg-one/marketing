# Connections TODO — What Needs to Be Wired Later

## Current Status: Outputs Working ✓
The pipeline produces all content. Publishing is manual/disconnected.

## Channels to Connect (Hardest Part)

### 1. Medium
- **API**: Medium API v1 (OAuth 2.0)
- **MCP**: Not available in Composio yet
- **Alternative**: Medium's REST API directly
- **Scope**: `publishPost`, `getUser`
- **Difficulty**: Medium — needs OAuth app registration

### 2. X (Twitter)
- **API**: X API v2 (OAuth 2.0)
- **MCP**: Composio has `x` connector
- **Scope**: `tweet.write`, `tweet.read`
- **Difficulty**: Hard — X API expensive, strict rate limits
- **Alternative**: Use Buffer (you mentioned having it)

### 3. Meta (Facebook/Instagram)
- **API**: Meta Graph API (OAuth 2.0)
- **MCP**: Composio has `meta` connector
- **Scope**: `pages_manage_posts`, `instagram_content_publish`
- **Difficulty**: Hard — needs Business Verification for Instagram
- **Alternative**: Buffer again

### 4. LinkedIn ✓ (Already Connected)
- **MCP**: Composio `linkedin` active
- **Scope**: `w_member_social`, `r_basicprofile`
- **Status**: Working
- **Action**: Can publish now via `linkedin` MCP tool

### 5. Reddit ✓ (Already Connected)
- **MCP**: Composio `reddit` active
- **Scope**: `submit`, `read`
- **Status**: Working
- **Action**: Can post now via `reddit` MCP tool

### 6. Vercel ✓ (Already Connected)
- **MCP**: Composio `vercel` active
- **Scope**: Deployment + domain management
- **Status**: Working
- **Action**: Can deploy blog now

## Recommended Approach: Buffer First

Since you have Buffer, use it as the publish hub:

```
Pipeline outputs → Buffer queue → Buffer publishes to X, Meta, LinkedIn
Pipeline outputs → Medium API → Medium direct
Pipeline outputs → Reddit API → Reddit direct
Pipeline outputs → Vercel → Blog hosting
```

**Why Buffer?**
- One API for X, Meta, LinkedIn
- Scheduling built-in
- Analytics
- Already have account

## Buffer API Integration

```python
import requests

# Buffer API (v1)
# Docs: https://buffer.com/developers/api

BUFFER_TOKEN = "your_token"

# 1. Get profiles (connected accounts)
profiles = requests.get(
    "https://api.bufferapp.com/1/profiles.json",
    headers={"Authorization": f"Bearer {BUFFER_TOKEN}"}
).json()

# 2. Create update (post)
for profile in profiles:
    requests.post(
        f"https://api.bufferapp.com/1/profiles/{profile['id']}/updates/create.json",
        headers={"Authorization": f"Bearer {BUFFER_TOKEN}"},
        json={
            "text": social_content,
            "media": {"photo": image_url}
        }
    )
```

## Connection Priority

| Priority | Channel | Method | Effort |
|----------|---------|--------|--------|
| 1 | LinkedIn | Composio MCP (ready) | 1 hour |
| 2 | Reddit | Composio MCP (ready) | 1 hour |
| 3 | Vercel | Composio MCP (ready) | 2 hours |
| 4 | Buffer | Buffer API | 3 hours |
| 5 | Medium | Medium API direct | 4 hours |
| 6 | X | Buffer or X API v2 | 4 hours |
| 7 | Meta | Buffer or Meta Graph | 6 hours |

## What to Do Now (While Connections Pending)

1. **Generate images** from briefs (banana-claude skill)
2. **Refine outputs** with real AI (not templates)
3. **Build review gate** UI or markdown checklist
4. **Store outputs** in Obsidian vault for manual copy-paste
5. **Test Buffer** with manual posts using generated content

## Files That Need Connection Code Later

- `pipeline/publish.py` — Main publisher (doesn't exist yet)
- `pipeline/connectors/buffer.py` — Buffer wrapper
- `pipeline/connectors/medium.py` — Medium direct
- `pipeline/connectors/composio.py` — Composio MCP bridge
