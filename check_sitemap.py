#!/usr/bin/env python3
"""Check sitemap completeness against actual HTML files"""

from pathlib import Path
import re

# Read sitemap
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Extract URLs from sitemap (without .html extension as sitemap uses clean URLs)
sitemap_urls = set()
for match in re.finditer(r'<loc>https://www\.sorinpyle\.com/([^<]+)</loc>', sitemap_content):
    url = match.group(1)
    sitemap_urls.add(url)

# Get all HTML files
html_files = []
html_files.extend(Path('.').glob('*.html'))
html_files.extend(Path('.').glob('locations/*.html'))
html_files.extend(Path('.').glob('card/*.html'))

# Convert HTML files to expected sitemap URLs
expected_urls = set()
for filepath in html_files:
    rel_path = str(filepath).replace('\\', '/')

    # Skip backup files
    if rel_path.endswith('.bak'):
        continue

    # Convert to sitemap format (without .html)
    if rel_path == 'index.html':
        expected_urls.add('')  # Homepage is just /
    else:
        url = rel_path.replace('.html', '')
        expected_urls.add(url)

# Find missing from sitemap
missing_from_sitemap = expected_urls - sitemap_urls
# Find extra in sitemap (shouldn't happen but check)
extra_in_sitemap = sitemap_urls - expected_urls

print("SITEMAP COMPLETENESS CHECK")
print("=" * 80)
print(f"\nTotal HTML files: {len(expected_urls)}")
print(f"Total sitemap entries: {len(sitemap_urls)}")
print()

if missing_from_sitemap:
    print("MISSING FROM SITEMAP:")
    print("-" * 80)
    for url in sorted(missing_from_sitemap):
        if url:
            print(f"  - {url}")
        else:
            print(f"  - / (homepage)")
    print()

if extra_in_sitemap:
    print("EXTRA IN SITEMAP (no corresponding HTML file):")
    print("-" * 80)
    for url in sorted(extra_in_sitemap):
        print(f"  - {url}")
    print()

if not missing_from_sitemap and not extra_in_sitemap:
    print("✓ Sitemap is complete and accurate!")
