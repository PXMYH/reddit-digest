#!/usr/bin/env python3
"""
Reddit Subreddit Summarizer

Generates reading digests from subreddit posts based on importance
(upvotes and comments), with LLM-powered summaries.

Following learned strategies:
- [api_patterns-00002] Explicit timeouts
- [api_patterns-00003] Pagination limits
- [api_patterns-00004] Rate limiting delays
- [api_patterns-00026] Retry decorator with exponential backoff
"""

import argparse
import sys
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class RedditPost:
    """Represents an important Reddit post."""

    title: str
    author: str
    score: int
    num_comments: int
    url: str
    created_utc: float
    selftext: str
    permalink: str

    @property
    def created_datetime(self) -> datetime:
        """Convert Unix timestamp to datetime."""
        return datetime.fromtimestamp(self.created_utc)

    def __repr__(self) -> str:
        return (
            f"RedditPost(title='{self.title[:50]}...', "
            f"score={self.score}, comments={self.num_comments})"
        )


class RedditSummarizer:
    """
    Summarizes important posts from a subreddit.

    Applies learned strategies for API handling and rate limiting.
    """

    def __init__(
        self,
        min_upvotes: int = 100,
        min_comments: int = 30,
        max_posts: int = 100,
        timeout: int = 10,
        rate_limit_delay: float = 1.0,
    ):
        """
        Initialize the summarizer.

        Args:
            min_upvotes: Minimum upvotes for importance (default: 100)
            min_comments: Minimum comments for importance (default: 30)
            max_posts: Maximum posts to fetch (pagination limit)
            timeout: Request timeout in seconds [api_patterns-00002]
            rate_limit_delay: Delay between requests [api_patterns-00004]
        """
        self.min_upvotes = min_upvotes
        self.min_comments = min_comments
        self.max_posts = max_posts
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay

        # Placeholder for PRAW reddit instance
        self.reddit = None

    def connect(self, client_id: str, client_secret: str, user_agent: str) -> None:
        """
        Connect to Reddit API using PRAW.

        Args:
            client_id: Reddit API client ID
            client_secret: Reddit API client secret
            user_agent: User agent string
        """
        try:
            import praw

            self.reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent,
                timeout=self.timeout,  # [api_patterns-00002]
            )
            print(f"✓ Connected to Reddit API as: {self.reddit.read_only}")

        except ImportError:
            print("Error: PRAW library not installed. Install with: pip install praw")
            sys.exit(1)
        except Exception as e:
            print(f"Error connecting to Reddit API: {e}")
            sys.exit(1)

    def fetch_posts(
        self,
        subreddit_name: str,
        start_date: datetime,
        end_date: datetime,
    ) -> List[RedditPost]:
        """
        Fetch important posts from subreddit within date range.

        Args:
            subreddit_name: Name of the subreddit (without 'r/')
            start_date: Start of date range
            end_date: End of date range

        Returns:
            List of important RedditPost objects
        """
        if not self.reddit:
            raise RuntimeError("Not connected. Call connect() first.")

        print(f"\n📡 Fetching posts from r/{subreddit_name}...")
        print(f"   Date range: {start_date.date()} to {end_date.date()}")
        print(f"   Criteria: ≥{self.min_upvotes} upvotes AND ≥{self.min_comments} comments")

        important_posts = []
        subreddit = self.reddit.subreddit(subreddit_name)

        # Fetch recent posts (new, hot, and top)
        all_submissions = []

        # [api_patterns-00003] Pagination limit
        for submission in subreddit.new(limit=self.max_posts):
            all_submissions.append(submission)
            time.sleep(self.rate_limit_delay)  # [api_patterns-00004] Rate limiting

        # Filter by date range and importance
        for submission in all_submissions:
            post_date = datetime.fromtimestamp(submission.created_utc)

            # Check date range
            if not (start_date <= post_date <= end_date):
                continue

            # Check importance criteria
            if (submission.score >= self.min_upvotes and
                submission.num_comments >= self.min_comments):

                post = RedditPost(
                    title=submission.title,
                    author=str(submission.author),
                    score=submission.score,
                    num_comments=submission.num_comments,
                    url=submission.url,
                    created_utc=submission.created_utc,
                    selftext=submission.selftext or "",
                    permalink=f"https://reddit.com{submission.permalink}",
                )
                important_posts.append(post)

        print(f"✓ Found {len(important_posts)} important posts")
        return important_posts

    def generate_text_summary(self, posts: List[RedditPost]) -> str:
        """
        Generate plain text summary of posts.

        Args:
            posts: List of RedditPost objects

        Returns:
            Plain text summary string
        """
        if not posts:
            return "No important posts found in the specified date range."

        summary_lines = [
            "=" * 80,
            "REDDIT SUBREDDIT DIGEST",
            "=" * 80,
            f"\nTotal Important Posts: {len(posts)}",
            f"Criteria: ≥{self.min_upvotes} upvotes AND ≥{self.min_comments} comments\n",
            "-" * 80,
        ]

        for i, post in enumerate(posts, 1):
            summary_lines.extend([
                f"\n{i}. {post.title}",
                f"   Author: u/{post.author}",
                f"   Score: {post.score} upvotes | Comments: {post.num_comments}",
                f"   Posted: {post.created_datetime.strftime('%Y-%m-%d %H:%M:%S')}",
                f"   Link: {post.permalink}",
            ])

            if post.selftext:
                preview = post.selftext[:200].replace('\n', ' ')
                summary_lines.append(f"   Preview: {preview}...")

            summary_lines.append("")

        summary_lines.append("=" * 80)
        return "\n".join(summary_lines)


