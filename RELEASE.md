# Release Process - Reddit Digest Generator

Guide for creating new releases with automated builds for Linux and macOS.

## Overview

The GitHub Actions workflow automatically builds executables for:
- **Linux** (Ubuntu, 64-bit)
- **macOS** (ARM64/Intel universal)

Releases are published to GitHub Releases with checksums.

## Creating a New Release

### Option 1: Git Tag (Recommended)

```bash
# Ensure you're on main branch with latest changes
git checkout main
git pull

# Create and push a version tag
git tag v1.0.0
git push origin v1.0.0
```

This automatically triggers the build workflow.

### Option 2: Manual Trigger (Testing)

1. Go to **Actions** tab in GitHub
2. Select **Build and Release Reddit Digest** workflow
3. Click **Run workflow**
4. Enter tag name (e.g., `v0.1.0-beta`)
5. Click **Run workflow**

## Release Workflow

When triggered, the workflow:

1. **Builds for Both Platforms** (parallel):
   - Ubuntu: `reddit-digest-linux`
   - macOS: `reddit-digest-macos`

2. **Generates Checksums**:
   - `reddit-digest-linux.sha256`
   - `reddit-digest-macos.sha256`

3. **Creates GitHub Release**:
   - Tag: `v1.0.0` (from git tag)
   - Title: `Reddit Digest Generator v1.0.0`
   - Assets: Executables + checksums
   - Release notes: Auto-generated

## Versioning

Follow [Semantic Versioning](https://semver.org/):

- **v1.0.0** - Major version (breaking changes)
- **v1.1.0** - Minor version (new features, backward compatible)
- **v1.1.1** - Patch version (bug fixes)

### Pre-release Tags

Use suffixes for pre-releases:
- `v1.0.0-alpha` - Alpha release
- `v1.0.0-beta` - Beta release
- `v1.0.0-rc1` - Release candidate

## Verifying Builds

After release is created:

### Linux

```bash
# Download
curl -LO https://github.com/YOUR_ORG/YOUR_REPO/releases/download/v1.0.0/reddit-digest-linux

# Verify checksum
curl -LO https://github.com/YOUR_ORG/YOUR_REPO/releases/download/v1.0.0/reddit-digest-linux.sha256
sha256sum -c reddit-digest-linux.sha256

# Test
chmod +x reddit-digest-linux
./reddit-digest-linux --help
```

### macOS

```bash
# Download
curl -LO https://github.com/YOUR_ORG/YOUR_REPO/releases/download/v1.0.0/reddit-digest-macos

# Verify checksum
curl -LO https://github.com/YOUR_ORG/YOUR_REPO/releases/download/v1.0.0/reddit-digest-macos.sha256
shasum -a 256 -c reddit-digest-macos.sha256

# Test
chmod +x reddit-digest-macos
./reddit-digest-macos --help
```

## Troubleshooting

### Build Failed

Check GitHub Actions logs:
1. Go to **Actions** tab
2. Click on the failed workflow run
3. Review build logs for errors

Common issues:
- **Missing dependencies**: Update `pyproject.toml`
- **PyInstaller errors**: Update `reddit_digest.spec` hiddenimports
- **Platform-specific issues**: Check matrix build logs

### Release Not Created

Ensure:
- Workflow has `contents: write` permission
- Tag name follows pattern `v*.*.*`
- Repository settings allow Actions to create releases

### Checksums Don't Match

Rebuild from clean state:
```bash
git clean -fdx
git pull
./build_executable.sh
```

## Continuous Integration

The workflow runs on:
- **Tag push**: `git push origin v*.*.*`
- **Manual trigger**: Via GitHub Actions UI

## Build Artifacts

Build artifacts are retained for 7 days in GitHub Actions:
- Useful for debugging
- Download from Actions tab → Workflow run → Artifacts

## Release Notes Template

When creating releases, include:

```markdown
## What's New in v1.0.0

### Features
- New feature descriptions
- Improvements and enhancements

### Bug Fixes
- Fixed issue #123: Description
- Fixed crash when...

### Breaking Changes
- Changed X to Y (migration guide below)

### Installation

**Linux**:
\`\`\`bash
curl -LO https://github.com/ORG/REPO/releases/download/v1.0.0/reddit-digest-linux
chmod +x reddit-digest-linux
\`\`\`

**macOS**:
\`\`\`bash
curl -LO https://github.com/ORG/REPO/releases/download/v1.0.0/reddit-digest-macos
chmod +x reddit-digest-macos
\`\`\`

### Full Changelog
See: https://github.com/ORG/REPO/compare/v0.9.0...v1.0.0
```

## Rollback

If a release has issues:

1. **Mark as pre-release**:
   - Edit release on GitHub
   - Check "This is a pre-release"

2. **Create hotfix**:
   ```bash
   git checkout v1.0.0
   git checkout -b hotfix/v1.0.1
   # Make fixes
   git commit -am "Fix critical bug"
   git tag v1.0.1
   git push origin v1.0.1
   ```

3. **Delete bad release** (last resort):
   - Delete release on GitHub
   - Delete tag: `git push --delete origin v1.0.0`

## Best Practices

1. **Test locally first**:
   ```bash
   ./build_executable.sh
   ./dist/reddit-digest --help
   ```

2. **Create release branch** for major versions:
   ```bash
   git checkout -b release/v1.0
   git push origin release/v1.0
   ```

3. **Update CHANGELOG.md** before tagging

4. **Use pre-release tags** for testing

5. **Verify on both platforms** before announcing

## GitHub Actions Configuration

The workflow is defined in:
[`.github/workflows/build-release.yml`](.github/workflows/build-release.yml)

Key settings:
- **Runs on**: `ubuntu-latest`, `macos-latest`
- **Python**: 3.12
- **Artifacts**: Retained 7 days
- **Permissions**: `contents: write` (for releases)

## Support

For build issues:
1. Check [Actions logs](https://github.com/YOUR_ORG/YOUR_REPO/actions)
2. Review [DEPLOYMENT.md](DEPLOYMENT.md) for setup
3. Open issue with build logs attached
