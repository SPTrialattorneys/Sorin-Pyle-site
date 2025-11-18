#!/usr/bin/env python3
"""
Fix footer indentation across all HTML files.
This script standardizes the indentation of footer_disclaimer and footer_bottom-bar divs.
"""

import os
import re
from pathlib import Path

def fix_footer_indentation(file_path):
    """Fix footer indentation in a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: Fix footer_disclaimer with incorrect indentation
        # Look for any amount of whitespace before <div class="footer_disclaimer">
        # and replace with exactly 12 spaces
        content = re.sub(
            r'^(\s*)<div class="footer_disclaimer">',
            r'            <div class="footer_disclaimer">',
            content,
            flags=re.MULTILINE
        )

        # Pattern 2: Fix footer_bottom-bar with incorrect indentation
        # Look for any amount of whitespace before <div class="footer_bottom-bar">
        # and replace with exactly 12 spaces
        content = re.sub(
            r'^(\s*)<div class="footer_bottom-bar">',
            r'            <div class="footer_bottom-bar">',
            content,
            flags=re.MULTILINE
        )

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix footer indentation across all HTML files."""
    # Get the script directory
    script_dir = Path(__file__).parent

    # List of all HTML files with footer_disclaimer
    html_files = [
        '404.html',
        '500.html',
        'accessibility.html',
        'attorneys.html',
        'blog.html',
        'cdl-owi-defense.html',
        'community-resources.html',
        'contact.html',
        'domestic-violence-defense.html',
        'drivers-license-restoration.html',
        'dui-defense.html',
        'faq.html',
        'first-offense-owi.html',
        'index.html',
        'jonathan-pyle.html',
        'locations/allegan-county.html',
        'locations/allendale-mi.html',
        'locations/calvin-university-student-defense.html',
        'locations/davenport-student-defense.html',
        'locations/ferris-student-defense.html',
        'locations/grand-haven-mi.html',
        'locations/grand-rapids-mi.html',
        'locations/grandville-mi.html',
        'locations/grcc-student-defense.html',
        'locations/gvsu-student-defense.html',
        'locations/holland-mi.html',
        'locations/hope-college-student-defense.html',
        'locations/hudsonville-mi.html',
        'locations/jenison-mi.html',
        'locations/kalamazoo-county.html',
        'locations/kent-county.html',
        'locations/kentwood-mi.html',
        'locations/muskegon-county.html',
        'locations/newaygo-county.html',
        'locations/other-michigan-counties.html',
        'locations/ottawa-county.html',
        'locations/saugatuck-mi.html',
        'locations/south-haven-mi.html',
        'locations/van-buren-county.html',
        'locations/walker-mi.html',
        'locations/wmu-student-defense.html',
        'locations/wyoming-mi.html',
        'locations/zeeland-mi.html',
        'locations.html',
        'practice-areas.html',
        'privacy-policy.html',
        'record-expungement.html',
        'repeat-offense-owi.html',
        'resources.html',
        'sorin-panainte.html',
        'super-drunk-high-bac.html',
        'your-rights.html'
    ]

    updated_count = 0
    skipped_count = 0

    print("Starting footer indentation fix...")
    print(f"Processing {len(html_files)} HTML files...\n")

    for html_file in html_files:
        file_path = script_dir / html_file

        if not file_path.exists():
            print(f"[WARN] File not found: {html_file}")
            skipped_count += 1
            continue

        if fix_footer_indentation(file_path):
            print(f"[FIXED] {html_file}")
            updated_count += 1
        else:
            print(f"[SKIP] {html_file}")
            skipped_count += 1

    print(f"\n{'='*60}")
    print(f"Footer indentation fix complete!")
    print(f"{'='*60}")
    print(f"Files updated: {updated_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Total files processed: {len(html_files)}")

if __name__ == '__main__':
    main()
