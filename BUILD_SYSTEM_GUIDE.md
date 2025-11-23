# Build System Guide

## Overview

This project uses **Eleventy** (11ty) static site generator with modern build tooling for optimal performance and developer experience.

### Technology Stack

| Tool | Purpose | Version |
|------|---------|---------|
| **Eleventy** | Static site generator | 3.1.2 |
| **Nunjucks** | Template engine | (via Eleventy) |
| **PostCSS** | CSS processing | 8.5.6 |
| **esbuild** | JavaScript bundling | 0.27.0 |
| **Sharp** | Image processing | 0.34.5 |
| **Critical** | Critical CSS extraction | 7.2.1 |
| **html-minifier-terser** | HTML minification | 7.2.0 |

---

## Directory Structure

```
sorin-pyle-site-html/
├── src/                          # Source files
│   ├── _data/                    # Data files (JSON, JS)
│   │   ├── images.json          # Responsive image manifest
│   │   ├── critical-homepage.css
│   │   ├── critical-attorneys.css
│   │   └── critical-practice-areas.css
│   ├── _includes/               # Reusable templates
│   │   ├── layouts/             # Layout templates
│   │   │   ├── base.njk        # Base layout (HTML structure)
│   │   │   └── page.njk        # Page layout (extends base)
│   │   └── partials/            # Partial templates
│   │       ├── header.njk       # Site header
│   │       ├── footer.njk       # Site footer
│   │       └── nav.njk          # Navigation menus
│   ├── assets/                  # Source assets
│   │   ├── styles/              # CSS source files
│   │   │   ├── main.css        # Main CSS entry point
│   │   │   ├── variables.css   # CSS custom properties
│   │   │   ├── typography.css  # Font styles
│   │   │   └── components/     # Component styles
│   │   └── scripts/             # JavaScript source files
│   │       ├── main.js          # Main JS entry point
│   │       ├── cookie-consent.js
│   │       ├── tracking.js
│   │       └── ...
│   ├── pages/                   # Page content
│   │   ├── index.njk            # Homepage
│   │   ├── attorneys.njk
│   │   ├── practice-areas.njk
│   │   └── ...
│   └── static/                  # Static assets (copied as-is)
│       └── ...
├── dist/                         # Build output (generated)
│   ├── index.html
│   ├── css/
│   │   └── main.min.css
│   ├── js/
│   │   ├── main.min.js
│   │   └── ...
│   └── images/
│       └── ... (responsive variants)
├── images/                       # Source images
│   └── ... (original images)
├── fonts/                        # Web fonts
│   └── ...
├── .eleventy.js                 # Eleventy configuration
├── postcss.config.js            # PostCSS configuration
├── esbuild.config.js            # esbuild configuration
├── process-images.mjs           # Image processing script
├── extract-critical-css.mjs     # Critical CSS extraction
└── package.json                 # npm dependencies & scripts
```

---

## Build Pipeline

### Build Flow

```
┌─────────────────────────────────────────────────────────┐
│ 1. Clean (Remove dist/)                                 │
└─────────────┬───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│ 2. Process Images (Sharp)                               │
│    • Generate WebP, AVIF variants                       │
│    • Create responsive sizes (320w-1920w)               │
│    • Generate images.json manifest                      │
└─────────────┬───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│ 3. Build HTML (Eleventy - First Pass)                   │
│    • Render Nunjucks templates                          │
│    • Generate 53 HTML pages                             │
│    • Copy static assets                                 │
└─────────────┬───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│ 4. Build CSS (PostCSS)                                  │
│    • Bundle @import statements                          │
│    • Add vendor prefixes (Autoprefixer)                 │
│    • Minify with cssnano (63% reduction)                │
└─────────────┬───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│ 5. Extract Critical CSS                                 │
│    • Analyze homepage, attorneys, practice-areas        │
│    • Extract above-the-fold CSS                         │
│    • Save to src/_data/critical-*.css                   │
└─────────────┬───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│ 6. Rebuild HTML (Eleventy - Second Pass)                │
│    • Inline critical CSS in <head>                      │
│    • Defer full CSS loading                             │
│    • HTML minification (production only)                │
└─────────────┬───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│ 7. Build JavaScript (esbuild)                           │
│    • Bundle modules                                     │
│    • Minify and tree-shake                              │
│    • Generate source maps                               │
└─────────────┴───────────────────────────────────────────┘
```

---

## Build Scripts

### Available Commands

```bash
# Development
npm start              # Start dev server with watch mode
npm run dev            # Same as start
npm run dev:watch      # Dev server + JS watch mode

# Building
npm run build          # Development build (no minification)
npm run build:prod     # Production build (full optimization)

# Individual Build Steps
npm run clean          # Remove dist/ directory
npm run build:images   # Process responsive images
npm run build:css      # Bundle and minify CSS
npm run build:js       # Bundle and minify JavaScript
npm run build:html     # Build HTML pages
npm run build:critical # Extract critical CSS
```

