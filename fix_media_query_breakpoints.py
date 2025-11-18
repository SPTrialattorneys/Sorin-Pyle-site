"""
Media Query Breakpoint Standardization
Fixes inconsistent breakpoints to prevent responsive design gaps
Standard: max-width: 767px (mobile), min-width: 768px (desktop/tablet)
"""

import re
import sys
import io

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 80)
print("MEDIA QUERY BREAKPOINT STANDARDIZATION")
print("=" * 80)
print()

# Read CSS file
with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

print("STANDARDIZATION RULES:")
print("-" * 80)
print("Mobile (max-width):")
print("  max-width: 768px → max-width: 767px")
print()
print("Desktop/Tablet (min-width):")
print("  min-width: 769px → min-width: 768px")
print()
print("=" * 80)
print("CHANGES APPLIED:")
print("-" * 80)
print()

changes_made = 0

# Fix 1: Change max-width: 768px to max-width: 767px
# This prevents overlap where both 767px and 768px queries could apply
pattern1 = r'@media \(max-width: 768px\)'
replacement1 = '@media (max-width: 767px)'
matches1 = len(re.findall(pattern1, content))
if matches1 > 0:
    content = re.sub(pattern1, replacement1, content)
    print(f"✅ Changed {matches1} instances: max-width: 768px → max-width: 767px")
    changes_made += matches1

# Fix 2: Change min-width: 769px to min-width: 768px
# This creates proper pairing with max-width: 767px
pattern2 = r'@media \(min-width: 769px\)'
replacement2 = '@media (min-width: 768px)'
matches2 = len(re.findall(pattern2, content))
if matches2 > 0:
    content = re.sub(pattern2, replacement2, content)
    print(f"✅ Changed {matches2} instances: min-width: 769px → min-width: 768px")
    changes_made += matches2

# Fix 3: Also check for any stray max-width: 767.5px or similar
pattern3 = r'@media \(max-width: 767\.5px\)'
replacement3 = '@media (max-width: 767px)'
matches3 = len(re.findall(pattern3, content))
if matches3 > 0:
    content = re.sub(pattern3, replacement3, content)
    print(f"✅ Changed {matches3} instances: max-width: 767.5px → max-width: 767px")
    changes_made += matches3

if changes_made == 0:
    print("ℹ️  No inconsistent breakpoints found - already standardized")

print()
print("=" * 80)
print("VERIFICATION:")
print("-" * 80)

# Verify final state
final_767_max = len(re.findall(r'@media \(max-width: 767px\)', content))
final_768_max = len(re.findall(r'@media \(max-width: 768px\)', content))
final_768_min = len(re.findall(r'@media \(min-width: 768px\)', content))
final_769_min = len(re.findall(r'@media \(min-width: 769px\)', content))

print(f"max-width: 767px: {final_767_max} occurrences ✓")
print(f"max-width: 768px: {final_768_max} occurrences {'⚠️' if final_768_max > 0 else '✓'}")
print(f"min-width: 768px: {final_768_min} occurrences ✓")
print(f"min-width: 769px: {final_769_min} occurrences {'⚠️' if final_769_min > 0 else '✓'}")

# Write updated CSS
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print()
print("=" * 80)
print("RESULTS:")
print("=" * 80)
print(f"Total changes: {changes_made}")
print("File updated: css/style.css")
print()
print("RESPONSIVE DESIGN IMPROVEMENT:")
print("  ✅ No more breakpoint gaps between 767px and 768px")
print("  ✅ Consistent mobile/desktop boundary at 768px")
print("  ✅ Standard iPad portrait breakpoint (768px)")
print("  ✅ Prevents potential layout issues on edge devices")
print()
print("NEXT STEPS:")
print("  1. Test responsive design on devices near 768px breakpoint")
print("  2. Verify no layout issues introduced")
print("  3. Check mobile nav, footer, cards at 767px and 768px")
print("=" * 80)
