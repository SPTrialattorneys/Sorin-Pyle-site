#!/usr/bin/env python3
"""
HTML Validation Test Script for Sorin & Pyle Website
Phase 1: Pre-Launch HTML Validation & Structure Audit
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Base directory
BASE_DIR = Path(r"C:\Users\jonpy\Downloads\S&P\sorin-pyle-site-html")

# Files to check (excluding backups and card subdirectory)
HTML_FILES = []
for pattern in ["*.html", "locations/*.html"]:
    HTML_FILES.extend(BASE_DIR.glob(pattern))

# Filter out backup files
HTML_FILES = [f for f in HTML_FILES if not any(x in f.name for x in ['.bak', '.backup', 'card/'])]

class HTMLValidator:
    def __init__(self):
        self.critical_errors = []
        self.high_priority = []
        self.medium_priority = []
        self.passes = []

    def check_heading_hierarchy(self, filepath):
        """Check for proper h1-h6 structure"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count h1 tags
        h1_tags = re.findall(r'<h1[^>]*>', content)
        if len(h1_tags) == 0:
            self.critical_errors.append(f"{filepath.name}: NO H1 TAG FOUND")
        elif len(h1_tags) > 1:
            self.critical_errors.append(f"{filepath.name}: MULTIPLE H1 TAGS ({len(h1_tags)} found)")

        # Check for skipped heading levels
        headings = re.findall(r'<h([1-6])[^>]*>', content)
        headings = [int(h) for h in headings]

        for i in range(len(headings) - 1):
            if headings[i+1] > headings[i] + 1:
                self.high_priority.append(f"{filepath.name}: Skipped heading level (h{headings[i]} to h{headings[i+1]})")

    def check_broken_links(self, filepath):
        """Check for broken internal links"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all internal HTML links
        links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)

        is_location_file = 'locations' in str(filepath)

        for link in links:
            # Skip external links and anchors
            if link.startswith('http') or link.startswith('#'):
                continue

            # Resolve path
            if is_location_file:
                if link.startswith('../'):
                    target_path = BASE_DIR / link.replace('../', '')
                else:
                    target_path = BASE_DIR / 'locations' / link
            else:
                if link.startswith('/'):
                    target_path = BASE_DIR / link.lstrip('/')
                else:
                    target_path = BASE_DIR / link

            # Check if file exists
            if not target_path.exists():
                self.critical_errors.append(f"{filepath.name}: BROKEN LINK -> {link} (target: {target_path.name})")

    def check_old_navigation_links(self, filepath):
        """Check for outdated navigation links"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Old links that should now redirect
        old_patterns = [
            (r'href=["\']resources\.html["\']', 'resources.html (should use dropdown: faq.html, blog.html, your-rights.html)'),
            (r'href=["\']local-resources\.html["\']', 'local-resources.html (renamed to community-resources.html)'),
        ]

        for pattern, message in old_patterns:
            if re.search(pattern, content):
                self.high_priority.append(f"{filepath.name}: OLD NAVIGATION LINK -> {message}")

    def check_duplicate_ids(self, filepath):
        """Check for duplicate ID attributes"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all IDs
        ids = re.findall(r'id=["\']([^"\']+)["\']', content)
        id_counts = defaultdict(int)
        for id_val in ids:
            id_counts[id_val] += 1

        duplicates = {k: v for k, v in id_counts.items() if v > 1}
        if duplicates:
            for id_val, count in duplicates.items():
                self.high_priority.append(f"{filepath.name}: DUPLICATE ID '{id_val}' used {count} times")

    def check_missing_alt_text(self, filepath):
        """Check for images missing alt attributes"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find img tags without alt attribute
        img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
        for img in img_tags:
            if 'alt=' not in img:
                self.high_priority.append(f"{filepath.name}: IMAGE MISSING ALT TEXT")
                break  # Only report once per file

    def check_unclosed_tags(self, filepath):
        """Basic check for unclosed tags"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count opening and closing tags for major elements
        elements = ['div', 'section', 'main', 'header', 'footer', 'nav', 'ul', 'ol']
        for elem in elements:
            opening = len(re.findall(f'<{elem}[\\s>]', content, re.IGNORECASE))
            closing = len(re.findall(f'</{elem}>', content, re.IGNORECASE))
            if opening != closing:
                self.critical_errors.append(
                    f"{filepath.name}: UNCLOSED <{elem}> TAG (found {opening} opening, {closing} closing)"
                )

    def check_semantic_html(self, filepath):
        """Check for proper semantic HTML structure"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for main tag
        if '<main' not in content:
            self.medium_priority.append(f"{filepath.name}: Missing <main> landmark element")

        # Check for skip link
        if 'skip-link' not in content and '404.html' not in str(filepath) and '500.html' not in str(filepath):
            self.medium_priority.append(f"{filepath.name}: Missing skip-to-content link")

    def check_path_consistency(self, filepath):
        """Check for correct ../ usage in location files"""
        is_location_file = 'locations' in str(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if is_location_file:
            # Location files SHOULD use ../
            root_links = ['href="images/', 'href="css/', 'href="js/', 'src="images/', 'src="css/', 'src="js/']
            for link_pattern in root_links:
                if link_pattern in content:
                    self.critical_errors.append(
                        f"{filepath.name}: INCORRECT PATH - Location file using '{link_pattern}' instead of '../{link_pattern.split('\"')[1]}'"
                    )
        else:
            # Root files should NOT use ../
            if '../' in content:
                # Exception: links to locations/ subfolder are ok
                bad_paths = re.findall(r'href=["\'](\.\./(?!locations)[^"\']+)["\']', content)
                if bad_paths:
                    self.critical_errors.append(
                        f"{filepath.name}: INCORRECT PATH - Root file using '../' for: {bad_paths[0]}"
                    )

    def validate_file(self, filepath):
        """Run all validation checks on a single file"""
        self.check_heading_hierarchy(filepath)
        self.check_broken_links(filepath)
        self.check_old_navigation_links(filepath)
        self.check_duplicate_ids(filepath)
        self.check_missing_alt_text(filepath)
        self.check_unclosed_tags(filepath)
        self.check_semantic_html(filepath)
        self.check_path_consistency(filepath)

    def print_report(self, total_files):
        """Print validation report"""
        print("\n" + "="*80)
        print("SORIN & PYLE WEBSITE - PHASE 1 HTML VALIDATION REPORT")
        print("="*80 + "\n")

        print(f"Total Pages Reviewed: {total_files}")
        print(f"Critical Errors: {len(self.critical_errors)}")
        print(f"High Priority Issues: {len(self.high_priority)}")
        print(f"Medium Priority Issues: {len(self.medium_priority)}")
        print("\n" + "-"*80 + "\n")

        if self.critical_errors:
            print("CRITICAL ERRORS (must fix before launch):")
            print("-" * 80)
            for error in sorted(self.critical_errors):
                print(f"  X {error}")
            print()

        if self.high_priority:
            print("HIGH PRIORITY (should fix soon):")
            print("-" * 80)
            for issue in sorted(self.high_priority):
                print(f"  ! {issue}")
            print()

        if self.medium_priority:
            print("MEDIUM PRIORITY (improvement opportunities):")
            print("-" * 80)
            for issue in sorted(self.medium_priority):
                print(f"  - {issue}")
            print()

        if not self.critical_errors and not self.high_priority and not self.medium_priority:
            print("ALL VALIDATION TESTS PASSED!")
            print("No critical errors, high priority issues, or medium priority issues found.")

        print("\n" + "="*80)
        print("END OF VALIDATION REPORT")
        print("="*80 + "\n")


def main():
    validator = HTMLValidator()

    print(f"Scanning {len(HTML_FILES)} HTML files...\n")

    for filepath in HTML_FILES:
        validator.validate_file(filepath)

    validator.print_report(len(HTML_FILES))


if __name__ == "__main__":
    main()
