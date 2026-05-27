# Social API Reality Check — What Actually Works

## The Hard Truth

Most social platforms **heavily restrict** or **completely block** automated posting via API.

## Platform-by-Platform Status

### X (Twitter) — EFFECTIVELY DEAD for bots
- **API v2**: $100/month basic tier, 3,000 tweets/month read limit
- **Write access**: Requires $5,000/month enterprise tier OR verified developer status
- **Rate limits**: Extremely aggressive anti-bot detection
- **Reality**: You cannot auto-post to X without paying $5K/month or being a major partner
- **Workaround**: Manual copy-paste, or Buffer (but Buffer still hits X API limits)

### Meta (Facebook/Instagram) — RESTRICTED
- **Graph API**: Requires Business Verification
- **Instagram**: Only Business/Creator accounts, content must be "organic"
- **Rate limits**: 25 posts/day per account, heavy spam detection
- **Reality**: Works for approved apps, but personal accounts blocked
- **Workaround**: Buffer, Creator Studio manual, or Meta Business Suite

### LinkedIn — MOST PERMISSIVE
- **API**: OAuth 2.0, `w_member_social` scope
- **Limits**: 150 requests/day for posts
- **Reality**: Actually works for personal profiles and company pages
- **Status**: ✅ Best option for automation
- **Caveat**: Posts marked "via [app name]" which looks less organic

### Reddit — MODERATELY PERMISSIVE
- **API**: OAuth 2.0, free tier available
- **Limits**: 60 requests/minute
- **Reality**: Works but subreddits have anti-bot rules
- **Status**: ✅ Works, but risk of ban if spammy
- **Caveat**: Must follow subreddit rules, engage genuinely

### Medium — RESTRICTED
- **API**: v1, OAuth required
- **Reality**: API is read-only for most; write access limited
- **Status**: ⚠️ Hard to get write access
- **Workaround**: Manual import, or Medium's "Import story" feature

## What Composio Actually Gives You

Composio MCP connectors are **wrappers around APIs**. They don't bypass restrictions.

| Connector | What It Can Do | What It CANNOT Do |
|-----------|---------------|-------------------|
| `linkedin` | Post to profile, get analytics | Post to groups, send DMs |
| `reddit` | Submit posts, comment | Bypass subreddit rules |
| `vercel` | Deploy, manage domains | Nothing blocked |
| `x` | Read tweets (maybe) | Post tweets (blocked) |
| `meta` | Read pages (maybe) | Post to personal profile |
| `medium` | Read articles | Publish articles |

## What Actually Works for Publishing

### Option 1: Buffer (Recommended)
- **What**: You manually queue posts in Buffer, Buffer posts them
- **Automation level**: Semi — you still create content, Buffer handles timing
- **Platforms**: X, Meta, LinkedIn, Pinterest, Mastodon
- **Cost**: Free tier: 3 channels, 10 posts/channel
- **Reality**: Buffer has API access because they're a verified partner

### Option 2: Manual Copy-Paste (Most Reliable)
- **What**: Pipeline generates content → you copy → paste into each platform
- **Automation level**: Zero
- **Platforms**: All of them
- **Reality**: 100% reliable, 100% human

### Option 3: RSS/IFTTT/Zapier (Limited)
- **What**: Blog RSS → trigger → post to social
- **Platforms**: LinkedIn (via Zapier), X (limited), Facebook (pages only)
- **Reality**: Brittle, often breaks, limited formatting

### Option 4: Browser Automation (Risky)
- **What**: Playwright/Selenium logs into platform, simulates human clicks
- **Platforms**: Any with web interface
- **Reality**: Against ToS, easy to detect, account ban risk

## Revised Pipeline Architecture

```
┌─────────────────┐
│  Blog Post      │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Pipeline │ ← AI generates all variants
    └────┬────┘
         │
    ┌────▼────┐
    │ Review   │ ← You say YES/NO
    └────┬────┘
         │
    ┌────▼────┐
    │ Outputs  │ ← 8 files ready
    └────┬────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐  ┌──▼────┐
│Manual │  │Buffer │ ← Semi-auto for some
│Paste  │  │Queue  │
└───┬───┘  └──┬────┘
    │         │
┌───▼─────────▼───┐
│ All Platforms   │
└─────────────────┘
```

## What the Pipeline Should Actually Do

1. **Generate** all content variants (✅ done)
2. **Format** them perfectly for each platform (✅ done)
3. **Create** a "publish kit" — one folder per post with all assets
4. **Offer** two paths:
   - **Manual**: Copy-paste instructions with pre-formatted text
   - **Buffer**: Generate a CSV/import file for Buffer queue

## Buffer CSV Format

```csv
profile,content,image,scheduled_at
linkedin,"Full article text...","hero-linkedin.png","2026-05-27T09:00:00Z"
twitter,"Thread: 1/ The software engineer...","hero-x.png","2026-05-27T09:15:00Z"
facebook,"🚨 The software engineer job...","hero-square.png","2026-05-27T09:30:00Z"
```

## Conclusion

**The pipeline is correct as-is.** It generates outputs. Publishing is a separate, harder problem.

Don't try to auto-post directly to X or Meta. Use:
- **LinkedIn**: Direct API (works)
- **Reddit**: Direct API (works with care)
- **X/Meta**: Buffer or manual
- **Medium**: Manual import

Focus on making the generated content so good that copy-pasting is fast.
