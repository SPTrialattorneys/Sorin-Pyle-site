#!/usr/bin/env python3
"""
Test navigation dropdown links across all HTML files
Validates that all Client Resources dropdown links are properly updated
"""

import os
import re
from pathlib import Path

# All HTML files to test
test_files = [
    # Root files (including new pages)
    "index.html",
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
    "faq.html",
    "your-rights.html",
    "blog.html",
    "community-resources.html",
    # Location files
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

def check_dropdown_links(filepath):
    """Check if file has correct dropdown links"""
    is_location = filepath.startswith("locations/")
    path_prefix = "../" if is_location else ""

    errors = []
    warnings = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Expected links (4 items in dropdown)
        expected_links = [
            f'{path_prefix}faq.html',
            f'{path_prefix}your-rights.html',
            f'{path_prefix}community-resources.html',
            f'{path_prefix}blog.html'
        ]

        # Check desktop dropdown
        desktop_dropdown = re.search(
            r'<li class="navbar_item navbar_dropdown".*?</ul>\s*</li>',
            content,
            re.DOTALL
        )

        if desktop_dropdown:
            dropdown_html = desktop_dropdown.group(0)
            for link in expected_links:
                if link not in dropdown_html:
                    errors.append(f"Missing desktop link: {link}")
        else:
            errors.append("Desktop dropdown not found")

        # Check mobile dropdown
        mobile_dropdown = re.search(
            r'<li class="mobile-nav_dropdown".*?</ul>\s*</li>',
            content,
            re.DOTALL
        )

        if mobile_dropdown:
            mobile_html = mobile_dropdown.group(0)
            for link in expected_links:
                if link not in mobile_html:
                    errors.append(f"Missing mobile link: {link}")
        else:
            errors.append("Mobile dropdown not found")

        # Check for old links (should not exist)
        old_patterns = [
            f'{path_prefix}resources.html#faq',
            f'{path_prefix}local-resources.html',
            f'{path_prefix}resources.html#blog',
            f'{path_prefix}resources.html#rights',
        ]

        for old_link in old_patterns:
            if old_link in content:
                warnings.append(f"Found old link: {old_link}")

        # Check footer link points to faq.html
        footer = re.search(r'<footer class="footer_component">.*?</footer>', content, re.DOTALL)
        if footer:
            footer_html = footer.group(0)
            if f'{path_prefix}faq.html' not in footer_html:
                errors.append("Footer 'Client Resources' link not pointing to faq.html")

        return errors, warnings

    except FileNotFoundError:
        return [f"File not found: {filepath}"], []
    except Exception as e:
        return [f"Error reading file: {e}"], []

def run_tests():
    """Run all navigation tests"""
    print("=" * 70)
    print("CLIENT RESOURCES NAVIGATION TEST SUITE")
    print("=" * 70)
    print()

    total_files = 0
    passed_files = 0
    failed_files = 0
    warning_files = 0

    for filepath in test_files:
        total_files += 1
        errors, warnings = check_dropdown_links(filepath)

        if errors:
            failed_files += 1
            print(f"[FAIL] {filepath}")
            for error in errors:
                print(f"       - {error}")
            if warnings:
                for warning in warnings:
                    print(f"       [WARN] {warning}")
            print()
        elif warnings:
            warning_files += 1
            passed_files += 1
            print(f"[PASS] {filepath}")
            for warning in warnings:
                print(f"       [WARN] {warning}")
            print()
        else:
            passed_files += 1
            print(f"[PASS] {filepath}")

    print()
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total files tested: {total_files}")
    print(f"Passed: {passed_files}")
    print(f"Failed: {failed_files}")
    print(f"Files with warnings: {warning_files}")

    if failed_files == 0:
        print()
        print("[SUCCESS] All navigation tests passed!")
        return True
    else:
        print()
        print("[FAILURE] Some tests failed. See details above.")
        return False

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
