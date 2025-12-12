# GitHub Self-Hosted Runner Setup

Guide for setting up a self-hosted GitHub Actions runner on your local machine to run Reddit digest workflows.

## Why Self-Hosted Runners?

**Benefits for Reddit Digest**:
- ✅ Uses your residential IP (no Reddit blocking)
- ✅ Runs on your schedule (no cloud costs)
- ✅ Access to local files and credentials
- ✅ Full control over environment

**Drawbacks**:
- Machine must be running during scheduled times
- You manage security and updates
- Uses your machine's resources

## Prerequisites

- **Operating System**: macOS, Linux, or Windows
- **GitHub Account**: With admin access to your repository
- **Machine Requirements**:
  - 2+ CPU cores
  - 4GB+ RAM
  - 10GB+ disk space
  - Stable internet connection

## Setup Instructions

### Step 1: Add Runner to Repository

1. **Navigate to Repository Settings**:
   ```
   GitHub Repository → Settings → Actions → Runners
   ```

2. **Click "New self-hosted runner"**

3. **Select Your Operating System**:
   - macOS
   - Linux
   - Windows

4. **Follow the Download Instructions**

### Step 2: macOS/Linux Setup

GitHub will show you commands like this:

```bash
# Create a directory for the runner
mkdir actions-runner && cd actions-runner

# Download the runner package (copy actual URL from GitHub)
curl -o actions-runner-osx-arm64-2.314.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.314.1/actions-runner-osx-arm64-2.314.1.tar.gz

# Extract the installer
tar xzf ./actions-runner-osx-arm64-2.314.1.tar.gz

# Configure the runner
./config.sh --url https://github.com/YOUR_ORG/YOUR_REPO --token YOUR_TOKEN

# Run the runner
./run.sh
```

### Step 3: Configure the Runner

When running `./config.sh`, you'll be asked:

```
Enter the name of the runner group to add this runner to: [press Enter for default]
→ Press Enter (uses default group)

Enter the name of runner: [press Enter for hostname]
→ Enter a descriptive name like "my-macbook-runner"

This runner will have the following labels: 'self-hosted', 'macOS', 'ARM64'
Enter any additional labels (ex. label-1,label-2): [press Enter to skip]
→ Press Enter (default labels are fine)

Enter name of work folder: [press Enter for _work]
→ Press Enter
```

### Step 4: Test the Runner

```bash
# Start the runner interactively (test mode)
./run.sh
```

You should see:
```
√ Connected to GitHub
Current runner version: '2.314.1'
2024-12-11 20:00:00Z: Listening for Jobs
```

### Step 5: Run as a Service (Recommended)

Running the runner as a service ensures it starts automatically.

#### macOS (launchd)

```bash
cd ~/actions-runner

# Install the service
sudo ./svc.sh install

# Start the service
sudo ./svc.sh start

# Check status
sudo ./svc.sh status

# View logs
tail -f ~/Library/Logs/runner.log
```

#### Linux (systemd)

```bash
cd ~/actions-runner

# Install the service
sudo ./svc.sh install

# Start the service
sudo ./svc.sh start

# Enable auto-start on boot
sudo systemctl enable actions.runner.*

# Check status
sudo ./svc.sh status

# View logs
journalctl -u actions.runner.* -f
```

### Step 6: Update Workflow to Use Self-Hosted Runner

Edit your workflow file to use `self-hosted` runner:

```yaml
# .github/workflows/reddit-digest.yml
jobs:
  generate-digests:
    runs-on: self-hosted  # Changed from ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      # ... rest of your workflow
```

Or for the build-release workflow:

```yaml
# .github/workflows/build-release.yml
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        include:
          - os: self-hosted  # Use your runner
            platform: macos
            executable_name: reddit-digest-macos
```

## Managing Your Runner

### Check Runner Status

**In GitHub**:
```
Repository → Settings → Actions → Runners
```

You'll see:
- Runner name
- Status (Online/Offline)
- Labels
- Operating system
- Last activity

**On Your Machine**:

```bash
# macOS/Linux
cd ~/actions-runner
sudo ./svc.sh status
```

### Stop the Runner

```bash
# Temporarily stop
sudo ./svc.sh stop

# Permanently remove service
sudo ./svc.sh uninstall
```

### Update the Runner

GitHub will notify you when updates are available:

```bash
cd ~/actions-runner

# Stop the service
sudo ./svc.sh stop

# Download and extract new version
# (GitHub will provide the commands)

# Start the service
sudo ./svc.sh start
```

### Remove the Runner

```bash
# Stop the service
sudo ./svc.sh stop
sudo ./svc.sh uninstall

# Remove from GitHub
./config.sh remove --token YOUR_TOKEN

# Delete the directory
cd ..
rm -rf actions-runner
```

## Security Best Practices

### 1. Use Runner Groups (Organizations)

For organization repositories:
```
Organization Settings → Actions → Runner groups
→ Create group with limited repository access
```

### 2. Limit Workflow Permissions

In workflow file:

```yaml
permissions:
  contents: read  # Minimal permissions
  actions: read
```

### 3. Use Repository Secrets

Never hardcode credentials in workflows:

```yaml
steps:
  - name: Run digest
    env:
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
    run: ./dist/reddit-digest stocks ...
```

### 4. Review Workflow Logs

Check logs regularly for suspicious activity:
```
Repository → Actions → [Workflow Run] → [Job]
```

### 5. Keep Runner Updated

