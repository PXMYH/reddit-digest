# Technical Documentation

This document contains technical details for developers and advanced users.

## Architecture

### Components

1. **Reddit Fetcher** (`fetcher.py`): Uses Reddit's public JSON API (no authentication required)
2. **Data Models** (`models.py`): Structured data for posts, summaries, and digests
3. **ACE Summarizer** (`summarizer.py`): AI-powered summarization with learning
4. **CLI Interface** (`summarize_subreddit.py`): Command-line tool

### ACE Framework Integration

The tool uses three ACE components:

- **Agent**: Generates summaries using learned skills
- **Reflector**: Analyzes summary quality (for future improvements)
- **SkillManager**: Updates the skillbook to improve over time
- **Skillbook**: Stores learned strategies for better summarization

As you use the tool more, it learns what makes a good summary and improves its output quality.

## Project Structure

```
reddit-digest/
├── reddit_summarizer/       # Main package
│   ├── __init__.py          # Package exports
│   ├── models.py            # Data models
│   ├── fetcher.py           # Reddit API integration
│   └── summarizer.py        # ACE-powered summarizer
├── summarize_subreddit.py   # CLI entry point
├── generate_index.py        # HTML index generator
├── requirements.txt         # Dependencies
├── digest/                  # Generated digests
├── docs/                    # Documentation
└── .github/workflows/       # GitHub Actions
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `SUBREDDIT` | Name of subreddit (without r/) | Required |
| `--start`, `-s` | Start date (YYYY-MM-DD) | Required with `--end` |
| `--end`, `-e` | End date (YYYY-MM-DD) | Required with `--start` |
| `--timeframe`, `-t` | Timeframe (week/month/year) | Alternative to start/end |
| `--summarize/--no-summarize` | Generate AI summaries | True for date range, False for timeframe |
| `--min-upvotes` | Minimum upvotes threshold | 100 |
| `--min-comments` | Minimum comments threshold | 30 |
| `--max-posts` | Maximum posts to analyze | 50 |
| `--model` | LLM model to use | `openrouter/mistralai/devstral-2512:free` |
| `--output`, `-o` | Output file path | auto-generated |
| `--skillbook` | Load existing skillbook | None |
| `--save-skillbook` | Save updated skillbook | None |
| `--no-comments` | Skip comment analysis | False |
| `--checkpoint` | Checkpoint file for resume | None |
| `--checkpoint-interval` | Save checkpoint every N posts | 5 |

**Note:** Use either `--start/--end` (date range mode) OR `--timeframe` (timeframe mode), not both.

## Using Different LLM Models

With OpenRouter, you have access to 100+ models:

```bash
# Claude (default - high quality)
uv run python summarize_subreddit.py python --timeframe week --summarize \
  --model openrouter/mistralai/devstral-2512:free

# GPT-4o (OpenAI)
uv run python summarize_subreddit.py python --timeframe week --summarize \
  --model openrouter/openai/gpt-4o

# Gemini Pro (Google)
uv run python summarize_subreddit.py python --timeframe week --summarize \
  --model openrouter/google/gemini-pro

# Llama 3.1 70B (Meta)
uv run python summarize_subreddit.py python --timeframe week --summarize \
  --model openrouter/meta-llama/llama-3.1-70b-instruct
```

See all available models at: https://openrouter.ai/models

### Direct Provider APIs (Alternative)

If you prefer to use provider APIs directly:
- Set `OPENAI_API_KEY` and use models like `gpt-4o-mini`
- Set `ANTHROPIC_API_KEY` and use models like `claude-3-5-sonnet`
- Local models via Ollama: `ollama/llama3`, `ollama/mistral`

## Export Formats

The tool supports **Markdown**, **JSON**, and **HTML** export formats:

```bash
# Markdown (default)
uv run python summarize_subreddit.py python --timeframe week --output digest.md

# JSON for programmatic use
uv run python summarize_subreddit.py python --timeframe week --output digest.json

# HTML for browser viewing
uv run python summarize_subreddit.py python --timeframe week --output digest.html
```

Format is auto-detected from file extension.

## Checkpoint Support

For long-running tasks, use checkpoints to save progress:

```bash
# Start with checkpoint
uv run python summarize_subreddit.py MachineLearning \
  --timeframe year --summarize \
  --checkpoint ml_progress.json \
  --checkpoint-interval 5

# If interrupted, re-run the same command to resume
```

## GitHub Actions Integration

### Example: Automated Weekly Digest

```yaml
name: Generate Weekly Digest

on:
  schedule:
    - cron: '0 12 * * 0'  # Every Sunday at noon UTC
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install uv
          uv pip install -r requirements.txt

      - name: Generate digests
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
        run: |
          uv run python summarize_subreddit.py Fire --timeframe week --summarize
          uv run python summarize_subreddit.py Python --timeframe week --summarize

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "<>"
          git add digest/
          git commit -m "Update weekly digests" || echo "No changes"
          git push
```

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_models.py

# Run with coverage
uv run pytest --cov=reddit_summarizer
```

### Code Quality

```bash
# Format code
uv run black reddit_summarizer/ tests/ *.py

# Type checking
uv run mypy reddit_summarizer/

# Linting
uv run pylint reddit_summarizer/
```

## Troubleshooting

### "No LLM API key found"
1. Get your OpenRouter API key at https://openrouter.ai/keys
2. Add `OPENROUTER_API_KEY=sk-or-v1-...` to your `.env` file

### "No posts found matching criteria"
- Lower `--min-upvotes` and `--min-comments` thresholds
- Verify the subreddit name is correct
- Check date range contains posts

### Rate Limiting (429 errors)
- The tool includes automatic rate limiting and retry logic
- Wait a minute and it will resume automatically
- Reduce `--max-posts` for heavy usage

## Applied ACE Strategies

- **[api_patterns-00002]**: Explicit timeout on HTTP requests (10s default)
- **[api_patterns-00003]**: Pagination limits for data collection (100 items max)
- **[api_patterns-00004]**: Rate limiting delays between API calls
- **[execution_patterns-00005]**: Progress checkpoints for multi-step tasks
