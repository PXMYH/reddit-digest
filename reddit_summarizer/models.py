"""
Data models for Reddit subreddit summarizer
"""

from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class RedditPost:
    """Represents a Reddit post with relevant metadata"""

    title: str
    author: str
    url: str
    selftext: str
    score: int  # upvotes
    num_comments: int
    created_utc: datetime
    permalink: str
    post_id: str
    subreddit: str

    @property
    def full_url(self) -> str:
        """Get the full Reddit URL"""
        return f"https://reddit.com{self.permalink}"

    def meets_threshold(self, min_upvotes: int = 100, min_comments: int = 30) -> bool:
        """Check if post meets importance thresholds"""
        return self.score >= min_upvotes and self.num_comments >= min_comments

    def to_dict(self) -> dict[str, str | int]:
        """Convert to dictionary for processing"""
        return {
            "title": self.title,
            "author": self.author,
            "content": (
                self.selftext[:1000] if self.selftext else "[Link Post]"
            ),  # Truncate long posts
            "upvotes": self.score,
            "comments": self.num_comments,
            "url": self.full_url,
            "date": self.created_utc.strftime("%Y-%m-%d"),
        }


@dataclass
class PostSummary:
    """Represents a summarized Reddit post"""

    post: RedditPost
    summary: str
    key_points: List[str]
    discussion_highlights: Optional[str] = None

    def to_markdown(self) -> str:
        """Convert summary to markdown format"""
        md = f"### [{self.post.title}]({self.post.full_url})\n\n"
        md += f"**Author:** u/{self.post.author} | "
        md += f"**Upvotes:** {self.post.score} | "
        md += f"**Comments:** {self.post.num_comments} | "
        md += f"**Date:** {self.post.created_utc.strftime('%Y-%m-%d')}\n\n"

        md += f"**Summary:** {self.summary}\n\n"

        if self.key_points:
            md += "**Key Points:**\n"
            for point in self.key_points:
                md += f"- {point}\n"
            md += "\n"

        if self.discussion_highlights:
            md += f"**Discussion Highlights:** {self.discussion_highlights}\n\n"

        md += "---\n\n"
        return md


@dataclass
class SubredditDigest:
    """Represents a complete digest of a subreddit"""

    subreddit: str
    start_date: datetime
    end_date: datetime
    post_summaries: List[PostSummary]
    total_posts_analyzed: int

    def to_markdown(self) -> str:
        """Convert digest to markdown format"""
        md = f"# r/{self.subreddit} Reading Digest\n\n"
        md += f"**Period:** {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}\n"
        md += f"**Posts Summarized:** {len(self.post_summaries)}\n"
        md += f"**Total Posts Analyzed:** {self.total_posts_analyzed}\n\n"
        md += "---\n\n"

        for i, summary in enumerate(self.post_summaries, 1):
            md += f"## {i}. "
            md += summary.to_markdown()

        return md

    def save_to_file(self, filepath: str) -> None:
        """Save digest to a markdown file"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_markdown())
