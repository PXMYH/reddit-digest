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
    Scan digest directory and return dict of ALL timeframe digests per subreddit.

    Returns:
        dict: {subreddit: {timeframe: filepath}}
              e.g., {'formula1': {'week': 'path/to/formula1-week.md', 'month': 'path/to/formula1-month.md'}}
    """
    digests = {}  # {subreddit: {timeframe: filepath}}

    # Pattern 1: New simple format (subreddit-timeframe.md)
    pattern1 = os.path.join(digest_dir, "*-*.md")
    for filepath in glob.glob(pattern1):
        filename = os.path.basename(filepath)
        match = re.match(r'(.+?)-(week|month|year)\.md$', filename)

        if match:
            subreddit = match.group(1)
            timeframe = match.group(2)

            if subreddit not in digests:
                digests[subreddit] = {}

            digests[subreddit][timeframe] = filepath

    # Pattern 2: Legacy date-based timeframe digests (subreddit_top_timeframe_date.md)
    pattern2 = os.path.join(digest_dir, "*_top_*_*.md")
    for filepath in glob.glob(pattern2):
        filename = os.path.basename(filepath)
        match = re.match(r'(.+?)_top_(week|month|year)_(\d{4}-\d{2}-\d{2})\.md$', filename)

        if match:
            subreddit = match.group(1)
            timeframe = match.group(2)
            date_str = match.group(3)
            date = datetime.strptime(date_str, '%Y-%m-%d')

            if subreddit not in digests:
                digests[subreddit] = {}

            # Only use legacy file if no new format exists for this subreddit/timeframe
            if timeframe not in digests[subreddit]:
                digests[subreddit][timeframe] = filepath

    return digests


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
    """Generate complete HTML page with tabbed interface and timeframe filtering.

    Args:
        digest_data: dict of {tab_id: parsed_digest_data}
        digest_metadata: dict of {tab_id: {'subreddit': str, 'timeframe': str}}
    """
    now = datetime.now().strftime('%Y-%m-%d %H:%M UTC')

    # Get unique subreddits and timeframes for organization
    subreddits = sorted(set(meta['subreddit'] for meta in digest_metadata.values()))

    # Define timeframe display order and labels
    timeframe_order = ['week', 'month', 'year']
    timeframe_labels = {'week': 'Weekly', 'month': 'Monthly', 'year': 'Yearly'}

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
                <option value="all">All Timeframes</option>
                <option value="week">Weekly</option>
                <option value="month">Monthly</option>
                <option value="year">Yearly</option>
            </select>
        </div>

        <div class="tabs">
"""

    # Generate tab buttons organized by subreddit, sorted by timeframe
    tab_ids = sorted(digest_data.keys(), key=lambda x: (
        digest_metadata[x]['subreddit'],
        timeframe_order.index(digest_metadata[x]['timeframe']) if digest_metadata[x]['timeframe'] in timeframe_order else 99
    ))

    first_tab = True
    for tab_id in tab_ids:
        meta = digest_metadata[tab_id]
        subreddit = meta['subreddit']
        timeframe = meta['timeframe']

        active_class = ' active' if first_tab else ''
        timeframe_label = timeframe_labels.get(timeframe, timeframe.title())
        display_name = f"{subreddit} ({timeframe_label})"

        html += f'            <button class="tab-button{active_class}" data-timeframe="{timeframe}" data-subreddit="{subreddit}" onclick="openTab(\'{tab_id}\')">{display_name}</button>\n'
        first_tab = False

    html += '        </div>\n\n'

    # Generate tab content for each digest
    first_tab = True
    for tab_id in tab_ids:
        data = digest_data[tab_id]
        active_class = ' active' if first_tab else ''
        html += f'        <div id="{tab_id}" class="tab-content{active_class}">\n'
        html += generate_digest_html(data)
        html += '        </div>\n\n'
        first_tab = False

    # Add scroll-to-top button (must be before script so getElementById can find it)
    html += '        <button id="scrollToTop" class="scroll-to-top" onclick="scrollToTop()" title="Scroll to top">↑</button>\n\n'

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

                // Find and activate the corresponding button
                var clickedButton = document.querySelector('[onclick="openTab(\\'' + tabName + '\\')"]');
                if (clickedButton) {
                    clickedButton.classList.add('active');
                }
            }

            function filterByTimeframe() {
                var selectedTimeframe = document.getElementById('timeframe-filter').value;
                var buttons = document.getElementsByClassName('tab-button');
                var firstVisibleButton = null;

                for (var i = 0; i < buttons.length; i++) {
                    var buttonTimeframe = buttons[i].getAttribute('data-timeframe');

                    if (selectedTimeframe === 'all' || buttonTimeframe === selectedTimeframe) {
                        buttons[i].style.display = '';
                        if (!firstVisibleButton) {
                            firstVisibleButton = buttons[i];
                        }
                    } else {
                        buttons[i].style.display = 'none';
                        // If this hidden button was active, we need to switch
                        if (buttons[i].classList.contains('active')) {
                            buttons[i].classList.remove('active');
                        }
                    }
                }

                // Check if any active button is still visible
                var activeButton = document.querySelector('.tab-button.active');
                var needsNewActive = !activeButton || activeButton.style.display === 'none';

                if (needsNewActive && firstVisibleButton) {
                    // Click the first visible button to activate it
                    var tabId = firstVisibleButton.getAttribute('onclick').match(/openTab\\('([^']+)'\\)/)[1];
                    openTab(tabId);
                    firstVisibleButton.classList.add('active');
                }
            }

            // Scroll to top functionality
            var scrollToTopBtn = document.getElementById('scrollToTop');
            window.addEventListener('scroll', function() {
                if (window.scrollY > 300) {
                    scrollToTopBtn.classList.add('visible');
                } else {
                    scrollToTopBtn.classList.remove('visible');
                }
            });

            function scrollToTop() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
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
        .scroll-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: #FF4500;
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(255, 69, 0, 0.4);
            transition: all 0.3s ease;
            opacity: 0;
            visibility: hidden;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .scroll-to-top:hover {
            background: #E03D00;
            transform: translateY(-3px);
            box-shadow: 0 6px 16px rgba(255, 69, 0, 0.5);
        }
        .scroll-to-top.visible {
            opacity: 1;
            visibility: visible;
        }
        @media (max-width: 768px) {
            h1 { font-size: 1.8em; }
            .tab-button { padding: 10px 16px; font-size: 0.9em; }
            .post { padding: 15px; }
        }
    </style>
    """


if __name__ == "__main__":
    print("🔍 Scanning digest files...")
    subreddit_digests = scan_digest_files()  # {subreddit: {timeframe: filepath}}

    if not subreddit_digests:
        print("❌ No digest files found in digest/ directory")
        exit(1)

    # Count total digests
    total_digests = sum(len(timeframes) for timeframes in subreddit_digests.values())
    print(f"✅ Found {total_digests} digests across {len(subreddit_digests)} subreddits")

    for subreddit, timeframes in sorted(subreddit_digests.items()):
        print(f"  - {subreddit}: {', '.join(sorted(timeframes.keys()))}")

    print("\n📖 Parsing digest content...")
    digest_data = {}  # {tab_id: parsed_content}
    digest_metadata = {}  # {tab_id: {'subreddit': str, 'timeframe': str}}

    for subreddit, timeframes in sorted(subreddit_digests.items()):
        for timeframe, filepath in sorted(timeframes.items()):
            tab_id = f"{subreddit}-{timeframe}"
            print(f"  - Parsing {tab_id}...")
            digest_data[tab_id] = parse_markdown_content(filepath)
            digest_metadata[tab_id] = {'subreddit': subreddit, 'timeframe': timeframe}

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
