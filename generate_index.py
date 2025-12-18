#!/usr/bin/env python3
"""
Generate index.html for GitHub Pages from Reddit digest markdown files.
Displays latest digest per subreddit in a tabbed interface with warm orange theme.
"""

import os
import re
import glob
from datetime import datetime
from html import escape
from pathlib import Path


def scan_digest_files(digest_dir="digest"):
    """
    Scan digest directory and return dict of latest digest per subreddit.

    Returns:
        dict: {subreddit: (filepath, end_date, timeframe)}
    """
    digests = {}

    # Pattern 1: Date range digests (subreddit_digest_start_to_end.md)
    pattern1 = os.path.join(digest_dir, "*_digest_*_to_*.md")
    for filepath in glob.glob(pattern1):
        filename = os.path.basename(filepath)
        match = re.match(r'(.+?)_digest_\d{4}-\d{2}-\d{2}_to_(\d{4}-\d{2}-\d{2})\.md$', filename)

        if match:
            subreddit = match.group(1)
            end_date_str = match.group(2)
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            # Keep latest digest per subreddit
            if subreddit not in digests or end_date > digests[subreddit][1]:
                digests[subreddit] = (filepath, end_date, None)  # None = date range mode

    # Pattern 2: Timeframe digests (subreddit_top_timeframe_date.md)
    pattern2 = os.path.join(digest_dir, "*_top_*_*.md")
    for filepath in glob.glob(pattern2):
        filename = os.path.basename(filepath)
        match = re.match(r'(.+?)_top_(hour|day|week|month|year|all)_(\d{4}-\d{2}-\d{2})\.md$', filename)

        if match:
            subreddit = match.group(1)
            timeframe = match.group(2)
            date_str = match.group(3)
            date = datetime.strptime(date_str, '%Y-%m-%d')

            # Keep latest digest per subreddit (comparing with existing)
            if subreddit not in digests or date > digests[subreddit][1]:
                digests[subreddit] = (filepath, date, timeframe)

    return {sub: (info[0], info[2]) for sub, info in digests.items()}  # Return (filepath, timeframe)


def parse_markdown_content(filepath):
    """
    Parse markdown digest file and extract structured content.

    Returns:
        dict: {
            'subreddit': str,
            'period': str,
            'posts_count': int,
            'posts': [{'title', 'link', 'author', 'upvotes', 'comments', 'date',
                       'summary', 'key_points', 'discussion'}]
        }
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract header info
    subreddit_match = re.search(r'# r/(\w+) Reading Digest', content)
    period_match = re.search(r'\*\*Period:\*\* (.+)', content)
    posts_match = re.search(r'\*\*Posts Summarized:\*\* (\d+)', content)

    data = {
        'subreddit': subreddit_match.group(1) if subreddit_match else 'Unknown',
        'period': period_match.group(1) if period_match else 'Unknown',
        'posts_count': int(posts_match.group(1)) if posts_match else 0,
        'posts': []
    }

    # Split by post sections (## N. ...)
    post_sections = re.split(r'\n## \d+\. ', content)[1:]  # Skip header

    for section in post_sections:
        post = parse_post_section(section)
        if post:
            data['posts'].append(post)

    return data


def parse_post_section(section):
    """Parse individual post section from markdown."""
    post = {}

    # Extract title and link
    title_match = re.match(r'\[(.+?)\]\((.+?)\)', section)
    if title_match:
        post['title'] = title_match.group(1)
        post['link'] = title_match.group(2)
    else:
        return None

    # Extract metadata
    author_match = re.search(r'\*\*Author:\*\* u/(\w+)', section)
    upvotes_match = re.search(r'\*\*Upvotes:\*\* ([\d,]+)', section)
    comments_match = re.search(r'\*\*Comments:\*\* (\d+)', section)
    date_match = re.search(r'\*\*Date:\*\* (\d{4}-\d{2}-\d{2})', section)

    post['author'] = author_match.group(1) if author_match else 'Unknown'
    post['upvotes'] = upvotes_match.group(1) if upvotes_match else '0'
    post['comments'] = comments_match.group(1) if comments_match else '0'
    post['date'] = date_match.group(1) if date_match else 'Unknown'

    # Extract summary
    summary_match = re.search(r'\*\*Summary:\*\* (.+?)(?=\n\*\*|$)', section, re.DOTALL)
    post['summary'] = summary_match.group(1).strip() if summary_match else ''

    # Extract key points
    key_points = []
    key_points_match = re.search(r'\*\*Key Points:\*\*\n((?:- .+\n?)+)', section)
    if key_points_match:
        for line in key_points_match.group(1).strip().split('\n'):
            if line.startswith('- '):
                key_points.append(line[2:].strip())
    post['key_points'] = key_points

    # Extract discussion highlights
    discussion_match = re.search(r'\*\*Discussion Highlights:\*\* (.+?)(?=\n---|$)', section, re.DOTALL)
    post['discussion'] = discussion_match.group(1).strip() if discussion_match else ''

    return post


def generate_html(digest_data, digest_metadata):
    """Generate complete HTML page with tabbed interface and timeframe filtering."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M UTC')
    subreddits = sorted(digest_data.keys())

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reddit Digest Reader</title>
    {generate_css()}
