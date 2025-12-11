# Reddit Subreddit Summarizer with ACE Framework

An AI-powered tool that generates reading digests from Reddit subreddits using the **ACE (Agentic Context Engineering)** framework for self-improving summarization.

## Features

- 🎯 **Smart Filtering**: Automatically identifies important posts (>100 upvotes, >30 comments)
- 🤖 **AI Summarization**: Uses GPT-4 or other LLMs to generate concise summaries
- 📈 **Self-Improving**: Leverages ACE framework to improve summary quality over time
- 💬 **Discussion Analysis**: Includes analysis of top comments and community consensus
- 📝 **Markdown Output**: Clean, formatted reading digests
- 🔄 **Flexible Date Ranges**: Fetch posts from any time period

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Reddit API Credentials

1. Go to https://www.reddit.com/prefs/apps
2. Click "create another app..."
3. Select "script" as the app type
4. Copy your `client_id` and `client_secret`

### 3. Configure Environment Variables

Create a `.env` file in the workspace directory:

```bash
# Reddit API Credentials (required)
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=RedditSummarizer/0.1.0

# OpenAI API Key (required for summarization)
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Basic Usage

```bash
python summarize_subreddit.py MachineLearning --start 2024-01-01 --end 2024-01-31
```

### Advanced Options

```bash
python summarize_subreddit.py python \
  --start 2024-12-01 \
  --end 2024-12-10 \
  --min-upvotes 200 \
  --min-comments 50 \
  --max-posts 25 \
  --model gpt-4o-mini \
  --output my_digest.md \
  --save-skillbook skillbook.json
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
| `--model` | LLM model to use | gpt-4o-mini |
| `--output`, `-o` | Output file path | auto-generated |
| `--skillbook` | Load existing skillbook | None |
| `--save-skillbook` | Save updated skillbook | None |
| `--no-comments` | Skip comment analysis | False |

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

1. **Reddit Fetcher** (`fetcher.py`): Uses PRAW to fetch posts matching criteria
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

## Supported LLM Models

The tool supports any model compatible with LiteLLM:

- OpenAI: `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`
- Anthropic: `claude-3-5-sonnet`, `claude-3-opus`
- Google: `gemini-pro`, `gemini-1.5-pro`
- Local models via Ollama: `ollama/llama3`, `ollama/mistral`

## Tips for Best Results

1. **Start with smaller date ranges** to avoid rate limits
2. **Save your skillbook** to reuse learned improvements
3. **Adjust thresholds** based on subreddit size (smaller subs may need lower thresholds)
4. **Use GPT-4 models** for higher quality summaries (but slower/more expensive)
5. **Enable comment analysis** for richer discussion insights

## Troubleshooting

### "Reddit API credentials not found"
- Make sure your `.env` file exists and contains valid credentials
- Check that environment variables are properly set

### "No posts found matching criteria"
- Try lowering `--min-upvotes` and `--min-comments` thresholds
- Verify the date range contains posts in that subreddit
- Check that the subreddit name is spelled correctly

### Rate Limiting
- Reddit API has rate limits (60 requests/minute)
- Reduce `--max-posts` if you hit limits
- Add delays between runs

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

```bash
python -m pytest tests/
```

### Code Quality

```bash
# Format code
black reddit_summarizer/ summarize_subreddit.py

# Type checking
mypy reddit_summarizer/
```

## License

This project uses the ACE framework and is intended for educational and research purposes.

## Credits

- **ACE Framework**: Agentic Context Engineering for self-improving AI
- **PRAW**: Python Reddit API Wrapper
- **LiteLLM**: Universal LLM API interface
