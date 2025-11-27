# Build Process Documentation

**Sorin & Pyle Website - Eleventy Build System**

---

## Overview

The site uses a multi-stage build process with Eleventy (11ty) static site generator, PostCSS for CSS processing, and esbuild for JavaScript bundling.

**Key Principle:** Always edit `src/` files, never `dist/` files. The `dist/` directory is auto-generated and changes are lost on rebuild.

---

## Build Scripts Reference

### Development Scripts

**`npm run dev`** or **`npm start`**
- Starts Eleventy development server with live reload
- Watches `src/` files for changes
- Serves site at `http://localhost:8080`
- **Use for:** Local development and testing

**`npm run dev:watch`**
- Runs `npm run dev` + esbuild in watch mode concurrently
- Auto-rebuilds CSS and JS on file changes
- **Use for:** Active development with instant feedback

---

### Production Build Scripts

**`npm run build:cloudflare`** ⭐ **CLOUDFLARE DEPLOYMENT**
```bash
npm run clean && npm run build:css && npm run build:html:prod && npm run build:js
```
- **Used by:** Cloudflare Pages automatic deployment
- **Does NOT extract critical CSS** (runs on Cloudflare servers without Puppeteer)
- **Sequence:**
  1. Clean dist/ directory
  2. Build and minify CSS
  3. Build HTML in production mode (minified)
  4. Build and minify JavaScript
- **Output:** Production-ready `dist/` folder
- **Time:** ~5-10 seconds

**`npm run build:prod`** ⭐ **LOCAL FULL BUILD**
```bash
npm run clean && npm run build:images && npm run build:html:prod && npm run build:css && npm run build:critical && npm run build:dedupe-critical && npm run build:html:prod && npm run build:js
```
- **Used by:** Developers before committing critical CSS changes
- **Includes critical CSS extraction + deduplication** (requires Puppeteer, X11 libraries)
- **Sequence:**
  1. Clean dist/ directory
  2. Process images (if process-images.mjs exists)
  3. Build HTML (first time - needed for critical CSS extraction)
  4. Build CSS
  5. Extract critical CSS from rendered HTML
  6. Deduplicate critical CSS (removes duplicate rules)
  7. **Build HTML again** (with deduplicated critical CSS inlined) ⬅️ Why it runs twice!
  8. Build JavaScript
- **Output:** Production-ready `dist/` + updated `src/_data/critical-*.css`
- **Time:** ~30-45 seconds
- **Important:** Commit extracted critical CSS files to git

**`npm run build`** ⭐ **LOCAL DEVELOPMENT BUILD**
```bash
npm run build:html && npm run build:css && npm run build:critical && npm run build:dedupe-critical && npm run build:html && npm run build:js
```
- Similar to `build:prod` but without `clean` or `build:images`
- **Build HTML runs twice** (before and after critical CSS extraction)
- **Use for:** Testing critical CSS changes locally

---

### Component Build Scripts

**`npm run build:html`**
- Runs Eleventy in development mode
- Generates HTML from `.njk` templates
- **No minification**

**`npm run build:html:prod`**
- Runs Eleventy in production mode (`NODE_ENV=production`)
- **Minifies HTML** using htmlmin transform
- Removes comments, collapses whitespace

**`npm run build:css`**
- Processes `src/assets/styles/main.css` with PostCSS
- Imports: core-brand.css, style-core.css, style.css, style-blog.css, etc.
- **Plugins:** postcss-import, autoprefixer, cssnano (minification)
- **Output:** `dist/css/main.min.css`

**`npm run build:js`**
- Bundles JavaScript with esbuild
- **Minifies and tree-shakes** unused code
- **Output:** `dist/js/*.js` (main.min.js, analytics.js, etc.)

**`npm run build:critical`**
- Extracts critical above-the-fold CSS from rendered HTML
- Uses `critical` npm package + Puppeteer
- Analyzes 3 viewports: 375px (mobile), 768px (tablet), 1920px (desktop)
- **Writes to:** `src/_data/critical-*.css` (4 files)
- **Local only** - Not run on Cloudflare deployment

**`npm run build:dedupe-critical`** ⭐ **NEW (Nov 26, 2025)**
- Removes duplicate CSS rules from critical CSS files
- Uses PostCSS with `postcss-discard-duplicates`
- **Reduction:** 20.7% file size savings (138 KB → 110 KB)
- **Writes to:** Same `src/_data/critical-*.css` files (in-place deduplication)

**`npm run clean`**
- Deletes `dist/` directory completely
- **Always run before full production build**

---

## Critical CSS Workflow

### Why Critical CSS?

