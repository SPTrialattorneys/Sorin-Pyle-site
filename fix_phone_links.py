import re
import os

# Phone number pattern to find and replace
# Find: tel:6162273303
# Replace: tel:+16162273303

def fix_phone_links(file_path):
    """Standardize phone links to international format"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has non-international format phone links
        if 'tel:6162273303' not in content:
            return False  # No changes needed

        # Replace tel:6162273303 with tel:+16162273303
        updated_content = content.replace('tel:6162273303', 'tel:+16162273303')

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        # Count how many replacements were made
        count = content.count('tel:6162273303')
        print(f"[DONE] {file_path} - Updated {count} phone link(s)")
        return True

    except Exception as e:
        print(f"[ERROR] {file_path} - {str(e)}")
        return False

def main():
    """Process all HTML files"""

    update_count = 0
    file_count = 0
    total_links = 0

    # Process root HTML files
    print("\n=== Processing Root HTML Files ===\n")
    root_files = [f for f in os.listdir('.') if f.endswith('.html')]

    for filename in sorted(root_files):
        if fix_phone_links(filename):
            update_count += 1
        file_count += 1

    # Process location HTML files
    print("\n=== Processing Location HTML Files ===\n")
    location_dir = 'locations'
    if os.path.exists(location_dir):
        location_files = [f for f in os.listdir(location_dir) if f.endswith('.html')]

        for filename in sorted(location_files):
            file_path = os.path.join(location_dir, filename)
            if fix_phone_links(file_path):
                update_count += 1
            file_count += 1

    # Process card HTML files
    print("\n=== Processing Card HTML Files ===\n")
    card_dir = 'card'
    if os.path.exists(card_dir):
        card_files = [f for f in os.listdir(card_dir) if f.endswith('.html')]

        for filename in sorted(card_files):
            file_path = os.path.join(card_dir, filename)
            if fix_phone_links(file_path):
                update_count += 1
            file_count += 1

    # Summary
    print("\n=== Summary ===")
    print(f"[INFO] Files updated: {update_count}")
    print(f"[INFO] Total files processed: {file_count}")
    print(f"[INFO] All phone links now use international format: tel:+16162273303")

if __name__ == "__main__":
    main()
