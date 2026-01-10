# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important: Always Use UV

**ALWAYS use `uv` to run ANY Python command in this project.** Never use `python` or `python3` directly, even for standard library modules like `http.server`.

```bash
# Correct
uv run python generate_index.py
uv run pytest
uv run python -m http.server 8888

# Incorrect - DO NOT use
python generate_index.py
python3 generate_index.py
python3 -m http.server 8888
```

## Repository Overview

This is a Reddit Subreddit Digest Generator that uses the ACE (Agentic Context Engineering) framework for self-improving AI summarization. The tool fetches posts from Reddit's public JSON API (no authentication required) and generates AI-powered reading digests using 100+ LLM models via OpenRouter or direct provider APIs.

## Development Commands

### Running the Tool Locally

```bash
# Date range mode (original behavior - with AI summaries)
uv run python summarize_subreddit.py LocalLLaMA --start 2025-12-10 --end 2025-12-17

# Timeframe mode (NEW - fast, no summaries by default)
uv run python summarize_subreddit.py Fire --timeframe week

# Timeframe mode with summaries (NEW)
uv run python summarize_subreddit.py Fire --timeframe week --summarize

# Timeframe options: week, month
uv run python summarize_subreddit.py Python --timeframe month --summarize

# With all options (date range mode)
uv run python summarize_subreddit.py python \
  --start 2024-12-01 --end 2024-12-10 \
  --min-upvotes 200 --min-comments 50 \
  --max-posts 25 \
  --model openrouter/openai/gpt-4o \
  --output my_digest.md \
  --save-skillbook skillbook.json \
  --checkpoint progress.json \
  --checkpoint-interval 10
```

### Building the Executable

```bash
# Build with helper script (recommended)
./scripts/build_executable.sh

# Or manually with PyInstaller
uv run pyinstaller --clean reddit_digest.spec

# Test the built executable
./dist/reddit-digest --help
./dist/reddit-digest test --start 2025-12-15 --end 2025-12-17 --max-posts 1 --no-comments
```

### Running Tests

```bash
# Run all tests with UV (recommended)
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_models.py
uv run pytest tests/test_fetcher.py
uv run pytest tests/test_summarizer.py

# Run with coverage
uv run pytest --cov=reddit_summarizer

# Without UV
pytest
python test_basic.py
```

### Code Quality

```bash
# Format code with Black
uv run black reddit_summarizer/ tests/ *.py

# Type checking
uv run mypy reddit_summarizer/

# Linting
uv run pylint reddit_summarizer/
```

We follow Google Python Style Guide: https://google.github.io/styleguide/pyguide.html

## Architecture

### Dual-Mode CLI

The tool supports two mutually exclusive modes for fetching posts:

**1. Date Range Mode** (`--start` + `--end`):
- Fetches posts within a specific date range
- Uses `/r/{subreddit}/new.json` endpoint
- Filters posts locally by date
- **Default behavior:** Generates AI summaries (can disable with `--no-summarize`)
- **Use case:** Historical analysis, specific date ranges

**2. Timeframe Mode** (`--timeframe`):
- Fetches top posts from a specific timeframe (week/month)
- Uses `/r/{subreddit}/top.json?t={timeframe}` endpoint
- Reddit handles timeframe filtering server-side
- **Default behavior:** No AI summaries (fast mode, can enable with `--summarize`)
- **Use case:** Quick overviews, periodic digests, GitHub Actions workflows

**Summarization Control:**
- `--summarize` / `--no-summarize` flag explicitly controls AI summary generation
- If not specified, defaults to:
  - `True` for date range mode (comprehensive analysis)
  - `False` for timeframe mode (fast data fetching)

### High-Level Data Flow

```
Reddit Public API → RedditFetcher → Filter by thresholds
                                           ↓
                         [RedditPost objects with created_utc]
                                           ↓
                         Sort by date (newest first) ← IMPORTANT
                                           ↓
                    RedditSummarizer (ACE-powered)
                    ├── LiteLLMClient (100+ models)
                    ├── Skillbook (learned strategies)
                    ├── Agent (generates summaries)
                    ├── Reflector (analyzes quality)
                    └── SkillManager (updates skillbook)
                                           ↓
                            [PostSummary objects]
                                           ↓
                             SubredditDigest
                                           ↓
                      Export (Markdown/JSON/HTML)
```

### Package Structure