**Problem:** CSS files block page rendering until fully downloaded
**Solution:** Inline above-the-fold CSS in `<head>`, defer loading of full CSS

**Benefits:**
- Faster Largest Contentful Paint (LCP)
- No "flash of unstyled content" (FOUC)
- Better Core Web Vitals scores

### Extraction Process

1. **Eleventy builds HTML** to `dist/` folder
2. **Critical CSS tool analyzes** rendered pages at 3 viewport sizes
3. **Extracts** CSS rules needed to render above-the-fold content
4. **Writes** to `src/_data/critical-*.css` (4 files)
5. **Deduplication** removes exact duplicate rules (20.7% reduction)
6. **Eleventy rebuilds HTML** with deduplicated critical CSS inlined in `<head>`

### Why Build HTML Twice?

**First Build:**
```
src/*.njk → dist/*.html (without critical CSS)
```
Critical CSS tool needs fully rendered HTML to analyze. First build creates the HTML that critical CSS extraction reads.

**Second Build:**
```
src/*.njk + src/_data/critical-*.css → dist/*.html (with critical CSS inlined)
```
After extraction + deduplication, Eleventy rebuilds HTML with critical CSS properly inlined. Templates use `{{ criticalCSS('critical-homepage.css') }}` filter to read and inline the CSS.

**This is intentional and required for the critical CSS system to work.**

---

## Validation Scripts

**`npm run validate:schema`**
- Validates all Schema.org JSON-LD markup
- Checks for required fields, valid types, proper formatting
- **Run before:** Committing schema changes

**`npm run validate:html`**
- Validates HTML for broken links, missing alt text, duplicate IDs
- Checks canonical URLs against sitemap.xml
- **Run before:** Committing HTML/template changes

**`npm run validate:all`**
- Runs both schema and HTML validation
- **Run before:** Every commit (also runs automatically via pre-commit hook)

**`npm run pre-commit-check`**
- Runs automatically on `git commit` (Husky hook)
- Checks:
  1. No `dist/` files staged
  2. No `console.log` in production JS
  3. No TODO comments in templates
  4. Schema validation passes
  5. HTML validation passes
- **Blocks commit** if validation fails
- **Skip with:** `git commit --no-verify` (not recommended)

---

## Deployment Workflows

### Local Development

```bash
npm run dev
# Edit files in src/
# Browser auto-refreshes on save
```

### Updating Critical CSS

```bash
# 1. Edit CSS in src/assets/styles/
vim src/assets/styles/style-core.css

# 2. Run full local build (includes critical CSS extraction)
npm run build:prod

# 3. Commit BOTH main CSS and critical CSS files
git add src/assets/styles/style-core.css src/_data/critical-*.css
git commit -m "Update mobile h1 font size"
git push
```

### Cloudflare Pages Deployment

**Automatic on every push to `main` branch:**

1. Developer pushes to GitHub
2. Cloudflare Pages detects push
3. Runs `npm run build:cloudflare`
4. Deploys `dist/` folder to production
5. **Uses committed critical CSS files** (does not re-extract)

**Why Cloudflare doesn't extract critical CSS:**
- Puppeteer requires X11 libraries not available in Cloudflare build environment
- Critical CSS files committed to git are used instead
- Faster deployments (no extraction step)

---

## File Organization

### Source Files (Edit These)

```
src/
├── pages/           # Nunjucks templates (.njk)
├── assets/
│   ├── styles/      # CSS files (main.css imports all)
│   └── scripts/     # JavaScript source files
├── _includes/
│   ├── layouts/     # Page layout templates
│   └── partials/    # Reusable components (header, footer)
├── _data/
│   ├── critical-*.css    # Auto-generated critical CSS (commit these!)
│   ├── navigation.json   # Site navigation structure
│   └── site.json         # Site-wide settings
└── blog/posts/      # Blog posts (Markdown)
```

### Built Files (Never Edit These)

```
dist/                # Auto-generated on every build
├── *.html           # Compiled HTML from .njk templates
├── css/
│   └── main.min.css # Minified CSS bundle
├── js/
│   └── *.js         # Minified JavaScript bundles
└── images/          # Optimized images
```

---

## Common Tasks

### Add New Page

1. Create `src/pages/my-page.njk`
2. Add to `src/_data/navigation.json` (if needed)
3. Run `npm run build:html:prod` to test
4. Commit and push

### Update Blog Post

1. Edit `src/blog/posts/YYYY-MM-DD-slug.md`
2. Run `npm run build:html:prod` to test
3. Commit and push

### Update Styles (Non-Critical)

1. Edit `src/assets/styles/*.css`
2. Run `npm run build:css` to rebuild
3. Refresh browser to see changes
4. Commit and push

