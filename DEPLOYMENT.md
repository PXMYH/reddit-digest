# Reddit Digest Generator - Deployment Guide

Complete guide for packaging and deploying the Reddit Digest Generator as a standalone executable.

## Overview

This deployment method creates a single executable file that:
- ✅ Bundles Python + all dependencies (no installation needed)
- ✅ Runs on your local machine (uses working IP, no Reddit blocking)
- ✅ Executes every 4 hours via cron/scheduler
- ✅ Auto-commits results to GitHub
- ✅ ~80-150MB file size (includes Python interpreter)

## Prerequisites

### Required
- macOS, Linux, or Windows
- UV package manager installed: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Git configured with push access to repository
- OpenRouter API key (for LLM summarization)

### Optional
- UPX (for executable compression): `brew install upx` (macOS)

## Quick Start

### 1. Build the Executable

```bash
cd examples/claude-code-loop/workspace

# Build executable (takes 2-5 minutes)
./build_executable.sh
```

This will:
1. Install dependencies with UV
2. Install PyInstaller
3. Bundle everything into `dist/reddit-digest`
4. Test the executable

### 2. Test the Executable

```bash
# Quick test with stocks subreddit
./dist/reddit-digest stocks \
  --start 2025-12-01 \
  --end 2025-12-07 \
  --min-upvotes 10 \
  --min-comments 10 \
  --max-posts 5
```

Expected output:
- Fetches posts from r/stocks
- Generates AI summaries
- Saves to `digest/stocks_digest_2025-12-01_to_2025-12-07.md`

### 3. Set Up Scheduled Execution

#### Option A: Cron (macOS/Linux) - Recommended

```bash
# Edit crontab
crontab -e

# Add this line (runs every 4 hours at :00 minutes):
0 */4 * * * /path/to/workspace/run_digest_scheduler.sh >> /path/to/logs/scheduler.log 2>&1
```

**Important:** Replace `/path/to/workspace` with your actual workspace path.

To get the full path:
```bash
cd examples/claude-code-loop/workspace
pwd  # Copy this path
```

#### Option B: Manual Execution

```bash
# Run all 5 subreddits once
./run_digest_scheduler.sh
```

#### Option C: macOS launchd (Alternative to cron)

Create `~/Library/LaunchAgents/com.reddit.digest.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.reddit.digest</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/workspace/run_digest_scheduler.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>14400</integer>  <!-- 4 hours in seconds -->
    <key>StandardOutPath</key>
    <string>/path/to/logs/digest.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/logs/digest_error.log</string>
</dict>
</plist>
```

Load the job:
```bash
launchctl load ~/Library/LaunchAgents/com.reddit.digest.plist
```

## Configuration

### Environment Variables

Create `.env` file in workspace directory:

```bash
# Required: OpenRouter API key for LLM summarization
OPENROUTER_API_KEY=your-api-key-here

# Optional: Change LLM model
# MODEL=openrouter/mistralai/devstral-2512:free  # Default (free)
# MODEL=openrouter/anthropic/claude-3-haiku  # Alternative
```

### Subreddit Configuration

Edit `run_digest_scheduler.sh` to customize subreddits:

```bash
# Line 13-19
SUBREDDITS=(
    "formula1"
    "LocalLLaMA"
    "Fire"
    "financialindependence"
    "Bogleheads"
    # Add more here...
)
```

### Filter Thresholds

Edit `run_digest_scheduler.sh` to change post filters:

```bash
# Line 21-22
MIN_UPVOTES=100  # Minimum post score
MIN_COMMENTS=20  # Minimum comment count
```

### Date Range

The scheduler automatically uses a **rolling 7-day window**. To change:

Edit `run_digest_scheduler.sh` line 56-62:

```bash
# For 14-day window:
START_DATE=$(date -v-14d +%Y-%m-%d)  # macOS
START_DATE=$(date -d '14 days ago' +%Y-%m-%d)  # Linux
```

## File Structure

```
workspace/
├── dist/
│   └── reddit-digest         # 80-150MB executable
├── digest/                    # Generated digests (auto-created)
├── logs/                      # Execution logs (auto-created)
├── reddit_digest.spec         # PyInstaller configuration
├── build_executable.sh        # Build script
├── run_digest_scheduler.sh    # Scheduler wrapper
├── .env                       # API keys (create this)
└── DEPLOYMENT.md             # This file
```

