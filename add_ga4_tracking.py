#!/usr/bin/env python3
"""
Add Google Analytics 4 tracking code to all HTML pages missing it.
Sorin & Pyle Law Firm Website - Pre-Launch Fix
"""

import os
import re

# GA4 tracking code to insert (from index.html lines 26-99)
GA4_CODE = """
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-LV7PKRF2YT"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-LV7PKRF2YT', {
            // Enhanced tracking for legal websites
            page_title: document.title,
            page_location: window.location.href,
            // Core Web Vitals tracking
            custom_map: {
                'custom_parameter_1': 'page_type',
                'custom_parameter_2': 'practice_area'
            }
        });

        // Track Core Web Vitals
        function trackWebVitals() {
            function sendToGoogleAnalytics({name, delta, value, id}) {
                gtag('event', name, {
                    event_category: 'Web Vitals',
                    event_label: id,
                    value: Math.round(name === 'CLS' ? delta * 1000 : delta),
                    non_interaction: true,
                });
            }

            // Load web-vitals library
            import('https://unpkg.com/web-vitals@3/dist/web-vitals.js').then(({onCLS, onFID, onFCP, onLCP, onTTFB}) => {
                onCLS(sendToGoogleAnalytics);
                onFID(sendToGoogleAnalytics);
                onFCP(sendToGoogleAnalytics);
                onLCP(sendToGoogleAnalytics);
                onTTFB(sendToGoogleAnalytics);
            });
        }

        // Track page engagement for legal sites
        function trackEngagement() {
            let engagementTime = 0;
            let lastActiveTime = Date.now();

            const trackTime = () => {
                const now = Date.now();
                engagementTime += now - lastActiveTime;
                lastActiveTime = now;
            };

            ['mousedown', 'touchstart', 'keydown', 'scroll'].forEach(event => {
                document.addEventListener(event, trackTime, {passive: true});
            });

            // Send engagement data on page unload
            window.addEventListener('beforeunload', () => {
                gtag('event', 'engagement_time', {
                    event_category: 'User Engagement',
                    value: Math.round(engagementTime / 1000),
                    non_interaction: true
                });
            });
        }

        // Initialize tracking when DOM is ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                trackWebVitals();
                trackEngagement();
            });
        } else {
            trackWebVitals();
            trackEngagement();
        }
    </script>
"""

# Pages that ALREADY have GA4 tracking (skip these)
PAGES_WITH_GA4 = [
    'index.html',
    'community-resources.html',
    'card.html',
    'card/sorin.html',
    'card/jonathan.html',
]

# Pages to update
ROOT_PAGES = [
    '404.html', '500.html', 'attorneys.html', 'blog.html', 'cdl-owi-defense.html',
    'contact.html', 'domestic-violence-defense.html', 'dui-defense.html',
    'drivers-license-restoration.html', 'faq.html', 'first-offense-owi.html',
    'jonathan-pyle.html', 'locations.html', 'practice-areas.html',
    'privacy-policy.html', 'record-expungement.html', 'repeat-offense-owi.html',
    'resources.html', 'sorin-panainte.html', 'super-drunk-high-bac.html',
    'your-rights.html'
]

LOCATION_PAGES = [
    'locations/allegan-county.html', 'locations/allendale-mi.html',
    'locations/calvin-university-student-defense.html',
    'locations/davenport-student-defense.html', 'locations/ferris-student-defense.html',
    'locations/grand-haven-mi.html', 'locations/grand-rapids-mi.html',
    'locations/grandville-mi.html', 'locations/grcc-student-defense.html',
    'locations/gvsu-student-defense.html', 'locations/holland-mi.html',
    'locations/hope-college-student-defense.html', 'locations/hudsonville-mi.html',
    'locations/jenison-mi.html', 'locations/kalamazoo-county.html',
    'locations/kent-county.html', 'locations/kentwood-mi.html',
    'locations/muskegon-county.html', 'locations/newaygo-county.html',
    'locations/other-michigan-counties.html', 'locations/ottawa-county.html',
    'locations/saugatuck-mi.html', 'locations/south-haven-mi.html',
    'locations/van-buren-county.html', 'locations/walker-mi.html',
    'locations/wmu-student-defense.html', 'locations/wyoming-mi.html',
    'locations/zeeland-mi.html'
]

ALL_PAGES = ROOT_PAGES + LOCATION_PAGES


def add_ga4_to_file(filepath):
    """Add GA4 tracking code to a single HTML file."""

    if not os.path.exists(filepath):
        print(f"  [WARN] File not found: {filepath}")
        return False

    # Read file content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if GA4 already exists (by checking for the tracking ID)
    if 'G-LV7PKRF2YT' in content:
        print(f"  [SKIP] Already has GA4: {filepath}")
        return False

    # Find insertion point: after Twitter card meta tag
    # Pattern: <meta name="twitter:card" content="summary_large_image">
    twitter_card_pattern = r'(<meta name="twitter:card" content="[^"]+">)'

    if not re.search(twitter_card_pattern, content):
        print(f"  [WARN] Could not find Twitter card meta tag in: {filepath}")
        return False

    # Insert GA4 code after Twitter card meta tag
    updated_content = re.sub(
        twitter_card_pattern,
        r'\1' + GA4_CODE,
        content,
        count=1
    )

    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"  [DONE] Added GA4 to: {filepath}")
    return True


def main():
    """Add GA4 tracking to all pages missing it."""

    print("=" * 70)
    print("ADDING GOOGLE ANALYTICS 4 TRACKING TO SORIN & PYLE WEBSITE")
    print("=" * 70)
    print()

    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print(f"Working directory: {os.getcwd()}")
    print(f"Total pages to update: {len(ALL_PAGES)}")
    print()

    updated_count = 0
    skipped_count = 0
    error_count = 0

    # Process all pages
    for page in ALL_PAGES:
        try:
            result = add_ga4_to_file(page)
            if result:
                updated_count += 1
            else:
                skipped_count += 1
        except Exception as e:
            print(f"  [ERROR] Error processing {page}: {str(e)}")
            error_count += 1

    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"[SUCCESS] Updated: {updated_count} pages")
    print(f"[SKIP] Skipped (already had GA4): {skipped_count} pages")
    print(f"[ERROR] Errors: {error_count} pages")
    print()

    if updated_count > 0:
        print("[SUCCESS] Google Analytics 4 tracking added to all missing pages.")
        print()
        print("NEXT STEPS:")
        print("1. Test in browser: Open any updated page and check console (F12)")
        print("2. Verify no errors: Should see NO 'gtag is not defined' errors")
        print("3. Check GA4 Real-Time: Visit https://analytics.google.com/")
        print("4. Browse 5-10 pages and verify they appear in Real-Time report")
        print()
    elif skipped_count == len(ALL_PAGES):
        print("[INFO] All pages already have GA4 tracking. No updates needed!")
    else:
        print("[WARN] Some pages were not updated. Check errors above.")

    print("=" * 70)


if __name__ == '__main__':
    main()
