# Reddit Summarizer - Quick Start

Get started with Reddit Summarizer in 3 simple steps!

## What It Does

Generates AI-powered reading digests from Reddit subreddits. Uses the ACE framework to self-improve summary quality over time.

## Installation

```bash
# Install dependencies (using uv - recommended)
uv pip install -r requirements.txt
```

## Setup

Create a `.env` file with your API key:

```bash
# Get your key at https://openrouter.ai/keys
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

## Basic Usage

```bash
# Summarize r/python from the last week (5 posts)
uv run python summarize_subreddit.py python \
  --start 2024-12-01 \
  --end 2024-12-10 \
  --max-posts 5

# Or without uv
python summarize_subreddit.py python \
  --start 2024-12-01 \
  --end 2024-12-10 \
  --max-posts 5
```

**Output:**
```
✅ Digest saved to: python_digest_2024-12-01_to_2024-12-10.md
```

## Common Commands

### Weekly digest
```bash
uv run python summarize_subreddit.py MachineLearning \
  --start 2024-12-01 --end 2024-12-07 \
  --min-upvotes 200 --min-comments 50
```

### Daily top 10
```bash
uv run python summarize_subreddit.py technology \
  --start 2024-12-10 --end 2024-12-10 \
  --max-posts 10
```

### Different LLM models
```bash
# Claude 3.5 Sonnet (default - high quality)
--model openrouter/mistralai/devstral-2512:free

# GPT-4o (OpenAI)
--model openrouter/openai/gpt-4o

# Gemini Pro (Google)
--model openrouter/google/gemini-pro
```

See all models: https://openrouter.ai/models

### Export formats
```bash
# Markdown (default)
--output digest.md

# JSON
--output digest.json

# HTML
--output digest.html
```

## Advanced Features

### Checkpoints (resumable processing)
```bash
uv run python summarize_subreddit.py AskReddit \
  --start 2024-01-01 --end 2024-12-31 \
  --max-posts 100 \
  --checkpoint progress.json \
  --checkpoint-interval 10
```

If interrupted, re-run the same command to resume!

### Skillbook (learning from experience)
```bash
# First run - learns
uv run python summarize_subreddit.py python \
  --start 2024-01-01 --end 2024-01-31 \
  --save-skillbook python_skills.json

# Next run - reuses learned skills
uv run python summarize_subreddit.py python \
  --start 2024-02-01 --end 2024-02-28 \
  --skillbook python_skills.json \
  --save-skillbook python_skills.json
```

## Troubleshooting

**"No LLM API key found"**
- Get API key at https://openrouter.ai/keys
- Add to `.env`: `OPENROUTER_API_KEY=sk-or-v1-...`

**"No posts found"**
- Lower thresholds: `--min-upvotes 50 --min-comments 10`
- Try different date range or subreddit

**Rate limiting**
- Built-in delays handle this automatically
- Wait 1-2 minutes if needed

## Options Reference

| Option | Default | Description |
|--------|---------|-------------|
| `--start`, `-s` | Required | Start date (YYYY-MM-DD) |
| `--end`, `-e` | Required | End date (YYYY-MM-DD) |
| `--min-upvotes` | 100 | Minimum upvotes filter |
| `--min-comments` | 30 | Minimum comments filter |
| `--max-posts` | 50 | Max posts to analyze |
| `--model` | claude-3.5-sonnet | LLM model to use |
| `--output`, `-o` | auto | Output file path |
| `--skillbook` | None | Load existing skillbook |
| `--save-skillbook` | None | Save updated skillbook |
| `--checkpoint` | None | Checkpoint file path |
| `--checkpoint-interval` | 5 | Save every N posts |

Run `uv run python summarize_subreddit.py --help` for full options.

## Next Steps

- Check [README.md](README.md) for detailed documentation
- See [example_usage.py](example_usage.py) for programmatic usage
- Browse models at https://openrouter.ai/models
- Explore the ACE framework at https://github.com/kayba-ai/agentic-context-engine

Happy summarizing!