```
workspace/
├── reddit_summarizer/           # Main package
│   ├── __init__.py              # Package exports with graceful fallbacks
│   ├── models.py                # Data models (RedditPost, PostSummary, SubredditDigest)
│   ├── fetcher.py               # Reddit API integration (PUBLIC API - no auth)
│   └── summarizer.py            # ACE-powered summarization engine
├── summarize_subreddit.py       # CLI entry point (Click-based)
├── reddit_digest.spec           # PyInstaller configuration
├── requirements.txt             # Python dependencies
├── .github/workflows/           # GitHub Actions CI/CD
│   ├── build-release.yml        # Build executables on tag push
│   └── reddit-digest.yml        # Scheduled digest generation (every 4 hours)
├── tests/                       # Comprehensive test suite (35+ tests)
│   ├── conftest.py              # Pytest fixtures
│   ├── test_models.py           # Data model tests
│   ├── test_fetcher.py          # Reddit API tests (mocked)
│   └── test_summarizer.py       # Summarizer tests
├── scripts/                     # Build and deployment scripts
│   ├── build_executable.sh      # PyInstaller build helper
│   └── run_digest_scheduler.sh  # Cron/scheduler wrapper
└── digest/                      # Generated markdown digests (git-tracked)
```

### Critical Implementation Details

#### 1. Date-Based Sorting (IMPORTANT)
**Location:** `reddit_summarizer/fetcher.py:234-235`

Posts are sorted by `created_utc` (newest first), NOT by upvotes. This ensures digests show the latest content first regardless of popularity.

```python
# Sort by creation date descending (newest first)
posts.sort(key=lambda p: p.created_utc, reverse=True)
```

**DO NOT change this back to score-based sorting** unless explicitly requested. This was an intentional design decision to prioritize recency over popularity.

#### 2. ACE Framework Integration
**Location:** `reddit_summarizer/summarizer.py:26-50`

The tool uses three ACE roles that share the same LLM instance:
- **Agent**: Produces summaries using learned strategies from the skillbook
- **Reflector**: Analyzes performance (for future self-improvement)
- **SkillManager**: Updates the skillbook with new strategies

**Key insight:** The ACE framework enables the tool to learn and improve summary quality over time. Skillbooks can be saved and reloaded to preserve learned improvements.

#### 3. PyInstaller Data Bundling (CRITICAL)
**Location:** `reddit_digest.spec:22-32`

LiteLLM requires specific data files to be bundled in the executable:

```python
datas=[
    ('reddit_summarizer', 'reddit_summarizer'),
    (f'{workspace_dir}/.venv/lib/python3.12/site-packages/tiktoken_ext', 'tiktoken_ext'),
    # CRITICAL: LiteLLM JSON configs must be included
    (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/*.json', 'litellm'),
    (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers', 'litellm/litellm_core_utils/tokenizers'),
    (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/containers', 'litellm/containers'),
    (f'{workspace_dir}/.venv/lib/python3.12/site-packages/litellm/llms/openai_like/*.json', 'litellm/llms/openai_like'),
],
```

**Warning:** Missing these data files will cause `FileNotFoundError: endpoints.json` at runtime. Always rebuild the executable after updating LiteLLM versions.

#### 4. GitHub Actions Workflow Chaining
**Location:** `.github/workflows/reddit-digest.yml:8-19`

The digest workflow automatically triggers after successful builds:

```yaml
workflow_run:
  workflows: ["Build and Release Reddit Digest"]
  types: [completed]
  branches: [main]

# Only runs if upstream build succeeded
if: ${{ github.event_name != 'workflow_run' || github.event.workflow_run.conclusion == 'success' }}
```

**Behavior:**
- On tag push (e.g., `v1.0.3`) → build-release.yml runs → reddit-digest.yml auto-triggers
- Scheduled runs (every 4 hours) continue independently
- Manual triggers work from GitHub UI

### API Integration Patterns

#### Reddit Public JSON API
**No authentication required!** The tool uses Reddit's public endpoints:

```python
url = f"https://www.reddit.com/r/{subreddit_name}/new.json"
```

**Robustness features:**
- Explicit timeouts (10s default) - prevents hanging requests
- Rate limiting delays (2s between calls) - respects API limits
- Pagination limits (100 items max) - prevents infinite loops
- Exponential backoff retry - handles transient errors

#### LLM Provider Integration
Uses LiteLLMClient for unified access to 100+ models:

```python
from ace.llm_providers.litellm_client import LiteLLMClient

# Works with OpenRouter, OpenAI, Anthropic, Google, etc.
llm = LiteLLMClient(model="openrouter/mistralai/devstral-2512:free")
```