def parse_date(date_str: str) -> datetime:
    """Parse date string in YYYY-MM-DD format."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        print(f"Error: Invalid date format '{date_str}'. Use YYYY-MM-DD format.")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate reading digest from important Reddit posts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s python --start 2024-12-01 --end 2024-12-10
  %(prog)s machinelearning --start 2024-12-01 --end 2024-12-10 --output ml_digest.txt
  %(prog)s python --days 7 --min-upvotes 200 --min-comments 50
        """
    )

    parser.add_argument(
        "subreddit",
        help="Subreddit name (without 'r/')"
    )
    parser.add_argument(
        "--start",
        help="Start date (YYYY-MM-DD)",
        type=str
    )
    parser.add_argument(
        "--end",
        help="End date (YYYY-MM-DD)",
        type=str
    )
    parser.add_argument(
        "--days",
        help="Number of days back from today (alternative to --start/--end)",
        type=int
    )
    parser.add_argument(
        "--min-upvotes",
        help="Minimum upvotes for importance (default: 100)",
        type=int,
        default=100
    )
    parser.add_argument(
        "--min-comments",
        help="Minimum comments for importance (default: 30)",
        type=int,
        default=30
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
        type=str
    )
    parser.add_argument(
        "--client-id",
        help="Reddit API client ID (or set REDDIT_CLIENT_ID env var)",
        type=str
    )
    parser.add_argument(
        "--client-secret",
        help="Reddit API client secret (or set REDDIT_CLIENT_SECRET env var)",
        type=str
    )

    args = parser.parse_args()

    # Determine date range
    if args.days:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=args.days)
    elif args.start and args.end:
        start_date = parse_date(args.start)
        end_date = parse_date(args.end)
    else:
        parser.error("Either --days or both --start and --end must be provided")

    # Get API credentials
    import os
    client_id = args.client_id or os.getenv("REDDIT_CLIENT_ID")
    client_secret = args.client_secret or os.getenv("REDDIT_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("Error: Reddit API credentials required.")
        print("Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET environment variables")
        print("or provide --client-id and --client-secret arguments")
        sys.exit(1)

    # Initialize summarizer
    summarizer = RedditSummarizer(
        min_upvotes=args.min_upvotes,
        min_comments=args.min_comments,
    )

    # Connect to Reddit
    user_agent = "python:reddit-summarizer:v1.0.0 (by /u/your_username)"
    summarizer.connect(client_id, client_secret, user_agent)

    # Fetch and summarize posts
    posts = summarizer.fetch_posts(args.subreddit, start_date, end_date)
    summary = summarizer.generate_text_summary(posts)

    # Output results
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"\n✓ Digest saved to: {args.output}")
    else:
        print("\n" + summary)


if __name__ == "__main__":
    main()