## Maintenance

### Rebuild After Code Changes

```bash
# Pull latest changes
git pull

# Rebuild executable
./build_executable.sh

# Test
./dist/reddit-digest --help
```

### Update Dependencies

```bash
# Update pyproject.toml dependencies
uv sync

# Rebuild
./build_executable.sh
```

### View Logs

```bash
# Today's log
cat logs/digest_$(date +%Y-%m-%d).log

# Recent logs
ls -lt logs/

# Follow live execution
tail -f logs/digest_$(date +%Y-%m-%d).log
```

### Verify Cron is Running

```bash
# List active cron jobs
crontab -l

# Check cron service (macOS)
launchctl list | grep cron

# Check cron service (Linux)
systemctl status cron
```

## Troubleshooting

### Build Errors

**Problem:** `pyinstaller: command not found`

**Solution:**
```bash
uv pip install pyinstaller
```

**Problem:** `ModuleNotFoundError` when running executable

**Solution:** Add missing module to `reddit_digest.spec` hiddenimports:
```python
hiddenimports=[
    'ace',
    'your_missing_module',  # Add here
    ...
]
```

Rebuild:
```bash
./build_executable.sh
```

### Runtime Errors

**Problem:** `OPENROUTER_API_KEY not found`

**Solution:** Create `.env` file with your API key:
```bash
echo "OPENROUTER_API_KEY=your-key" > .env
```

**Problem:** `Subreddit r/xyz is private, banned, or quarantined`

**Solution:** Reddit may be blocking your IP. This shouldn't happen with residential IPs, but if it does:
1. Check subreddit name spelling
2. Try with a different subreddit
3. Wait a few minutes and retry (rate limiting)

**Problem:** Git push fails

**Solution:**
```bash
# Check git credentials
git config --get user.name
git config --get user.email

# Ensure push access
git remote -v

# Test manual push
cd workspace
git add digest/
git commit -m "test"
git push
```

### Cron Not Running

**Problem:** Cron job doesn't execute

**Solution:**
```bash
# Check cron logs (macOS)
log show --predicate 'process == "cron"' --last 1h

# Check cron logs (Linux)
grep CRON /var/log/syslog

# Test script manually
/path/to/workspace/run_digest_scheduler.sh

# Verify PATH in cron
crontab -e
# Add at top:
PATH=/usr/local/bin:/usr/bin:/bin
```

## Performance

### Build Time
- First build: 2-5 minutes
- Subsequent builds: 1-3 minutes

### Execution Time (per subreddit)
- Fetching posts: 5-30 seconds
- AI summarization: 1-3 minutes (depends on post count)
- Total per run (5 subreddits): 5-15 minutes

### Disk Usage
- Executable: 80-150MB
- Digests: ~10-50KB per file
- Logs: ~5-10KB per run

## Security Considerations

1. **API Keys**: Never commit `.env` file to git
2. **Executable**: Don't share the built executable (contains embedded code)
3. **Git Access**: Ensure GitHub token/SSH key has minimal required permissions
4. **Logs**: Logs may contain API endpoints - don't expose publicly

## Alternative Deployment: Docker (Optional)

If you prefer containerization:

```dockerfile
# Dockerfile (create this)
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
CMD ["uv", "run", "python", "summarize_subreddit.py"]
```

Build and run:
```bash
docker build -t reddit-digest .
docker run -e OPENROUTER_API_KEY=your-key reddit-digest stocks --start 2025-12-01 --end 2025-12-07
```

## Support

If you encounter issues:

1. Check logs in `logs/` directory
2. Test executable manually: `./dist/reddit-digest --help`
3. Verify environment: `cat .env` (check API key is set)
4. Review GitHub Actions setup (if using): `.github/workflows/reddit-digest.yml`

## Next Steps

After successful deployment:

1. ✅ Monitor first few runs via logs
2. ✅ Verify digests are generated in `digest/` directory
3. ✅ Check GitHub commits are pushed automatically
4. ✅ Adjust subreddit filters if needed
5. ✅ Add more subreddits to track

Enjoy your automated Reddit digests! 📰✨
