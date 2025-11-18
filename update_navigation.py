#!/usr/bin/env python3
"""
Update navigation dropdown across all HTML files
Changes Client Resources dropdown from 3 items to 4 items with new URLs
"""

import os
import re

# Root HTML files (excluding index.html which is already done, and new pages)
root_files = [
    "attorneys.html",
    "contact.html",
    "practice-areas.html",
    "locations.html",
    "privacy-policy.html",
    "drivers-license-restoration.html",
    "record-expungement.html",
    "sorin-panainte.html",
    "jonathan-pyle.html",
    "resources.html",
    "dui-defense.html",
    "domestic-violence-defense.html",
    "404.html",
    "500.html",
    "card.html",
]

# Location HTML files
location_files = [
    "locations/ottawa-county.html",
    "locations/kent-county.html",
    "locations/allegan-county.html",
    "locations/kalamazoo-county.html",
    "locations/muskegon-county.html",
    "locations/van-buren-county.html",
    "locations/newaygo-county.html",
    "locations/other-michigan-counties.html",
    "locations/allendale-mi.html",
    "locations/calvin-university-student-defense.html",
    "locations/davenport-student-defense.html",
    "locations/ferris-student-defense.html",
    "locations/grand-haven-mi.html",
    "locations/grand-rapids-mi.html",
    "locations/grandville-mi.html",
    "locations/grcc-student-defense.html",
    "locations/gvsu-student-defense.html",
    "locations/holland-mi.html",
    "locations/hope-college-student-defense.html",
    "locations/hudsonville-mi.html",
    "locations/jenison-mi.html",
    "locations/kentwood-mi.html",
    "locations/saugatuck-mi.html",
    "locations/south-haven-mi.html",
    "locations/walker-mi.html",
    "locations/wmu-student-defense.html",
    "locations/wyoming-mi.html",
    "locations/zeeland-mi.html",
]

def update_dropdown_navigation(content, is_location=False):
    """Update the Client Resources dropdown menu with 4 items"""
    path_prefix = "../" if is_location else ""

    # Old pattern (3 items):
    # <li role="none"><a href="resources.html#faq" role="menuitem">Frequently Asked Questions</a></li>
    # <li role="none"><a href="local-resources.html" role="menuitem">Community Support Resources</a></li>
    # <li role="none"><a href="resources.html#blog" role="menuitem">Firm News & Updates</a></li>

    # New pattern (4 items):
    new_dropdown = f'''<li role="none"><a href="{path_prefix}faq.html" role="menuitem">Frequently Asked Questions</a></li>
                            <li role="none"><a href="{path_prefix}your-rights.html" role="menuitem">Know Your Rights</a></li>
                            <li role="none"><a href="{path_prefix}community-resources.html" role="menuitem">Community Resources</a></li>
                            <li role="none"><a href="{path_prefix}blog.html" role="menuitem">Firm News & Updates</a></li>'''

    new_dropdown_mobile = f'''<li role="none"><a href="{path_prefix}faq.html" role="menuitem">Frequently Asked Questions</a></li>
                    <li role="none"><a href="{path_prefix}your-rights.html" role="menuitem">Know Your Rights</a></li>
                    <li role="none"><a href="{path_prefix}community-resources.html" role="menuitem">Community Resources</a></li>
                    <li role="none"><a href="{path_prefix}blog.html" role="menuitem">Firm News & Updates</a></li>'''

    # Pattern for desktop dropdown (with proper indentation spacing)
    desktop_pattern = rf'<li role="none"><a href="{re.escape(path_prefix)}resources\.html#faq" role="menuitem">Frequently Asked Questions</a></li>\s*<li role="none"><a href="{re.escape(path_prefix)}local-resources\.html" role="menuitem">Community Support Resources</a></li>\s*<li role="none"><a href="{re.escape(path_prefix)}resources\.html#blog" role="menuitem">Firm News & Updates</a></li>'

    # Replace desktop dropdown
    content = re.sub(desktop_pattern, new_dropdown, content, flags=re.DOTALL)

    # Pattern for mobile dropdown
    mobile_pattern = rf'<li role="none"><a href="{re.escape(path_prefix)}resources\.html#faq" role="menuitem">Frequently Asked Questions</a></li>\s*<li role="none"><a href="{re.escape(path_prefix)}local-resources\.html" role="menuitem">Community Support Resources</a></li>\s*<li role="none"><a href="{re.escape(path_prefix)}resources\.html#blog" role="menuitem">Firm News & Updates</a></li>'

    # Replace mobile dropdown
    content = re.sub(mobile_pattern, new_dropdown_mobile, content, flags=re.DOTALL)

    return content

def update_footer_link(content, is_location=False):
    """Update footer Client Resources link to point to faq.html"""
    path_prefix = "../" if is_location else ""

    # Update various footer link patterns
    content = re.sub(
        rf'<li><a href="{re.escape(path_prefix)}resources\.html">Firm Updates & Resources</a></li>',
        f'<li><a href="{path_prefix}faq.html">Client Resources</a></li>',
        content
    )

    content = re.sub(
        rf'<li><a href="{re.escape(path_prefix)}resources\.html">Client Resources</a></li>',
        f'<li><a href="{path_prefix}faq.html">Client Resources</a></li>',
        content
    )

    return content

def update_file(filepath, is_location=False):
    """Update navigation and footer in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update dropdown navigation
        updated_content = update_dropdown_navigation(content, is_location)

        # Update footer link
        updated_content = update_footer_link(updated_content, is_location)

        # Only write if content changed
        if updated_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"[OK] Updated: {filepath}")
            return True
        else:
            print(f"  No changes needed: {filepath}")
            return False
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return False
    except Exception as e:
        print(f"[ERROR] Error updating {filepath}: {e}")
        return False

def main():
    """Main execution function"""
    print("=" * 60)
    print("Client Resources Navigation Update Script")
    print("=" * 60)

    updated_count = 0

    print("\nUpdating root HTML files...")
    for filename in root_files:
        if update_file(filename, is_location=False):
            updated_count += 1

    print("\nUpdating location HTML files...")
    for filename in location_files:
        if update_file(filename, is_location=True):
            updated_count += 1

    print("\n" + "=" * 60)
    print(f"Update complete! {updated_count} files updated.")
    print("=" * 60)

if __name__ == "__main__":
    main()
