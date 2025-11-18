#!/usr/bin/env python3
"""
Check all HTML files for meta description length issues.
Identify descriptions over 160 characters that will be truncated in Google.
"""

import glob
import re

# Get all HTML files
root_files = glob.glob('*.html')
location_files = glob.glob('locations/*.html')
card_files = glob.glob('card/*.html')

all_files = root_files + location_files + card_files

# Exclude error pages
all_files = [f for f in all_files if '404.html' not in f and '500.html' not in f]

over_160 = []
optimal = []

for file_path in sorted(all_files):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find meta description
        match = re.search(r'<meta name="description" content="([^"]+)"', content)
        if match:
            description = match.group(1)
            length = len(description)
            
            if length > 160:
                over_160.append({
                    'file': file_path,
                    'length': length,
                    'description': description,
                    'overage': length - 160
                })
            else:
                optimal.append({
                    'file': file_path,
                    'length': length
                })
        else:
            print(f"WARN: No meta description found in {file_path}")
    
    except Exception as e:
        print(f"ERROR: {file_path}: {e}")

# Print results
print(f"\n=== META DESCRIPTION LENGTH ANALYSIS ===\n")
print(f"Total files checked: {len(all_files)}")
print(f"Optimal length (<=160 chars): {len(optimal)}")
print(f"Too long (>160 chars): {len(over_160)}")

if over_160:
    print(f"\n=== PAGES NEEDING META DESCRIPTION OPTIMIZATION ({len(over_160)} pages) ===\n")
    
    # Sort by overage (worst first)
    over_160.sort(key=lambda x: x['overage'], reverse=True)
    
    for item in over_160:
        print(f"\nFile: {item['file']}")
        print(f"Length: {item['length']} characters ({item['overage']} over limit)")
        print(f"Current: {item['description'][:100]}...")
        print(f"Truncated in Google: {item['description'][:160]}...")

print(f"\n=== SUMMARY ===")
print(f"Pages needing optimization: {len(over_160)}")
print(f"Average overage: {sum(item['overage'] for item in over_160) / len(over_160):.1f} characters" if over_160 else "")
