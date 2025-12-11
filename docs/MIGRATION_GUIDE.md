# Migration Guide - v2.0 Updates

## 🎉 What's New

The Reddit Subreddit Summarizer has been upgraded with major improvements:

1. **No Reddit API credentials required** - Now uses Reddit's public JSON API
2. **OpenRouter integration** - Access to 100+ LLM models with one API key
3. **Simpler setup** - Just one API key needed (OpenRouter or OpenAI)

## Breaking Changes

### ❌ Removed: Reddit API Authentication

**Old way (v1.0):**
```bash
# .env file
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=RedditSummarizer/0.1.0
OPENAI_API_KEY=your_openai_key
```

**New way (v2.0):**
```bash
# .env file
OPENROUTER_API_KEY=your_openrouter_key

# Reddit credentials NO LONGER NEEDED! 🎉
```

### ⚙️ Changed: Default LLM Model

**Old default:** `gpt-4o-mini` (OpenAI)
**New default:** `openrouter/anthropic/claude-3.5-sonnet` (OpenRouter)

## Migration Steps

### Step 1: Update Dependencies

```bash
pip install -r requirements.txt
```

The new `requirements.txt` no longer includes PRAW and uses `requests` instead.

### Step 2: Get OpenRouter API Key

1. Visit https://openrouter.ai/keys
2. Sign up or log in
3. Create a new API key
4. Copy the key (starts with `sk-or-...`)

### Step 3: Update .env File

**Remove these lines:**
```bash
REDDIT_CLIENT_ID=...
REDDIT_CLIENT_SECRET=...
REDDIT_USER_AGENT=...
```

**Add this line:**
```bash
OPENROUTER_API_KEY=sk-or-v1-...
```

### Step 4: Update Your Scripts (if using programmatically)

**Old code:**
```python
from reddit_summarizer import RedditFetcher, RedditSummarizer

# Old: Required Reddit API credentials
fetcher = RedditFetcher(
    client_id="your_id",
    client_secret="your_secret"
)

summarizer = RedditSummarizer(model="gpt-4o-mini")
```

**New code:**
```python
from reddit_summarizer import RedditFetcher, RedditSummarizer

# New: No Reddit credentials needed!
fetcher = RedditFetcher()  # That's it!

# New: OpenRouter by default
summarizer = RedditSummarizer(
    model="openrouter/anthropic/claude-3.5-sonnet"
)
```

## Compatibility

### What Still Works

✅ All command-line options remain the same
✅ Output formats (Markdown, JSON, HTML) unchanged
✅ Checkpointing and resume functionality
✅ Skillbook persistence and learning
✅ All filtering options (min-upvotes, min-comments)

### What Changed

🔄 Default model is now OpenRouter-based
🔄 Reddit data fetched via public JSON API (no auth)
🔄 Slightly different rate limiting behavior (more permissive)

## Using OpenRouter vs Direct APIs

### Option 1: OpenRouter (Recommended)

**Advantages:**
- ✅ One API key for 100+ models
- ✅ Access to OpenAI, Anthropic, Google, Meta, Cohere, and more
- ✅ Automatic fallback if one provider is down
- ✅ Competitive pricing
- ✅ Usage analytics

**Available models:**
```bash
# Anthropic Claude
openrouter/anthropic/claude-3.5-sonnet
openrouter/anthropic/claude-3-opus

# OpenAI
openrouter/openai/gpt-4o
openrouter/openai/gpt-4-turbo

# Google
openrouter/google/gemini-pro
openrouter/google/gemini-1.5-pro

# Meta
openrouter/meta-llama/llama-3.1-70b-instruct

# See all at: https://openrouter.ai/models
```

### Option 2: Direct Provider APIs

You can still use provider APIs directly:

```bash
# .env
OPENAI_API_KEY=sk-...
# or
ANTHROPIC_API_KEY=sk-ant-...
```

Then use models without the `openrouter/` prefix:
```bash
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model gpt-4o-mini
```

## Examples

### Basic Usage (OpenRouter)
```bash
# With OpenRouter (default)
export OPENROUTER_API_KEY=sk-or-v1-...
python summarize_subreddit.py python --start 2024-12-01 --end 2024-12-10
```

### Using Different Models
```bash
# GPT-4o via OpenRouter
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/openai/gpt-4o

# Claude 3 Opus via OpenRouter
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/anthropic/claude-3-opus

# Gemini Pro via OpenRouter
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/google/gemini-pro
```

## Benefits of v2.0

### Simpler Setup
- **Before:** Get Reddit API credentials, create app, manage OAuth
- **After:** Just get one OpenRouter API key

### More Flexibility
- **Before:** Locked to one LLM provider
- **After:** Switch between 100+ models with same API key

### Better Reliability
- **Before:** Reddit API rate limits and authentication issues
- **After:** Public API is more permissive, no auth failures

### Cost Efficiency
- **Before:** Tied to OpenAI pricing
- **After:** Choose from multiple providers, compare prices

## Troubleshooting

### "No LLM API key found"
**Solution:** Set `OPENROUTER_API_KEY` in `.env` or use `OPENAI_API_KEY`

### "Subreddit does not exist" (but it does)
**Solution:** The public API works the same way. Check spelling and try again.

### "Module 'praw' not found"
**Solution:** Remove old environment and reinstall:
```bash
pip uninstall praw prawcore
pip install -r requirements.txt
```

### Model not working
**Solution:**
1. Check model name at https://openrouter.ai/models
2. Ensure you have credits in your OpenRouter account
3. Try the default model first to verify API key works

## Questions?

- OpenRouter docs: https://openrouter.ai/docs
- Reddit public API: https://www.reddit.com/dev/api
- Full guide: See SUBREDDIT_SUMMARIZER_GUIDE.md

## Summary

🎉 **You now have:**
- ✅ Simpler setup (no Reddit credentials)
- ✅ More LLM options (100+ models)
- ✅ Better reliability (public API)
- ✅ Same great features

**Quick migration checklist:**
- [ ] Install updated dependencies (`pip install -r requirements.txt`)
- [ ] Get OpenRouter API key (https://openrouter.ai/keys)
- [ ] Update `.env` with `OPENROUTER_API_KEY`
- [ ] Remove old `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET`
- [ ] Test with: `python summarize_subreddit.py python --start 2024-12-01 --end 2024-12-10 --max-posts 5`

Enjoy the upgraded Reddit Summarizer! 🚀
