# Reddit Digest Quick Start Guide

## 🚀 Installation (30 seconds)

```bash
# 1. Clone and navigate
git clone https://github.com/PXMYH/reddit-digest
cd reddit-digest

# 2. Install dependencies
uv pip install -r requirements.txt

# 3. Set up API key (create .env file)
echo "OPENROUTER_API_KEY=sk-or-v1-your-key-here" > .env

# Get your free API key at: https://openrouter.ai/keys
```

**That's it!** No Reddit API credentials needed.

## 📝 Common Commands

### Fast Mode (No AI Summaries)
Perfect for quick overviews and when you just want the post list:

```bash
# Get top posts from past week (~5 seconds)
uv run python summarize_subreddit.py Python --timeframe week

# Get top posts from past month
uv run python summarize_subreddit.py MachineLearning --timeframe month
```

**Output**: `digest/{subreddit}-{timeframe}.md`

### Full Digest Mode (With AI Summaries)
For comprehensive analysis with AI-powered summaries:

```bash
# Top posts from past week WITH summaries (~2-3 minutes)
uv run python summarize_subreddit.py Fire --timeframe week --summarize

# Top posts from past month WITH summaries
uv run python summarize_subreddit.py Python --timeframe month --summarize
```

**Output**: Full digest with summaries, key points, and discussion analysis

### Date Range Mode (Original)
For specific time periods:

```bash
# Get posts from December 14-17, 2025
uv run python summarize_subreddit.py Bogleheads \
  --start 2025-12-14 \
  --end 2025-12-17

# With custom filtering
uv run python summarize_subreddit.py LocalLLaMA \
  --start 2025-12-01 \
  --end 2025-12-17 \
  --min-upvotes 200 \
  --max-posts 30
```

**Output**: `digest/{subreddit}_digest_{start}_to_{end}.md`

## 🎯 Use Cases

### Use Case 1: Daily Quick Scan
```bash
# Fast mode - see what's trending this week
uv run python summarize_subreddit.py Python --timeframe week
uv run python summarize_subreddit.py MachineLearning --timeframe week
```

**Time**: ~10 seconds total
**Output**: Post listings with titles, scores, comments

### Use Case 2: Weekly Deep Dive
```bash
# Full mode - comprehensive analysis of past week
uv run python summarize_subreddit.py Python --timeframe week --summarize
```

**Time**: 2-3 minutes
**Output**: AI summaries, key insights, discussion highlights

### Use Case 3: Custom Research
```bash
# Specific date range with custom filters
uv run python summarize_subreddit.py Bogleheads \
  --start 2025-01-01 \
  --end 2025-12-31 \
  --min-upvotes 500 \
  --min-comments 100 \
  --max-posts 20
```

**Time**: 3-5 minutes
**Output**: Highly curated digest of most impactful posts

## 🔧 Common Options

| Flag | Purpose | Example |
|------|---------|---------|
| `--timeframe` | Quick fetch by time period | `--timeframe week` |
| `--summarize` | Add AI summaries (off by default for timeframe) | `--summarize` |
| `--start` / `--end` | Date range mode | `--start 2025-12-01 --end 2025-12-31` |
| `--min-upvotes` | Filter by minimum upvotes | `--min-upvotes 200` |
| `--min-comments` | Filter by minimum comments | `--min-comments 50` |
| `--max-posts` | Limit number of posts | `--max-posts 30` |
| `--model` | Choose LLM model | `--model openrouter/openai/gpt-4o` |
| `--output` | Custom output file | `--output my_digest.md` |
| `--no-comments` | Skip comment analysis | `--no-comments` |

## 🎨 Output Formats

The tool automatically detects format from file extension:

```bash
# Markdown (default, human-readable)
uv run python summarize_subreddit.py Python --timeframe week --output digest.md

# JSON (programmatic use)
uv run python summarize_subreddit.py Python --timeframe week --output digest.json

# HTML (rich viewing in browser)
uv run python summarize_subreddit.py Python --timeframe week --output digest.html
```

## 📊 View Your Digests

After generating digests, view them in a beautiful web interface:

```bash
# Generate index page from all digests
python generate_index.py

# Open in browser
open docs/index.html
```

The index page includes:
- ✅ Tabbed interface for each subreddit
- ✅ Filter by timeframe (week/month)
- ✅ Click post titles to open on Reddit
- ✅ Auto-generated from digest/ folder

## ⚡ Pro Tips

