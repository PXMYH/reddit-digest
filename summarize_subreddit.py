#!/usr/bin/env python3
"""
Reddit Subreddit Summarizer - Main CLI Script

Generate reading digests from Reddit subreddits with AI-powered summarization
using the ACE (Agentic Context Engineering) framework.

Usage:
    python summarize_subreddit.py <subreddit> --start 2024-01-01 --end 2024-01-31
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import click
from dotenv import load_dotenv

from reddit_summarizer import RedditFetcher, RedditSummarizer


# Load environment variables
load_dotenv()


@click.command()
@click.argument("subreddit")
@click.option(
    "--start",
    "-s",
    default=None,
    help="Start date (YYYY-MM-DD) - required with --end",
)
@click.option(
    "--end",
    "-e",
    default=None,
    help="End date (YYYY-MM-DD) - required with --start",
)
@click.option(
    "--timeframe",
    "-t",
    type=click.Choice(["hour", "day", "week", "month", "year", "all"], case_sensitive=False),
    default=None,
    help="Timeframe for top posts (alternative to --start/--end)",
)
@click.option(
    "--min-upvotes",
    default=100,
    help="Minimum upvotes threshold (default: 100)",
)
@click.option(
    "--min-comments",
    default=30,
    help="Minimum comments threshold (default: 30)",
)
@click.option(
    "--max-posts",
    default=50,
    help="Maximum number of posts to analyze (default: 50)",
)
@click.option(
    "--model",
    default="openrouter/mistralai/devstral-2512:free",
    help="LLM model to use (default: openrouter/mistralai/devstral-2512:free)",
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="Output file path (default: <subreddit>_digest_<date>.md)",
)
@click.option(
    "--skillbook",
    default=None,
    help="Path to existing skillbook to load",
)
@click.option(
    "--save-skillbook",
    default=None,
    help="Path to save updated skillbook",
)
@click.option(
    "--no-comments",
    is_flag=True,
    help="Skip fetching and analyzing comments",
)
@click.option(
    "--checkpoint",
    default=None,
    help="Path to checkpoint file for resumable processing",
)
@click.option(
    "--checkpoint-interval",
    default=5,
    help="Save checkpoint every N posts (default: 5)",
)
@click.option(
    "--summarize/--no-summarize",
    default=None,
    help="Generate AI summaries (default: True for date range, False for timeframe)",
)
def main(
    subreddit: str,
    start: str,
    end: str,
    timeframe: str,
    min_upvotes: int,
    min_comments: int,
    max_posts: int,
    model: str,
    output: str,
    skillbook: str,
    save_skillbook: str,
    no_comments: bool,
    checkpoint: str,
    checkpoint_interval: int,
    summarize: bool,
):
    """
    Generate a reading digest for a subreddit.

    SUBREDDIT: Name of the subreddit (without 'r/' prefix)

    Examples:
        # Date range mode (with summaries by default)
        python summarize_subreddit.py MachineLearning --start 2024-01-01 --end 2024-01-31

        # Timeframe mode (no summaries by default, fast)
        python summarize_subreddit.py Fire --timeframe year

        # Timeframe mode with summaries
        python summarize_subreddit.py Fire --timeframe year --summarize
    """
    click.echo(f"\n🤖 Reddit Subreddit Summarizer with ACE Framework\n")
    click.echo(f"Subreddit: r/{subreddit}")

    # Validate mutually exclusive options
    date_mode = start is not None or end is not None
    timeframe_mode = timeframe is not None

    if date_mode and timeframe_mode:
        click.echo("❌ Error: Cannot use both --start/--end and --timeframe", err=True)
        click.echo("   Use either date range OR timeframe, not both", err=True)
        sys.exit(1)

    if not date_mode and not timeframe_mode:
        click.echo("❌ Error: Must specify either --start/--end or --timeframe", err=True)
        sys.exit(1)

    # Date range mode validation
    if date_mode:
        if start is None or end is None:
            click.echo("❌ Error: Both --start and --end are required for date range mode", err=True)
            sys.exit(1)

        try:
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
        except ValueError as e:
            click.echo(f"❌ Error parsing dates: {e}", err=True)
            sys.exit(1)

        if start_date > end_date:
            click.echo("❌ Error: Start date must be before end date", err=True)
            sys.exit(1)

        click.echo(f"Mode: Date range ({start} to {end})")
    else:
        # Timeframe mode
        start_date = None
        end_date = None
        click.echo(f"Mode: Timeframe (top posts from past {timeframe})")

    # Determine if we should summarize
    if summarize is None:
        # Default behavior: True for date range, False for timeframe
        summarize = date_mode

    click.echo(f"Filters: ≥{min_upvotes} upvotes, ≥{min_comments} comments")
    click.echo(f"Summarization: {'Enabled' if summarize else 'Disabled (fast mode)'}")
    click.echo(f"Model: {model}\n")

    # Check for LLM API key (OpenRouter recommended)
    if not os.getenv("OPENROUTER_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        click.echo("⚠️  Warning: No LLM API key found!", err=True)
        click.echo("\nFor OpenRouter (recommended), set: OPENROUTER_API_KEY")
        click.echo("Get your key at: https://openrouter.ai/keys")
        click.echo("\nAlternatively, set OPENAI_API_KEY for OpenAI models.")
        click.echo("\nNote: Reddit API credentials are NO LONGER REQUIRED!")
        click.echo("The tool now uses Reddit's public JSON API.\n")

    try:
        # Initialize fetcher
        click.echo("🔧 Initializing components...")
        fetcher = RedditFetcher()

        # Fetch posts based on mode
        click.echo(f"\n📥 Fetching posts from r/{subreddit}...")
        if date_mode:
            posts = fetcher.fetch_posts(
                subreddit_name=subreddit,
                start_date=start_date,
                end_date=end_date,
                min_upvotes=min_upvotes,
                min_comments=min_comments,
                max_posts=max_posts,
            )
        else:
            # Timeframe mode
            posts = fetcher.fetch_posts_by_timeframe(
                subreddit_name=subreddit,
                timeframe=timeframe,
                min_upvotes=min_upvotes,
                min_comments=min_comments,
                max_posts=max_posts,
            )

        if not posts:
            click.echo(f"\n⚠️  No posts found matching criteria.")
            sys.exit(0)

        click.echo(f"✅ Found {len(posts)} posts matching criteria\n")

        # Handle summarization
        if summarize:
            # Full digest generation with AI summaries
            summarizer = RedditSummarizer(
                model=model,
                skillbook_path=skillbook,
                fetcher=fetcher,
            )

            click.echo("🔮 Generating digest with AI summaries...")
            if checkpoint:
                click.echo(f"📂 Checkpoint enabled: {checkpoint}")
                click.echo(f"   Saving every {checkpoint_interval} posts")

            digest = summarizer.generate_digest(
                posts=posts,
                subreddit=subreddit,
                start_date=start_date if date_mode else datetime.now(),
                end_date=end_date if date_mode else datetime.now(),
                include_comments=not no_comments,
                checkpoint_file=checkpoint,
                checkpoint_interval=checkpoint_interval,
            )
        else:
            # Fast mode: no summaries, just create digest from posts
            from reddit_summarizer.models import SubredditDigest, PostSummary

            click.echo("⚡ Fast mode: Creating digest without AI summaries...")

            # Create minimal post summaries (no AI-generated content)
            post_summaries = []
            for post in posts:
                summary = PostSummary(
                    post=post,
                    summary="",  # No summary
                    key_points=[],  # No key points
                    discussion_highlights="",  # No discussion
                )
                post_summaries.append(summary)

            digest = SubredditDigest(
                subreddit=subreddit,
                start_date=start_date if date_mode else datetime.now(),
                end_date=end_date if date_mode else datetime.now(),
                total_posts_analyzed=len(posts),
                post_summaries=post_summaries,
            )

        # Create digest directory if it doesn't exist
        digest_dir = Path("digest")
        digest_dir.mkdir(exist_ok=True)

        # Determine output path
        if not output:
            if date_mode:
                output = digest_dir / f"{subreddit}_digest_{start}_to_{end}.md"
            else:
                # Timeframe mode: use timeframe in filename
                today = datetime.now().strftime("%Y-%m-%d")
                output = digest_dir / f"{subreddit}_top_{timeframe}_{today}.md"
        else:
            output = digest_dir / Path(output).name

        # Save digest
        digest.save_to_file(str(output))
        click.echo(f"\n✅ Digest saved to: {output}")

        # Print stats
        click.echo(f"\n📊 Summary Stats:")
        click.echo(f"  Posts analyzed: {digest.total_posts_analyzed}")
        if summarize:
            click.echo(f"  Posts summarized: {len(digest.post_summaries)}")
        else:
            click.echo(f"  Posts listed: {len(digest.post_summaries)} (no AI summaries)")

        # Print skillbook stats (only if summarization was enabled)
        if summarize:
            summarizer.print_skillbook_stats()

            # Save skillbook if requested
            if save_skillbook:
                summarizer.save_skillbook(save_skillbook)

        click.echo(f"\n✨ Done! Check {output} for your reading digest.\n")

    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
