#!/usr/bin/env bash
set -euo pipefail

# Reddit Digest Generator - Build Script
# Packages the Python application into a standalone executable using PyInstaller

echo "🔨 Reddit Digest Generator - Build Script"
echo "=========================================="
echo ""

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: UV is not installed"
    echo "   Install UV: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ UV is installed"

# Check if we're in the correct directory
if [ ! -f "summarize_subreddit.py" ]; then
    echo "❌ Error: summarize_subreddit.py not found"
    echo "   Please run this script from the workspace directory"
    exit 1
fi

echo "✅ Found summarize_subreddit.py"

# Sync dependencies
echo ""
echo "📦 Installing dependencies with UV..."
uv sync

# Install PyInstaller (dev dependency)
echo ""
echo "📦 Installing PyInstaller..."
uv pip install pyinstaller

# Clean previous builds
if [ -d "build" ] || [ -d "dist" ]; then
    echo ""
    echo "🧹 Cleaning previous build artifacts..."
    rm -rf build dist
fi

# Build the executable
echo ""
echo "🔨 Building executable with PyInstaller..."
echo "   This may take a few minutes..."
echo ""

uv run pyinstaller reddit_digest.spec

# Check if build was successful
if [ -f "dist/reddit-digest" ]; then
    echo ""
    echo "✅ Build successful!"
    echo ""
    echo "📦 Executable location: $(pwd)/dist/reddit-digest"

    # Get file size
    SIZE=$(du -h dist/reddit-digest | cut -f1)
    echo "📊 File size: $SIZE"

    echo ""
    echo "🧪 Testing executable..."
    if ./dist/reddit-digest --help > /dev/null 2>&1; then
        echo "✅ Executable works!"
    else
        echo "⚠️  Warning: Executable may have issues"
    fi

    echo ""
    echo "📋 Next steps:"
    echo "   1. Test with a sample command:"
    echo "      ./dist/reddit-digest stocks --start 2025-12-01 --end 2025-12-07 --min-upvotes 10 --min-comments 10 --max-posts 5"
    echo ""
    echo "   2. Set up scheduled execution:"
    echo "      ./run_digest_scheduler.sh"
    echo ""
    echo "   3. View deployment guide:"
    echo "      cat DEPLOYMENT.md"
    echo ""
else
    echo ""
    echo "❌ Build failed"
    echo "   Check the error messages above for details"
    exit 1
fi
