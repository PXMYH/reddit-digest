# Reddit Subreddit Summarizer with ACE Framework

An AI-powered tool that generates reading digests from Reddit subreddits using the **ACE (Agentic Context Engineering)** framework for self-improving summarization.

## Features

- 🚫 **No Authentication Required**: Uses Reddit's public JSON API - no API credentials needed!
- 🌐 **100+ LLM Models**: Access OpenAI, Anthropic, Google, Meta, and more via OpenRouter
- 🎯 **Smart Filtering**: Automatically identifies important posts (>100 upvotes, >30 comments)
- 🤖 **AI Summarization**: Uses Claude, GPT-4, Gemini, or other LLMs for concise summaries
- 📈 **Self-Improving**: Leverages ACE framework to improve summary quality over time
- 💬 **Discussion Analysis**: Includes analysis of top comments and community consensus
- 📝 **Multiple Output Formats**: Export as Markdown, JSON, or styled HTML
- 🔄 **Flexible Date Ranges**: Fetch posts from any time period
- 📊 **Progress Indicators**: Real-time progress bars with tqdm for better user experience
- 💾 **Checkpoint Support**: Resumable processing for long-running tasks
- ⏱️ **Smart Rate Limiting**: Respects Reddit's public API limits
- 🔄 **Automatic Retry**: Exponential backoff for transient API errors
- 🔒 **Timeout Protection**: Prevents hanging requests with configurable timeouts
- ✅ **Comprehensive Tests**: 35+ passing tests with pytest
- 🔐 **Type Safety**: Complete type hints for better IDE support and error prevention
- 🎨 **Code Quality**: Formatted with Black, validated with proper error handling

## Installation

### 1. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 2. Get OpenRouter API Key

1. Visit https://openrouter.ai/keys
2. Sign up or log in
3. Create a new API key
4. Copy the key (starts with `sk-or-...`)

### 3. Configure Environment Variable

Create a `.env` file in the workspace directory:

```bash
# OpenRouter API Key (RECOMMENDED - access to 100+ models)
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Alternative: Use OpenAI directly (if you prefer)
# OPENAI_API_KEY=sk-your-openai-key

# NOTE: Reddit API credentials are NO LONGER REQUIRED!
# The tool now uses Reddit's public JSON API.
```

**That's it!** No Reddit API setup needed.

## Usage

### Basic Usage

```bash
# Using uv (recommended)
uv run python summarize_subreddit.py MachineLearning --start 2024-01-01 --end 2024-01-31

# Or directly with python
python summarize_subreddit.py MachineLearning --start 2024-01-01 --end 2024-01-31
```

### Advanced Options

```bash
uv run python summarize_subreddit.py python \
  --start 2024-12-01 \
  --end 2024-12-10 \
  --min-upvotes 200 \
  --min-comments 50 \
  --max-posts 25 \
  --model openrouter/openai/gpt-4o \
  --output my_digest.md \
  --save-skillbook skillbook.json \
  --checkpoint progress.json \
  --checkpoint-interval 10
```

### Using Different LLM Models

With OpenRouter, you have access to 100+ models:

```bash
# Claude 3.5 Sonnet (default - high quality)
uv run python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/mistralai/devstral-2512:free

# GPT-4o (OpenAI's latest)
uv run python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/openai/gpt-4o

# Gemini Pro (Google's model)
uv run python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/google/gemini-pro

# Llama 3.1 70B (Meta's open model)
uv run python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --model openrouter/meta-llama/llama-3.1-70b-instruct
```

See all available models at: https://openrouter.ai/models

### Export Formats

The tool supports **Markdown**, **JSON**, and **HTML** export formats:

```bash
# Export as Markdown (default)
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --output digest.md

# Export as JSON for programmatic use
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --output digest.json

# Export as styled HTML for rich viewing in browser
python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --output digest.html
```

The format is automatically detected based on the file extension (.md, .json, or .html).

### Resumable Processing with Checkpoints

For long-running summarization tasks, use checkpoints to save progress:

```bash
# Start with checkpoint
python summarize_subreddit.py MachineLearning \
  --start 2024-01-01 --end 2024-12-31 \
  --checkpoint ml_progress.json \
  --checkpoint-interval 5

# If interrupted, simply re-run the same command
# It will automatically resume from the last checkpoint!
python summarize_subreddit.py MachineLearning \
  --start 2024-01-01 --end 2024-12-31 \
  --checkpoint ml_progress.json
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `SUBREDDIT` | Name of subreddit (without r/) | Required |
| `--start`, `-s` | Start date (YYYY-MM-DD) | Required |
| `--end`, `-e` | End date (YYYY-MM-DD) | Required |
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

## Example Output

The tool generates a markdown file with:

```markdown
# r/MachineLearning Reading Digest

**Period:** 2024-01-01 to 2024-01-31
**Posts Summarized:** 15
**Total Posts Analyzed:** 15

---

## 1. [Post Title](https://reddit.com/r/MachineLearning/...)

**Author:** u/username | **Upvotes:** 450 | **Comments:** 89 | **Date:** 2024-01-15

**Summary:** Brief 2-3 sentence summary of the post content...

**Key Points:**
- First key insight from the post
- Second important point
- Third notable discussion topic

