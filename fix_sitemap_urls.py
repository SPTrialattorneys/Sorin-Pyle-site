import re

# Read sitemap
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Define URL patterns that need .html extension
# These are all the actual .html files in the site
urls_needing_html = [
    # Root pages
    'attorneys',
    'practice-areas',
    'locations',
    'contact',
    'sorin-panainte',
    'jonathan-pyle',
    'privacy-policy',
    'faq',
    'your-rights',
    'blog',
    'community-resources',
    'dui-defense',
    'first-offense-owi',
    'super-drunk-high-bac',
    'cdl-owi-defense',
    'repeat-offense-owi',
    'domestic-violence-defense',
    'record-expungement',
    'drivers-license-restoration',
    'card',
    # Location pages - cities
    'locations/holland-mi',
    'locations/grand-rapids-mi',
    'locations/grand-haven-mi',
    'locations/allendale-mi',
    'locations/hudsonville-mi',
    'locations/zeeland-mi',
    'locations/wyoming-mi',
    'locations/kentwood-mi',
    'locations/saugatuck-mi',
    'locations/walker-mi',
    'locations/grandville-mi',
    'locations/south-haven-mi',
    'locations/jenison-mi',
    # Location pages - student defense
    'locations/gvsu-student-defense',
    'locations/grcc-student-defense',
    'locations/hope-college-student-defense',
    'locations/calvin-university-student-defense',
    'locations/wmu-student-defense',
    'locations/ferris-student-defense',
    'locations/davenport-student-defense',
    # Location pages - counties
    'locations/ottawa-county',
    'locations/kent-county',
    'locations/allegan-county',
    'locations/van-buren-county',
    'locations/kalamazoo-county',
    'locations/muskegon-county',
    'locations/newaygo-county',
    'locations/other-michigan-counties',
]

# Special cases - card subfolder
card_urls = [
    'card/sorin',
    'card/jonathan',
]

update_count = 0

# Update each URL to add .html extension
for url in urls_needing_html:
    # Pattern: <loc>https://www.sorinpyle.com/URL</loc>
    # Replace with: <loc>https://www.sorinpyle.com/URL.html</loc>
    pattern = f'(<loc>https://www.sorinpyle.com/{re.escape(url)})(</loc>)'
    replacement = f'\\1.html\\2'

    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        update_count += 1
        content = new_content
        print(f"[DONE] Updated: {url} -> {url}.html")

# Update card URLs separately
for url in card_urls:
    pattern = f'(<loc>https://www.sorinpyle.com/{re.escape(url)})(</loc>)'
    replacement = f'\\1.html\\2'

    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        update_count += 1
        content = new_content
        print(f"[DONE] Updated: {url} -> {url}.html")

# Write updated sitemap
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n[INFO] Total URLs updated: {update_count}")
print("[INFO] Sitemap URLs now match canonical URLs with .html extensions")
print("[INFO] Homepage (/) left unchanged (correct as root URL)")