### Tip 1: Fast Mode First, Then Summarize
```bash
# 1. Quick scan to see what's available (~5 seconds)
uv run python summarize_subreddit.py Fire --timeframe month

# 2. Review the output, then decide if you want summaries
uv run python summarize_subreddit.py Fire --timeframe month --summarize
```

### Tip 2: Use Checkpoints for Large Jobs
```bash
# For long-running summarization (>20 posts)
uv run python summarize_subreddit.py MachineLearning \
  --timeframe month \
  --summarize \
  --checkpoint progress.json \
  --checkpoint-interval 10

# If interrupted, just re-run the same command - it resumes!
```

### Tip 3: Save Your Skillbook
```bash
# The ACE framework learns as it processes posts
uv run python summarize_subreddit.py Python \
  --timeframe month \
  --summarize \
  --save-skillbook learned_skills.json

# Reuse learned skills on next run
uv run python summarize_subreddit.py Python \
  --timeframe week \
  --summarize \
  --skillbook learned_skills.json
```

### Tip 4: Batch Processing
```bash
# Process multiple subreddits in one go
for sub in Fire Python Bogleheads LocalLLaMA; do
  uv run python summarize_subreddit.py "$sub" --timeframe week
done

# Then generate the index
python generate_index.py
```

## 🤖 GitHub Actions Automation

### Quick Setup (5 minutes)

1. **Add API key to repository secrets**:
   - Go to Settings → Secrets → Actions
   - Add `OPENROUTER_API_KEY` with your key

2. **Create workflow file** (e.g., `.github/workflows/weekly-digest.yml`):

```yaml
name: Weekly Top Posts

on:
  schedule:
    - cron: '0 12 * * 0'  # Every Sunday at noon
  workflow_dispatch:      # Manual trigger

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install uv
          uv pip install -r requirements.txt

      - name: Generate weekly digests
        run: |
          uv run python summarize_subreddit.py Fire --timeframe week
          uv run python summarize_subreddit.py Python --timeframe week

      - name: Generate index
        run: python generate_index.py

      - name: Commit
        run: |
          git config user.name "GitHub Actions Bot"
          git config user.email "<>"
          git add digest/ docs/
          git commit -m "chore: weekly digest $(date +%Y-%m-%d)" || echo "No changes"
          git push
```

3. **Enable GitHub Actions** in repository settings

**Done!** Digests will generate automatically every week.

## 🐛 Troubleshooting

### "No LLM API key found"
→ Add `OPENROUTER_API_KEY` to your `.env` file
→ Get free key at: https://openrouter.ai/keys

### "No posts found matching criteria"
→ Lower thresholds: `--min-upvotes 50 --min-comments 20`
→ Try a different timeframe
→ Check subreddit name spelling

### Rate limiting (429 errors)
→ Tool includes automatic retry logic
→ Wait a minute, it will resume automatically
→ Reddit's public API is fairly permissive

### "Module not found"
→ Run: `uv pip install -r requirements.txt`

## 📚 More Resources

- **Full Documentation**: See [README.md](README.md)
- **Developer Guide**: See [CLAUDE.md](CLAUDE.md)
- **Migration Guide**: See [MIGRATION.md](MIGRATION.md)
- **Available Models**: https://openrouter.ai/models

## 🎓 Learning Path

1. **Start simple**: `--timeframe week` (fast mode)
2. **Try summaries**: `--timeframe week --summarize`
3. **Explore date ranges**: `--start YYYY-MM-DD --end YYYY-MM-DD`
4. **Customize filters**: `--min-upvotes`, `--max-posts`
5. **Advanced features**: `--checkpoint`, `--skillbook`
6. **Automate**: GitHub Actions workflows

---

**Quick Reference Card**

```
┌─────────────────────────────────────────────────────────────┐
│                    Reddit Digest Cheat Sheet                │
├─────────────────────────────────────────────────────────────┤
│ Fast mode:        --timeframe week                          │
│ With summaries:   --timeframe week --summarize              │
│ Date range:       --start 2025-12-01 --end 2025-12-31      │
│ Custom filters:   --min-upvotes 200 --max-posts 30         │
│ Checkpoint:       --checkpoint progress.json                │
│ View digests:     python generate_index.py                  │
│ Help:             uv run python summarize_subreddit.py --help│
└─────────────────────────────────────────────────────────────┘
```

**Time Estimates**

| Command | Time | Output |
|---------|------|--------|
| `--timeframe week` | ~5s | Post list |
| `--timeframe week --summarize` | ~2-3min | Full digest |
| `--timeframe month` | ~10s | Post list |
| `--timeframe month --summarize` | ~3-5min | Full digest |
| Date range (7 days) | ~3-5min | Full digest |
