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
        md = f"[{self.post.title}]({self.post.full_url})\n\n"
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

    def to_html(self) -> str:
        """Convert summary to HTML format"""
        html = '<div class="post-summary">\n'
        html += f'  <h3><a href="{self.post.full_url}">{self.post.title}</a></h3>\n'
        html += '  <div class="post-meta">\n'
        html += f'    <span class="author">u/{self.post.author}</span> | \n'
        html += f'    <span class="upvotes">▲ {self.post.score}</span> | \n'
        html += f'    <span class="comments">💬 {self.post.num_comments}</span> | \n'
        date = self.post.created_utc.strftime('%Y-%m-%d')
        html += f'    <span class="date">{date}</span>\n'
        html += '  </div>\n'
        html += f'  <p class="summary"><strong>Summary:</strong> {self.summary}</p>\n'

        if self.key_points:
            html += '  <div class="key-points">\n'
            html += '    <strong>Key Points:</strong>\n'
            html += '    <ul>\n'
            for point in self.key_points:
                html += f'      <li>{point}</li>\n'
            html += '    </ul>\n'
            html += '  </div>\n'

        if self.discussion_highlights:
            html += '  <p class="discussion"><strong>Discussion Highlights:</strong> '
            html += f'{self.discussion_highlights}</p>\n'

        html += '</div>\n'
        html += '<hr>\n'
        return html


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
        start = self.start_date.strftime('%Y-%m-%d')
        end = self.end_date.strftime('%Y-%m-%d')
        md += f"**Period:** {start} to {end}\n"
        md += f"**Posts Summarized:** {len(self.post_summaries)}\n"
        md += f"**Total Posts Analyzed:** {self.total_posts_analyzed}\n\n"
        md += "---\n\n"

        for i, summary in enumerate(self.post_summaries, 1):
            md += f"## {i}. "
            md += summary.to_markdown()

        return md

    def to_json(self) -> dict:
        """Convert digest to JSON-serializable dictionary"""
        return {
            "subreddit": self.subreddit,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "end_date": self.end_date.strftime('%Y-%m-%d'),
            "total_posts_analyzed": self.total_posts_analyzed,
            "posts_summarized": len(self.post_summaries),
            "summaries": [
                {
                    "title": summary.post.title,
                    "author": summary.post.author,
                    "url": summary.post.full_url,
                    "upvotes": summary.post.score,
                    "comments": summary.post.num_comments,
                    "date": summary.post.created_utc.strftime('%Y-%m-%d'),
                    "summary": summary.summary,
                    "key_points": summary.key_points,
                    "discussion_highlights": summary.discussion_highlights,
                }
                for summary in self.post_summaries
            ]
        }

    def to_html(self) -> str:
        """Convert digest to styled HTML format"""
        start = self.start_date.strftime('%Y-%m-%d')
        end = self.end_date.strftime('%Y-%m-%d')

        html = '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        html += '  <meta charset="UTF-8">\n'
        html += '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        html += f'  <title>r/{self.subreddit} Reading Digest</title>\n'
        html += '  <style>\n'
        html += '    body { font-family: -apple-system, system-ui, sans-serif; '
        html += 'max-width: 900px; margin: 0 auto; padding: 20px; '
        html += 'background: #f5f5f5; }\n'
        html += '    h1 { color: #ff4500; border-bottom: 3px solid #ff4500; '
        html += 'padding-bottom: 10px; }\n'
        html += '    .meta { color: #666; margin-bottom: 30px; }\n'
        html += '    .post-summary { background: white; padding: 20px; '
        html += 'margin-bottom: 20px; border-radius: 8px; '
        html += 'box-shadow: 0 2px 4px rgba(0,0,0,0.1); }\n'
        html += '    .post-summary h3 { margin-top: 0; color: #1a1a1b; }\n'
        html += '    .post-summary a { color: #0079d3; text-decoration: none; }\n'
        html += '    .post-summary a:hover { text-decoration: underline; }\n'
        html += '    .post-meta { color: #7c7c7c; font-size: 14px; margin-bottom: 15px; }\n'
        html += '    .summary { line-height: 1.6; }\n'
        html += '    .key-points ul { line-height: 1.8; }\n'
        html += '    .discussion { background: #f8f9fa; padding: 10px; '
        html += 'border-left: 3px solid #0079d3; margin-top: 15px; }\n'
        html += '    hr { border: none; border-top: 1px solid #edeff1; margin: 20px 0; }\n'
        html += '  </style>\n'
        html += '</head>\n<body>\n'
        html += f'  <h1>r/{self.subreddit} Reading Digest</h1>\n'
        html += '  <div class="meta">\n'
        html += f'    <strong>Period:</strong> {start} to {end}<br>\n'
        html += f'    <strong>Posts Summarized:</strong> {len(self.post_summaries)}<br>\n'
        html += f'    <strong>Total Posts Analyzed:</strong> {self.total_posts_analyzed}\n'
        html += '  </div>\n\n'

        for i, summary in enumerate(self.post_summaries, 1):
            html += f'  <div class="post-number">Post #{i}</div>\n'
            html += '  ' + summary.to_html().replace('\n', '\n  ')

        html += '</body>\n</html>\n'
        return html

    def save_to_file(self, filepath: str) -> None:
        """Save digest to markdown, JSON, or HTML file based on extension"""
        import json

        if filepath.endswith('.json'):
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.to_json(), f, indent=2, ensure_ascii=False)
        elif filepath.endswith('.html'):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self.to_html())
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self.to_markdown())
