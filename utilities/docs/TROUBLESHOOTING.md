# Troubleshooting Guide - Sorin & Pyle Website

**⏱️ 15-minute read** | For full documentation, see [AI_CONTEXT.md](../../AI_CONTEXT.md) Section 10

---

## 📚 Quick Navigation

**Other Guides:**
- [Quick Start](../../QUICK_START.md) - 5-minute onboarding
- [CSS Guide](CSS_GUIDE.md) - CSS workflow and critical CSS
- [Schema Guide](SCHEMA_GUIDE.md) - Schema markup templates
- [Content Guide](CONTENT_GUIDE.md) - Creating new pages

---

## 🚨 Common Issues Index

**Jump to Section:**
1. [Build Errors](#-build-errors)
2. [CSS Not Loading](#-css-not-loading)
3. [Critical CSS Issues](#-critical-css-issues)
4. [Schema Validation Errors](#-schema-validation-errors)
5. [Deployment Issues](#-deployment-issues)
6. [JavaScript Errors](#-javascript-errors)
7. [Git & Version Control](#-git--version-control)
8. [Performance Issues](#-performance-issues)

---

## 🛠️ Build Errors

### **Error 1: "Cannot find module 'eleventy'"**

**Symptom:**
```bash
npm run build:html:prod
Error: Cannot find module '@11ty/eleventy'
```

**Cause:** Node modules not installed

**Fix:**
```bash
npm install
```

**Explanation:** The `node_modules/` folder contains all dependencies. Run `npm install` after cloning the repo or if `node_modules/` is missing.

---

### **Error 2: "Cannot find dist/ directory" (Critical CSS)**

**Symptom:**
```bash
npm run build:critical
❌ dist directory not found. Run "npm run build:html" first.
```

**Cause:** Critical CSS extraction requires built HTML files to analyze

**Fix:**
```bash
# Step 1: Build HTML first
npm run build:html:prod

# Step 2: Extract critical CSS
npm run build:critical

# Step 3: Rebuild HTML with new critical CSS
npm run build:html:prod
```

**Better Fix:** Use automated build command:
```bash
npm run build:cloudflare
```

This runs all steps in correct order: CSS → HTML → Critical → HTML → JS

---

### **Error 3: "Error: Failed to parse source map"**

**Symptom:**
```bash
npm run build:css
Error: Failed to parse source map from 'src/assets/styles/main.css.map'
```

**Cause:** Leftover source map file from previous build

**Fix:**
```bash
# Delete old source maps
rm dist/css/*.map

# Rebuild CSS
npm run build:css
```

**Prevention:** Source maps are disabled in production (`sourceMap: false` in postcss.config.cjs)

---

### **Error 4: "Path must be a string" (Eleventy)**

**Symptom:**
```bash
npm run build:html:prod
Error: Path must be a string. Received undefined
```

**Cause:** Missing or incorrect permalink in front matter

**Fix:** Check `.njk` file front matter:

```yaml
---
layout: layouts/page.njk
title: "Page Title"
description: "Meta description"
permalink: "/page-name.html"  # ← Make sure this exists!
---
```

**Common Mistakes:**
- ❌ Missing `permalink` field entirely
- ❌ Typo: `permanlink` or `perma-link`
- ❌ Missing leading slash: `page-name.html` (should be `/page-name.html`)

---

### **Error 5: "Template render error" (Nunjucks)**

**Symptom:**
```bash
npm run build:html:prod
Template render error: (src/pages/example.njk)
  Error: expected variable end
```

**Cause:** Syntax error in Nunjucks template

**Common Causes:**
1. **Unclosed tag:**
   ```njk
   {% if condition %}  {# Missing {% endif %} #}
   ```

2. **Unescaped curly braces:**
   ```njk
   <script>
     const obj = { foo: "bar" };  {# Nunjucks tries to parse this! #}
   </script>
   ```

3. **Missing closing tag:**
   ```njk
   {{ site.title  {# Missing closing }} #}
   ```

**Fix:** Escape literal curly braces in JavaScript:
```njk
<script>
  const obj = {{ '{' }} foo: "bar" {{ '}' }};
</script>
```

Or use `{% raw %}` blocks:
```njk
<script>
{% raw %}
  const obj = { foo: "bar" };
{% endraw %}
</script>
```

---

## 🎨 CSS Not Loading

### **Issue 1: Styles Not Appearing on Page**

**Symptom:** Page displays with no styling, broken layout

**Diagnosis Checklist:**

1. **Check browser console for 404 errors:**
   - Open DevTools (F12)
   - Check Network tab for failed CSS requests
   - Look for red 404 status codes

2. **Verify CSS file exists:**
   ```bash
   ls dist/css/main.min.css
   # Should show file, not "No such file or directory"
   ```

3. **Check HTML `<link>` tag path:**
   ```html
   <!-- Root files (index.html, etc.) -->
   <link rel="stylesheet" href="css/main.min.css">

   <!-- Location subfolder files (locations/*.html) -->
   <link rel="stylesheet" href="../css/main.min.css">
   ```

**Fix:**
```bash
# Rebuild CSS
npm run build:css

# Rebuild HTML
npm run build:html:prod

# Verify file exists
ls dist/css/main.min.css
```

---

### **Issue 2: CSS Changes Not Showing Up**

**Symptom:** Updated `src/assets/styles/style-core.css` but changes don't appear on site

**Possible Causes:**

**Cause 1: Forgot to rebuild CSS**
```bash
# Fix: Rebuild CSS
npm run build:css
```

**Cause 2: Edited dist/css/main.min.css directly (WRONG)**
```bash
# Never edit dist/ files directly!
# Edit src/assets/styles/*.css instead

# Then rebuild:
npm run build:css
```

**Cause 3: Browser cache**
```bash
# Hard refresh browser:
# Windows/Linux: Ctrl + Shift + R
# Mac: Cmd + Shift + R
```

**Cause 4: Critical CSS not updated** (for above-the-fold styles)
```bash
# For changes to critical CSS areas (mobile nav, hero section):
npm run build:cloudflare
# This extracts new critical CSS and rebuilds
```

---

### **Issue 3: Mobile Breakpoint Not Working**

**Symptom:** Mobile styles (max-width: 767px) not applying on mobile devices

**Diagnosis:**
```css
/* Check for typos in media query */
@media (max-width: 767px) {  /* ✅ Correct */
@media (max-width 767px) {   /* ❌ Missing colon */
@media max-width: 767px {    /* ❌ Missing parentheses */
```

**Common Mistakes:**
- Missing colon after `max-width`
- Missing parentheses around condition
- Wrong breakpoint (767px vs 768px - site uses 767px)
- Media query not closed (missing `}`)

**Fix:** Verify syntax in `src/assets/styles/style-core.css` and rebuild:
```bash
npm run build:css
```

---

## 🔥 Critical CSS Issues

### **Issue 1: Above-the-Fold Content Not Styled**

**Symptom:** Page loads with unstyled content briefly, then styles load (FOUC - Flash of Unstyled Content)

**Cause:** Critical CSS not inlined in `<head>` or out of date

**Fix:**
```bash
# Extract new critical CSS
npm run build:cloudflare
```

**Verification:**
```bash
# Check that critical CSS was updated
git status
# Should show: modified: src/_data/critical-*.css

# Commit if correct
git add src/_data/critical-*.css
git commit -m "Update critical CSS"
```

---

### **Issue 2: Critical CSS Extraction Timeout**

**Symptom:**
```bash
npm run build:critical
❌ Error extracting critical CSS for homepage: timeout
```

**Cause:** Page too complex or external resources slow

**Fix:** Increase timeout in `utilities/extract-critical-css.mjs`:

```javascript
// Line 85-87
penthouse: {
  timeout: 60000,      // ← Increase to 120000 (2 minutes)
  renderWaitTime: 1000
}
```

---

### **Issue 3: Wrong Critical CSS Applied**

**Symptom:** Homepage has attorneys page critical CSS (or vice versa)

**Cause:** Incorrect critical CSS file referenced in template

**Check Layout File:**

**For homepage (index.njk):**
```njk
{% block criticalCSS %}
<style>
{{ 'critical-homepage.css' | criticalCSS | safe }}  {# ✅ Correct #}
</style>
{% endblock %}
```

**For service pages (dui-defense.njk, etc.):**
```njk
{% extends "layouts/page.njk" %}  {# Uses critical-page-layout.css #}
```

**Fix:** Verify each page extends correct layout or references correct critical CSS file.

---

## ✅ Schema Validation Errors

### **Error 1: "Missing field 'address'" (CRITICAL)**

**Symptom:** Google Rich Results Test shows "Missing field 'address'" error

**Cause:** LegalService schema missing required address field

**Fix:** Add complete address object to LegalService schema:

```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "217 E 24th St Ste 107",
    "addressLocality": "Holland",
    "addressRegion": "MI",
    "postalCode": "49423",
    "addressCountry": "US"
  },
  "telephone": "+16162273303",
  "image": "https://www.sorinpyle.com/images/ottawa-county-courthouse.avif"
}
```

**Note:** All three fields (address, telephone, image) are REQUIRED by Google.

---

### **Error 2: "The property X is not recognized by Google"**

**Symptom:** Google Rich Results Test shows warning "The property serviceType is not recognized by Google for an object of type LegalService"

**Severity:** WARNING (not an error)

**Action:** Safe to ignore. This means Google doesn't use that property for rich results, but it's still valid schema.org markup and may be used by other search engines or AI systems.

---

### **Error 3: "Unnamed item"**

**Symptom:** Google Rich Results Test shows "Unnamed item" error

**Cause:** Provider reference includes duplicate `@type`

**Wrong:**
```json
"provider": {
  "@type": "LegalService",  {# ❌ Remove this #}
  "@id": "https://www.sorinpyle.com/#legalservice"
}
```

**Correct:**
```json
"provider": {
  "@id": "https://www.sorinpyle.com/#legalservice"
}
```

**Fix:** Remove `@type` field from provider reference - just use `@id`.

---

### **Error 4: "aggregateRating with reviewCount: 0"**

**Symptom:** Google Rich Results Test shows error "reviewCount must be a positive integer"

**Cause:** AggregateRating included with zero reviews

**Fix:** Remove entire `aggregateRating` block:

```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  // Remove this entire block:
  // "aggregateRating": {
  //   "@type": "AggregateRating",
  //   "ratingValue": "5",
  //   "reviewCount": 0  ← Invalid!
  // }
}
```

**Important:** You can only include `aggregateRating` if you have **visible reviews on your own pages**. Embedded Google Maps reviews don't count.

---

### **Error 5: Invalid JSON Syntax**

**Symptom:**
```bash
Google Rich Results Test: Error parsing structured data
SyntaxError: Unexpected token } in JSON
```

**Common Causes:**
1. **Trailing comma:**
   ```json
   {
     "name": "Sorin & Pyle",
     "telephone": "+16162273303",  {# ← Remove trailing comma #}
   }
   ```

2. **Unescaped quotes:**
   ```json
   {
     "description": "We're the best"  {# ❌ Apostrophe breaks JSON #}
   }
   ```

3. **Missing comma:**
   ```json
   {
     "name": "Sorin & Pyle"
     "telephone": "+16162273303"  {# ❌ Missing comma above #}
   }
   ```

**Fix:** Use JSON validator: https://jsonlint.com/

**Prevention:** Use proper escaping:
```json
{
  "description": "We're the best"  // ✅ Single quotes inside double quotes OK
  "description": "She said \"hello\""  // ✅ Escaped double quotes
}
```

---

## 🚀 Deployment Issues

### **Issue 1: Changes Not Appearing on Live Site**

**Symptom:** Pushed to GitHub but changes not live on www.sorinpyle.com

**Diagnosis Steps:**

1. **Check if push succeeded:**
   ```bash
   git log --oneline -1
   # Should show your latest commit

   git push
   # Should say "Everything up-to-date"
   ```

2. **Check Cloudflare Pages deployment:**
   - Go to Cloudflare Pages dashboard
   - Check recent deployments
   - Look for failed builds (red X)

3. **Wait for deployment:**
   - Cloudflare build time: 2-3 minutes
   - CDN cache propagation: 1-2 minutes
   - Total: 3-5 minutes after push

**Fix:** If deployment failed, check Cloudflare build logs for errors.

---

### **Issue 2: "Build failed" on Cloudflare Pages**

**Symptom:** Cloudflare Pages shows "Build failed" in deployment log

**Common Causes:**

**Cause 1: Build command failed**
```bash
# Check if build works locally:
npm run build:cloudflare

# If it fails, fix the error before pushing
```

**Cause 2: Missing dependencies in package.json**
```bash
# Cloudflare runs: npm install
# Make sure all dependencies are in package.json

# Check:
cat package.json | grep "dependencies"
```

**Cause 3: Node version mismatch**
```bash
# Cloudflare Pages uses Node 20.x by default
# Check .nvmrc or package.json "engines" field

# Add to package.json if needed:
"engines": {
  "node": ">=20.0.0"
}
```

---

### **Issue 3: 404 Error on Location Pages**

**Symptom:** www.sorinpyle.com/locations/holland-mi.html shows 404 Not Found

**Cause 1: File not committed to git**
```bash
# Check git status
git status

# If file shows as "Untracked":
git add src/pages/locations/holland-mi.njk
git commit -m "Add Holland MI location page"
git push
```

**Cause 2: File not built**
```bash
# Verify file exists in dist/:
ls dist/locations/holland-mi.html

# If missing, rebuild:
npm run build:html:prod
```

**Cause 3: Cloudflare Pages build didn't include file**
- Check Cloudflare Pages deployment logs
- Verify "Build output directory: dist"
- Ensure file is in dist/ after build

---

## 💻 JavaScript Errors

### **Error 1: "gtag is not defined"**

**Symptom:** Browser console shows `ReferenceError: gtag is not defined`

**Cause:** Google Analytics script not loaded before inline tracking code

**Fix:** Ensure Google Tag Manager script loads first:

```html
<!-- Load GTM first -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LV7PKRF2YT"></script>

<!-- Then load analytics.js (defines gtag function) -->
<script src="js/analytics.js"></script>

<!-- Then inline tracking -->
<script>
  // Now gtag() is available
  gtag('event', 'page_view');
</script>
```

---

### **Error 2: "Cannot read property 'addEventListener' of null"**

**Symptom:** JavaScript error when trying to attach event listener

**Cause:** Element doesn't exist on page (wrong ID or class name)

**Fix:**
```javascript
// ❌ Wrong - errors if element missing
document.getElementById('myButton').addEventListener('click', handler);

// ✅ Correct - check if element exists first
const button = document.getElementById('myButton');
if (button) {
  button.addEventListener('click', handler);
}
```

---

### **Error 3: "Unexpected token" (JavaScript)**

**Symptom:** Browser console shows `SyntaxError: Unexpected token`

**Common Causes:**
1. Nunjucks trying to parse JavaScript curly braces
2. Missing semicolon
3. Incorrect arrow function syntax

**Fix:** Use `{% raw %}` blocks for JavaScript:
```njk
<script>
{% raw %}
  const data = { foo: 'bar' };
  const items = arr.map(item => item.value);
{% endraw %}
</script>
```

---

## 📦 Git & Version Control

### **Issue 1: Accidentally Committed dist/ Files**

**Symptom:** `git status` shows hundreds of `dist/` files

**Cause:** Forgot `.gitignore` or it's not working

**Fix:**
```bash
# Remove dist/ from git tracking
git rm -r --cached dist/

# Verify .gitignore includes dist/
echo "dist/" >> .gitignore

# Commit
git add .gitignore
git commit -m "Remove dist/ from git tracking"
git push
```

**Prevention:** Always check `git status` before committing.

---

### **Issue 2: Merge Conflict in dist/ Files**

**Symptom:** Git shows merge conflicts in `dist/*.html` files

**Cause:** Multiple people built HTML locally (dist/ should never be committed)

**Fix:**
```bash
# Accept their version (doesn't matter - we'll rebuild)
git checkout --theirs dist/

# Remove dist/ from git (should be in .gitignore)
git rm -r --cached dist/

# Rebuild locally
npm run build:cloudflare

# Commit .gitignore update
git add .gitignore
git commit -m "Fix: Remove dist/ from version control"
git push
```

---

### **Issue 3: "Your branch is ahead of 'origin/main' by X commits"**

**Symptom:** `git status` shows you have unpushed commits

**Fix:**
```bash
# Push commits to GitHub
git push

# If push rejected (someone else pushed first):
git pull --rebase
git push
```

---

## ⚡ Performance Issues

### **Issue 1: Page Load Time > 3 Seconds**

**Diagnosis:**
- Open Chrome DevTools
- Go to Network tab
- Reload page
- Check waterfall for slow resources

**Common Culprits:**
1. **Large images:**
   - Optimize with TinyPNG API
   - Use AVIF format
   - Target: < 50KB for thumbnails, < 150KB for full images

2. **Too many HTTP requests:**
   - Combine CSS files (we use main.css with @import)
   - Combine JS files (we use esbuild bundling)
   - Use CSS sprites for icons

3. **Unoptimized JavaScript:**
   - Defer non-critical JS
   - Use `async` or `defer` attributes on `<script>` tags
   - Minimize third-party scripts

**Fix:**
```bash
# Optimize images
python utilities/optimize_images_tinify.py

# Rebuild and check size
npm run build:cloudflare
ls -lh dist/images/*.avif
```

---

### **Issue 2: Large CSS File (> 100KB)**

**Symptom:** `main.min.css` is larger than expected

**Diagnosis:**
```bash
# Check CSS file size
ls -lh dist/css/main.min.css
# Should be ~57KB (after October 2025 minification fix)
```

**Fix (if minification disabled):**

Check `postcss.config.cjs`:
```javascript
cssnano({
  preset: ['default', {
    discardComments: { removeAll: true },
    normalizeWhitespace: true,
    colormin: true,
    minifySelectors: true
  }]
})
```

**Known Issue:** cssnano is intentionally disabled (October 2025) - site uses 80KB unminified CSS. Re-enable when testing complete.

---

### **Issue 3: Mobile Navigation Lag**

**Symptom:** Mobile menu animation stutters or lags

**Cause:** Too many DOM manipulations or heavy CSS animations

**Fix:**

1. **Use CSS transforms (GPU-accelerated):**
   ```css
   /* ✅ Good - uses GPU */
   .mobile-nav_menu {
     transform: translateY(-100%);
     transition: transform 0.3s ease;
   }

   /* ❌ Bad - repaints layout */
   .mobile-nav_menu {
     top: -100%;
     transition: top 0.3s ease;
   }
   ```

2. **Use will-change for animations:**
   ```css
   .mobile-nav_menu {
     will-change: transform;
   }
   ```

3. **Reduce JavaScript work:**
   ```javascript
   // Throttle scroll events
   let scrollTimeout;
   window.addEventListener('scroll', () => {
     if (scrollTimeout) clearTimeout(scrollTimeout);
     scrollTimeout = setTimeout(handleScroll, 100);
   });
   ```

---

## 🆘 Emergency Fixes

### **Site Down / White Screen**

**Diagnosis Steps:**
1. Check browser console for errors (F12)
2. Check if CSS loaded (Network tab)
3. Check if JavaScript errors present (Console tab)
4. Check Cloudflare Pages deployment status

**Quick Fix:**
```bash
# Revert to last working commit
git log --oneline -5
# Find last working commit hash

git revert <commit-hash>
git push
# Cloudflare will rebuild from working version
```

---

### **Google Rich Results Errors After Schema Update**

**Quick Fix:**
```bash
# Test schema locally first
npm run build:html:prod

# Open dist/[page].html
# Copy schema block
# Paste into: https://search.google.com/test/rich-results
# Fix errors BEFORE pushing
```

---

### **CSS Completely Broken After Update**

**Quick Fix:**
```bash
# Rebuild from source
npm run build:css
npm run build:html:prod

# If still broken, revert changes
git checkout src/assets/styles/style-core.css
npm run build:cloudflare
```

---

## 📞 Getting Help

### **Before Asking for Help:**
1. ✅ Check this troubleshooting guide
2. ✅ Check browser console for errors
3. ✅ Try rebuilding: `npm run build:cloudflare`
4. ✅ Check git status: `git status`
5. ✅ Try hard refresh: Ctrl+Shift+R (Windows) / Cmd+Shift+R (Mac)

### **When Asking for Help:**
Include these details:
1. Error message (exact text)
2. Steps to reproduce
3. What you've tried
4. Browser/OS version
5. Recent changes made

### **Documentation Resources:**
- [AI_CONTEXT.md](../../AI_CONTEXT.md) - Comprehensive documentation
- [QUICK_START.md](../../QUICK_START.md) - Quick reference
- [CSS_GUIDE.md](CSS_GUIDE.md) - CSS workflows
- [SCHEMA_GUIDE.md](SCHEMA_GUIDE.md) - Schema templates
- [CONTENT_GUIDE.md](CONTENT_GUIDE.md) - Creating pages
- [CLAUDE.md](../../CLAUDE.md) - Project history and recent changes

---

**Still stuck?** Check [AI_CONTEXT.md](../../AI_CONTEXT.md) Section 10 (Common Issues) for additional troubleshooting guidance.
