#!/usr/bin/env python3
"""
Update footer navigation across all HTML files
Replaces "Quick Links" with improved conversion-focused footer structure
"""

import re
import sys
import io
from pathlib import Path

# Handle Windows Unicode output
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Old footer structure (Quick Links + Client Portal)
OLD_FOOTER_ROOT = r'''                <div class="footer_column">
                    <h3>Quick Links</h3>
                    <ul class="footer_list">
                        <li><a href="index\.html">About</a></li>
                        <li><a href="attorneys\.html">Attorneys</a></li>
                        <li><a href="practice-areas\.html">Practice Areas</a></li>
                        <li><a href="locations\.html">Locations</a></li>
                        <li><a href="faq\.html">Client Resources</a></li>
                        <li><a href="contact\.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer_column">
                    <h3>Client Portal</h3>
                    <ul class="footer_list">
                        <li><a href="https://www\.clio\.com/clients/" target="_blank" rel="noopener noreferrer">Clio Client Portal</a></li>
                        <li><a href="https://app\.clio\.com/link/v2/2/2/81d5d84d1d449d617bc5b8d5ff9658fb\?hmac=e9a2a8e1fbd96a550ff5212173791d674bb93c42d08b7eb7564e8cee53e54ab9" target="_blank" rel="noopener noreferrer">Pay Engagement Fee</a></li>
                        <li><a href="https://app\.clio\.com/clients/" target="_blank" rel="noopener noreferrer">Pay Outstanding Invoice</a></li>
                    </ul>
                </div>'''

OLD_FOOTER_SUBFOLDER = r'''                <div class="footer_column">
                    <h3>Quick Links</h3>
                    <ul class="footer_list">
                        <li><a href="\.\./index\.html">About</a></li>
                        <li><a href="\.\./attorneys\.html">Attorneys</a></li>
                        <li><a href="\.\./practice-areas\.html">Practice Areas</a></li>
                        <li><a href="\.\./locations\.html">Locations</a></li>
                        <li><a href="\.\./faq\.html">Client Resources</a></li>
                        <li><a href="\.\./contact\.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer_column">
                    <h3>Client Portal</h3>
                    <ul class="footer_list">
                        <li><a href="https://www\.clio\.com/clients/" target="_blank" rel="noopener noreferrer">Clio Client Portal</a></li>
                        <li><a href="https://app\.clio\.com/link/v2/2/2/81d5d84d1d449d617bc5b8d5ff9658fb\?hmac=e9a2a8e1fbd96a550ff5212173791d674bb93c42d08b7eb7564e8cee53e54ab9" target="_blank" rel="noopener noreferrer">Pay Engagement Fee</a></li>
                        <li><a href="https://app\.clio\.com/clients/" target="_blank" rel="noopener noreferrer">Pay Outstanding Invoice</a></li>
                    </ul>
                </div>'''

# New footer structure (Practice Areas + Client Portal)
NEW_FOOTER_ROOT = '''                <div class="footer_column">
                    <h3>Practice Areas</h3>
                    <ul class="footer_list">
                        <li><a href="dui-defense.html">DUI / OWI Defense</a></li>
                        <li><a href="domestic-violence-defense.html">Domestic Violence</a></li>
                        <li><a href="record-expungement.html">Record Expungement</a></li>
                        <li><a href="drivers-license-restoration.html">License Restoration</a></li>
                        <li><a href="practice-areas.html">View All Practices</a></li>
                    </ul>
                </div>
                <div class="footer_column">
                    <h3>Client Portal</h3>
                    <ul class="footer_list">
                        <li><a href="https://www.clio.com/clients/" target="_blank" rel="noopener noreferrer">Clio Client Portal</a></li>
                        <li><a href="https://app.clio.com/link/v2/2/2/81d5d84d1d449d617bc5b8d5ff9658fb?hmac=e9a2a8e1fbd96a550ff5212173791d674bb93c42d08b7eb7564e8cee53e54ab9" target="_blank" rel="noopener noreferrer">Pay Engagement Fee</a></li>
                        <li><a href="https://app.clio.com/clients/" target="_blank" rel="noopener noreferrer">Pay Outstanding Invoice</a></li>
                    </ul>
                </div>'''