</head>
<body>
    <header>
        <div class="container">
            <h1>🔥 Reddit Digest Reader</h1>
            <div class="last-updated">Last Updated: {now}</div>
        </div>
    </header>

    <div class="container">
        <div class="filter-controls">
            <label for="timeframe-filter">Filter by timeframe:</label>
            <select id="timeframe-filter" onchange="filterByTimeframe()">
                <option value="week">Top - Week</option>
                <option value="month">Top - Month</option>
                <option value="year">Top - Year</option>
                <option value="all-time">Top - All Time</option>
            </select>
        </div>

        <div class="tabs">
"""

    # Generate tab buttons with data-timeframe attribute
    for i, subreddit in enumerate(subreddits):
        active_class = ' active' if i == 0 else ''
        timeframe = digest_metadata.get(subreddit, None)
        timeframe_attr = f' data-timeframe="{timeframe}"' if timeframe else ' data-timeframe="date-range"'
        html += f'            <button class="tab-button{active_class}"{timeframe_attr} onclick="openTab(\'{subreddit}\')">{subreddit}</button>\n'

    html += '        </div>\n\n'

    # Generate tab content for each subreddit
    for i, subreddit in enumerate(subreddits):
        data = digest_data[subreddit]
        active_class = ' active' if i == 0 else ''
        html += f'        <div id="{subreddit}" class="tab-content{active_class}">\n'
        html += generate_digest_html(data)
        html += '        </div>\n\n'

    # Add JavaScript for tabs and filtering
    html += """        <script>
            function openTab(tabName) {
                // Hide all tab content
                var tabs = document.getElementsByClassName('tab-content');
                for (var i = 0; i < tabs.length; i++) {
                    tabs[i].classList.remove('active');
                }

                // Remove active class from all buttons
                var buttons = document.getElementsByClassName('tab-button');
                for (var i = 0; i < buttons.length; i++) {
                    buttons[i].classList.remove('active');
                }

                // Show selected tab and mark button as active
                document.getElementById(tabName).classList.add('active');
                event.currentTarget.classList.add('active');
            }

            function filterByTimeframe() {
                var selectedTimeframe = document.getElementById('timeframe-filter').value;
                var buttons = document.getElementsByClassName('tab-button');
                var visibleButtons = [];

                // Filter tab buttons based on selected timeframe
                for (var i = 0; i < buttons.length; i++) {
                    var button = buttons[i];
                    var buttonTimeframe = button.getAttribute('data-timeframe');

                    if (selectedTimeframe === 'all-time' && buttonTimeframe === 'all') {
                        button.style.display = '';
                        visibleButtons.push(button);
                    } else if (buttonTimeframe === selectedTimeframe) {
                        button.style.display = '';
                        visibleButtons.push(button);
                    } else {
                        button.style.display = 'none';  // Hide
                    }
                }

                // Activate the first visible button if current tab is hidden
                if (visibleButtons.length > 0) {
                    var activeButton = document.querySelector('.tab-button.active');
                    if (!activeButton || activeButton.style.display === 'none') {
                        visibleButtons[0].click();
                    }
                }
            }
        </script>
    </div>
</body>
</html>"""

    return html


def generate_digest_html(data):
    """Generate HTML for a single subreddit digest."""
    html = f"""            <div class="digest-header">
                <h2>r/{escape(data['subreddit'])} Reading Digest</h2>
                <div class="digest-meta">
                    <strong>Period:</strong> {escape(data['period'])} |
                    <strong>Posts:</strong> {data['posts_count']}
                </div>
            </div>

"""

    for i, post in enumerate(data['posts'], 1):
        html += f"""            <div class="post">
                <div class="post-title">
                    {i}. <a href="{escape(post['link'])}" target="_blank">{escape(post['title'])}</a>
                </div>
                <div class="post-meta">
                    <strong>Author:</strong> u/{escape(post['author'])} |
                    <strong>Upvotes:</strong> {escape(post['upvotes'])} |
                    <strong>Comments:</strong> {escape(post['comments'])} |
                    <strong>Date:</strong> {escape(post['date'])}
                </div>
                <div class="post-summary">{escape(post['summary'])}</div>
