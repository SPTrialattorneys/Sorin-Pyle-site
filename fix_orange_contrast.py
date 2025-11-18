"""
Orange Link Contrast Fix - WCAG AA Accessibility Compliance
Updates orange color from #FF8A28 (2.28:1 contrast) to #B25616 (4.79:1 contrast)
Achieves WCAG AA 4.5:1 minimum for normal body text
"""

import re
import sys
import io

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read core-brand.css
with open('css/core-brand.css', 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("ORANGE LINK CONTRAST FIX - WCAG AA COMPLIANCE")
print("=" * 80)
print()

# Show current color
print("CURRENT COLOR:")
print("  #FF8A28 (main accent orange)")
print("  Contrast ratio: 2.28:1 on #FDFBF6 background")
print("  WCAG AA Status: FAIL (needs 4.5:1 for body text)")
print()

# Find and replace main accent-orange
old_line = '  --accent-orange: #FF8A28;      /* Main accent color (preserved) */'
new_line = '  --accent-orange: #B25616;      /* Main accent color (WCAG AA 4.79:1) */'

if old_line in content:
    content = content.replace(old_line, new_line)
    print("✅ Updated --accent-orange: #FF8A28 → #B25616")
else:
    print("⚠️  WARNING: Could not find exact match for --accent-orange line")
    print("    Will try alternate pattern...")
    # Try regex pattern
    content = re.sub(
        r'(--accent-orange:\s+)#FF8A28(.*)',
        r'\1#B25616\2',
        content
    )
    print("✅ Updated --accent-orange via regex")

# Update the orange-700 hover state to be slightly darker
old_700 = '  --accent-orange-700: #E67821;  /* Hover/active states */'
new_700 = '  --accent-orange-700: #9E4B12;  /* Hover/active states (darker) */'

if old_700 in content:
    content = content.replace(old_700, new_700)
    print("✅ Updated --accent-orange-700: #E67821 → #9E4B12 (hover state)")
else:
    print("⚠️  WARNING: Could not find exact match for --accent-orange-700")
    content = re.sub(
        r'(--accent-orange-700:\s+)#E67821(.*)',
        r'\1#9E4B12\2',
        content
    )
    print("✅ Updated --accent-orange-700 via regex")

# Write updated file
with open('css/core-brand.css', 'w', encoding='utf-8') as f:
    f.write(content)

print()
print("=" * 80)
print("NEW COLOR:")
print("  #B25616 (accessible orange)")
print("  Contrast ratio: 4.79:1 on #FDFBF6 background")
print("  WCAG AA Status: PASS (exceeds 4.5:1 requirement)")
print()
print("HOVER STATE:")
print("  #9E4B12 (darker hover)")
print("  Maintains visual hierarchy with proper contrast")
print()
print("=" * 80)
print("FILE UPDATED: css/core-brand.css")
print("=" * 80)
print()
print("NEXT STEPS:")
print("  1. Regenerate style.min.css from style.css")
print("  2. Test across all pages to ensure visual consistency")
print("  3. Verify contrast in browser DevTools")
print("  4. Update documentation")
