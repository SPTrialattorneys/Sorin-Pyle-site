# CSS Guide - Sorin & Pyle Website

**Last Updated:** November 24, 2025
**Read Time:** 10-12 minutes

> **Quick Reference:** Essential CSS workflow for styling updates on the Sorin & Pyle Eleventy site.
>
> **See Also:**
> [QUICK_START.md](../../QUICK_START.md) | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | [AI_CONTEXT.md](../../AI_CONTEXT.md)

---

## 📋 Table of Contents

1. [Quick Reference](#quick-reference)
2. [CSS Architecture Overview](#css-architecture-overview)
3. [Standard CSS Update Workflow](#standard-css-update-workflow)
4. [Critical CSS Update Workflow](#critical-css-update-workflow)
5. [Critical CSS Automation](#critical-css-automation)
6. [Mobile Breakpoints & Responsive Design](#mobile-breakpoints--responsive-design)
7. [Troubleshooting CSS Issues](#troubleshooting-css-issues)
8. [File Organization](#file-organization)

---

## 🚀 Quick Reference

### Essential Commands

```bash
# Build CSS only
npm run build:css                # PostCSS processes src/assets/styles/ → dist/css/main.min.css

# Build HTML (before critical extraction)
npm run build:html:prod          # Eleventy builds HTML from src/pages/*.njk

# Extract critical CSS (requires dist/ to exist)
npm run build:critical           # Auto-extracts above-the-fold CSS from dist/*.html

# Full production build (recommended)
npm run build:cloudflare         # Complete: Clean → CSS → HTML → Critical → HTML → JS
```

### Critical Rules

- ✅ **Edit main CSS only**: `src/assets/styles/*.css` (single source of truth)
- 🤖 **Critical CSS auto-generated**: `src/_data/critical-*.css` (don't manually edit)
- 🔄 **Build twice for CSS changes**: CSS → HTML → Critical → HTML (automated in `build:cloudflare`)

---

## 🏗️ CSS Architecture Overview

### Dual CSS System Explained

The site uses **TWO separate CSS systems** for optimal performance:

```
┌─────────────────────────────────────────────────────────────┐
│  MAIN CSS (Deferred Loading)                                 │
│  src/assets/styles/*.css → dist/css/main.min.css            │
│  Loads AFTER page render (non-blocking)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
              ┌───────────────────────────────┐
              │   PostCSS Build Pipeline      │
              │   - postcss-import            │
              │   - autoprefixer              │
              │   - cssnano (DISABLED)        │
              └───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  CRITICAL CSS (Inline in <head>)                            │
│  src/_data/critical-*.css                                    │
│  Displays FIRST (above-the-fold instant render)             │
│  Auto-extracted from rendered HTML                          │
└─────────────────────────────────────────────────────────────┘
```

### Why This Matters

**Performance Optimization:**
- **Critical CSS** = Inline in `<head>` → Browser displays above-the-fold content INSTANTLY
- **Main CSS** = Deferred loading → Non-blocking, loads after initial render
- **Result:** Fast First Contentful Paint (FCP) and Largest Contentful Paint (LCP)

**Eliminates Flash of Unstyled Content (FOUC):**
- Critical CSS ensures proper styling from first render
- No white page or layout shifts while CSS loads

---

### CSS Source Files

**Location:** `src/assets/styles/`

```
main.css (entry point) imports:
  ├─ core-brand.css       # CSS variables, resets, brand colors
  ├─ style-core.css       # Core component styles (navbar, footer, buttons)
  ├─ style.css            # Page-specific styles
  ├─ style-blog.css       # Blog page styles
  ├─ style-faq.css        # FAQ page styles
  ├─ style-card-pages.css # Digital business card styles
  └─ cookie-consent.css   # Cookie consent banner
```

**Build Output:** `dist/css/main.min.css` (bundled, NOT minified - see cssnano note below)

---

### Critical CSS Files (Auto-Generated)

**Location:** `src/_data/`

1. **`critical-homepage.css`** (~28KB) - Extracted from `dist/index.html`
2. **`critical-attorneys.css`** (~22KB) - Extracted from `dist/attorneys.html`
3. **`critical-practice-areas.css`** (~19KB) - Extracted from `dist/practice-areas.html`
4. **`critical-page-layout.css`** (~15KB) - Extracted from `dist/dui-defense.html` (used by 25+ pages)

**⚠️ IMPORTANT:** These files are **auto-generated during build**. Do NOT manually edit them!

---

### Loading Mechanism

**In Page Frontmatter** (index.njk, attorneys.njk, practice-areas.njk):
```njk
---
criticalCSSFile: critical-homepage.css
---
```

**In base.njk Template:**
```njk
<style>{{ criticalCSSFile | criticalCSS | safe }}</style>
```

**In page.njk Layout** (25+ pages):
```njk
<style>{{ 'critical-page-layout.css' | criticalCSS | safe }}</style>
```

**Main CSS Deferred Loading:**
```html
<link rel="preload" href="/css/main.min.css?v=20251123" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

---

## ✏️ Standard CSS Update Workflow

**Use this workflow when changing styles that are NOT above-the-fold** (e.g., footer, buttons, FAQ styles, mobile menu).

### Step 1: Edit Main CSS

```bash
# Edit the appropriate CSS file
src/assets/styles/style-core.css    # Core components
src/assets/styles/style.css          # Page-specific styles
src/assets/styles/core-brand.css     # CSS variables, brand colors
```

**Example: Change button hover color**
```css
/* src/assets/styles/style-core.css */
.button:hover {
  background-color: var(--primary-blue-dark);  /* Changed from --primary-blue */
}
```

### Step 2: Build CSS

```bash
npm run build:css
# Output: dist/css/main.min.css updated
```

### Step 3: Test Locally (Optional)

```bash
npm run dev
# Open http://localhost:8080 and verify changes
```

### Step 4: Commit and Deploy

```bash
git add src/assets/styles/style-core.css
git commit -m "Update button hover color"
git push
# Cloudflare auto-deploys in 2-3 minutes
```

---

## 🔥 Critical CSS Update Workflow

**Use this workflow when changing above-the-fold styles** (navbar, hero section, h1 headings, container padding, mobile layout).

### ✅ AUTOMATED (November 24, 2025)

The critical CSS system is now **fully automated**. You only need to update main CSS - critical CSS extracts automatically during build!

### Step 1: Update Main CSS Only

```bash
# Edit the main CSS source (single source of truth)
src/assets/styles/style-core.css
```

**Example: Change mobile h1 font size**
```css
/* src/assets/styles/style-core.css */
@media (max-width: 767px) {
  h1 {
    font-size: 2rem;           /* Changed from 2.5rem */
    line-height: 1.25;
    word-wrap: break-word;
    overflow-wrap: break-word;
  }
}
```

### Step 2: Run Automated Build

```bash
npm run build:cloudflare

# This runs:
# 1. npm run build:css           → Build main CSS
# 2. npm run build:html:prod     → Build HTML to dist/
# 3. npm run build:critical      → Auto-extract critical CSS from dist/
# 4. npm run build:html:prod     → Rebuild HTML with new critical CSS
# 5. npm run build:js            → Bundle JavaScript
```

**OR for local testing:**
```bash
npm run build:css               # 1. Build main CSS
npm run build:html:prod         # 2. Build HTML to dist/
npm run build:critical          # 3. Auto-extract critical CSS
npm run build:html:prod         # 4. Rebuild HTML with new critical CSS
```

### Step 3: Verify Critical CSS Updated

```bash
# Check that critical CSS files were regenerated
ls -lh src/_data/critical-*.css

# Expected output:
# critical-homepage.css         28KB
# critical-attorneys.css        22KB
# critical-practice-areas.css   19KB
# critical-page-layout.css      15KB
```

### Step 4: Commit and Deploy

```bash
git add src/assets/styles/style-core.css src/_data/critical-*.css
git commit -m "Update mobile h1 font size"
git push
```

**Note:** Both main CSS and auto-generated critical CSS files must be committed together!

---

## 🤖 Critical CSS Automation

### How It Works

**Script:** `utilities/extract-critical-css.mjs`
**Package:** `critical` npm package v7.2.1
**Integration:** Runs automatically in `npm run build:cloudflare`

### Extraction Process

1. **Analyzes rendered HTML** in `dist/` folder
2. **Identifies above-the-fold CSS** for 3 viewports:
   - Mobile: 375px × 667px
   - Tablet: 768px × 1024px
   - Desktop: 1920px × 1080px
3. **Extracts minimal CSS** needed for instant render
4. **Writes minified output** to `src/_data/critical-*.css`

### Configuration

**Pages Extracted** (`utilities/extract-critical-css.mjs` lines 26-65):
```javascript
const PAGES = [
  {
    name: 'homepage',
    url: '/index.html',
    output: 'critical-homepage.css',
    dimensions: [
      { width: 375, height: 667 },   // Mobile
      { width: 1920, height: 1080 }  // Desktop
    ]
  },
  {
    name: 'attorneys',
    url: '/attorneys.html',
    output: 'critical-attorneys.css',
    dimensions: [{ width: 375, height: 667 }, { width: 1920, height: 1080 }]
  },
  {
    name: 'practice-areas',
    url: '/practice-areas.html',
    output: 'critical-practice-areas.css',
    dimensions: [{ width: 375, height: 667 }, { width: 1920, height: 1080 }]
  },
  {
    name: 'page-layout',
    url: '/dui-defense.html',              // Representative page using page.njk layout
    output: 'critical-page-layout.css',
    dimensions: [
      { width: 375, height: 667 },         // Mobile
      { width: 768, height: 1024 },        // Tablet
      { width: 1920, height: 1080 }        // Desktop
    ]
  }
];
```

### When Critical CSS is Re-extracted

- ✅ Automatically on every `npm run build:cloudflare` (production deployment)
- ✅ Automatically on every `npm run build` (local development build)
- ✅ Manually via `npm run build:critical` (for testing)

### Benefits of Automation

- ✅ Update 1 file instead of 5 files
- ✅ No risk of forgetting to sync critical CSS files
- ✅ Consistent critical CSS across all pages
- ✅ Eliminates manual editing of minified CSS
- ✅ Prevents incidents like November 24 multi-commit fix

---

## 📱 Mobile Breakpoints & Responsive Design

### Standard Breakpoints

```css
/* Mobile - phones */
@media (max-width: 767px) {
  /* Applies to devices < 768px */
}

/* Extra small mobile - iPhone SE, small phones */
@media (max-width: 374px) {
  /* Applies to devices < 375px */
}

/* Small mobile - older phones */
@media (max-width: 600px) {
  /* Applies to devices < 601px */
}

/* Tablet and Desktop */
@media (min-width: 768px) {
  /* Applies to devices >= 768px */
}

/* Tablet only */
@media (max-width: 991px) {
  /* Applies to devices < 992px */
}

/* Desktop */
@media (min-width: 1024px) {
  /* Applies to devices >= 1024px */
}

/* Large desktop */
@media (min-width: 1600px) {
  /* Applies to devices >= 1600px */
}
```

### ⚠️ CRITICAL: page.njk Mobile Fixes Required

**IMPORTANT:** Not all pages use dedicated critical CSS files!

Pages using `page.njk` layout (attorney profiles, service pages, location pages) get critical CSS from `src/_includes/layouts/page.njk` with **hardcoded inline styles**.

**Required Mobile Styles** (`page.njk` lines 6-10):
```njk
{% block criticalCSS %}
<style>
{{ 'critical-page-layout.css' | criticalCSS | safe }}
</style>
{% endblock %}
```

The `critical-page-layout.css` file is now **auto-extracted** from `dist/dui-defense.html` and includes mobile breakpoint fixes.

**Why This Matters:**
- `page.njk` is extended by 25+ pages
- Without mobile breakpoints → horizontal overflow on mobile
- Main CSS loads deferred → too late to prevent initial overflow
- Critical CSS MUST include mobile fixes for instant proper render

---

### Mobile Typography Rules

**Prevent Text Overflow:**
```css
@media (max-width: 767px) {
  h1 {
    font-size: 2rem;              /* Smaller than desktop (was 2.5rem) */
    line-height: 1.25;
    word-wrap: break-word;         /* Allow words to wrap */
    overflow-wrap: break-word;     /* Modern browser support */
    max-width: 100%;               /* Prevent overflow */
  }
}

@media (max-width: 374px) {
  h1 {
    font-size: 2rem;              /* Same size, tighter line-height */
    line-height: 1.1;
    word-wrap: break-word;
    overflow-wrap: break-word;
  }
}
```

**Container Padding:**
```css
@media (max-width: 767px) {
  .container-large {
    padding-left: 1.25rem;        /* 20px */
    padding-right: 1.25rem;
  }
}

@media (max-width: 374px) {
  .container-large {
    padding-left: 1rem;           /* 16px for small phones */
    padding-right: 1rem;
  }
}
```

---

## 🐛 Troubleshooting CSS Issues

### CSS Not Loading

**Checklist:**
1. ✅ **Check CSS version query string:** `main.min.css?v=20251123`
2. ✅ **Check path in base.njk:** Correct `/css/main.min.css`?
3. ✅ **Check build succeeded:** `npm run build:css` no errors?
4. ✅ **Check file exists:** `dist/css/main.min.css` present after build?
5. ✅ **Check browser console:** F12 → Network tab for 404 errors

**Solution:**
```bash
# Rebuild CSS and verify
npm run build:css
ls -lh dist/css/main.min.css

# If file missing, check PostCSS errors:
npx postcss src/assets/styles/main.css -o dist/css/main.min.css
```

---

### Critical CSS Not Updating

**Symptom:** CSS changes not visible on live site, but main.min.css updated

**Cause:** Critical CSS (loads first) still has old values

**Solution:**
```bash
# Run full build to extract critical CSS
npm run build:cloudflare

# OR manually:
npm run build:css           # Build main CSS
npm run build:html:prod     # Build HTML to dist/
npm run build:critical      # Extract critical CSS
npm run build:html:prod     # Rebuild HTML with new critical CSS
```

**Verify critical CSS updated:**
```bash
ls -lht src/_data/critical-*.css | head -n 4
# Should show recent timestamps (within last few minutes)
```

---

### Mobile Styles Not Working

**Symptom:** Desktop styles look good, but mobile has horizontal scroll or broken layout

**Common Causes:**
1. **Breakpoint not applied:** Check media query syntax (`max-width: 767px`)
2. **Critical CSS missing mobile styles:** Run `npm run build:critical`
3. **Text overflow:** Missing `word-wrap: break-word` on headings
4. **Container padding:** Missing responsive padding on `.container-large`

**Solution:**
```bash
# 1. Update main CSS with mobile breakpoint
Edit: src/assets/styles/style-core.css

# 2. Run full build to extract critical CSS
npm run build:cloudflare

# 3. Test on mobile viewport (Chrome DevTools)
# Press F12 → Toggle device toolbar → iPhone 12 Pro
```

---

### Styles Being Overridden

**Symptom:** Your CSS not applying, other styles taking precedence

**Cause:** CSS specificity conflict

**Debugging:**
```
1. Open browser DevTools (F12)
2. Inspect element
3. Look for crossed-out styles in Styles panel
4. Check what's overriding your styles
```

**Solution - Increase Specificity:**
```css
/* Before (low specificity) */
.button {
  background-color: blue;
}

/* After (higher specificity) */
.button.button {
  background-color: blue;
}

/* OR use more specific selector */
.cta-buttons .button {
  background-color: blue;
}
```

---

## 📁 File Organization

### CSS File Naming Conventions

**Source Files:** `src/assets/styles/`
- `core-brand.css` - CSS variables, resets, brand colors
- `style-core.css` - Core component styles (navbar, footer, buttons, forms)
- `style.css` - Page-specific styles (homepage, attorneys, practice areas)
- `style-blog.css` - Blog page styles
- `style-faq.css` - FAQ page styles
- `style-card-pages.css` - Digital business card styles
- `cookie-consent.css` - Cookie consent banner

**Entry Point:** `main.css` (imports all other CSS)

**Build Output:** `dist/css/main.min.css` (bundled, NOT minified)

**Critical CSS:** `src/_data/critical-*.css` (auto-generated, minified)

---

### When to Edit Which File

**Brand Colors / CSS Variables:**
```bash
src/assets/styles/core-brand.css
# --primary-blue, --primary-blue-dark, --white, --text-color, etc.
```

**Core Components** (navbar, footer, buttons, forms):
```bash
src/assets/styles/style-core.css
```

**Page-Specific Styles:**
```bash
src/assets/styles/style.css
```

**Blog Styles:**
```bash
src/assets/styles/style-blog.css
```

**FAQ Styles:**
```bash
src/assets/styles/style-faq.css
```

**Business Card Styles:**
```bash
src/assets/styles/style-card-pages.css
```

**Cookie Consent:**
```bash
src/assets/styles/cookie-consent.css
```

---

### ⚠️ PostCSS cssnano Temporarily Disabled

**From `postcss.config.js` lines 12-20:**
```javascript
// Minify and optimize CSS - TEMPORARILY DISABLED FOR TESTING
/*
require('cssnano')({
  preset: ['default', { ... }]
})
*/
```

**Impact:**
- CSS is NOT minified by PostCSS
- Output `dist/css/main.min.css` is NOT actually minified (same size as source ~80KB)
- File is still named `.min.css` for backwards compatibility with templates

**To Re-Enable:**
1. Uncomment cssnano plugin in `postcss.config.js`
2. Rebuild CSS: `npm run build:css`
3. Expected file size reduction: ~28% (80KB → 57KB)

**Why Disabled:** Intentionally disabled during testing phase. Re-enable when ready for production optimization.

---

## 📚 Additional Resources

- **Comprehensive Docs:** [AI_CONTEXT.md](../../AI_CONTEXT.md) - Section 4.1 (Dual CSS Architecture)
- **Troubleshooting:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - CSS troubleshooting section
- **Quick Start:** [QUICK_START.md](../../QUICK_START.md) - Essential commands

**Critical CSS Automation Script:**
- Location: `utilities/extract-critical-css.mjs`
- Package: `critical@7.2.1` npm package
- Documentation: https://github.com/addyosmani/critical

---

**Last Updated:** November 24, 2025
**Maintained By:** AI-assisted documentation system
**Questions?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or [AI_CONTEXT.md](../../AI_CONTEXT.md)