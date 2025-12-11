"""
Reddit data fetcher using public JSON API (no authentication required)
"""

import time
from datetime import datetime
from typing import List, Optional, Callable, TypeVar
import requests
from .models import RedditPost

T = TypeVar("T")


class RedditFetcher:
    """Fetches posts from Reddit using public JSON API (no authentication required)"""

    def __init__(
        self,
        user_agent: str = "RedditSummarizer/1.0.0",
        timeout: int = 10,
        rate_limit_delay: float = 2.0,
    ):
        """
        Initialize Reddit JSON API client

        Args:
            user_agent: User agent string for requests (default: RedditSummarizer/1.0.0)
            timeout: Request timeout in seconds (default: 10) [api_patterns-00002]
            rate_limit_delay: Delay between API calls in seconds (default: 2.0) [api_patterns-00004]
        """
        self.user_agent = user_agent
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

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
            except (requests.Timeout, requests.ConnectionError) as e:
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
            except (ValueError, requests.HTTPError) as e:
                # Don't retry for permanent errors
                raise e

        # If we get here, all retries failed
        if last_exception:
            raise last_exception
        return func()  # One last try

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
        Fetch posts from a subreddit within a date range that meet thresholds using public JSON API

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
            requests.HTTPError: If subreddit doesn't exist or is inaccessible
            requests.RequestException: If there are network or API errors
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

        posts = []
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()

        # Reddit's public JSON API endpoint - use 'new' to get posts in time order
        # Note: Reddit's API doesn't support date filtering directly, so we fetch
        # posts sorted by 'new' and filter them by date locally
        url = f"https://www.reddit.com/r/{subreddit_name}/new.json"
        params = {"limit": 100}  # Fetch most recent posts
        after = None

        # Track if we've gone too far back in time
        posts_checked = 0
        max_posts_to_check = 1000  # Safety limit to avoid infinite loops

        # Fetch posts in batches using pagination
        while len(posts) < max_posts and posts_checked < max_posts_to_check:
            if after:
                params["after"] = after

            try:
                # Rate limiting: delay between API calls [api_patterns-00004]
                if after:
                    time.sleep(self.rate_limit_delay)

                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                data = response.json()

                if "data" not in data or "children" not in data["data"]:
                    break

                children = data["data"]["children"]
                if not children:
                    break

                # Track if we've gone past the start date (posts are in reverse chronological order)
                all_posts_too_old = True

                for child in children:
                    post_data = child["data"]
                    posts_checked += 1

                    # Check if within date range
                    created_utc = post_data.get("created_utc", 0)

                    # If post is newer than end_date, skip but keep looking
                    if created_utc > end_timestamp:
                        all_posts_too_old = False
                        continue

                    # If post is older than start_date, we can stop pagination
                    if created_utc < start_timestamp:
                        continue

                    # Post is in range!
                    all_posts_too_old = False

                    # Check if meets thresholds
                    score = post_data.get("score", 0)
                    num_comments = post_data.get("num_comments", 0)
                    if score < min_upvotes or num_comments < min_comments:
                        continue

                    try:
                        post = RedditPost(
                            title=post_data.get("title", ""),
                            author=post_data.get("author", "[deleted]"),
                            url=post_data.get("url", ""),
                            selftext=post_data.get("selftext", ""),
                            score=score,
                            num_comments=num_comments,
                            created_utc=datetime.fromtimestamp(created_utc),
                            permalink=post_data.get("permalink", ""),
                            post_id=post_data.get("id", ""),
                            subreddit=subreddit_name,
                        )
                        posts.append(post)
                    except Exception as e:
                        # Skip individual posts that fail to parse
                        print(f"Warning: Failed to parse post: {e}")
                        continue

                    # Stop if we've reached the max [api_patterns-00003]
                    if len(posts) >= max_posts:
                        break

                # If all posts in this batch were too old, we can stop pagination
                if all_posts_too_old:
                    break

                # Get next page token
                after = data["data"].get("after")
                if not after or len(posts) >= max_posts:
                    break

            except requests.HTTPError as e:
                if e.response.status_code == 404:
                    raise ValueError(f"Subreddit r/{subreddit_name} does not exist")
                elif e.response.status_code == 403:
                    raise ValueError(
                        f"Subreddit r/{subreddit_name} is private, banned, or quarantined"
                    )
                else:
                    raise requests.RequestException(f"Reddit API error: {e}")
            except requests.RequestException as e:
                raise requests.RequestException(f"Reddit API error: {e}")

        # Sort by score (upvotes) descending
        posts.sort(key=lambda p: p.score, reverse=True)
        return posts

    def fetch_post_comments(self, post: RedditPost, limit: int = 10) -> List[dict]:
        """
        Fetch top comments for a post using public JSON API with retry logic

        Args:
            post: RedditPost object
            limit: Maximum number of top-level comments to fetch

        Returns:
            List of comment dictionaries

        Raises:
            requests.RequestException: If there are network or API errors
        """
        if limit <= 0:
            raise ValueError("limit must be positive")

        def _fetch_comments_impl() -> List[dict]:
            """Internal implementation wrapped by retry logic"""
            try:
                # Reddit's public JSON API for comments
                url = f"https://www.reddit.com{post.permalink}.json"
                params = {"limit": limit, "sort": "top"}

                response = self.session.get(url, params=params, timeout=self.timeout)
                response.raise_for_status()
                data = response.json()

                comments = []

                # Comments are in the second listing
                if len(data) >= 2 and "data" in data[1] and "children" in data[1]["data"]:
                    for child in data[1]["data"]["children"][:limit]:
                        if child["kind"] == "t1":  # t1 = comment
                            comment_data = child["data"]
                            try:
                                comments.append(
                                    {
                                        "author": comment_data.get("author", "[deleted]"),
                                        "body": comment_data.get("body", ""),
                                        "score": comment_data.get("score", 0),
                                    }
                                )
                            except Exception as e:
                                # Skip individual comments that fail to parse
                                print(f"Warning: Failed to parse comment: {e}")
                                continue

                return comments

            except requests.RequestException as e:
                raise requests.RequestException(
                    f"Reddit API error fetching comments: {e}. Please try again later."
                )

        # Use retry logic for robustness
        return self._retry_with_backoff(_fetch_comments_impl)
