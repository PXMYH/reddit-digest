# Reddit Digest GitHub Actions Workflow

This workflow automatically generates Reddit digests for specified subreddits every 4 hours using pre-built executables.

## Quick Start

Get your Reddit digests up and running in 3 steps:

1. **Add API Key**: Go to Repository Settings → Secrets → Actions → Add `OPENROUTER_API_KEY` ([get one free](https://openrouter.ai/keys))
2. **Enable Actions**: Settings → Actions → General → Enable "Read and write permissions"
3. **Run Manually**: Actions tab → "Reddit Digest Generator" → "Run workflow"

Done! Digests will be generated every 4 hours and auto-committed to the `digest/` directory.

## Setup Instructions

### 1. Add Repository Secret

You need to add your OpenRouter API key as a GitHub repository secret:

1. Go to your GitHub repository settings
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `OPENROUTER_API_KEY`
5. Value: Your OpenRouter API key (get one at https://openrouter.ai/keys)
6. Click **Add secret**

### 2. Enable GitHub Actions

If this is a new repository, you may need to enable GitHub Actions:

1. Go to **Settings** → **Actions** → **General**
2. Under **Actions permissions**, select **Allow all actions and reusable workflows**
3. Under **Workflow permissions**, select **Read and write permissions**
4. Check **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

### 3. Workflow Details

**File**: `.github/workflows/reddit-digest.yml`

**Schedule**: Runs every 4 hours (cron: `0 */4 * * *`)

**Subreddits monitored**:
- `formula1` (Formula 1 racing)
- `LocalLLaMA` (Local LLM development)
- `Fire` (Financial Independence Retire Early)
- `financialindependence` (Financial Independence)
- `Bogleheads` (Passive investing)

**Filters**:
- Minimum upvotes: 100
- Minimum comments: 20
- Date range: Last 7 days (automatically calculated)

**Output**: Digest files are saved to the `digest/` directory and automatically committed back to the repository.

## Manual Trigger

You can manually trigger the workflow:

1. Go to **Actions** tab in your repository
2. Select **Reddit Digest Generator** workflow
3. Click **Run workflow**
4. Select branch (usually `main`)
5. Click **Run workflow**

## Customization

### Change Schedule

Edit the cron expression in `reddit-digest.yml`:

```yaml
on:
  schedule:
    - cron: '0 */4 * * *'  # Every 4 hours
    # Examples:
    # - cron: '0 */2 * * *'  # Every 2 hours
    # - cron: '0 0 * * *'    # Daily at midnight
    # - cron: '0 */6 * * *'  # Every 6 hours
```

### Add More Subreddits

Add a new step to the workflow:

```yaml
- name: Generate YourSubreddit digest
  env:
    OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
  run: |
    ./reddit-digest YourSubreddit \
      --start ${{ steps.dates.outputs.start_date }} \
      --end ${{ steps.dates.outputs.end_date }} \
      --min-upvotes 100 \
      --min-comments 20
  continue-on-error: true
```

### Change Filters

Modify the `--min-upvotes` and `--min-comments` parameters:

```yaml
--min-upvotes 50   # Lower threshold for smaller subreddits
--min-comments 10  # Lower threshold for less active discussions
```

### Change Date Range

The workflow currently uses a rolling 3-day window. To change this, modify the date calculation step:

```yaml
- name: Calculate date range (last 7 days)
  id: dates
  run: |
    END_DATE=$(date +%Y-%m-%d)
    # macOS: use -v, Linux: use -d '7 days ago'
    START_DATE=$(date -v-7d +%Y-%m-%d)
    echo "start_date=$START_DATE" >> $GITHUB_OUTPUT
    echo "end_date=$END_DATE" >> $GITHUB_OUTPUT
```

## Troubleshooting

### Workflow fails with "API key not found"

- Ensure you've added `OPENROUTER_API_KEY` to repository secrets
- Check the secret name matches exactly (case-sensitive)

### No digests are generated

- Check the Actions tab for error logs
- Verify the date range has posts matching your filter criteria
- Lower the `--min-upvotes` and `--min-comments` thresholds

### Commits not being pushed

- Ensure **Workflow permissions** are set to **Read and write permissions** in repository settings
- Check the Actions tab for permission errors

### Rate limiting issues

- OpenRouter free tier has rate limits
- Consider spacing out subreddit processing or upgrading your plan
- Add `sleep` commands between digest generations if needed

## Workflow Structure

```
1. Checkout repository
2. Download pre-built executable from latest GitHub release
3. Calculate rolling 3-day date range
4. Generate digests for each subreddit (parallel execution)
5. Auto-commit and push results to digest/ directory
```

**Benefits of Pre-built Executable:**
- ✅ **Fast startup** (~10 seconds vs 2-5 minutes)
- ✅ **No dependencies** (standalone binary)
- ✅ **Auto-updates** (always uses latest release)
- ✅ **Simple maintenance** (no workflow changes needed)

Each digest generation step uses `continue-on-error: true` to ensure one failure doesn't stop the entire workflow.

## Viewing Results

Generated digests are saved to the `digest/` directory with filenames like:

```
digest/formula1_digest_2025-12-04_to_2025-12-11.md
digest/LocalLLaMA_digest_2025-12-04_to_2025-12-11.md
digest/Fire_digest_2025-12-04_to_2025-12-11.md
```

Each digest includes:
- Post summaries
- Key points
- Discussion highlights
- Metadata (upvotes, comments, author, date)