### Build Script Details

**Development Build (`npm run build`):**
```bash
npm run build:html &&         # Build HTML
npm run build:css &&          # Bundle CSS
npm run build:critical &&     # Extract critical CSS
npm run build:html &&         # Rebuild with critical CSS
npm run build:js              # Bundle JavaScript
```
- No HTML minification
- Faster build time (~30 seconds)
- Full source maps
- Easier debugging

**Production Build (`npm run build:prod`):**
```bash
npm run clean &&              # Clean dist/
npm run build:images &&       # Process images
npm run build:html:prod &&    # Build HTML (minified)
npm run build:css &&          # Bundle CSS
npm run build:critical &&     # Extract critical CSS
npm run build:html:prod &&    # Rebuild (minified)
npm run build:js              # Bundle JavaScript
```
- HTML minification enabled
- Complete optimization pipeline
- ~45 seconds total
- Production-ready output

---

## Configuration Files

### .eleventy.js

Eleventy configuration file controls template processing.

**Key Configuration:**

```javascript
// Pass-through copies
eleventyConfig.addPassthroughCopy("src/static");
eleventyConfig.addPassthroughCopy({"images": "images"});
eleventyConfig.addPassthroughCopy({"fonts": "fonts"});

// Custom filters
eleventyConfig.addFilter("date", ...);           // Date formatting
eleventyConfig.addFilter("replace", ...);        // String replacement
eleventyConfig.addFilter("criticalCSS", ...);    // Inline critical CSS

// Custom shortcodes
eleventyConfig.addShortcode("responsiveImage", ...);  // Responsive images

// HTML minification (production only)
if (process.env.NODE_ENV === 'production') {
  eleventyConfig.addTransform("htmlmin", ...);
}

// Directory structure
dir: {
  input: "src",
  output: "dist",
  includes: "_includes",
  data: "_data"
}
```

**Customization Points:**
- Add new filters for template logic
- Add new shortcodes for reusable components
- Modify pass-through copies for new asset types
- Adjust build performance settings

### postcss.config.js

PostCSS configuration for CSS processing.

**Plugins (in order):**

1. **postcss-import** - Bundle @import statements
2. **autoprefixer** - Add vendor prefixes
3. **cssnano** - Minify CSS

**Browser Support:**
```javascript
overrideBrowserslist: [
  '>= 0.5%',            // Browsers with >0.5% usage
  'last 2 major versions',
  'not dead',
  'Chrome >= 60',
  'Firefox >= 60',
  'Edge >= 79',
  'Safari >= 12',
  'iOS >= 12'
]
```

**Optimization Settings:**
- Remove comments
- Normalize whitespace
- Minify font values and gradients
- Merge longhand properties
- Color optimization

### esbuild.config.js

esbuild configuration for JavaScript bundling.

**Entry Points:**
- `main.min.js` - Main site JavaScript
- `cookie-consent.js` - GDPR/CCPA banner
- `tracking.js` - Analytics event tracking
- `business-card.js` - Digital business cards
- `qr-campaign.js` - QR code landing pages

**Build Settings:**
```javascript
{
  bundle: true,              // Bundle all dependencies
  minify: true,              // Minify output
  sourcemap: true,           // Generate source maps
  target: 'es2020',          // Target modern browsers
  format: 'iife',            // Browser-compatible format
  treeShaking: true,         // Remove unused code
  platform: 'browser'        // Browser environment
}
```

**Output:**
- Total size: ~10KB (all 5 bundles)
- Build time: ~11ms
- Source maps for debugging

### process-images.mjs

Sharp-based image processing configuration.

**Responsive Widths:**
```javascript
widths: [320, 640, 768, 1024, 1280, 1920]
```

**Output Formats:**
- **AVIF** - Most efficient (~50% smaller than JPEG)
- **WebP** - Widely supported (~30% smaller than JPEG)
- **Original** - JPEG/PNG fallback for older browsers

**Quality Settings:**
```javascript
quality: {
  jpeg: 85,   // Good quality, reasonable file size
  webp: 85,   // Same quality as JPEG
  avif: 80,   // Slightly lower (AVIF more efficient)
  png: 90     // Higher quality for graphics
}
```

**Skip Logic:**
- SVG files (copied as-is)
- Already-optimized files (ending in `-NNNw.ext`)
- Special files (logo, favicon)

### extract-critical-css.mjs

Critical CSS extraction using the `critical` package.