**Discussion Highlights:** Community consensus or notable debate points...

---
```

## How It Works

### Architecture

1. **Reddit Fetcher** (`fetcher.py`): Uses Reddit's **public JSON API** (no authentication required)
2. **Data Models** (`models.py`): Structured data for posts, summaries, and digests
3. **ACE Summarizer** (`summarizer.py`): AI-powered summarization with learning
4. **CLI Interface** (`summarize_subreddit.py`): User-friendly command-line tool

### ACE Framework Integration

The tool uses three ACE components:

- **Agent**: Generates summaries using learned skills
- **Reflector**: Analyzes summary quality (for future improvements)
- **SkillManager**: Updates the skillbook to improve over time
- **Skillbook**: Stores learned strategies for better summarization

As you use the tool more, it learns what makes a good summary and improves its output quality.

### Direct Provider APIs (Alternative)

If you prefer to use provider APIs directly:
- Set `OPENAI_API_KEY` and use models like `gpt-4o-mini`
- Set `ANTHROPIC_API_KEY` and use models like `claude-3-5-sonnet`
- Local models via Ollama: `ollama/llama3`, `ollama/mistral`

## Tips for Best Results

1. **Start with smaller date ranges** to avoid rate limits
2. **Save your skillbook** to reuse learned improvements
3. **Adjust thresholds** based on subreddit size (smaller subs may need lower thresholds)
4. **Use GPT-4 models** for higher quality summaries (but slower/more expensive)
5. **Enable comment analysis** for richer discussion insights
6. **Use checkpoints** for processing >20 posts to enable resume on interruption
7. **Adjust rate limits** if you have higher API quotas (modify timeout/delay in code)

## Troubleshooting

### "No LLM API key found"
**Solution:**
1. Get your OpenRouter API key at https://openrouter.ai/keys
2. Add `OPENROUTER_API_KEY=sk-or-v1-...` to your `.env` file
3. Alternatively, use `OPENAI_API_KEY` if you prefer OpenAI directly

### "No posts found matching criteria"
**Solution:**
- Try lowering `--min-upvotes` and `--min-comments` thresholds
- Verify the date range contains posts in that subreddit
- Check that the subreddit name is spelled correctly

### Rate Limiting (429 errors)
**Solution:**
- Reddit's public API is fairly permissive
- The tool includes automatic rate limiting and retry logic
- Wait a minute and it will resume automatically
- For heavy usage, reduce `--max-posts` or add longer delays

### "Module 'requests' not found"
**Solution:**
- Run `uv pip install -r requirements.txt` or `pip install -r requirements.txt`
- Make sure you're using the updated requirements.txt (v2.0)

## Project Structure

```
workspace/
├── reddit_summarizer/       # Main package
│   ├── __init__.py          # Package exports
│   ├── models.py            # Data models
│   ├── fetcher.py           # Reddit API integration
│   └── summarizer.py        # ACE-powered summarizer
├── summarize_subreddit.py   # CLI entry point
├── requirements.txt         # Dependencies
├── .env                     # Configuration (not in git)
└── README.md                # This file
```

## Development

### Running Tests

The project includes comprehensive unit and integration tests:

```bash
# Run all tests (using uv - recommended)
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_models.py

# Run with coverage report
uv run pytest --cov=reddit_summarizer

# Run basic tests (no pytest required)
uv run python test_basic.py

# Or without uv
pytest
python test_basic.py
```

**Test Coverage:**
- ✅ Unit tests for all data models (RedditPost, PostSummary, SubredditDigest)
- ✅ Integration tests for Reddit API fetching (with mocked API)
- ✅ Edge cases and error handling
- ✅ File I/O operations

### Code Quality

The codebase follows Python best practices:

```bash
# Format code with Black (using uv - recommended)
uv run black reddit_summarizer/ tests/ *.py

# Type checking with MyPy
uv run mypy reddit_summarizer/

# Run linter
uv run pylint reddit_summarizer/

# Or without uv
black reddit_summarizer/ tests/ *.py
mypy reddit_summarizer/
pylint reddit_summarizer/
```

**Quality Features:**
- ✅ Comprehensive type hints throughout the codebase
- ✅ Consistent code formatting with Black (line length: 100)
- ✅ Full docstring coverage for all public functions
- ✅ Proper error handling and validation
- ✅ Progress indicators with tqdm for better UX

## License

This project uses the ACE framework and is intended for educational and research purposes.

## Recent Improvements

This tool has been enhanced with learned strategies from the ACE framework's skillbook:

### Applied Strategies
- **[api_patterns-00002]**: Set explicit timeout parameter on HTTP requests (10s default)
- **[api_patterns-00003]**: Implement pagination limits for data collection (100 items max)
- **[api_patterns-00004]**: Add rate limiting delays between API calls (1s default for Reddit)
- **[execution_patterns-00005]**: Create progress checkpoints for multi-step tasks

### Key Enhancements
1. **Timeout Protection**: All Reddit API calls now have explicit timeouts
2. **Rate Limiting**: Automatic delays between requests to respect API limits
3. **Checkpoint System**: Save progress every N posts, auto-resume on interruption
4. **Improved Reliability**: Better error handling and recovery mechanisms
