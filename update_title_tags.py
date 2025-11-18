"""
Title Tag Length Optimization Script
Updates 30 HTML files with optimized title tags (50-60 characters)
"""

import os
import re
import sys

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Dictionary of file paths and their new optimized title tags
title_updates = {
    # WORST OFFENDERS (over 10 chars)
    'blog/_site/blog/understanding-dui-charges-in-michigan-what-you-need-to-know/index.html': 'Understanding DUI Charges in Michigan | Sorin & Pyle Blog',
    'locations/davenport-student-defense.html': 'Davenport Student Defense Lawyer | Grand Rapids MI Attorney',
    'locations/calvin-university-student-defense.html': 'Calvin University Student Lawyer | Grand Rapids Attorney',
    'locations/ferris-student-defense.html': 'Ferris State Student Lawyer | Big Rapids MI Attorney',
    'your-rights.html': 'Know Your Rights | Michigan Criminal Defense Guide',
    'locations/grand-haven-mi.html': 'Grand Haven MI Criminal Lawyer | Ottawa County Courthouse',
    'locations/wmu-student-defense.html': 'WMU Student Defense Lawyer | Kalamazoo Criminal Attorney',
    'locations/south-haven-mi.html': 'South Haven MI Criminal Lawyer | Van Buren County Attorney',
    'domestic-violence-defense.html': 'Domestic Violence Lawyer Holland MI | Ottawa County DV',
    'locations/grcc-student-defense.html': 'GRCC Student Lawyer | Grand Rapids Criminal Defense',

    # MODERATE OFFENDERS (6-10 chars over)
    'locations/allendale-mi.html': 'Allendale MI Criminal Lawyer | GVSU Student Defense',
    'locations/saugatuck-mi.html': 'Saugatuck MI Criminal Lawyer | Allegan County Attorney',
    'locations/hudsonville-mi.html': 'Hudsonville MI Criminal Lawyer | Ottawa County DUI Attorney',
    'record-expungement.html': 'Record Expungement Lawyer Michigan | Clear Your Record',
    'locations/grandville-mi.html': 'Grandville MI Criminal Lawyer | Kent County Attorney',
    'locations/kentwood-mi.html': 'Kentwood MI Criminal Lawyer | 61st District Court Attorney',

    # MINOR OFFENDERS (5-6 chars over)
    'repeat-offense-owi.html': '2nd & 3rd Offense OWI Michigan | Repeat DUI Defense',
    'locations/holland-mi.html': 'Holland MI Criminal Lawyer | Ottawa County Attorney',
    'locations/jenison-mi.html': 'Jenison MI Criminal Lawyer | Ottawa County Attorney',
    'locations/wyoming-mi.html': 'Wyoming MI Criminal Lawyer | 61st District Court Attorney',

    # BARELY OVER (2-4 chars over)
    'faq.html': 'FAQ | Criminal Defense Questions | Sorin & Pyle',
    'card/sorin.html': 'Sorin Panainte | Criminal Defense Attorney Contact Card',
    'card/jonathan.html': 'Jonathan Pyle | Criminal Defense Attorney Contact Card',
    'locations/hope-college-student-defense.html': 'Hope College Student Lawyer | Holland MI Attorney',
    'locations/zeeland-mi.html': 'Zeeland MI Criminal Lawyer | Ottawa County Attorney',
    'community-resources.html': 'Community Resources | West Michigan County Support Services',
    'locations/grand-rapids-mi.html': 'Grand Rapids MI Criminal Lawyer | Kent County Attorney',
    'locations/walker-mi.html': 'Walker MI Criminal Lawyer | Kent County Attorney',
    'drivers-license-restoration.html': 'Michigan License Restoration | Get Your Driver License Back',
    'super-drunk-high-bac.html': 'Michigan Super Drunk Law | High BAC 0.17% Defense',
}

def update_title_tag(file_path, new_title):
    """Update the title tag in an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match title tag
        pattern = r'(<title>)[^<]+(</title>)'
        replacement = f'\\1{new_title}\\2'

        # Check if title tag exists
        if not re.search(pattern, content):
            print(f"  ⚠️  WARNING: No title tag found in {file_path}")
            return False

        # Replace title tag
        updated_content = re.sub(pattern, replacement, content)

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return True

    except FileNotFoundError:
        print(f"  ❌ ERROR: File not found: {file_path}")
        return False
    except Exception as e:
        print(f"  ❌ ERROR updating {file_path}: {e}")
        return False

def main():
    print("=" * 80)
    print("TITLE TAG LENGTH OPTIMIZATION")
    print("=" * 80)
    print(f"Total files to update: {len(title_updates)}")
    print("Target: 50-60 characters for optimal Google display")
    print()

    success_count = 0
    fail_count = 0

    for file_path, new_title in title_updates.items():
        print(f"Updating: {file_path}")
        print(f"  New title ({len(new_title)} chars): {new_title}")

        if update_title_tag(file_path, new_title):
            print("  ✅ Success")
            success_count += 1
        else:
            fail_count += 1

        print()

    print("=" * 80)
    print("RESULTS:")
    print("=" * 80)
    print(f"✅ Successfully updated: {success_count} files")
    if fail_count > 0:
        print(f"❌ Failed: {fail_count} files")
    print()

    if success_count == len(title_updates):
        print("🎉 ALL TITLE TAGS OPTIMIZED SUCCESSFULLY!")
    else:
        print("⚠️  Some files failed to update. Please review errors above.")

if __name__ == "__main__":
    main()