**Pages Processed:**
1. Homepage (`/index.html`)
2. Attorneys (`/attorneys.html`)
3. Practice Areas (`/practice-areas.html`)

**Viewport Sizes:**
- Mobile: 375×667
- Tablet: 768×1024
- Desktop: 1920×1080

**Process:**
1. Analyze HTML at all 3 viewport sizes
2. Extract CSS needed for above-the-fold content
3. Minify extracted CSS
4. Save to `src/_data/critical-*.css`
5. Inline in HTML on second build pass

**Results:**
- Homepage: 14.06 KB
- Attorneys: 11.21 KB
- Practice Areas: 10.23 KB

---

## Template System

### Nunjucks Template Engine

**Why Nunjucks:**
- Powerful template inheritance
- Filters and functions
- Conditional logic
- Loops and iterations
- Similar to Jinja2 (Python) and Liquid

### Template Structure

**Base Template** (`src/_includes/layouts/base.njk`):
```nunjucks
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ title }}</title>

  {# Critical CSS - Inlined #}
  {% if criticalCSSFile %}
  <style>
    {{ criticalCSSFile | criticalCSS | safe }}
  </style>
  {% endif %}

  {# Full CSS - Deferred #}
  <link rel="preload" href="/css/main.min.css" as="style">
  <noscript><link rel="stylesheet" href="/css/main.min.css"></noscript>

  {% block head %}{% endblock %}
</head>
<body>
  {% include "partials/header.njk" %}

  <main id="main-content">
    {% block content %}{% endblock %}
  </main>

  {% include "partials/footer.njk" %}

  <script src="/js/main.min.js"></script>
  {% block scripts %}{% endblock %}
</body>
</html>
```

**Page Template** (`src/_includes/layouts/page.njk`):
```nunjucks
---
layout: layouts/base.njk
---

{% block content %}
  {{ content | safe }}
{% endblock %}
```

**Page Content** (`src/pages/index.njk`):
```nunjucks
---
layout: layouts/page.njk
title: "West Michigan Criminal Defense Lawyer"
description: "..."
permalink: /index.html
criticalCSSFile: critical-homepage.css
---

<section class="section_home-hero">
  <div class="container-large">
    <div class="grid_2-col">
      <div>
        <h1>West Michigan Criminal Defense Attorneys</h1>
        <p>We give a damn about your case.</p>
      </div>
      <div>
        {% responsiveImage "/images/holland-michigan-criminal-defense-lawyers.avif",
                          "Criminal defense attorneys in Holland, Michigan",
                          "(min-width: 768px) 50vw, 100vw",
                          "eager" %}
      </div>
    </div>
  </div>
</section>
```

### Custom Filters

**Date Filter:**
```nunjucks
{{ "now" | date("Y") }}
<!-- Outputs: 2025 -->
```

**Critical CSS Filter:**
```nunjucks
{{ "critical-homepage.css" | criticalCSS | safe }}
<!-- Outputs: Inlined CSS content -->
```

**Replace Filter:**
```nunjucks
{{ imagePath | replace("\\.avif$", "-320w.avif") }}
<!-- Outputs: Modified image path -->
```

### Custom Shortcodes

**Responsive Image Shortcode:**
```nunjucks
{% responsiveImage "/images/attorney.avif",
                   "Attorney photo",
                   "(min-width: 768px) 400px, 100vw",
                   "lazy" %}
```

Outputs:
```html
<picture>
  <source type="image/avif"
          srcset="/images/attorney-320w.avif 320w,
                  /images/attorney-640w.avif 640w, ..."
          sizes="(min-width: 768px) 400px, 100vw">
  <source type="image/webp" srcset="...">
  <img src="/images/attorney-640w.jpg"
       alt="Attorney photo"
       srcset="..."
       sizes="..."
       loading="lazy">
</picture>
```

---

## Performance Optimizations

### Critical CSS Strategy

**Problem:** Full CSS blocks rendering until downloaded

**Solution:** Inline critical CSS, defer full CSS

**Implementation:**
1. Extract above-the-fold CSS (Critical package)
2. Inline in `<head>` via Nunjucks filter
3. Load full CSS with `rel="preload"` + JavaScript

**Impact:**
- Faster First Contentful Paint (FCP)
- Improved Largest Contentful Paint (LCP)
- Better Lighthouse performance score

### Responsive Images

**Problem:** Large images slow page load on mobile

**Solution:** Generate multiple sizes and formats

**Implementation:**
- Sharp processes images at 6 widths
- Browser selects appropriate size via `srcset`
- Modern browsers use AVIF, fallback to WebP/JPEG

**File Size Savings:**
- AVIF: ~50-70% smaller than JPEG
- WebP: ~30-40% smaller than JPEG
- Mobile downloads only needed size

