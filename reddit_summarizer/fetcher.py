"""
Reddit data fetcher using PRAW (Python Reddit API Wrapper)
"""

import os
import time
from datetime import datetime
from typing import List, Optional, Callable, TypeVar, Any
import praw
from praw.exceptions import PRAWException
from prawcore.exceptions import (
    NotFound,
    Forbidden,
    ServerError,
    RequestException,
    ResponseException,
)
from .models import RedditPost

T = TypeVar("T")


class RedditFetcher:
    """Fetches posts from Reddit using PRAW"""

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        user_agent: Optional[str] = None,
        timeout: int = 10,
        rate_limit_delay: float = 1.0,
    ):
        """
        Initialize Reddit API client

        Args:
            client_id: Reddit API client ID (defaults to REDDIT_CLIENT_ID env var)
            client_secret: Reddit API client secret (defaults to REDDIT_CLIENT_SECRET env var)
            user_agent: User agent string (defaults to REDDIT_USER_AGENT env var)
            timeout: Request timeout in seconds (default: 10) [api_patterns-00002]
            rate_limit_delay: Delay between API calls in seconds (default: 1.0) [api_patterns-00004]
        """
        self.client_id = client_id or os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = user_agent or os.getenv("REDDIT_USER_AGENT", "RedditSummarizer/0.1.0")
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Reddit API credentials not provided. Set REDDIT_CLIENT_ID and "
                "REDDIT_CLIENT_SECRET environment variables or pass them to constructor."
            )

        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            timeout=self.timeout,  # Following api_patterns-00002
        )

    def _retry_with_backoff(
        self,
        func: Callable[..., T],
        max_retries: int = 3,
        initial_delay: float = 1.0,
        backoff_factor: float = 2.0,
    ) -> T:
        """
        Retry a function with exponential backoff for transient errors

        Args:
            func: Function to retry
            max_retries: Maximum number of retry attempts (default: 3)
            initial_delay: Initial delay in seconds (default: 1.0)
            backoff_factor: Multiplier for delay between retries (default: 2.0)

        Returns:
            Result from the function

        Raises:
            The last exception if all retries fail
        """
        delay = initial_delay
        last_exception = None

        for attempt in range(max_retries + 1):
            try:
                return func()
            except (ServerError, ResponseException) as e:
                last_exception = e
                if attempt < max_retries:
                    print(
                        f"⚠️  Transient error (attempt {attempt + 1}/{max_retries + 1}): {e}"
                    )
                    print(f"   Retrying in {delay:.1f}s...")
                    time.sleep(delay)
                    delay *= backoff_factor
                else:
                    print(f"❌ All retry attempts failed after {max_retries + 1} tries")
            except (NotFound, Forbidden, ValueError) as e:
                # Don't retry for permanent errors
                raise e

        # If we get here, all retries failed
        raise last_exception

    def fetch_posts(
        self,
        subreddit_name: str,
        start_date: datetime,
        end_date: datetime,
        min_upvotes: int = 100,
        min_comments: int = 30,
        max_posts: int = 100,
    ) -> List[RedditPost]:
        """
        Fetch posts from a subreddit within a date range that meet thresholds

        Args:
            subreddit_name: Name of the subreddit (without 'r/')
            start_date: Start of date range
            end_date: End of date range
            min_upvotes: Minimum upvotes threshold (default: 100)
            min_comments: Minimum comments threshold (default: 30)
            max_posts: Maximum number of posts to fetch (default: 100)

        Returns:
            List of RedditPost objects that meet the criteria

        Raises:
            ValueError: If subreddit name is invalid or parameters are invalid
            NotFound: If subreddit doesn't exist
            Forbidden: If subreddit is private or banned
            RequestException: If there are network or API errors
        """
        # Validate inputs
        if not subreddit_name or not subreddit_name.strip():
            raise ValueError("Subreddit name cannot be empty")

        if start_date >= end_date:
            raise ValueError("Start date must be before end date")

        if min_upvotes < 0 or min_comments < 0:
            raise ValueError("Thresholds cannot be negative")

        if max_posts <= 0:
            raise ValueError("max_posts must be positive")

        try:
            subreddit = self.reddit.subreddit(subreddit_name)

            # Test if subreddit exists and is accessible
            _ = subreddit.id  # This will raise NotFound or Forbidden if issues

            posts = []

            # Convert to Unix timestamps
            start_timestamp = start_date.timestamp()
            end_timestamp = end_date.timestamp()

            # Fetch posts sorted by top in the time range
            # PRAW doesn't have built-in date filtering, so we'll fetch more and filter
            for submission in subreddit.top(time_filter="all", limit=max_posts * 3):
                # Rate limiting: delay between fetches [api_patterns-00004]
                if len(posts) > 0:  # Don't delay on first fetch
                    time.sleep(self.rate_limit_delay)

                # Check if within date range
                if submission.created_utc < start_timestamp:
                    continue
                if submission.created_utc > end_timestamp:
                    continue

                # Check if meets thresholds
                if submission.score < min_upvotes:
                    continue
                if submission.num_comments < min_comments:
                    continue

                try:
                    post = RedditPost(
                        title=submission.title,
                        author=str(submission.author) if submission.author else "[deleted]",
                        url=submission.url,
                        selftext=submission.selftext,
                        score=submission.score,
                        num_comments=submission.num_comments,
                        created_utc=datetime.fromtimestamp(submission.created_utc),
                        permalink=submission.permalink,
                        post_id=submission.id,
                        subreddit=subreddit_name,
                    )
                    posts.append(post)
                except Exception as e:
                    # Skip individual posts that fail to parse
                    print(f"Warning: Failed to parse post {submission.id}: {e}")
                    continue

                # Stop if we've reached the max [api_patterns-00003]
                if len(posts) >= max_posts:
                    break

            # Sort by score (upvotes) descending
            posts.sort(key=lambda p: p.score, reverse=True)

            return posts

        except NotFound:
            raise NotFound(f"Subreddit r/{subreddit_name} does not exist")
        except Forbidden:
            raise Forbidden(f"Subreddit r/{subreddit_name} is private, banned, or quarantined")
        except (ServerError, ResponseException) as e:
            raise RequestException(f"Reddit API error: {e}. Please try again later.")
        except PRAWException as e:
            raise RequestException(f"Reddit API error: {e}")

    def fetch_post_comments(self, post: RedditPost, limit: int = 10) -> List[dict]:
        """
        Fetch top comments for a post with retry logic

        Args:
            post: RedditPost object
            limit: Maximum number of top-level comments to fetch

        Returns:
            List of comment dictionaries

        Raises:
            RequestException: If there are network or API errors
        """
        if limit <= 0:
            raise ValueError("limit must be positive")

        def _fetch_comments_impl() -> List[dict]:
            """Internal implementation wrapped by retry logic"""
            try:
                submission = self.reddit.submission(id=post.post_id)
                submission.comment_sort = "top"
                submission.comment_limit = limit

                comments = []
                for comment in submission.comments[:limit]:
                    if hasattr(comment, "body"):  # Skip MoreComments objects
                        try:
                            comments.append(
                                {
                                    "author": (
                                        str(comment.author) if comment.author else "[deleted]"
                                    ),
                                    "body": comment.body,
                                    "score": comment.score,
                                }
                            )
                        except Exception as e:
                            # Skip individual comments that fail to parse
                            print(f"Warning: Failed to parse comment: {e}")
                            continue

                return comments

            except (ServerError, ResponseException) as e:
                raise RequestException(
                    f"Reddit API error fetching comments: {e}. Please try again later."
                )
            except PRAWException as e:
                raise RequestException(f"Reddit API error fetching comments: {e}")

        # Use retry logic for robustness
        return self._retry_with_backoff(_fetch_comments_impl)