**Supported patterns:**
- OpenRouter: `openrouter/provider/model` (recommended - no extra config)
- Direct OpenAI: `gpt-4o-mini` (requires OPENAI_API_KEY)
- Direct Anthropic: `claude-3-5-sonnet` (requires ANTHROPIC_API_KEY)
- Local models: `ollama/llama3` (requires Ollama running)

## Environment Configuration

Create `.env` file in workspace directory:

```bash
# OpenRouter API Key (RECOMMENDED - access to 100+ models)
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Alternative: Use OpenAI directly
# OPENAI_API_KEY=sk-your-openai-key

# Alternative: Use Anthropic directly
# ANTHROPIC_API_KEY=sk-ant-your-key

# NOTE: Reddit API credentials are NO LONGER REQUIRED!
```

## Common Workflows

### Adding a New LLM Model
1. Find model ID at https://openrouter.ai/models
2. Use via CLI: `--model openrouter/provider/model-name`
3. Or update default in `summarize_subreddit.py:67`

### Modifying Post Sorting Logic
**Location:** `reddit_summarizer/fetcher.py:234-235`

Current: Sorts by `created_utc` (newest first)

To change sorting criteria:
```python
posts.sort(key=lambda p: p.FIELD_NAME, reverse=True)
# FIELD_NAME options: created_utc, score, num_comments
```

### Adding New Export Formats
**Location:** `reddit_summarizer/models.py:SubredditDigest`

Add new method to SubredditDigest class:
```python
def to_new_format(self) -> str:
    # Implementation here
    pass
```

Then update `save_to_file()` to detect new file extension.

### Updating GitHub Actions Workflows
**Trigger chain:** Tag push → Build → Auto-deploy

To modify the chain:
1. **build-release.yml**: Builds executables for Linux + macOS
2. **reddit-digest.yml**: Downloads executable, generates digests, commits to repo

**DO NOT modify** the `workflow_run` trigger unless you want to break automatic deployment after builds.

## Testing Guidelines

### Unit Tests
- **models.py**: Test data model serialization, validation, format conversion
- **fetcher.py**: Mock Reddit API responses, test filtering/pagination
- **summarizer.py**: Mock LLM responses, test ACE integration

### Integration Tests
Run with actual API calls (requires API key):
```bash
OPENROUTER_API_KEY=your-key uv run pytest tests/test_integration.py -v
```

### Manual Testing Checklist
Before releasing:
1. ✅ Build executable: `./scripts/build_executable.sh`
2. ✅ Test help: `./dist/reddit-digest --help`
3. ✅ Test execution: `./dist/reddit-digest test --start 2025-12-15 --end 2025-12-17 --max-posts 1 --no-comments`
4. ✅ Verify no LiteLLM errors (especially `endpoints.json` error)
5. ✅ Check digest output in `digest/` directory
6. ✅ Verify newest posts appear first in digest

## Deployment

### Local Development
Use `uv run python summarize_subreddit.py` for fast iteration with hot reloading.

### Production (GitHub Actions)
1. **Tag a release:** `git tag v1.0.3 && git push origin v1.0.3`
2. **build-release.yml** creates executables for Linux + macOS
3. **reddit-digest.yml** automatically triggers, downloads executable, generates digests
4. Results committed to `digest/` directory and GitHub Pages

### Self-Hosted Runner
The digest workflow runs on `[self-hosted, mac-mini]` runner.

**Requirements:**
- macOS machine with GitHub Actions runner installed
- OpenRouter API key configured as repository secret
- Git push access to repository

## Troubleshooting

### "FileNotFoundError: endpoints.json"
**Root cause:** LiteLLM data files not bundled in PyInstaller executable

**Solution:** Rebuild executable with updated `reddit_digest.spec`:
```bash
uv run pyinstaller --clean reddit_digest.spec
```

Verify lines 28-31 in spec file include LiteLLM JSON files.

### "No posts found matching criteria"
**Root cause:** Thresholds too high or date range invalid

**Solution:** Lower thresholds or expand date range:
```bash
--min-upvotes 10 --min-comments 5
```

### Workflow Chain Not Triggering
**Root cause:** `workflow_run` trigger misconfigured

**Solution:** Verify in `reddit-digest.yml`:
- Workflow name matches `build-release.yml` exactly: `"Build and Release Reddit Digest"`
- Branch filter includes the branch where tags are pushed: `branches: [main]`

### Posts Not Sorted by Date
**Root cause:** Sorting logic reverted to score-based

**Solution:** Check `reddit_summarizer/fetcher.py:234-235` ensures:
```python
posts.sort(key=lambda p: p.created_utc, reverse=True)
```
