# Reddit Summarizer - Quick Start Guide

Get started with the Reddit Subreddit Summarizer in 5 minutes!

## Prerequisites

- Python 3.11+ installed
- Reddit account (for API access)
- OpenAI API key (or any LiteLLM-compatible provider)

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `praw` - Reddit API wrapper
- `ace-framework` - AI learning framework
- `click` - CLI framework
- `python-dotenv` - Environment variable management
- `tqdm` - Progress bars

## Step 2: Get Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps
2. Click **"create another app..."**
3. Fill in:
   - **name**: `my-reddit-summarizer`
   - **App type**: Select **"script"**
   - **description**: Leave blank or add description
   - **about url**: Leave blank
   - **redirect uri**: `http://localhost:8080`
4. Click **"create app"**
5. Note down:
   - **client_id**: String under "personal use script"
   - **client_secret**: String next to "secret"

## Step 3: Configure Environment

Create a `.env` file in the workspace directory:

```bash
# Reddit API credentials
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=RedditSummarizer/0.1.0

# OpenAI API key (or other LLM provider)
OPENAI_API_KEY=your_openai_api_key_here
```

**Security Note:** Never commit `.env` file to version control!

## Step 4: Run Your First Summary

Try this command to summarize r/python from the last week:

```bash
python summarize_subreddit.py python \
  --start 2024-12-01 \
  --end 2024-12-10 \
  --max-posts 5
```

**Expected output:**
```
🤖 Reddit Subreddit Summarizer with ACE Framework

Subreddit: r/python
Date range: 2024-12-01 to 2024-12-10
Filters: ≥100 upvotes, ≥30 comments
Model: gpt-4o-mini

🔧 Initializing components...
📥 Fetching posts from r/python...
✅ Found 5 posts matching criteria

🔮 Generating digest with AI summaries...
Summarizing posts: 100%|████████████| 5/5 [00:15<00:00, 3.21s/post]

✅ Digest saved to: python_digest_2024-12-01_to_2024-12-10.md

📊 Summary Stats:
  Posts analyzed: 5
  Posts summarized: 5

✨ Done! Check python_digest_2024-12-01_to_2024-12-10.md for your reading digest.
```

## Step 5: View Your Digest

Open the generated markdown file to see your AI-powered reading digest:

```bash
cat python_digest_2024-12-01_to_2024-12-10.md
```

## Common Use Cases

### Weekly Digest for Your Favorite Subreddit

```bash
python summarize_subreddit.py MachineLearning \
  --start 2024-12-01 \
  --end 2024-12-07 \
  --min-upvotes 200 \
  --min-comments 50 \
  --output weekly_ml_digest.md
```

### Quick Daily Summary (Top 10 Posts)

```bash
python summarize_subreddit.py technology \
  --start 2024-12-10 \
  --end 2024-12-10 \
  --max-posts 10 \
  --min-upvotes 500
```

### Long-Running Summary with Checkpoints

For processing many posts (prevents losing progress):

```bash
python summarize_subreddit.py AskReddit \
  --start 2024-01-01 \
  --end 2024-12-31 \
  --max-posts 100 \
  --checkpoint askreddit_progress.json \
  --checkpoint-interval 10
```

If interrupted, just re-run the same command - it will resume automatically!

### Save Learned Skills for Reuse

The tool learns from experience. Save the skillbook to reuse:

```bash
# First run - learns from experience
python summarize_subreddit.py python \
  --start 2024-01-01 --end 2024-01-31 \
  --save-skillbook python_skills.json

# Next run - reuses learned skills for better summaries
python summarize_subreddit.py python \
  --start 2024-02-01 --end 2024-02-28 \
  --skillbook python_skills.json \
  --save-skillbook python_skills.json
```

## Troubleshooting

### "Reddit API credentials not found"

**Problem:** Missing or incorrect `.env` file

**Solution:**
1. Check that `.env` exists in the workspace directory
2. Verify `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` are set
3. Ensure no extra quotes around values

### "No posts found matching criteria"

**Problem:** Filters too strict for the subreddit/date range

**Solution:**
- Lower thresholds: `--min-upvotes 50 --min-comments 10`
- Expand date range
- Try a different subreddit with more activity

### Rate Limiting Errors

**Problem:** Reddit API throttling (60 requests/minute)

**Solution:**
- Reduce `--max-posts` to fewer posts
- Wait 1-2 minutes between runs
- The tool has built-in rate limiting (1 second delay between requests)

### "ModuleNotFoundError: No module named 'praw'"

**Problem:** Dependencies not installed

**Solution:**
```bash
pip install -r requirements.txt
```

## Next Steps

- Read the full [README.md](README.md) for advanced features
- Check [example_usage.py](example_usage.py) for programmatic usage
- Explore the [tests/](tests/) directory to understand the codebase
- Experiment with different LLM models (see README for options)

## Tips for Best Results

1. **Start small**: Process 5-10 posts first to test
2. **Use checkpoints**: For any task >20 posts
3. **Save skillbooks**: Reuse learned knowledge across runs
4. **Adjust thresholds**: Based on subreddit size (small subs need lower thresholds)
5. **Try different models**: `gpt-4o-mini` is fast and cheap, `gpt-4o` is higher quality

## Getting Help

- Check the [README.md](README.md) for detailed documentation
- Review [example_usage.py](example_usage.py) for API usage
- Run with `--help` flag: `python summarize_subreddit.py --help`

Happy summarizing! 🚀
