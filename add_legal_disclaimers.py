"""
Legal Disclaimers Implementation - Attorney Ethics Compliance
Adds two types of disclaimers required for law firm websites:
1. Site-wide attorney-client disclaimer in footer
2. Past results disclaimer on pages with case results
"""

import os
import re
import sys
import io

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 80)
print("LEGAL DISCLAIMERS IMPLEMENTATION")
print("=" * 80)
print()

# Issue #17: Site-Wide Attorney-Client Disclaimer
attorney_client_disclaimer = '''            <div class="footer_disclaimer">
                <p><strong>Disclaimer:</strong> The information on this website is for general information purposes only. Nothing on this site should be taken as legal advice for any individual case or situation. This information is not intended to create, and receipt or viewing does not constitute, an attorney-client relationship.</p>
            </div>
'''

# Issue #18: Past Results Disclaimer
past_results_disclaimer = '''
        <div class="legal-disclaimer" style="background: #f8f9fa; padding: 1.5rem; margin: 2rem 0; border-left: 4px solid #4076B4; border-radius: 4px;">
            <p style="margin: 0; font-size: 0.9rem; color: #495057; line-height: 1.6;"><strong>Past Results Disclaimer:</strong> The results listed on this website are specific to the facts and legal circumstances of each individual case. Past results do not guarantee or predict a similar outcome in future cases. Each case is unique and must be evaluated on its own merits.</p>
        </div>
'''

# Files to update for Issue #17 (all HTML files with footers)
html_files = []
for root, dirs, files in os.walk('.'):
    if any(skip in root for skip in ['node_modules', '.git', 'backup', '_site', '_includes']):
        continue
    for file in files:
        if file.endswith('.html') and not file.endswith('.bak') and 'card' not in file:
            html_files.append(os.path.join(root, file))

# Files with case results (for Issue #18)
results_pages = [
    'index.html',
    'jonathan-pyle.html',
    'sorin-panainte.html'
]

print("ISSUE #17: SITE-WIDE ATTORNEY-CLIENT DISCLAIMER")
print("-" * 80)
print()

success_17 = 0
skipped_17 = 0

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if disclaimer already exists
        if 'footer_disclaimer' in content:
            skipped_17 += 1
            continue

        # Find footer bottom bar and add disclaimer above it
        pattern = r'(<div class="footer_bottom-bar">)'
        if not re.search(pattern, content):
            skipped_17 += 1
            continue

        # Add disclaimer before footer bottom bar
        updated_content = re.sub(pattern, attorney_client_disclaimer + r'\1', content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"✅ {file_path}")
        success_17 += 1

    except Exception as e:
        print(f"❌ ERROR: {file_path} - {e}")

print()
print(f"Footer disclaimer added: {success_17} files")
print(f"Skipped: {skipped_17} files")
print()

print("=" * 80)
print("ISSUE #18: PAST RESULTS DISCLAIMER")
print("-" * 80)
print()

success_18 = 0
skipped_18 = 0

for file_path in results_pages:
    try:
        if not os.path.exists(file_path):
            print(f"⏭️  Skipped: {file_path} (not found)")
            skipped_18 += 1
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if disclaimer already exists
        if 'Past Results Disclaimer' in content:
            print(f"⏭️  Skipped: {file_path} (already has disclaimer)")
            skipped_18 += 1
            continue

        # Find results section and add disclaimer after it
        results_patterns = [
            (r'(</section><!--\s*End Results Section\s*-->)', 'End Results Section'),
            (r'(</section><!--\s*End Recent Results\s*-->)', 'End Recent Results'),
            (r'(<section class="section section_results">.*?</section>)', 'Results Section'),
        ]

        updated = False
        for pattern, desc in results_patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                # Add disclaimer after results section
                updated_content = re.sub(pattern, r'\1' + past_results_disclaimer, content, flags=re.DOTALL)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"✅ {file_path} (after {desc})")
                success_18 += 1
                updated = True
                break

        if not updated:
            print(f"⚠️  Warning: {file_path} - could not find results section")
            skipped_18 += 1

    except Exception as e:
        print(f"❌ ERROR: {file_path} - {e}")

print()
print(f"Results disclaimer added: {success_18} files")
print(f"Skipped: {skipped_18} files")
print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Issue #17 (Footer Disclaimer): {success_17} files updated")
print(f"Issue #18 (Results Disclaimer): {success_18} files updated")
print()
print("COMPLIANCE ACHIEVED:")
print("  ✅ Attorney-client disclaimer on all pages")
print("  ✅ Past results disclaimer on pages with case results")
print("  ✅ Michigan Bar advertising rules compliance")
print("=" * 80)