### HTML Minification

**Problem:** HTML comments and whitespace increase file size

**Solution:** Strip unnecessary characters (production only)

**Settings:**
```javascript
{
  useShortDoctype: true,        // <!DOCTYPE html>
  removeComments: true,          // Remove HTML comments
  collapseWhitespace: true,      // Remove extra spaces
  minifyCSS: true,               // Minify inline CSS
  minifyJS: true,                // Minify inline JS
  conservativeCollapse: true     // Keep some whitespace for readability
}
```

**Impact:**
- ~10-15% HTML file size reduction
- Faster page downloads
- No visual or functional impact

### JavaScript Tree Shaking

**Problem:** Unused code increases bundle size

**Solution:** esbuild removes unreferenced code

**Example:**
```javascript
// util.js
export function usedFunction() { ... }
export function unusedFunction() { ... }

// main.js
import { usedFunction } from './util.js';

// Output: Only usedFunction included in bundle
```

**Impact:**
- Smaller JavaScript bundles
- Faster script execution
- Better caching efficiency

---

## Development Workflow

### Local Development

```bash
# 1. Install dependencies
npm install

# 2. Start development server
npm start

# Server runs at http://localhost:8080
# Live reload enabled for HTML, CSS, JS changes
```

**Hot Reload:**
- HTML: Automatic rebuild and refresh
- CSS: Reload stylesheet without page refresh
- JavaScript: Requires manual refresh (esbuild watch mode)

### Making Changes

**HTML/Templates:**
1. Edit files in `src/pages/` or `src/_includes/`
2. Eleventy automatically rebuilds
3. Browser refreshes automatically

**CSS:**
1. Edit files in `src/assets/styles/`
2. PostCSS automatically rebuilds
3. Run `npm run build:critical` if above-the-fold styles changed
4. Run `npm run build:html` to regenerate pages

**JavaScript:**
1. Edit files in `src/assets/scripts/`
2. Run `npm run build:js` (or use `npm run dev:watch`)
3. Refresh browser to see changes

**Images:**
1. Add images to `images/` directory
2. Run `npm run build:images` to generate responsive variants
3. Use `responsiveImage` shortcode in templates

### Adding New Pages

1. Create new Nunjucks file in `src/pages/`:
   ```nunjucks
   ---
   layout: layouts/page.njk
   title: "Page Title"
   description: "Meta description"
   permalink: /new-page.html
   ---

   <h1>Page Content</h1>
   ```

2. Eleventy automatically:
   - Renders template
   - Creates `/dist/new-page.html`
   - Includes in build output

3. Add to navigation if needed:
   - Edit `src/_includes/partials/nav.njk`
   - Add new `<li><a href="/new-page.html">Link Text</a></li>`

---

## Troubleshooting

### Build Fails

**Error:** `Cannot find module 'postcss'`

**Solution:**
```bash
rm -rf node_modules package-lock.json
npm install
```

**Error:** `Eleventy build failed`

**Check:**
1. Nunjucks syntax errors in templates
2. Missing frontmatter in page files
3. Invalid filter or shortcode usage
4. Check console for detailed error message

### Images Not Generating

**Error:** Sharp fails to process images

**Solutions:**
1. Verify Sharp installed correctly: `npm install sharp --force`
2. Check image file permissions
3. Ensure images/ directory exists
4. Check process-images.mjs for error messages

### Critical CSS Not Inlining

**Problem:** Critical CSS not appearing in HTML

**Solutions:**
1. Verify `criticalCSSFile` set in page frontmatter
2. Check critical-*.css files exist in `src/_data/`
3. Run `npm run build:critical` before final HTML build
4. Confirm criticalCSS filter defined in .eleventy.js

### Development Server Not Updating

**Problem:** Changes not reflected in browser

**Solutions:**
1. Hard refresh browser (Ctrl+F5 / Cmd+Shift+R)
2. Clear browser cache
3. Restart development server
4. Check Eleventy console for build errors
5. Verify file saved (check file modification time)

---

## Maintenance

### Updating Dependencies

```bash
# Check for outdated packages
npm outdated

# Update all dependencies to latest compatible versions
npm update

# Update specific package
npm install package-name@latest --save-dev

# Test after updates
npm run build:prod
```

**Critical packages to monitor:**
- @11ty/eleventy (breaking changes in major versions)
- postcss, postcss-cli (breaking changes possible)
- sharp (native module, platform-specific)

### Adding New Dependencies

```bash
# Production dependency
npm install package-name

# Development dependency (build tools)
npm install --save-dev package-name
```

Update build scripts if needed (package.json, configs).

---

**Last Updated:** November 22, 2025
**Build System Version:** 1.0
**Eleventy Version:** 3.1.2