### Update Styles (Critical/Above-Fold)

1. Edit `src/assets/styles/style-core.css` (or other CSS)
2. Run `npm run build:prod` (extracts critical CSS)
3. **Commit BOTH main CSS and critical CSS files:**
   ```bash
   git add src/assets/styles/*.css src/_data/critical-*.css
   git commit -m "Update above-fold styles"
   git push
   ```

### Update JavaScript

1. Edit `src/assets/scripts/*.js`
2. Run `npm run build:js` to rebuild
3. Refresh browser to see changes
4. Commit and push

---

## Performance Optimization Features

### Critical CSS Deduplication (Nov 26, 2025)

**Problem:** Critical CSS files contained ~50-60% duplicate rules (138 KB total)

**Solution:** PostCSS deduplication removes exact duplicate rules

**Results:**
- Homepage: 51 KB → 43 KB (16.1% reduction)
- Attorneys: 31 KB → 24 KB (21.4% reduction)
- Practice Areas: 26 KB → 20 KB (23.6% reduction)
- Page Layout: 31 KB → 23 KB (25.0% reduction)
- **Total: 138 KB → 110 KB (20.7% reduction)**

**Runs automatically** in `build:prod` and `build` workflows.

### CSS Processing

- **PostCSS Import:** Bundles multiple CSS files into one
- **Autoprefixer:** Adds vendor prefixes for browser compatibility
- **cssnano:** Minifies CSS (removes whitespace, comments, optimizes values)

### JavaScript Bundling

- **esbuild:** Ultra-fast bundler (10-100x faster than webpack)
- **Minification:** Removes whitespace, shortens variable names
- **Tree Shaking:** Removes unused code

### HTML Minification

- **htmlmin:** Removes comments, collapses whitespace
- **Only in production mode** (`build:html:prod`)

---

## Troubleshooting

### "Module not found" errors

**Solution:** Run `npm install` to install dependencies

### CSS changes not showing

**Solution:**
1. Clear browser cache (Ctrl+Shift+R)
2. Check cache version in `src/_includes/layouts/base.njk` (update `?v=` parameter)
3. Rebuild CSS: `npm run build:css`

### Critical CSS not updating

**Solution:**
1. Run full build: `npm run build:prod`
2. Commit updated critical CSS files: `git add src/_data/critical-*.css`

### Pre-commit validation failing

**Solution:**
1. Check errors: `npm run validate:all`
2. Fix reported issues
3. Or skip validation (not recommended): `git commit --no-verify`

### Cloudflare deployment failing

**Solution:**
1. Check build command: `npm run build:cloudflare`
2. Verify `dist/` folder generates locally
3. Check Cloudflare Pages build logs for errors

---

## Dependencies

### Production Dependencies
(None - all dependencies are devDependencies for build process)

### Development Dependencies

**Core Build Tools:**
- `@11ty/eleventy` - Static site generator
- `postcss` + `postcss-cli` - CSS processing
- `esbuild` - JavaScript bundling

**CSS Plugins:**
- `postcss-import` - CSS file imports
- `autoprefixer` - Browser compatibility
- `cssnano` - Minification
- `postcss-discard-duplicates` - Critical CSS deduplication

**Critical CSS:**
- `critical` - Above-the-fold CSS extraction

**Validation & Quality:**
- `husky` - Git hooks
- `node-html-parser` - HTML validation
- `html-minifier-terser` - HTML minification

**Image Processing:**
- `sharp` - Image optimization

**Utilities:**
- `cross-env` - Cross-platform environment variables
- `concurrently` - Run multiple commands simultaneously

---

## Build Times (Reference)

**Local Development:**
- `npm run dev`: 1-2 seconds startup
- Live reload: < 1 second

**Production Builds:**
- `npm run build:cloudflare`: 5-10 seconds
- `npm run build:prod`: 30-45 seconds (includes critical CSS extraction)
- Critical CSS extraction: ~20 seconds (4 pages × 3 viewports)

**Cloudflare Pages Deployment:**
- Build: 5-10 seconds
- Deploy: 10-20 seconds
- **Total: 15-30 seconds** from push to live

---

## Version History

- **Nov 26, 2025:** Added critical CSS deduplication (20.7% reduction)
- **Nov 25, 2025:** Added blog pagination system
- **Nov 24, 2025:** Critical CSS automation implemented
- **Oct 26, 2025:** Initial documentation

---

## Questions?

See:
- [CLAUDE.md](CLAUDE.md) - Project overview and recent changes
- [AI_CONTEXT.md](AI_CONTEXT.md) - Comprehensive technical documentation
- [QUICK_START.md](QUICK_START.md) - 5-minute quick reference
