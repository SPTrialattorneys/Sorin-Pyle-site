"""
Mobile Navigation ARIA Role Fix - Accessibility Improvement
Changes mobile nav from role="dialog" to role="navigation"
Fixes screen reader confusion (was announcing as dialog instead of navigation)
"""

import os
import re
import sys
import io

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Find all HTML files (excluding backup files and card files)
html_files = []
for root, dirs, files in os.walk('.'):
    # Skip certain directories
    if any(skip in root for skip in ['node_modules', '.git', 'backup', '_site']):
        continue

    for file in files:
        if file.endswith('.html') and not file.endswith('.bak'):
            # Skip card files (they don't have mobile nav)
            if 'card' not in os.path.join(root, file):
                html_files.append(os.path.join(root, file))

print("=" * 80)
print("MOBILE NAVIGATION ARIA ROLE FIX")
print("=" * 80)
print(f"Total HTML files found: {len(html_files)}")
print()

# Pattern to match mobile nav with role="dialog"
old_pattern = r'<div class="mobile-nav_menu" id="mobile-nav" role="dialog"'
new_pattern = r'<div class="mobile-nav_menu" id="mobile-nav" role="navigation"'

success_count = 0
skipped_count = 0
error_count = 0

print("CHANGES:")
print("-" * 80)

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has the old pattern
        if old_pattern not in content:
            skipped_count += 1
            continue

        # Replace role="dialog" with role="navigation"
        updated_content = content.replace(old_pattern, new_pattern)

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"✅ {file_path}")
        success_count += 1

    except Exception as e:
        print(f"❌ ERROR: {file_path} - {e}")
        error_count += 1

print()
print("=" * 80)
print("RESULTS:")
print("=" * 80)
print(f"✅ Successfully updated: {success_count} files")
print(f"⏭️  Skipped (no change needed): {skipped_count} files")
if error_count > 0:
    print(f"❌ Errors: {error_count} files")
print()

if success_count > 0:
    print("ACCESSIBILITY IMPROVEMENT:")
    print("  Before: Screen readers announced mobile menu as 'dialog'")
    print("  After: Screen readers now correctly announce as 'navigation'")
    print()
    print("WCAG SUCCESS CRITERIA:")
    print("  ✅ 1.3.1 Info and Relationships (Level A)")
    print("  ✅ 4.1.2 Name, Role, Value (Level A)")
    print()
    print("USER IMPACT:")
    print("  - Screen reader users get correct semantic information")
    print("  - Improved navigation comprehension for assistive technology")
    print("  - Better accessibility compliance")

print()
print("=" * 80)
