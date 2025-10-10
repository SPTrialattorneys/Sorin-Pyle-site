# Header & Footer Maintenance Guide

## Overview

Your site now uses **shared header and footer files** to ensure consistency across all 20+ HTML pages. This means you can update navigation in ONE place and it applies everywhere.

## Shared Include Files

Located in `_includes/` folder:
- `_includes/header.html` - Navigation (desktop + mobile)
- `_includes/footer.html` - Footer with contact info and links

## How to Update Navigation

### Adding a New Menu Item

1. Open `_includes/header.html`
2. Find the desktop navigation section (around line 17)
3. Add your new menu item:

```html
<li class="navbar_item" role="none">
    <a href="new-page.html" class="navbar_link" role="menuitem">New Page</a>
</li>
```

4. Also add it to the mobile navigation (around line 37)
5. Run the update script (see below)

### Changing Navigation Text

1. Edit `_includes/header.html`
2. Find the menu item and change the text
3. Update both desktop AND mobile menus
4. Run the update script

### Example: Changing "About" to "Home"

In `_includes/header.html`, change:
```html
<a href="index.html" class="navbar_link" role="menuitem">About</a>
```

To:
```html
<a href="index.html" class="navbar_link" role="menuitem">Home</a>
```

Do this in BOTH the desktop menu AND mobile menu sections.

## How to Update Footer

### Changing Contact Information

1. Open `_includes/footer.html`
2. Update the information:

```html
<div class="footer_column">
    <h3>Sorin & Pyle, PC</h3>
    <p>NEW ADDRESS HERE<br>CITY, STATE ZIP</p>
    <p>
        <a href="tel:NEW PHONE">NEW PHONE DISPLAY</a><br>
        <a href="mailto:NEW EMAIL">NEW EMAIL</a>
    </p>
</div>
```

3. Run the update script

### Adding Footer Links

Edit the "Quick Links" section in `_includes/footer.html`:

```html
<div class="footer_column">
    <h3>Quick Links</h3>
    <ul class="footer_list">
        <li><a href="index.html">About</a></li>
        <!-- Add new link here -->
        <li><a href="new-page.html">New Page</a></li>
    </ul>
</div>
```

## Applying Changes to All Pages

After editing `_includes/header.html` or `_includes/footer.html`, run this command:

```bash
node update-includes.cjs
```

This automatically updates all 20+ HTML files with your changes.

## What the Update Script Does

The `update-includes.cjs` script:
1. Reads `_includes/header.html` and `_includes/footer.html`
2. Finds the header/footer sections in each HTML file
3. Replaces them with the updated versions
4. Reports which files were updated

## Important Notes

⚠️ **Always edit the include files, never individual HTML pages** for header/footer changes

✅ **After editing includes**, always run `node update-includes.cjs`

✅ **Keep backups** before running updates (git commit your changes first)

## Common Scenarios

### Scenario 1: Add a new page to navigation

1. Edit `_includes/header.html`
2. Add menu item to desktop nav
3. Add same menu item to mobile nav
4. Run `node update-includes.cjs`
5. Done! All 20+ pages now have the new menu item

### Scenario 2: Change phone number

1. Edit `_includes/footer.html`
2. Update phone number in contact section
3. Update phone number in all  footer column sections if needed
4. Run `node update-includes.cjs`
5. Done! Phone number updated everywhere

### Scenario 3: Rebrand "Firm News & FAQs"

1. Edit `_includes/header.html`
2. Change text in desktop menu
3. Change text in mobile menu
4. Edit `_includes/footer.html`
5. Change text in footer Quick Links
6. Run `node update-includes.cjs`
7. Done! Name changed everywhere

## Files Updated by Script

The script updates these files automatically:
- `index.html`
- `attorneys.html`
- `contact.html`
- `practice-areas.html`
- `locations.html`
- `resources.html`
- `local-resources.html`
- `privacy-policy.html`
- `record-expungement.html`
- `drivers-license-restoration.html`
- `jonathan-pyle.html`
- `sorin-panainte.html`
- `locations/ottawa-county.html`
- `locations/kent-county.html`
- `locations/allegan-county.html`
- `locations/kalamazoo-county.html`
- `locations/muskegon-county.html`
- `locations/van-buren-county.html`
- `locations/newaygo-county.html`
- `locations/other-michigan-counties.html`

## Troubleshooting

**Q: Script says "markers not found" for a file**
A: That file doesn't have the standard header/footer structure. You may need to update it manually.

**Q: Changes didn't apply to all pages**
A: Make sure you ran `node update-includes.cjs` after editing the include files.

**Q: Accidentally broke something**
A: Use git to revert: `git checkout -- _includes/header.html` or restore from backup.

## Benefits of This System

✅ Update navigation in ONE place, applies to 20+ pages
✅ Consistent header/footer across entire site
✅ No more manual copy/paste across files
✅ Easy to maintain and update
✅ Reduces human error

## Future Additions

When you create new HTML pages:
1. Copy header section from any existing page
2. Copy footer section from any existing page
3. Future updates will automatically include the new page

---

**Quick Reference Commands:**

```bash
# Update all pages with latest header/footer
node update-includes.cjs

# Check which files have old headers/footers
grep -l "Firm Updates & Resources" *.html
```
