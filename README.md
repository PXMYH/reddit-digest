# Reddit Digest

Generate AI-powered reading digests from Reddit subreddits. No Reddit API credentials required.

## Setup

### 1. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 2. Get an API key

1. Visit https://openrouter.ai/keys
2. Create a new API key
3. Create a `.env` file:

```bash
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

## Usage

### Quick digest (no AI summaries)

```bash
uv run python summarize_subreddit.py Python --timeframe week
```

### With AI summaries

```bash
uv run python summarize_subreddit.py Python --timeframe week --summarize
```

### Available timeframes

- `week` - Top posts from the past week
- `month` - Top posts from the past month

### Custom date range

```bash
uv run python summarize_subreddit.py Python --start 2025-01-01 --end 2025-01-07
```

### Common options

```bash
uv run python summarize_subreddit.py Python \
  --timeframe month \
  --summarize \
  --min-upvotes 200 \
  --min-comments 50 \
  --max-posts 25
```

## Output

Digests are saved to the `digest/` folder:
- `Python-week.md` - Weekly digest
- `Python-month.md` - Monthly digest

## Documentation

- [Quick Start](docs/QUICK_START.md) - Common commands and use cases
- [Technical Details](docs/TECHNICAL.md) - Architecture, all CLI options, GitHub Actions examples
- [Developer Guide](CLAUDE.md) - Development commands and guidelines

## Live Demo

View generated digests: https://pxmyh.github.io/reddit-digest/
