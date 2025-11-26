# Utilities Folder

This directory contains build tools, validation scripts, and documentation for the Sorin & Pyle website.

## Directory Structure

```
utilities/
├── README.md                    # This file
├── docs/                        # Task-focused documentation
│   ├── CSS_GUIDE.md            # CSS development guide
│   ├── SCHEMA_GUIDE.md         # Schema markup guide
│   ├── CONTENT_GUIDE.md        # Content editing guide
│   └── TROUBLESHOOTING.md      # Common issues & solutions
├── legacy/                      # Archived one-time scripts (64 files)
│   └── *.py                    # Historical migration/fix scripts
├── extract-critical-css.mjs    # ACTIVE: Extract critical CSS
├── generate-schema.js          # ACTIVE: Schema template generator
├── pre-commit-check.js         # ACTIVE: Pre-commit validation
├── process-images.mjs          # ACTIVE: Image optimization
├── validate-html.js            # ACTIVE: HTML validation
└── validate-schema.js          # ACTIVE: Schema markup validation
```

---

## Active Scripts

These scripts are actively used in the build process or development workflow:

### `validate-schema.js`
**Purpose:** Validates all JSON-LD schema markup across the site
**Usage:** `npm run validate:schema`
**When:** Before committing changes to schema markup
**Output:** Reports errors/warnings for LegalService, Person, BlogPosting, FAQPage, BreadcrumbList schemas

### `validate-html.js`
**Purpose:** Validates HTML for broken links, missing alt text, duplicate IDs, meta descriptions
**Usage:** `npm run validate:html`
**When:** Automatically runs on git commit (if HTML/template files staged)
**Checks:**
- Broken internal links (href, src)
- Missing image alt text
- Duplicate HTML IDs
- Missing/empty meta descriptions
- Canonical URL consistency with sitemap.xml

### `pre-commit-check.js`
**Purpose:** Runs all validation checks before git commit
**Usage:** Automatic via Husky pre-commit hook
**When:** Runs on `git commit`
**Checks:**
- Check 1-4: Schema validation (LegalService, Person, BlogPosting, etc.)
- Check 5: HTML validation (links, alt text, meta descriptions)

### `extract-critical-css.mjs`
**Purpose:** Extracts above-the-fold CSS for inline rendering
**Usage:** `npm run build:critical`
**When:** After CSS changes affecting above-the-fold styles
**Output:** Writes to `src/_data/critical-*.css` (4 files)
**Note:** Runs **locally only** (not on Cloudflare) - commit extracted files

### `process-images.mjs`
**Purpose:** Optimizes images with Sharp (AVIF, WebP, responsive variants)
**Usage:** `npm run build:images`
**When:** After adding new images to `images/` folder
**Output:** Generates responsive image variants and `src/_data/images.json` manifest

### `generate-schema.js`
**Purpose:** Generates schema markup templates for pages
**Usage:** Node script (not in package.json)
**When:** Creating new location or service pages
**Note:** Helper tool for consistent schema generation

---

## Legacy Scripts (`legacy/` folder)

The `legacy/` directory contains **64 Python scripts** from historical development sessions. These are **one-time migration/fix scripts** that have already been run and should not be executed again.

### Categories of Legacy Scripts:

**Migration Scripts (5 files):**
- `migrate-location-pages.py` - Migrated location pages to Eleventy
- `migrate-main-pages.py` - Migrated main pages to Eleventy
- `migrate-practice-pages.py` - Migrated practice area pages
- `migrate-resource-pages.py` - Migrated resource pages
- `migrate-utility-pages.py` - Migrated utility pages

**Fix Scripts (30+ files):**
- `fix_*.py` - One-time fixes for footer, phone links, sitemap, etc.
- `add_*.py` - Scripts that added GA4, accessibility links, cookie consent, etc.
- `update_*.py` - Historical update scripts

**Duplicate Versions:**
- `*_v2.py`, `*_v3.py` - Multiple versions of same script from iterative development

**Other Scripts:**
- Conversion scripts (async CSS, dropdown to button, etc.)
- Cleanup scripts
- Analysis/categorization tools

### ⚠️ Important Notes on Legacy Scripts:

1. **DO NOT RUN** - These scripts have already been executed
2. **DO NOT DELETE** - Kept for historical reference and understanding past changes
3. **Reference Only** - Useful for understanding how site was built/migrated
4. **No Maintenance** - Not actively maintained, may not work with current codebase

If you need to perform similar operations, **create a new script** based on legacy examples rather than re-running old scripts.

---

## Documentation (`docs/` folder)

Task-focused guides for common development tasks:

### `CSS_GUIDE.md` (10 min read)
- CSS architecture overview
- Component styling patterns
- Critical CSS system
- Mobile-first responsive design
- Common styling tasks

### `SCHEMA_GUIDE.md` (10 min read)
- Schema.org markup patterns
- LegalService schema for service pages
- Person schema for attorney profiles
- BlogPosting schema for blog posts
- FAQPage schema for Q&A content
- Validation best practices

### `CONTENT_GUIDE.md` (12 min read)
- Writing blog posts in Markdown
- Adding new practice area pages
- Location page creation
- MRPC 7.1 compliance (attorney advertising ethics)
- SEO best practices

### `TROUBLESHOOTING.md` (15 min read)
- Build failures
- Schema validation errors
- Critical CSS issues
- Common HTML validation warnings
- Deployment problems

---

## Common Development Tasks

### Before Committing Changes:
```bash
npm run validate:all        # Run all validation checks
npm run pre-commit-check    # Full pre-commit validation
```

### After CSS Changes:
```bash
npm run build:css           # Build main CSS
npm run build:critical      # Extract critical CSS (local only!)
npm run build:html:prod     # Rebuild HTML with new critical CSS
git add src/_data/critical-*.css src/assets/styles/*.css
```

### After Adding Images:
```bash
npm run build:images        # Optimize and create responsive variants
git add images/ src/_data/images.json
```

### After Schema Changes:
```bash
npm run validate:schema     # Check for schema errors
npm run build:html          # Rebuild HTML
```

---

## Build Process Integration

### Active Scripts in `package.json`:

```json
{
  "build:critical": "node utilities/extract-critical-css.mjs",
  "build:images": "node process-images.mjs",
  "validate:schema": "node utilities/validate-schema.js",
  "validate:html": "node utilities/validate-html.js",
  "validate:all": "npm run validate:schema && npm run validate:html",
  "pre-commit-check": "node utilities/pre-commit-check.js"
}
```

### Husky Pre-Commit Hook:

Automatically runs `utilities/pre-commit-check.js` when:
- Committing `.njk`, `.html`, or `src/` files
- Schema or HTML validation errors will block commit
- Warnings don't block (but should be reviewed)

---

## Adding New Utilities

If you need to create a new utility script:

1. **Choose appropriate language:**
   - JavaScript (`.js`/`.mjs`) for active build tools
   - Python only if integrating with existing Python tooling
   - Node.js preferred for consistency with Eleventy

2. **Add to package.json** if it's part of build/validation workflow

3. **Document in this README** under "Active Scripts" section

4. **Create corresponding documentation** in `docs/` if needed

---

## Questions?

- **Quick Start:** See [QUICK_START.md](../QUICK_START.md) (5 min)
- **Full Technical Docs:** See [AI_CONTEXT.md](../AI_CONTEXT.md) (~16,000 words)
- **Package Scripts:** Run `npm run docs` to see all documentation
