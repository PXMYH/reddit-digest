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
    required=True,
    help="Start date (YYYY-MM-DD)",
)
@click.option(
    "--end",
    "-e",
    required=True,
    help="End date (YYYY-MM-DD)",
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
    default="gpt-4o-mini",
    help="LLM model to use (default: gpt-4o-mini)",
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
def main(
    subreddit: str,
    start: str,
    end: str,
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
):
    """
    Generate a reading digest for a subreddit within a date range.

    SUBREDDIT: Name of the subreddit (without 'r/' prefix)

    Example:
        python summarize_subreddit.py MachineLearning --start 2024-01-01 --end 2024-01-31
    """
    click.echo(f"\n🤖 Reddit Subreddit Summarizer with ACE Framework\n")
    click.echo(f"Subreddit: r/{subreddit}")

    # Parse dates
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError as e:
        click.echo(f"❌ Error parsing dates: {e}", err=True)
        sys.exit(1)

    if start_date > end_date:
        click.echo("❌ Error: Start date must be before end date", err=True)
        sys.exit(1)

    click.echo(f"Date range: {start} to {end}")
    click.echo(f"Filters: ≥{min_upvotes} upvotes, ≥{min_comments} comments")
    click.echo(f"Model: {model}\n")

    # Check for Reddit API credentials
    if not os.getenv("REDDIT_CLIENT_ID") or not os.getenv("REDDIT_CLIENT_SECRET"):
        click.echo("❌ Error: Reddit API credentials not found!", err=True)
        click.echo("\nPlease set the following environment variables:")
        click.echo("  - REDDIT_CLIENT_ID")
        click.echo("  - REDDIT_CLIENT_SECRET")
        click.echo("\nGet credentials at: https://www.reddit.com/prefs/apps")
        sys.exit(1)

    try:
        # Initialize fetcher and summarizer
        click.echo("🔧 Initializing components...")
        fetcher = RedditFetcher()
        summarizer = RedditSummarizer(
            model=model,
            skillbook_path=skillbook,
            fetcher=fetcher,
        )

        # Fetch posts
        click.echo(f"\n📥 Fetching posts from r/{subreddit}...")
        posts = fetcher.fetch_posts(
            subreddit_name=subreddit,
            start_date=start_date,
            end_date=end_date,
            min_upvotes=min_upvotes,
            min_comments=min_comments,
            max_posts=max_posts,
        )

        if not posts:
            click.echo(f"\n⚠️  No posts found matching criteria.")
            sys.exit(0)

        click.echo(f"✅ Found {len(posts)} posts matching criteria\n")

        # Generate digest
        click.echo("🔮 Generating digest with AI summaries...")
        if checkpoint:
            click.echo(f"📂 Checkpoint enabled: {checkpoint}")
            click.echo(f"   Saving every {checkpoint_interval} posts")

        digest = summarizer.generate_digest(
            posts=posts,
            subreddit=subreddit,
            start_date=start_date,
            end_date=end_date,
            include_comments=not no_comments,
            checkpoint_file=checkpoint,
            checkpoint_interval=checkpoint_interval,
        )

        # Determine output path
        if not output:
            output = f"{subreddit}_digest_{start}_to_{end}.md"

        # Save digest
        digest.save_to_file(output)
        click.echo(f"\n✅ Digest saved to: {output}")

        # Print stats
        click.echo(f"\n📊 Summary Stats:")
        click.echo(f"  Posts analyzed: {digest.total_posts_analyzed}")
        click.echo(f"  Posts summarized: {len(digest.post_summaries)}")

        # Print skillbook stats
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