NEW_FOOTER_SUBFOLDER = '''                <div class="footer_column">
                    <h3>Practice Areas</h3>
                    <ul class="footer_list">
                        <li><a href="../dui-defense.html">DUI / OWI Defense</a></li>
                        <li><a href="../domestic-violence-defense.html">Domestic Violence</a></li>
                        <li><a href="../record-expungement.html">Record Expungement</a></li>
                        <li><a href="../drivers-license-restoration.html">License Restoration</a></li>
                        <li><a href="../practice-areas.html">View All Practices</a></li>
                    </ul>
                </div>
                <div class="footer_column">
                    <h3>Client Portal</h3>
                    <ul class="footer_list">
                        <li><a href="https://www.clio.com/clients/" target="_blank" rel="noopener noreferrer">Clio Client Portal</a></li>
                        <li><a href="https://app.clio.com/link/v2/2/2/81d5d84d1d449d617bc5b8d5ff9658fb?hmac=e9a2a8e1fbd96a550ff5212173791d674bb93c42d08b7eb7564e8cee53e54ab9" target="_blank" rel="noopener noreferrer">Pay Engagement Fee</a></li>
                        <li><a href="https://app.clio.com/clients/" target="_blank" rel="noopener noreferrer">Pay Outstanding Invoice</a></li>
                    </ul>
                </div>'''

def update_footer(file_path, is_subfolder=False):
    """Update footer navigation in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        old_pattern = OLD_FOOTER_SUBFOLDER if is_subfolder else OLD_FOOTER_ROOT
        new_footer = NEW_FOOTER_SUBFOLDER if is_subfolder else NEW_FOOTER_ROOT

        # Use regex to find and replace
        updated_content = re.sub(old_pattern, new_footer, content, flags=re.DOTALL)

        # Check if update was made
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        return False
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return False

def main():
    root_dir = Path('.')

    # Files to update in root directory
    root_files = [
        'attorneys.html',
        'practice-areas.html',
        'contact.html',
        'locations.html',
        'privacy-policy.html',
        '404.html',
        '500.html',
        'faq.html',
        'your-rights.html',
        'blog.html',
        'community-resources.html',
        'dui-defense.html',
        'domestic-violence-defense.html',
        'record-expungement.html',
        'drivers-license-restoration.html',
        'cdl-owi-defense.html',
        'first-offense-owi.html',
        'repeat-offense-owi.html',
        'super-drunk-high-bac.html',
        'jonathan-pyle.html',
        'sorin-panainte.html',
    ]

    # Subfolders with HTML files
    subfolders = ['locations', 'card']

    updated_count = 0
    skipped_count = 0

    print("🔄 Updating footer navigation across all HTML files...\n")

    # Update root files
    print("📁 Root directory files:")
    for filename in root_files:
        file_path = root_dir / filename
        if file_path.exists():
            if update_footer(file_path, is_subfolder=False):
                print(f"   ✅ {filename}")
                updated_count += 1
            else:
                print(f"   ⚠️  {filename} (no changes needed)")
                skipped_count += 1
        else:
            print(f"   ⏭️  {filename} (file not found)")
            skipped_count += 1

    # Update subfolder files
    for subfolder in subfolders:
        subfolder_path = root_dir / subfolder
        if subfolder_path.exists() and subfolder_path.is_dir():
            print(f"\n📁 {subfolder}/ directory:")
            html_files = sorted(subfolder_path.glob('*.html'))
            for file_path in html_files:
                if update_footer(file_path, is_subfolder=True):
                    print(f"   ✅ {file_path.name}")
                    updated_count += 1
                else:
                    print(f"   ⚠️  {file_path.name} (no changes needed)")
                    skipped_count += 1

    print(f"\n{'='*60}")
    print(f"✅ Footer navigation update complete!")
    print(f"   Files updated: {updated_count}")
    print(f"   Files skipped: {skipped_count}")
    print(f"{'='*60}\n")

    print("📊 Changes made:")
    print("   • Replaced 'Quick Links' with 'Practice Areas' (service-focused)")
    print("   • Featured high-value services: DUI, DV, Expungement, License Restoration")
    print("   • Maintained 'Client Portal' section")
    print("   • Total footer columns: 4 (unchanged)")
    print("   • Focus: Conversion optimization with direct service links")

if __name__ == '__main__':
    main()
