#!/usr/bin/env python3
"""
Add accessibility statement link to all page footers.
This script adds a link to accessibility.html in the footer bottom bar.
"""

import glob

# Get all HTML files
root_files = glob.glob('*.html')
location_files = glob.glob('locations/*.html')
card_files = glob.glob('card/*.html')

# Exclude the files we just created and error pages
exclude_files = ['accessibility.html', '404.html', '500.html']
root_files = [f for f in root_files if f not in exclude_files]

# Pattern for root files
OLD_PATTERN_ROOT = '© 2025 Sorin & Pyle, PC. All Rights Reserved. | <a href="privacy-policy.html">Privacy Policy</a>'
NEW_PATTERN_ROOT = '© 2025 Sorin & Pyle, PC. All Rights Reserved. | <a href="privacy-policy.html">Privacy Policy</a> | <a href="accessibility.html">Accessibility</a>'

# Pattern for location files (with ../)
OLD_PATTERN_LOC = '© 2025 Sorin & Pyle, PC. All Rights Reserved. | <a href="../privacy-policy.html">Privacy Policy</a>'
NEW_PATTERN_LOC = '© 2025 Sorin & Pyle, PC. All Rights Reserved. | <a href="../privacy-policy.html">Privacy Policy</a> | <a href="../accessibility.html">Accessibility</a>'

updated_count = 0
skipped_count = 0
error_count = 0

# Process root directory files
print("Processing root directory files...")
for file_path in root_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if OLD_PATTERN_ROOT in content and 'href="accessibility.html"' not in content:
            content = content.replace(OLD_PATTERN_ROOT, NEW_PATTERN_ROOT)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  OK {file_path}")
            updated_count += 1
        elif 'href="accessibility.html"' in content:
            print(f"  SKIP {file_path} - Already has accessibility link")
            skipped_count += 1
        else:
            print(f"  WARN {file_path} - Pattern not found")
            error_count += 1

    except Exception as e:
        print(f"  ERROR {file_path}: {e}")
        error_count += 1

# Process location files (use ../ for parent directory)
print("\nProcessing location files...")
for file_path in location_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if OLD_PATTERN_LOC in content and 'href="../accessibility.html"' not in content:
            content = content.replace(OLD_PATTERN_LOC, NEW_PATTERN_LOC)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  OK {file_path}")
            updated_count += 1
        elif 'href="../accessibility.html"' in content:
            print(f"  SKIP {file_path} - Already has accessibility link")
            skipped_count += 1
        else:
            print(f"  WARN {file_path} - Pattern not found")
            error_count += 1

    except Exception as e:
        print(f"  ERROR {file_path}: {e}")
        error_count += 1

# Process card files (use ../ for parent directory)
print("\nProcessing card files...")
for file_path in card_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if OLD_PATTERN_LOC in content and 'href="../accessibility.html"' not in content:
            content = content.replace(OLD_PATTERN_LOC, NEW_PATTERN_LOC)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  OK {file_path}")
            updated_count += 1
        elif 'href="../accessibility.html"' in content:
            print(f"  SKIP {file_path} - Already has accessibility link")
            skipped_count += 1
        else:
            print(f"  WARN {file_path} - Pattern not found")
            error_count += 1

    except Exception as e:
        print(f"  ERROR {file_path}: {e}")
        error_count += 1

print(f"\nDONE Accessibility link deployment complete!")
print(f"   Files updated: {updated_count}")
print(f"   Files skipped (already has link): {skipped_count}")
print(f"   Files with warnings/errors: {error_count}")
print(f"   Total files processed: {len(root_files) + len(location_files) + len(card_files)}")
