#!/usr/bin/env python3
"""
SEO & Metadata Audit Script
Analyzes all HTML files for SEO compliance
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser
import json

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self.meta_description = None
        self.canonical = None
        self.og_tags = {}
        self.has_schema = False
        self.schema_types = []
        self.ai_optimization = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'title':
            self.current_tag = 'title'

        elif tag == 'meta':
            name = attrs_dict.get('name', '').lower()
            property_val = attrs_dict.get('property', '').lower()
            content = attrs_dict.get('content', '')

            if name == 'description':
                self.meta_description = content
            elif name == 'ai-optimization':
                self.ai_optimization = content
            elif property_val.startswith('og:'):
                self.og_tags[property_val] = content

        elif tag == 'link':
            rel = attrs_dict.get('rel', '')
            if rel == 'canonical':
                self.canonical = attrs_dict.get('href', '')

        elif tag == 'script':
            type_val = attrs_dict.get('type', '')
            if type_val == 'application/ld+json':
                self.current_tag = 'schema'

    def handle_data(self, data):
        if hasattr(self, 'current_tag'):
            if self.current_tag == 'title':
                self.title = data.strip()
                self.current_tag = None
            elif self.current_tag == 'schema':
                try:
                    schema_data = json.loads(data)
                    self.has_schema = True
                    if '@type' in schema_data:
                        schema_type = schema_data['@type']
                        if isinstance(schema_type, list):
                            self.schema_types.extend(schema_type)
                        else:
                            self.schema_types.append(schema_type)
                    elif isinstance(schema_data, list):
                        for item in schema_data:
                            if '@type' in item:
                                self.schema_types.append(item['@type'])
                except:
                    pass
                self.current_tag = None

def analyze_file(filepath):
    """Analyze a single HTML file for SEO metadata"""
    parser = SEOParser()

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            parser.feed(content)

        # Check for microdata schema (itemscope/itemtype)
        if not parser.has_schema:
            if 'itemscope' in content and 'itemtype' in content:
                parser.has_schema = True
                # Extract itemtype values
                itemtype_matches = re.findall(r'itemtype="https?://schema\.org/(\w+)"', content)
                parser.schema_types.extend(itemtype_matches)

        return {
            'title': parser.title,
            'title_length': len(parser.title) if parser.title else 0,
            'meta_description': parser.meta_description,
            'meta_length': len(parser.meta_description) if parser.meta_description else 0,
            'canonical': parser.canonical,
            'og_tags': parser.og_tags,
            'has_schema': parser.has_schema,
            'schema_types': list(set(parser.schema_types)),
            'ai_optimization': parser.ai_optimization
        }
    except Exception as e:
        return {'error': str(e)}

def main():
    base_dir = Path(__file__).parent

    # Collect all HTML files
    html_files = []
    html_files.extend(base_dir.glob('*.html'))
    html_files.extend(base_dir.glob('locations/*.html'))
    html_files.extend(base_dir.glob('card/*.html'))

    # Exclude backup files
    html_files = [f for f in html_files if not f.name.endswith('.bak')]

    results = {}
    for filepath in sorted(html_files):
        rel_path = filepath.relative_to(base_dir)
        results[str(rel_path)] = analyze_file(filepath)

    # Analysis
    total_pages = len(results)

    print("=" * 80)
    print("SEO & METADATA AUDIT REPORT")
    print("=" * 80)
    print(f"\nTotal Pages Analyzed: {total_pages}")
    print()

    # Statistics
    pages_with_title = sum(1 for r in results.values() if r.get('title'))
    pages_with_description = sum(1 for r in results.values() if r.get('meta_description'))
    pages_with_canonical = sum(1 for r in results.values() if r.get('canonical'))
    pages_with_schema = sum(1 for r in results.values() if r.get('has_schema'))
    pages_with_og = sum(1 for r in results.values() if len(r.get('og_tags', {})) >= 4)
    pages_with_ai = sum(1 for r in results.values() if r.get('ai_optimization'))

    print("SUMMARY STATISTICS")
    print("-" * 80)
    print(f"Title Tags:          {pages_with_title}/{total_pages} ({pages_with_title/total_pages*100:.1f}%)")
    print(f"Meta Descriptions:   {pages_with_description}/{total_pages} ({pages_with_description/total_pages*100:.1f}%)")
    print(f"Canonical URLs:      {pages_with_canonical}/{total_pages} ({pages_with_canonical/total_pages*100:.1f}%)")
    print(f"Schema Markup:       {pages_with_schema}/{total_pages} ({pages_with_schema/total_pages*100:.1f}%)")
    print(f"Open Graph (4+ tags): {pages_with_og}/{total_pages} ({pages_with_og/total_pages*100:.1f}%)")
    print(f"AI Optimization:     {pages_with_ai}/{total_pages} ({pages_with_ai/total_pages*100:.1f}%)")
    print()

    # CRITICAL ISSUES
    critical_issues = []

    for page, data in results.items():
        if data.get('error'):
            critical_issues.append(f"{page}: Parse error - {data['error']}")
        elif not data.get('canonical'):
            critical_issues.append(f"{page}: MISSING canonical URL")
        elif not data.get('title'):
            critical_issues.append(f"{page}: MISSING title tag")
        elif not data.get('meta_description'):
            critical_issues.append(f"{page}: MISSING meta description")

    if critical_issues:
        print("CRITICAL ISSUES (Missing Essential Tags)")
        print("-" * 80)
        for issue in sorted(critical_issues):
            print(f"  - {issue}")
        print()

    # HIGH PRIORITY ISSUES
    high_priority = []

    # Check for duplicate titles
    titles = {}
    for page, data in results.items():
        title = data.get('title')
        if title:
            if title not in titles:
                titles[title] = []
            titles[title].append(page)

    for title, pages in titles.items():
        if len(pages) > 1:
            high_priority.append(f"DUPLICATE TITLE: '{title}' used on {len(pages)} pages: {', '.join(pages)}")

    # Check for duplicate descriptions
    descriptions = {}
    for page, data in results.items():
        desc = data.get('meta_description')
        if desc:
            if desc not in descriptions:
                descriptions[desc] = []
            descriptions[desc].append(page)

    for desc, pages in descriptions.items():
        if len(pages) > 1:
            high_priority.append(f"DUPLICATE DESCRIPTION on {len(pages)} pages: {', '.join(pages)}")

    # Check canonical URL format
    for page, data in results.items():
        canonical = data.get('canonical')
        if canonical:
            # Determine expected URL
            if page.startswith('locations\\') or page.startswith('locations/'):
                page_path = page.replace('\\', '/').replace('.html', '')
                expected = f"https://www.sorinpyle.com/{page_path}"
            elif page.startswith('card\\') or page.startswith('card/'):
                page_path = page.replace('\\', '/').replace('.html', '')
                expected = f"https://www.sorinpyle.com/{page_path}"
            elif page == 'index.html':
                expected = "https://www.sorinpyle.com/"
            else:
                expected = f"https://www.sorinpyle.com/{page.replace('.html', '')}"

            if canonical != expected:
                high_priority.append(f"{page}: INCORRECT canonical URL - Found: {canonical}, Expected: {expected}")

    # Check Open Graph completeness
    for page, data in results.items():
        og_tags = data.get('og_tags', {})
        if og_tags and len(og_tags) < 4:
            missing = []
            if 'og:title' not in og_tags:
                missing.append('og:title')
            if 'og:description' not in og_tags:
                missing.append('og:description')
            if 'og:url' not in og_tags:
                missing.append('og:url')
            if 'og:image' not in og_tags:
                missing.append('og:image')
            if 'og:type' not in og_tags:
                missing.append('og:type')
            if missing:
                high_priority.append(f"{page}: INCOMPLETE Open Graph tags - Missing: {', '.join(missing)}")

    if high_priority:
        print("HIGH PRIORITY ISSUES")
        print("-" * 80)
        for issue in sorted(high_priority):
            print(f"  - {issue}")
        print()

    # MEDIUM PRIORITY ISSUES
    medium_priority = []

    for page, data in results.items():
        title_len = data.get('title_length', 0)
        meta_len = data.get('meta_length', 0)

        if title_len > 0:
            if title_len < 30:
                medium_priority.append(f"{page}: Title too short ({title_len} chars) - Optimal: 50-60")
            elif title_len > 70:
                medium_priority.append(f"{page}: Title too long ({title_len} chars) - Optimal: 50-60")

        if meta_len > 0:
            if meta_len < 120:
                medium_priority.append(f"{page}: Meta description too short ({meta_len} chars) - Optimal: 150-160")
            elif meta_len > 170:
                medium_priority.append(f"{page}: Meta description too long ({meta_len} chars) - Optimal: 150-160")

        if not data.get('ai_optimization'):
            medium_priority.append(f"{page}: Missing AI optimization meta tag")

    if medium_priority:
        print("MEDIUM PRIORITY ISSUES (Optimization Opportunities)")
        print("-" * 80)
        for issue in sorted(medium_priority):
            print(f"  - {issue}")
        print()

    # SCHEMA VALIDATION
    schema_issues = []

    # Expected schema by page type
    schema_expectations = {
        'dui-defense.html': ['LegalService'],
        'domestic-violence-defense.html': ['LegalService'],
        'first-offense-owi.html': ['LegalService'],
        'super-drunk-high-bac.html': ['LegalService'],
        'cdl-owi-defense.html': ['LegalService'],
        'repeat-offense-owi.html': ['LegalService'],
        'faq.html': ['FAQPage'],
        'your-rights.html': ['Article'],
        'blog.html': ['BlogPosting'],
        'jonathan-pyle.html': ['Person'],
        'sorin-panainte.html': ['Person'],
    }

    for page, expected_types in schema_expectations.items():
        if page in results:
            data = results[page]
            if not data.get('has_schema'):
                schema_issues.append(f"{page}: MISSING schema markup (expected: {', '.join(expected_types)})")
            else:
                found_types = data.get('schema_types', [])
                for expected_type in expected_types:
                    if expected_type not in found_types:
                        schema_issues.append(f"{page}: Missing '{expected_type}' schema (found: {', '.join(found_types)})")

    # Check location pages for BreadcrumbList
    for page in results.keys():
        if page.startswith('locations\\') or page.startswith('locations/'):
            data = results[page]
            if data.get('has_schema'):
                types = data.get('schema_types', [])
                if 'BreadcrumbList' not in types and 'BreadcrumbList' not in str(types):
                    schema_issues.append(f"{page}: Missing BreadcrumbList schema")

    if schema_issues:
        print("SCHEMA MARKUP ISSUES")
        print("-" * 80)
        for issue in sorted(schema_issues):
            print(f"  - {issue}")
        print()

    # PERFECT PAGES
    perfect_pages = []
    for page, data in results.items():
        if (data.get('title') and
            data.get('meta_description') and
            data.get('canonical') and
            50 <= data.get('title_length', 0) <= 70 and
            150 <= data.get('meta_length', 0) <= 170 and
            len(data.get('og_tags', {})) >= 4):
            perfect_pages.append(page)

    if perfect_pages:
        print("PERFECT SEO METADATA (Well-Optimized Pages)")
        print("-" * 80)
        for page in sorted(perfect_pages):
            print(f"  ✓ {page}")
        print()

    # Save detailed results to JSON
    with open(base_dir / 'seo_audit_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("=" * 80)
    print(f"Detailed results saved to: seo_audit_results.json")
    print("=" * 80)

if __name__ == '__main__':
    main()