"""

        if post['key_points']:
            html += """                <div class="key-points">
                    <h4>Key Points</h4>
                    <ul>
"""
            for point in post['key_points']:
                html += f"                        <li>{escape(point)}</li>\n"
            html += """                    </ul>
                </div>
"""

        if post['discussion']:
            html += f"""                <div class="discussion">
                    <h4>Discussion Highlights</h4>
                    <p>{escape(post['discussion'])}</p>
                </div>
"""

        html += "            </div>\n\n"

    return html


def generate_css():
    """Generate embedded CSS with orange/warm theme."""
    return """
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #FFF8F0;
            color: #1A1A1B;
            line-height: 1.6;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .filter-controls {
            background: white;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .filter-controls label {
            font-weight: 600;
            color: #1a1a1b;
        }
        .filter-controls select {
            padding: 8px 12px;
            border: 2px solid #e0e0e0;
            border-radius: 4px;
            font-size: 14px;
            background: white;
            cursor: pointer;
            transition: border-color 0.2s;
        }
        .filter-controls select:hover {
            border-color: #FF4500;
        }
        .filter-controls select:focus {
            outline: none;
            border-color: #FF4500;
            box-shadow: 0 0 0 2px rgba(255, 69, 0, 0.1);
        }
        header {
            background: linear-gradient(135deg, #FF4500 0%, #FF8B60 100%);
            color: white;
            padding: 30px 0;
            margin-bottom: 30px;
            box-shadow: 0 2px 8px rgba(255, 69, 0, 0.2);
        }
        h1 { font-size: 2.5em; text-align: center; margin-bottom: 10px; }
        .last-updated { text-align: center; opacity: 0.9; font-size: 0.95em; }
        .tabs {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .tab-button {
            padding: 12px 24px;
            border: none;
            background: #f0f0f0;
            color: #1A1A1B;
            cursor: pointer;
            border-radius: 6px;
            font-size: 1em;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        .tab-button:hover { background: #FFE5D9; }
        .tab-button.active {
            background: #FF4500;
            color: white;
            box-shadow: 0 2px 6px rgba(255, 69, 0, 0.3);
        }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        .digest-header {
            background: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #FF4500;
        }
        .digest-header h2 { color: #FF4500; margin-bottom: 15px; }
        .digest-meta { color: #666; font-size: 0.95em; }
        .post {
            background: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: box-shadow 0.3s ease;
        }
        .post:hover { box-shadow: 0 4px 12px rgba(255, 69, 0, 0.15); }
        .post-title {
            font-size: 1.3em;
            margin-bottom: 10px;
        }
        .post-title a {
            color: #0079D3;
            text-decoration: none;
            font-weight: 600;
        }
        .post-title a:hover { text-decoration: underline; }
        .post-meta {
            color: #666;
            font-size: 0.9em;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }
        .post-summary { margin-bottom: 15px; }
        .key-points {
            background: #FFF8F0;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 15px;
        }
        .key-points h4 { color: #FF4500; margin-bottom: 10px; font-size: 1em; }
        .key-points ul { margin-left: 20px; }
        .key-points li { margin-bottom: 5px; }
        .discussion {
            background: #F8F9FA;
            padding: 15px;
            border-radius: 6px;
            border-left: 3px solid #0079D3;
        }
        .discussion h4 { color: #0079D3; margin-bottom: 8px; font-size: 1em; }
        @media (max-width: 768px) {
            h1 { font-size: 1.8em; }
            .tab-button { padding: 10px 16px; font-size: 0.9em; }
            .post { padding: 15px; }
        }
    </style>
    """


if __name__ == "__main__":
    print("🔍 Scanning digest files...")
    latest_digests = scan_digest_files()

    if not latest_digests:
        print("❌ No digest files found in digest/ directory")
        exit(1)

    print(f"✅ Found {len(latest_digests)} subreddits: {', '.join(sorted(latest_digests.keys()))}")

    print("\n📖 Parsing digest content...")
    digest_data = {}
    digest_metadata = {}  # Track timeframe per subreddit
    for subreddit, (filepath, timeframe) in sorted(latest_digests.items()):
        print(f"  - Parsing {subreddit}...")
        digest_data[subreddit] = parse_markdown_content(filepath)
        digest_metadata[subreddit] = timeframe

    print("\n🎨 Generating HTML...")
    html_content = generate_html(digest_data, digest_metadata)

    # Create docs directory if it doesn't exist
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    # Write HTML file
    output_path = docs_dir / "index.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ Successfully generated {output_path}")
    print(f"📊 Total posts: {sum(len(d['posts']) for d in digest_data.values())}")
    print("\n🌐 Ready for GitHub Pages!")
