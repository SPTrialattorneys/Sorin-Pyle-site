#!/usr/bin/env python3
"""
Update footer text from 'View All Practices' to 'View All Practice Areas'
across all HTML files in the Sorin & Pyle website.
"""

import os
import re

# List of all files that need updating (from grep results)
root_files = [
    'index.html',
    'attorneys.html',
    'practice-areas.html',
    'locations.html',
    'faq.html',
    'your-rights.html',
    'blog.html',
    'community-resources.html',
    'domestic-violence-defense.html',
    'record-expungement.html',
    'drivers-license-restoration.html',
    'cdl-owi-defense.html',
    'first-offense-owi.html',
    'repeat-offense-owi.html',
    'super-drunk-high-bac.html',
    'jonathan-pyle.html',
    'sorin-panainte.html',
    'contact.html',
    'dui-defense.html'
]

location_files = [
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
    'locations/zeeland-mi.html'
]

all_files = root_files + location_files

# Statistics
total_files = len(all_files)
updated_files = 0
skipped_files = 0
error_files = []

print(f"Starting update of {total_files} files...")
print("=" * 60)

for filepath in all_files:
    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if the old text exists
        if 'View All Practices' in content:
            # Replace the text
            new_content = content.replace('View All Practices', 'View All Practice Areas')

            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            updated_files += 1
            print(f"[OK] Updated: {filepath}")
        else:
            skipped_files += 1
            print(f"[SKIP] Skipped (text not found): {filepath}")

    except Exception as e:
        error_files.append(filepath)
        print(f"[ERROR] Error updating {filepath}: {str(e)}")

print("=" * 60)
print(f"\nUpdate Summary:")
print(f"  Total files processed: {total_files}")
print(f"  Files updated: {updated_files}")
print(f"  Files skipped: {skipped_files}")
print(f"  Files with errors: {len(error_files)}")

if error_files:
    print(f"\nFiles with errors:")
    for f in error_files:
        print(f"  - {f}")

print("\nDone!")
