import re
import os

# Footer bottom bar patterns
ROOT_COPYRIGHT_PATTERN = r'(<div class="footer_bottom-bar">\s*© 2025 Sorin & Pyle, PC\. All Rights Reserved\.)'
LOCATION_COPYRIGHT_PATTERN = ROOT_COPYRIGHT_PATTERN

# Privacy policy link to insert
ROOT_PRIVACY_LINK = r'\1 | <a href="privacy-policy.html">Privacy Policy</a>'
LOCATION_PRIVACY_LINK = r'\1 | <a href="../privacy-policy.html">Privacy Policy</a>'

def add_privacy_policy_link(file_path, is_location_file=False):
    """Add privacy policy link to footer bottom bar if not already present"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if privacy policy link already exists
        if 'privacy-policy.html">Privacy Policy</a>' in content:
            print(f"[SKIP] {file_path} - Privacy policy link already exists")
            return False

        # Choose pattern and replacement based on file type
        if is_location_file:
            pattern = LOCATION_COPYRIGHT_PATTERN
            replacement = LOCATION_PRIVACY_LINK
        else:
            pattern = ROOT_COPYRIGHT_PATTERN
            replacement = ROOT_PRIVACY_LINK

        # Check if pattern exists
        if not re.search(pattern, content):
            print(f"[WARN] {file_path} - Footer bottom bar not found with expected pattern")
            return False

        # Add privacy policy link
        updated_content = re.sub(pattern, replacement, content, count=1)

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"[DONE] {file_path} - Privacy policy link added")
        return True

    except Exception as e:
        print(f"[ERROR] {file_path} - {str(e)}")
        return False

def main():
    """Process all HTML files"""

    success_count = 0
    skip_count = 0
    error_count = 0

    # Process root HTML files
    print("\n=== Processing Root HTML Files ===\n")
    root_files = [f for f in os.listdir('.') if f.endswith('.html')]

    for filename in sorted(root_files):
        result = add_privacy_policy_link(filename, is_location_file=False)
        if result:
            success_count += 1
        elif 'already exists' in str(result):
            skip_count += 1
        else:
            error_count += 1

    # Process location HTML files
    print("\n=== Processing Location HTML Files ===\n")
    location_dir = 'locations'
    if os.path.exists(location_dir):
        location_files = [f for f in os.listdir(location_dir) if f.endswith('.html')]

        for filename in sorted(location_files):
            file_path = os.path.join(location_dir, filename)
            result = add_privacy_policy_link(file_path, is_location_file=True)
            if result:
                success_count += 1
            elif 'already exists' in str(result):
                skip_count += 1
            else:
                error_count += 1

    # Summary
    print("\n=== Summary ===")
    print(f"[DONE] Successfully updated: {success_count} files")
    print(f"[SKIP] Already had privacy link: {skip_count} files")
    print(f"[ERROR] Errors encountered: {error_count} files")
    print(f"[INFO] Total files processed: {success_count + skip_count + error_count}")

if __name__ == "__main__":
    main()
