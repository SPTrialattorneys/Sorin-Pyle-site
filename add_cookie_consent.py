import re
import os

# HTML to insert in <head> section (after existing CSS)
COOKIE_CSS = '''    <!-- Cookie Consent Banner -->
    <link rel="stylesheet" href="css/cookie-consent.css">'''

# HTML to insert before closing </body> tag (after existing scripts)
COOKIE_JS = '''    <!-- Cookie Consent Banner -->
    <script src="js/cookie-consent.js" defer></script>'''

# For location subfolder files
COOKIE_CSS_LOCATION = '''    <!-- Cookie Consent Banner -->
    <link rel="stylesheet" href="../css/cookie-consent.css">'''

COOKIE_JS_LOCATION = '''    <!-- Cookie Consent Banner -->
    <script src="../js/cookie-consent.js" defer></script>'''

# For card subfolder files
COOKIE_CSS_CARD = '''    <!-- Cookie Consent Banner -->
    <link rel="stylesheet" href="../css/cookie-consent.css">'''

COOKIE_JS_CARD = '''    <!-- Cookie Consent Banner -->
    <script src="../js/cookie-consent.js" defer></script>'''

def add_cookie_consent(file_path, is_location=False, is_card=False):
    """Add cookie consent CSS and JS to HTML file"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already added
        if 'cookie-consent.css' in content:
            print(f"[SKIP] {file_path} - Cookie consent already added")
            return False

        # Choose correct paths based on file location
        if is_location or is_card:
            css_to_add = COOKIE_CSS_LOCATION if is_location else COOKIE_CSS_CARD
            js_to_add = COOKIE_JS_LOCATION if is_location else COOKIE_JS_CARD
        else:
            css_to_add = COOKIE_CSS
            js_to_add = COOKIE_JS

        # Add CSS before </head>
        if '</head>' in content:
            content = content.replace('</head>', css_to_add + '\n</head>', 1)
        else:
            print(f"[WARN] {file_path} - No </head> tag found")
            return False

        # Add JS before </body>
        if '</body>' in content:
            content = content.replace('</body>', js_to_add + '\n</body>', 1)
        else:
            print(f"[WARN] {file_path} - No </body> tag found")
            return False

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[DONE] {file_path} - Cookie consent added")
        return True

    except Exception as e:
        print(f"[ERROR] {file_path} - {str(e)}")
        return False

def main():
    """Process all HTML files"""

    update_count = 0
    skip_count = 0

    # Process root HTML files
    print("\n=== Processing Root HTML Files ===\n")
    root_files = [f for f in os.listdir('.') if f.endswith('.html')]

    for filename in sorted(root_files):
        result = add_cookie_consent(filename, is_location=False, is_card=False)
        if result:
            update_count += 1
        else:
            skip_count += 1

    # Process location HTML files
    print("\n=== Processing Location HTML Files ===\n")
    location_dir = 'locations'
    if os.path.exists(location_dir):
        location_files = [f for f in os.listdir(location_dir) if f.endswith('.html')]

        for filename in sorted(location_files):
            file_path = os.path.join(location_dir, filename)
            result = add_cookie_consent(file_path, is_location=True, is_card=False)
            if result:
                update_count += 1
            else:
                skip_count += 1

    # Process card HTML files
    print("\n=== Processing Card HTML Files ===\n")
    card_dir = 'card'
    if os.path.exists(card_dir):
        card_files = [f for f in os.listdir(card_dir) if f.endswith('.html')]

        for filename in sorted(card_files):
            file_path = os.path.join(card_dir, filename)
            result = add_cookie_consent(file_path, is_location=False, is_card=True)
            if result:
                update_count += 1
            else:
                skip_count += 1

    # Summary
    print("\n=== Summary ===")
    print(f"[INFO] Files updated: {update_count}")
    print(f"[INFO] Files skipped: {skip_count}")
    print(f"[INFO] Cookie consent banner added to all pages")
    print(f"[INFO] CSS: css/cookie-consent.css")
    print(f"[INFO] JS: js/cookie-consent.js")

if __name__ == "__main__":
    main()
