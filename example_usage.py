#!/usr/bin/env python3
"""
Example usage of the Reddit Subreddit Summarizer

This script demonstrates how to use the RedditFetcher and RedditSummarizer
programmatically in your own Python code.
"""

from datetime import datetime, timedelta
from dotenv import load_dotenv
from reddit_summarizer import RedditFetcher, RedditSummarizer

# Load environment variables
load_dotenv()


def main():
    """Example usage of the Reddit summarizer"""

    # Configuration
    subreddit_name = "python"
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)  # Last 7 days

    print("🤖 Reddit Subreddit Summarizer - Example Usage\n")
    print(f"Subreddit: r/{subreddit_name}")
    print(f"Date range: {start_date.date()} to {end_date.date()}\n")

    # Step 1: Initialize the Reddit fetcher
    print("1. Initializing Reddit fetcher...")
    fetcher = RedditFetcher()

    # Step 2: Fetch posts
    print("2. Fetching posts...")
    posts = fetcher.fetch_posts(
        subreddit_name=subreddit_name,
        start_date=start_date,
        end_date=end_date,
        min_upvotes=100,
        min_comments=30,
        max_posts=10,  # Limit to 10 for demo
    )

    print(f"   Found {len(posts)} posts\n")

    if not posts:
        print("⚠️  No posts found matching criteria")
        return

    # Step 3: Initialize the summarizer
    print("3. Initializing ACE-powered summarizer...")
    summarizer = RedditSummarizer(
        model="gpt-4o-mini",  # Fast and cost-effective
        skillbook_path=None,  # Start with empty skillbook
    )

    # Step 4: Generate summaries
    print("4. Generating summaries with AI...\n")
    digest = summarizer.generate_digest(
        posts=posts,
        subreddit=subreddit_name,
        start_date=start_date,
        end_date=end_date,
        include_comments=True,
    )

    # Step 5: Save the digest
    output_file = f"{subreddit_name}_example_digest.md"
    digest.save_to_file(output_file)
    print(f"\n✅ Digest saved to: {output_file}")

    # Step 6: Display stats
    print(f"\n📊 Summary:")
    print(f"   Posts analyzed: {digest.total_posts_analyzed}")
    print(f"   Posts summarized: {len(digest.post_summaries)}")

    # Step 7: Display skillbook stats
    summarizer.print_skillbook_stats()

    # Optional: Save skillbook for reuse
    skillbook_file = "example_skillbook.json"
    summarizer.save_skillbook(skillbook_file)

    print(f"\n✨ Done! Check {output_file} for your reading digest.")

    # Example: Print first summary
    if digest.post_summaries:
        print("\n" + "=" * 70)
        print("SAMPLE OUTPUT (First Post Summary):")
        print("=" * 70)
        print(digest.post_summaries[0].to_markdown())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