Enable auto-updates (recommended):
```bash
# During setup, answer "yes" to:
"Allow the runner to update itself? (Y/N)"
```

## Troubleshooting

### Runner Shows Offline

**Check if service is running**:
```bash
# macOS
sudo ./svc.sh status
sudo ./svc.sh start

# View logs
tail -f ~/Library/Logs/runner.log
```

**Common causes**:
- Machine is off/sleeping
- Network issues
- Runner token expired
- Service crashed

### Workflow Doesn't Trigger

**Check**:
1. Runner is online in GitHub Settings
2. Workflow uses `runs-on: self-hosted`
3. Workflow trigger conditions are met (tag push, schedule, etc.)

### Permission Errors

**Fix runner permissions**:
```bash
cd ~/actions-runner
sudo chown -R $(whoami) .
```

### Runner Not Starting on Boot

**macOS**:
```bash
# Check launchd service
launchctl list | grep actions.runner

# Reload service
sudo launchctl unload ~/Library/LaunchAgents/actions.runner.*.plist
sudo launchctl load ~/Library/LaunchAgents/actions.runner.*.plist
```

**Linux**:
```bash
# Check systemd service
sudo systemctl status actions.runner.*

# Enable auto-start
sudo systemctl enable actions.runner.*
```

### Disk Space Issues

Runner cache can grow large:

```bash
# Clean actions cache
cd ~/actions-runner/_work/_temp
rm -rf *

# Clean old workflows
cd ~/actions-runner/_work/YOUR_REPO
git clean -fdx
```

## Advanced Configuration

### Multiple Runners

Run multiple runners on same machine:

```bash
# Create second runner directory
mkdir actions-runner-2 && cd actions-runner-2

# Download and configure
# Use different name during config.sh

# Install as separate service
sudo ./svc.sh install
sudo ./svc.sh start
```

### Custom Labels

Add labels during setup:

```bash
./config.sh --url https://github.com/YOUR_ORG/YOUR_REPO \
            --token YOUR_TOKEN \
            --labels my-label,another-label
```

Use in workflows:

```yaml
jobs:
  build:
    runs-on: [self-hosted, my-label]
```

### Environment Variables

Set environment for all workflow runs:

```bash
# Create .env file
cd ~/actions-runner
cat > .env <<EOF
OPENROUTER_API_KEY=your-key-here
CUSTOM_VAR=value
EOF

# Restart service
sudo ./svc.sh restart
```

### Resource Limits

Limit runner resource usage:

**macOS** (launchd):
```xml
<!-- Edit ~/Library/LaunchAgents/actions.runner.*.plist -->
<dict>
    <key>SoftResourceLimits</key>
    <dict>
        <key>NumberOfFiles</key>
        <integer>1024</integer>
    </dict>
</dict>
```

**Linux** (systemd):
```bash
# Edit service file
sudo systemctl edit actions.runner.*

[Service]
MemoryLimit=2G
CPUQuota=50%
```

## Monitoring

### View Runner Logs

**macOS**:
```bash
# Real-time logs
tail -f ~/Library/Logs/runner.log

# Recent errors
grep ERROR ~/Library/Logs/runner.log | tail -20
```

**Linux**:
```bash
# Real-time logs
journalctl -u actions.runner.* -f

# Recent errors
journalctl -u actions.runner.* --priority=err
```

### Health Check Script

Create `~/actions-runner/healthcheck.sh`:

```bash
#!/bin/bash
STATUS=$(curl -s https://api.github.com/repos/YOUR_ORG/YOUR_REPO/actions/runners)
echo "$STATUS" | jq '.runners[] | select(.name=="my-macbook-runner") | .status'
```

Run via cron:
```bash
# Check every hour
0 * * * * ~/actions-runner/healthcheck.sh
```

## Comparison: Self-Hosted vs GitHub-Hosted

| Feature | Self-Hosted | GitHub-Hosted |
|---------|-------------|---------------|
| Cost | Free (your hardware) | Free (public repos), paid (private) |
| IP Address | Your residential IP | GitHub datacenter IPs |
| Setup | Manual configuration | Zero setup |
| Maintenance | You manage updates | GitHub manages |
| Performance | Your hardware | Standard VM specs |
| Availability | Depends on machine | Always available |
| Security | You control | GitHub controls |

## For Reddit Digest Use Case

**Recommended Setup**:

1. **Use self-hosted runner** for scheduled digest generation:
   - Runs on your machine every 4 hours
   - Uses your IP (no Reddit blocking)
   - Workflow: `.github/workflows/reddit-digest.yml`

2. **Use GitHub-hosted runners** for releases:
   - Builds executables for multiple platforms
   - No need for local machine to be on
   - Workflow: `.github/workflows/build-release.yml`

**Hybrid Workflow Configuration**:

```yaml
# .github/workflows/reddit-digest.yml (self-hosted)
jobs:
  generate-digests:
    runs-on: self-hosted  # Your machine

# .github/workflows/build-release.yml (GitHub-hosted)
jobs:
  build:
    runs-on: ${{ matrix.os }}  # GitHub's runners
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
```

## Next Steps

1. **Set up runner**: Follow Step 1-5 above
2. **Update workflow**: Change `runs-on: self-hosted`
3. **Test**: Push a commit or manually trigger workflow
4. **Monitor**: Check Actions tab for successful run
5. **Schedule**: Workflow will run on schedule automatically

Your runner will now execute workflows using your machine and residential IP, solving the Reddit blocking issue!
