#!/usr/bin/env python3
"""
Add accessibility statement link to all page footers.
This script adds a link to accessibility.html in the footer Quick Links section.
"""

import os
import glob

# Get all HTML files
root_files = glob.glob('*.html')
location_files = glob.glob('locations/*.html')
card_files = glob.glob('card/*.html')

# Exclude the files we just created and error pages
exclude_files = ['accessibility.html', '404.html', '500.html']
root_files = [f for f in root_files if f not in exclude_files]

# Old footer patterns to look for
OLD_PATTERN_1 = '''                <h3>Quick Links</h3>
                <ul class="footer_list">
                    <li><a href="index.html">About</a></li>
                    <li><a href="attorneys.html">Attorneys</a></li>
                    <li><a href="practice-areas.html">Practice Areas</a></li>
                    <li><a href="locations.html">Locations</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>'''

NEW_PATTERN_1 = '''                <h3>Quick Links</h3>
                <ul class="footer_list">
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="accessibility.html">Accessibility</a></li>'''

# Pattern for files that might have the newer structure already (without accessibility)
OLD_PATTERN_2 = '''                <h3 class="footer_heading">Quick Links</h3>
                <ul class="footer_list">
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                </ul>'''

NEW_PATTERN_2 = '''                <h3 class="footer_heading">Quick Links</h3>
                <ul class="footer_list">
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="accessibility.html">Accessibility</a></li>
                </ul>'''

# Process root directory files
print("Processing root directory files...")
for file_path in root_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Try first pattern
        if OLD_PATTERN_1 in content:
            content = content.replace(OLD_PATTERN_1, NEW_PATTERN_1)
            print(f"  OK {file_path} - Updated (pattern 1)")
        # Try second pattern
        elif OLD_PATTERN_2 in content:
            content = content.replace(OLD_PATTERN_2, NEW_PATTERN_2)
            print(f"  OK {file_path} - Updated (pattern 2)")
        else:
            # Check if accessibility link already exists
            if 'href="accessibility.html"' in content:
                print(f"  SKIP {file_path} - Already has accessibility link")
            else:
                print(f"  WARN {file_path} - Footer pattern not found (may need manual update)")
                continue

        # Write updated content if changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    except Exception as e:
        print(f"  ERROR Error processing {file_path}: {e}")

# Process location files (use ../ for parent directory)
print("\nProcessing location files...")
OLD_PATTERN_LOC = '''                <h3 class="footer_heading">Quick Links</h3>
                <ul class="footer_list">
                    <li><a href="../faq.html">FAQ</a></li>
                    <li><a href="../privacy-policy.html">Privacy Policy</a></li>
                </ul>'''

NEW_PATTERN_LOC = '''                <h3 class="footer_heading">Quick Links</h3>
                <ul class="footer_list">
                    <li><a href="../faq.html">FAQ</a></li>
                    <li><a href="../privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="../accessibility.html">Accessibility</a></li>
                </ul>'''

for file_path in location_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        if OLD_PATTERN_LOC in content:
            content = content.replace(OLD_PATTERN_LOC, NEW_PATTERN_LOC)
            print(f"  OK {file_path} - Updated")
        elif 'href="../accessibility.html"' in content:
            print(f"  SKIP {file_path} - Already has accessibility link")
        else:
            print(f"  WARN {file_path} - Footer pattern not found (may need manual update)")
            continue

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    except Exception as e:
        print(f"  ERROR Error processing {file_path}: {e}")

# Process card files (use ../ for parent directory)
print("\nProcessing card files...")
for file_path in card_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        if OLD_PATTERN_LOC in content:
            content = content.replace(OLD_PATTERN_LOC, NEW_PATTERN_LOC)
            print(f"  OK {file_path} - Updated")
        elif 'href="../accessibility.html"' in content:
            print(f"  SKIP {file_path} - Already has accessibility link")
        else:
            print(f"  WARN {file_path} - Footer pattern not found (may need manual update)")
            continue

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    except Exception as e:
        print(f"  ERROR Error processing {file_path}: {e}")

print("\nDONE Accessibility link deployment complete!")
print(f"   Root files processed: {len(root_files)}")
print(f"   Location files processed: {len(location_files)}")
print(f"   Card files processed: {len(card_files)}")
print(f"   Total: {len(root_files) + len(location_files) + len(card_files)} files")
