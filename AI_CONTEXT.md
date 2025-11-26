# AI CONTEXT - Sorin & Pyle Eleventy Website

**Last Updated:** November 24, 2025
**Project:** Criminal Defense Law Firm Website
**Tech Stack:** Eleventy 3.1.2, Cloudflare Pages, PostCSS, esbuild

> **⚡ Quick Start:** New to this project? Read [QUICK_START.md](QUICK_START.md) first (5-minute read).
> This document provides comprehensive technical documentation (~16,000 words).

> **📚 Task-Focused Guides:** For focused work on specific tasks, use these guides:
> - [CSS Guide](utilities/docs/CSS_GUIDE.md) - CSS workflows, critical CSS, mobile breakpoints (10 min)
> - [Schema Guide](utilities/docs/SCHEMA_GUIDE.md) - Schema templates, validation, Rich Results (10 min)
> - [Content Guide](utilities/docs/CONTENT_GUIDE.md) - Creating pages, SEO checklists (12 min)
> - [Troubleshooting Guide](utilities/docs/TROUBLESHOOTING.md) - Common errors and fixes (15 min)

---

## 1. PROJECT OVERVIEW

**Sorin & Pyle, PC** - Criminal defense law firm website serving West Michigan (Holland, Grand Rapids, and 7 surrounding counties). The site is a high-performance static website built with Eleventy, optimized for SEO, accessibility (WCAG 2.1 Level AA), and Core Web Vitals.

**Key Features:**
- 8 practice area service pages (DUI, Domestic Violence, Expungement, etc.)
- 28 location landing pages (cities + counties + university student defense)
- Client resources (FAQ, Know Your Rights, Community Directory)
- **Blog System:** Eleventy 11ty blog with Markdown authoring, RSS feed, card grid UI
- Digital business cards with vCard downloads
- Google Analytics 4 with event tracking and Core Web Vitals monitoring
- GDPR/CCPA compliant cookie consent system
- IndexNow integration for instant search engine indexing

**Business Context:**
- Primary markets: Holland MI, Grand Rapids MI, Ottawa County, Kent County
- Target clients: Criminal defendants, DUI arrests, domestic violence charges
- Unique positioning: "WE GIVE A [EXPLETIVE]!" - bold, judgment-free representation
- Former public defenders with trial experience

---

## 2. BUILD SYSTEM ARCHITECTURE

### 2.1 Eleventy Configuration (`.eleventy.js`)

**Core Settings:**
```javascript
input: 'src',                    // Source files directory
output: 'dist',                  // Build output directory
templateFormats: ['njk', 'html', 'md'],
markdownTemplateEngine: 'njk',
htmlTemplateEngine: 'njk',
pathPrefix: '/'
```

**Build Optimizations:**
- **HTML Minification** (production only via `NODE_ENV=production`):
  - Uses `html-minifier-terser` package
  - Removes comments, collapses whitespace
  - Minifies inline CSS and JavaScript
  - Conservative collapse (preserves readability)
- **Quiet Mode:** Reduced console output for faster builds
- **Deep Merge:** Cached data for incremental builds
- **Watch Targets:** Auto-rebuild on changes to `src/assets/styles/` and `src/assets/scripts/`

**Plugins:**
1. **`@11ty/eleventy-plugin-rss@2.0.0`** - RSS/Atom feed generation for blog
   - Adds `dateToRfc3339` filter (RFC 3339 date format)
   - Adds `getNewestCollectionItemDate` filter (latest post date)
   - Adds `htmlToAbsoluteUrls` filter (convert relative URLs for RSS)

**Custom Filters:**
1. **`date`** - Format dates (supports `Y` for year, ISO for full dates)
2. **`readableDate`** - Human-readable dates (e.g., "October 6, 2025")
3. **`isoDate`** - ISO 8601 date format (YYYY-MM-DD)
4. **`htmlDateString`** - HTML5 datetime attribute format
5. **`replace`** - String replacement with regex (used for responsive image srcsets)
6. **`criticalCSS`** - Reads and inlines critical CSS files from `src/_data/`

**Collections:**
1. **`posts`** - All blog posts from `src/blog/posts/` directory
   - Sorted by date (newest first)
   - Filtered by `src/blog/posts/**/*.md` glob pattern
   - Available as `collections.posts` in templates

**Custom Shortcodes:**
1. **`responsiveImage`** - Generates `<picture>` elements with AVIF/WebP/fallback formats
   - Reads from `src/_data/images.json` manifest
   - Generates srcset with multiple widths (220w, 400w, 450w, 800w)
   - Format priority: AVIF → WebP → JPEG/PNG
   - Supports custom sizes and loading attributes

**Passthrough Copy (Static Files):**
```javascript
'src/static/'  → 'dist/',
'images/'      → 'dist/images/',
'fonts/'       → 'dist/fonts/',
'_headers'     → 'dist/_headers'  // Cloudflare Pages security headers
```

---

### 2.2 Package.json Scripts

**Development:**
```bash
npm run dev              # Eleventy dev server with live reload (localhost:8080)
npm run dev:watch        # Watch CSS/JS changes (run in separate terminal)
```

**Build Commands:**
```bash
npm run build:html       # Build HTML without minification
npm run build:html:prod  # Build HTML with minification (NODE_ENV=production)
npm run build:css        # PostCSS → dist/css/main.min.css
npm run build:js         # esbuild → dist/js/*.js
npm run build:images     # Sharp image processing (script gitignored)
npm run build:critical   # Extract critical CSS (script gitignored)
npm run clean            # Remove dist/ directory
```

**Composite Builds:**
```bash
npm run build            # Development: HTML → CSS → Critical → HTML → JS
npm run build:prod       # Full production: Clean → Images → HTML → CSS → Critical → HTML → JS
npm run build:cloudflare # Cloudflare deployment: Clean → CSS → HTML → JS (SKIPS images/critical)
```

**Key Dependencies:**
- `@11ty/eleventy@3.1.2` - Static site generator
- `esbuild@0.27.0` - JavaScript bundler
- `postcss@8.5.6` + `postcss-cli@11.0.1` - CSS processing
- `autoprefixer@10.4.22` - Browser compatibility
- `cssnano@7.1.2` - CSS minification (CURRENTLY DISABLED)
- `html-minifier-terser@7.2.0` - HTML minification
- `sharp@0.34.5` - Image processing
- `critical@7.2.1` - Critical CSS extraction

---

### 2.3 Asset Pipeline

#### CSS Processing (`postcss.config.js`)

**PostCSS Plugins (ORDER MATTERS):**
1. **`postcss-import`** (MUST be first) - Resolves `@import` statements, bundles CSS files
2. **`autoprefixer`** - Adds vendor prefixes
   - Targets: `>= 0.5%` market share, last 2 versions, Chrome 60+, Firefox 60+, Edge 79+, Safari 12+, iOS 12+
3. **`cssnano`** - Minification (**TEMPORARILY DISABLED - See Section 6.6**)

**CSS Source Files** (`src/assets/styles/`):
```
main.css (entry point) imports:
  ├─ core-brand.css       # CSS variables, resets, brand colors
  ├─ style-core.css       # Core component styles
  ├─ style.css            # Page-specific styles
  ├─ style-blog.css       # Blog page styles
  ├─ style-faq.css        # FAQ page styles
  ├─ style-card-pages.css # Digital business card styles
  └─ cookie-consent.css   # Cookie consent banner
```

**Build Output:** `dist/css/main.min.css` (all CSS bundled, NOT minified due to cssnano disabled)

**Critical CSS** (`src/_data/critical-*.css`):
- `critical-homepage.css` (1,385 chars) - Inlined in `<head>` of homepage
- `critical-attorneys.css` - Inlined in attorneys page
- `critical-practice-areas.css` - Inlined in practice areas page
- **CRITICAL:** See Section 4.1 for dual CSS update requirements

---

#### JavaScript Bundling (`esbuild.config.js`)

**Entry Points:**
```javascript
'main.min':       'src/assets/scripts/main.js',            // Core site functionality
'analytics':      'src/assets/scripts/analytics.js',       // Google Analytics 4
'cookie-consent': 'src/assets/scripts/cookie-consent.js',  // GDPR/CCPA compliance
'tracking':       'src/assets/scripts/tracking.js',        // Event tracking
'business-card':  'src/assets/scripts/business-card.js',   // vCard downloads
'qr-campaign':    'src/assets/scripts/qr-campaign.js'      // QR code campaigns
```

**Build Configuration:**
- **Output:** `dist/js/`
- **Format:** IIFE (Immediately Invoked Function Expression) for browser compatibility
- **Target:** ES2020, Chrome 80+, Firefox 78+, Safari 14+, Edge 88+
- **Features:** Bundle ✅, Minify ✅, Sourcemaps ✅, Tree shaking ✅

**JavaScript Functionality:**
- `main.js` - Mobile menu, dropdown navigation, FAQ accordions
- `analytics.js` - GA4 initialization, Core Web Vitals tracking, consent mode
- `cookie-consent.js` - GDPR/CCPA consent banner, localStorage management
- `tracking.js` - Event listeners for phone/CTA clicks
- `business-card.js` - vCard download tracking
- `qr-campaign.js` - QR code campaign UTM tracking

---

#### Image Processing

**Image Manifest:** `src/_data/images.json` - Generated by Sharp (script gitignored):
```json
{
  "attorney-name": {
    "variants": [
      { "format": "avif", "width": 220, "url": "/images/attorney-220w.avif" },
      { "format": "avif", "width": 400, "url": "/images/attorney-400w.avif" },
      { "format": "webp", "width": 220, "url": "/images/attorney-220w.webp" }
    ]
  }
}
```

**Responsive Image Shortcode** (in `.eleventy.js`):
```njk
{% responsiveImage "/images/attorney.avif", "Alt text", "(max-width: 768px) 220px, 220px", "lazy" %}
```

**Output:**
```html
<picture>
  <source type="image/avif" srcset="/images/attorney-220w.avif 220w, /images/attorney-400w.avif 400w" sizes="...">
  <source type="image/webp" srcset="/images/attorney-220w.webp 220w, /images/attorney-400w.webp 400w" sizes="...">
  <img src="/images/attorney-400w.jpg" srcset="..." alt="Alt text" loading="lazy">
</picture>
```

---

## 3. PROJECT STRUCTURE

### 3.1 Directory Tree

```
sorin-pyle-site-html/
├── .eleventy.js              # Eleventy configuration
├── package.json              # Dependencies and build scripts
├── esbuild.config.js         # JavaScript bundler config
├── postcss.config.js         # CSS processor config
├── _headers                  # Cloudflare Pages security headers
├── CLAUDE.md                 # Comprehensive project documentation
├── AI_CONTEXT.md            # This file (AI persistent context)
├── src/                      # ⚡ SOURCE FILES (EDIT THESE)
│   ├── pages/                # Page templates (Nunjucks .njk files)
│   │   ├── index.njk         # Homepage
│   │   ├── attorneys.njk     # Attorney listing
│   │   ├── practice-areas.njk # Practice areas overview
│   │   ├── contact.njk       # Contact page
│   │   ├── sorin-panainte.njk # Attorney profile
│   │   ├── jonathan-pyle.njk  # Attorney profile
│   │   ├── dui-defense.njk   # DUI/OWI service page
│   │   ├── domestic-violence-defense.njk # DV service page
│   │   ├── record-expungement.njk # Expungement service
│   │   ├── drivers-license-restoration.njk # License restoration
│   │   ├── first-offense-owi.njk # First OWI page
│   │   ├── repeat-offense-owi.njk # Repeat OWI page
│   │   ├── super-drunk-high-bac.njk # Super Drunk page
│   │   ├── cdl-owi-defense.njk # CDL OWI page
│   │   ├── faq.njk           # FAQ page (FAQPage schema)
│   │   ├── blog.njk          # Blog archive page (card grid)
│   │   ├── your-rights.njk   # Know Your Rights
│   │   ├── community-resources.njk # Community directory
│   │   ├── privacy-policy.njk # Privacy policy
│   │   ├── accessibility.njk  # Accessibility statement
│   │   ├── card.njk          # Digital business card
│   │   ├── 404.njk, 500.njk  # Error pages
│   │   └── locations/        # 28 location pages
│   │       ├── ottawa-county.njk, kent-county.njk (7 county pages)
│   │       ├── holland-mi.njk, grand-rapids-mi.njk (8 city pages)
│   │       └── gvsu-student-defense.njk (7 university pages)
│   ├── blog/                 # Blog system (Eleventy 11ty)
│   │   └── posts/            # Markdown blog posts
│   │       └── 2025-10-06-understanding-dui-charges-michigan.md
│   ├── feed.njk              # RSS/Atom feed for blog
│   ├── _includes/            # Reusable templates
│   │   ├── layouts/
│   │   │   ├── base.njk      # Base HTML layout (all pages extend)
│   │   │   ├── page.njk      # Standard page layout (extends base)
│   │   │   └── blog-post.njk # Individual blog post layout (BlogPosting schema)
│   │   └── partials/
│   │       ├── header.njk    # Navbar (desktop + mobile)
│   │       └── footer.njk    # Footer component
│   ├── _data/                # Global data files (JSON + CSS)
│   │   ├── site.json         # Firm info, attorneys, contact, hours
│   │   ├── navigation.json   # Main nav, footer nav (data-driven)
│   │   ├── authors.json      # Blog author data (Sorin, Jonathan, Firm)
│   │   ├── images.json       # Image variants manifest (Sharp output)
│   │   ├── critical-homepage.css # Inlined homepage CSS
│   │   ├── critical-attorneys.css # Inlined attorneys CSS
│   │   └── critical-practice-areas.css # Inlined practice areas CSS
│   ├── assets/
│   │   ├── styles/           # CSS source files
│   │   │   ├── main.css      # Entry point (imports all CSS)
│   │   │   ├── core-brand.css # Variables, resets
│   │   │   ├── style-core.css # Core components
│   │   │   ├── style.css     # Page-specific styles
│   │   │   ├── style-blog.css # Blog card grid styles
│   │   │   └── (3 more CSS files: style-faq.css, style-card-pages.css, cookie-consent.css)
│   │   └── scripts/          # JavaScript source files
│   │       ├── main.js, analytics.js, cookie-consent.js, tracking.js
│   │       └── business-card.js, qr-campaign.js
│   └── static/               # Static assets (copied as-is)
├── images/                   # Image assets (copied to dist/)
├── fonts/                    # Web fonts (copied to dist/)
├── utilities/                # Development tools and scripts
│   ├── README.md             # Comprehensive utilities documentation
│   ├── docs/                 # Task-focused guides (CSS, Schema, Content, Troubleshooting)
│   ├── templates/            # Schema markup templates + README
│   ├── legacy/               # 66 archived Python/Node scripts (reference only)
│   ├── validate-schema.js    # Schema validation script (pre-commit)
│   ├── validate-html.js      # HTML validation script (pre-commit)
│   ├── pre-commit-check.js   # Pre-commit hook runner
│   ├── extract-critical-css.mjs # Critical CSS extraction (local only)
│   ├── process-images.mjs    # Image optimization with Sharp
│   └── generate-schema.js    # Schema template generator
└── dist/                     # ⛔ BUILD OUTPUT (NEVER EDIT)
    ├── (all .html files)     # Built from src/pages/*.njk
    ├── locations/            # Built location pages
    ├── css/main.min.css      # Bundled, processed CSS
    ├── js/*.js               # Bundled, minified JavaScript
    ├── images/               # Copied/processed images
    └── fonts/                # Copied fonts
```

---

### 3.2 Template Hierarchy

**Layout Inheritance:**
```
base.njk (HTML shell, <head>, CSS/JS loading, analytics)
  ↳ page.njk (adds critical CSS, content wrapper, sections)
      ↳ index.njk (homepage content)
      ↳ attorneys.njk (attorney listing)
      ↳ blog.njk (blog archive page with card grid)
      ↳ dui-defense.njk (DUI service page)
      ↳ locations/holland-mi.njk (city page)
      ↳ (all other pages extend page.njk)
  ↳ blog-post.njk (individual blog posts with BlogPosting schema)
      ↳ src/blog/posts/*.md (Markdown blog posts)
```

**How It Works:**
1. All pages set `layout: layouts/base.njk` or `layout: layouts/page.njk` in frontmatter
2. `page.njk` extends `base.njk` and adds page-specific structure
3. Page content goes in `{% block content %}...{% endblock %}`
4. Partials (`header.njk`, `footer.njk`) included via `{% include "partials/header.njk" %}`

---

### 3.3 Data Cascade

**Global Data Flow:**
```
src/_data/*.json (Global Data)
  ↓
site.json → Available as {{ site.* }} in ALL templates
  - site.title, site.phone, site.email, site.address
  - site.attorneys[0].name, site.attorneys[0].photo
  - site.analytics.measurementId

navigation.json → Available as {{ navigation.* }} in ALL templates
  - navigation.main[] (desktop/mobile nav links)
  - navigation.footer.practiceAreas[], navigation.footer.locations[]

authors.json → Available as {{ authors.* }} in ALL templates
  - authors['sorin'], authors['jonathan'], authors['firm']
  - Used in blog posts for author attribution and schema markup

images.json → Used internally by {% responsiveImage %} shortcode
  ↓
Template Frontmatter (---...---)
  - layout, title, description, permalink, criticalCSSFile
  ↓
Page Content ({% block content %})
```

**Example Usage:**
```njk
{# Access global site data #}
<a href="tel:{{ site.phone.link }}">{{ site.phone.display }}</a>

{# Loop through navigation #}
{% for item in navigation.main %}
  <a href="{{ item.url }}">{{ item.text }}</a>
{% endfor %}

{# Loop through attorneys #}
{% for attorney in site.attorneys %}
  <h3>{{ attorney.name }}</h3>
  <img src="{{ attorney.photo }}" alt="{{ attorney.name }}">
{% endfor %}
```

---

## 4. CRITICAL SYSTEMS

### 4.1 ✅ DUAL CSS ARCHITECTURE - AUTOMATED (November 24, 2025)

**SIMPLIFIED SYSTEM:**
> **The site uses TWO separate CSS systems with AUTOMATED synchronization:**
> 1. **Main CSS** (Deferred Loading) - `src/assets/styles/*.css` (edit this)
> 2. **Critical CSS** (Inline in HTML `<head>`) - `src/_data/critical-*.css` (auto-generated)

**Why This Matters:**
- **Critical CSS** loads inline in `<head>` → displays FIRST (above-the-fold instant render)
- **Main CSS** loads deferred → displays AFTER page load (non-blocking)
- **Automation** extracts critical CSS from rendered HTML → eliminates manual synchronization

**Critical CSS Files (Auto-Generated):**
1. **`src/_data/critical-homepage.css`** (~15KB) - Extracted from `dist/index.html`
2. **`src/_data/critical-attorneys.css`** (~12KB) - Extracted from `dist/attorneys.html`
3. **`src/_data/critical-practice-areas.css`** (~11KB) - Extracted from `dist/practice-areas.html`
4. **`src/_data/critical-page-layout.css`** (~10KB) - Extracted from `dist/dui-defense.html` (used by 25+ pages)

**Loading Mechanism:**
```njk
{# In page frontmatter (index.njk, attorneys.njk, practice-areas.njk): #}
---
criticalCSSFile: critical-homepage.css
---

{# In base.njk template: #}
<style>{{ criticalCSSFile | criticalCSS | safe }}</style>

{# In page.njk layout (25+ pages): #}
<style>{{ 'critical-page-layout.css' | criticalCSS | safe }}</style>

{# Main CSS deferred (loads after above-the-fold render): #}
<link rel="preload" href="/css/main.min.css?v=20251123" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

**✅ AUTOMATED Update Workflow (Example: Mobile h1 Font Size):**
```bash
# Step 1: Update main CSS ONLY (single source of truth)
Edit: src/assets/styles/style-core.css
Change: @media (max-width: 767px) { h1 { font-size: 2rem; } }

# Step 2: Run automated build
npm run build:cloudflare

# OR for local testing:
npm run build:css           # Build main CSS
npm run build:html:prod     # Build HTML to dist/
npm run build:critical      # Auto-extract critical CSS from dist/
npm run build:html:prod     # Rebuild HTML with new critical CSS

# Step 3: Commit and deploy
git add src/assets/styles/style-core.css src/_data/critical-*.css
git commit -m "Update mobile h1 font size"
git push
```

**Automation Details:**
- **Script:** `utilities/extract-critical-css.mjs`
- **Package:** `critical` npm package v7.2.1
- **Process:** Analyzes rendered HTML in `dist/` folder for 3 viewports (375px, 768px, 1920px)
- **Output:** Minified critical CSS written to `src/_data/critical-*.css`
- **Integration:** Runs automatically in `npm run build:cloudflare` (production deployment)

**Benefits of Automation:**
- ✅ Update 1 file instead of 5 files
- ✅ No risk of forgetting to sync critical CSS files
- ✅ Consistent critical CSS across all pages
- ✅ Eliminates manual editing of minified CSS
- ✅ Prevents incidents like November 24 multi-commit fix

**When Critical CSS is Re-extracted:**
- Automatically on every `npm run build:cloudflare` (production deployment)
- Automatically on every `npm run build` (local development build)
- Manually via `npm run build:critical` (for testing)

---

### 4.2 Data-Driven Navigation

**Global Site Data** (`src/_data/site.json`):
```json
{
  "title": "Sorin & Pyle, PC",
  "phone": {
    "display": "(616) 227-3303",
    "link": "tel:+16162273303"
  },
  "email": "justice@callsbp.com",
  "address": {
    "street": "217 E 24th St Ste 107",
    "city": "Holland",
    "state": "MI",
    "zip": "49423"
  },
  "hours": {
    "office": "Mon-Fri 9 AM - 5 PM",
    "phone": "24/7 for messages & scheduling"
  },
  "attorneys": [
    {
      "name": "Sorin Panainte",
      "slug": "sorin-panainte",
      "barNumber": "P85326",
      "photo": "/images/sorin-panainte-criminal-defense-attorney-holland-mi.avif"
    },
    {
      "name": "Jonathan Pyle",
      "slug": "jonathan-pyle",
      "barNumber": "P81692",
      "photo": "/images/jonathan-pyle-criminal-defense-attorney-holland-mi.avif"
    }
  ],
  "analytics": {
    "measurementId": "G-LV7PKRF2YT"
  }
}
```

**Navigation Data** (`src/_data/navigation.json`):
```json
{
  "main": [
    { "text": "About", "url": "/" },
    { "text": "Attorneys", "url": "/attorneys.html" },
    { "text": "Practice Areas", "url": "/practice-areas.html" },
    { "text": "Locations", "url": "/locations.html" },
    {
      "text": "Client Resources",
      "url": "#",
      "dropdown": [
        { "text": "Frequently Asked Questions", "url": "/faq.html" },
        { "text": "Know Your Rights", "url": "/your-rights.html" },
        { "text": "Community Resources", "url": "/community-resources.html" },
        { "text": "Firm News & Updates", "url": "/blog.html" }
      ]
    },
    { "text": "Contact", "url": "/contact.html" }
  ],
  "footer": {
    "practiceAreas": [
      { "text": "OWI / Drunk Driving", "url": "/dui-defense.html" },
      { "text": "Domestic Violence", "url": "/domestic-violence-defense.html" },
      { "text": "Record Expungement", "url": "/record-expungement.html" },
      { "text": "Driver License Restoration", "url": "/drivers-license-restoration.html" }
    ]
  }
}
```

**Usage in Templates:**
```njk
{# Desktop Navigation (header.njk) #}
{% for item in navigation.main %}
  {% if item.dropdown %}
    <button class="navbar_dropdown-toggle" aria-haspopup="true" aria-expanded="false">
      {{ item.text }}
    </button>
    <ul class="navbar_dropdown-menu" role="menu">
      {% for subitem in item.dropdown %}
        <li><a href="{{ subitem.url }}">{{ subitem.text }}</a></li>
      {% endfor %}
    </ul>
  {% else %}
    <a href="{{ item.url }}">{{ item.text }}</a>
  {% endif %}
{% endfor %}
```

---

### 4.3 Analytics & Tracking

**Google Analytics 4:**
- **Measurement ID:** `G-LV7PKRF2YT` (from `site.json`)
- **Scripts:**
  - `https://www.googletagmanager.com/gtag/js?id=G-LV7PKRF2YT` (async loaded)
  - `analytics.js` - Global `gtag()` function, consent mode, Core Web Vitals
  - `tracking.js` - Event listeners for clicks

**Event Tracking Classes:**
```html
<!-- Phone click tracking -->
<a href="tel:+16162273303" class="track-phone-click" data-event-label="Header Phone">
  (616) 227-3303
</a>

<!-- CTA click tracking -->
<a href="/contact.html" class="track-cta-click" data-cta-type="primary">
  Free Consultation
</a>

<!-- Generic click tracking -->
<a href="#" class="track-click"
   data-event-category="Navigation"
   data-event-action="Click"
   data-event-label="Client Resources">
  Client Resources
</a>
```

**Cookie Consent (GDPR/CCPA):**
- Blocks Google Analytics until user accepts cookies
- Stores consent in localStorage with version and timestamp
- 1-second delay before banner appears (UX best practice)
- Consent structure:
  ```json
  {
    "version": "1.0",
    "accepted": true,
    "timestamp": "2025-10-26T12:34:56.789Z"
  }
  ```

**Core Web Vitals Tracking:**
- CLS (Cumulative Layout Shift)
- FID (First Input Delay)
- FCP (First Contentful Paint)
- LCP (Largest Contentful Paint)
- TTFB (Time to First Byte)

---

### 4.4 Blog System (Eleventy 11ty)

**Architecture:**
- **Blog Archive Page:** `src/pages/blog.njk` - Professional 2-column card grid
- **Individual Posts:** Markdown files in `src/blog/posts/` → Auto-generated HTML pages
- **RSS Feed:** `src/feed.njk` → `/feed.xml` (15 most recent posts)
- **Layout Template:** `src/_includes/layouts/blog-post.njk` (BlogPosting schema)
- **Author Data:** `src/_data/authors.json` (Sorin, Jonathan, Firm)

**Blog Archive Page Features:**
```njk
{# Card Grid Layout #}
<div class="blog-grid">  <!-- 2 columns desktop, 1 column mobile -->
  {% for post in collections.posts %}
    <a href="{{ post.url }}" class="blog-card" data-category="{{ post.data.category | lower }}">
      <picture>
        <img src="{{ post.data.featuredImage }}" alt="{{ post.data.featuredImageAlt }}"
             class="blog-card_image" width="400" height="300" loading="lazy">
      </picture>
      <div class="blog-card_content">
        <h2 class="blog-card_title">{{ post.data.title }}</h2>
        <p class="blog-card_meta">
          <time datetime="{{ post.date | htmlDateString }}">{{ post.date | readableDate }}</time>
          <span class="blog-category blog-category-{{ post.data.category | lower }}">
            {{ post.data.category }}
          </span>
        </p>
        <p class="blog-card_byline">By {{ authors[post.data.author].name }}</p>
        <p class="blog-card_excerpt">{{ post.data.description }}</p>
        <span class="blog-card_readmore">Read Full Article →</span>
      </div>
    </a>
  {% endfor %}
</div>

{# Category Filter Buttons #}
<button class="category-filter-btn active" data-category="all">All</button>
<button class="category-filter-btn" data-category="community">Community</button>
<button class="category-filter-btn" data-category="legal">Legal</button>
<button class="category-filter-btn" data-category="michigan">Michigan Law</button>
<button class="category-filter-btn" data-category="case">Case Analysis</button>
```

**Category Filtering (JavaScript):**
```javascript
// Client-side filtering without page reload
filterButtons.forEach(button => {
  button.addEventListener('click', function() {
    const category = this.dataset.category;

    // Filter cards by data-category attribute
    cards.forEach(card => {
      const cardCategory = card.dataset.category;
      if (category === 'all' || cardCategory === category) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
});
```

**CSS Card Grid Design (Professional Style):**
```css
.blog-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);  /* 2 columns desktop */
  gap: 2rem;
  margin-bottom: 3rem;
}

@media (max-width: 767px) {
  .blog-grid {
    grid-template-columns: 1fr;  /* 1 column mobile */
  }
}

.blog-card {
  background: var(--white);
  border-radius: var(--border-radius-card);
  box-shadow: var(--shadow-soft);
  border-left: 4px solid var(--primary-blue);  /* Left border accent */
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.blog-card:hover {
  transform: translateY(-4px);  /* Lift effect */
  box-shadow: var(--shadow-hover);
}

.blog-card_image {
  width: 100%;
  height: 225px;  /* Fixed height for consistency */
  object-fit: cover;
  display: block;
}
```

**Category Tag Colors:**
- **Community** (green `#28a745`) - Pro bono work, events, volunteering
- **Legal** (blue `var(--primary-blue)`) - Attorney commentary, opinions
- **Michigan Law** (purple `#6f42c1`) - New laws, court decisions
- **Case Analysis** (orange `#fd7e14`) - High-profile case analysis

**Markdown Post Example:**
```markdown
---
layout: layouts/blog-post.njk
title: "Understanding DUI Charges in Michigan"
description: "Learn about Michigan's drunk driving laws and your legal rights."
date: 2025-10-06
author: "sorin"
category: "legal"
featuredImage: "/images/dui-defense-michigan.avif"
featuredImageAlt: "Michigan DUI defense attorney"
tags:
  - DUI
  - criminal defense
  - Michigan law
---

# Understanding DUI Charges in Michigan

Michigan's drunk driving laws are complex...
```

**BlogPosting Schema (Auto-Generated):**
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Understanding DUI Charges in Michigan",
  "description": "Learn about Michigan's drunk driving laws...",
  "image": "https://www.sorinpyle.com/images/dui-defense-michigan.avif",
  "author": {
    "@type": "Person",
    "name": "Sorin Panainte",
    "url": "https://www.sorinpyle.com/sorin-panainte.html",
    "jobTitle": "Criminal Defense Attorney",
    "worksFor": {
      "@type": "LegalService",
      "name": "Sorin & Pyle, PC"
    }
  },
  "publisher": {
    "@type": "LegalService",
    "name": "Sorin & Pyle, PC",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.sorinpyle.com/images/sorin-pyle-stacked-color.avif"
    }
  },
  "datePublished": "2025-10-06",
  "dateModified": "2025-10-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.sorinpyle.com/blog/understanding-dui-charges-michigan.html"
  },
  "articleSection": "legal"
}
```

**RSS Feed (`src/feed.njk`):**
```xml
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Sorin & Pyle, PC - Firm News & Updates</title>
  <link href="https://www.sorinpyle.com/feed.xml" rel="self"/>
  <updated>{{ collections.posts | getNewestCollectionItemDate | dateToRfc3339 }}</updated>
  {%- for post in collections.posts | slice(0, 15) %}
  <entry>
    <title>{{ post.data.title }}</title>
    <link href="{{ site.url }}{{ post.url }}"/>
    <updated>{{ post.date | dateToRfc3339 }}</updated>
    <content type="html">{{ post.templateContent | htmlToAbsoluteUrls(site.url) }}</content>
  </entry>
  {%- endfor %}
</feed>
```

**Individual Post Page Features:**
- **Breadcrumb navigation:** Home > Firm News > [Post Title]
- **Social sharing buttons:** Facebook, Twitter, LinkedIn
- **Related posts:** Up to 3 posts from same category
- **Back to blog link:** Returns to archive page

**Authors Data Structure (`src/_data/authors.json`):**
```json
{
  "sorin": {
    "name": "Sorin Panainte",
    "title": "Criminal Defense Attorney",
    "profileUrl": "/sorin-panainte.html",
    "schemaType": "Person"
  },
  "jonathan": {
    "name": "Jonathan Pyle",
    "title": "Criminal Defense Attorney",
    "profileUrl": "/jonathan-pyle.html",
    "schemaType": "Person"
  },
  "firm": {
    "name": "Sorin & Pyle, Trial Lawyers",
    "profileUrl": "/attorneys.html",
    "schemaType": "Organization"
  }
}
```

**Blog UI/UX Features:**
- Professional card grid layout (industry standard for law firms)
- Left border accent (4px solid blue) ties cards to brand color
- Hover effects (lift + shadow) for interactivity
- Category filtering without page reload
- Responsive images (400x300, lazy loading)
- Interactive CTAs (orange "Read Full Article →" links)
- Mobile-first design (single column stack <768px)

**SEO Optimizations:**
- BlogPosting schema markup on all posts
- RSS feed at `/feed.xml` for syndication
- Breadcrumb schema for navigation context
- Social sharing meta tags (Open Graph, Twitter Cards)
- Category and tag metadata for taxonomy
- Author attribution with Person schema

**Performance:**
- Featured images lazy loaded (below-the-fold)
- Category filter uses client-side JavaScript (no server round-trip)
- RSS feed limited to 15 posts (prevents bloat)
- Card grid uses CSS Grid for efficient layout

---

## 5. DEPLOYMENT & HOSTING

### 5.1 Cloudflare Pages

**Auto-Deployment Setup:**
- **Repository:** `https://github.com/SPTrialattorneys/Sorin-Pyle-site.git`
- **Branch:** `main` (auto-deploys on push)
- **Build Command:** `npm run build:cloudflare`
- **Build Output Directory:** `dist`
- **Node.js Version:** 20.x
- **Environment Variables:** `NODE_ENV=production` (for HTML minification)

**Deployment Workflow:**
1. Developer pushes to `main` branch on GitHub
2. Cloudflare Pages detects push webhook
3. Runs `npm install` to install dependencies
4. Runs `npm run build:cloudflare`:
   - `npm run clean` - Removes old `dist/` directory
   - `npm run build:css` - PostCSS processes CSS → `dist/css/main.min.css`
   - `npm run build:html:prod` - Eleventy builds HTML with minification
   - `npm run build:js` - esbuild bundles JavaScript → `dist/js/*.js`
5. Cloudflare deploys `dist/` directory to global CDN
6. Site live at `https://www.sorinpyle.com` in 2-3 minutes

**Manual Rebuild Trigger:**
```bash
# Method 1: Empty commit
git commit --allow-empty -m "Trigger Cloudflare rebuild"
git push

# Method 2: Touch trigger file
echo $(date) > .cloudflare-rebuild-trigger.txt
git add .cloudflare-rebuild-trigger.txt
git commit -m "Trigger rebuild"
git push

# Method 3: Cloudflare dashboard → Deployments → Retry deployment
```

---

### 5.2 Security Headers (`_headers` file)

Cloudflare Pages reads `_headers` file to set HTTP security headers:

```
/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Cross-Origin-Opener-Policy: same-origin
  Permissions-Policy: accelerometer=(), camera=(), geolocation=(), microphone=()
  Content-Security-Policy: script-src 'self' https://www.google.com https://www.gstatic.com https://www.googletagmanager.com https://unpkg.com https://static.cloudflareinsights.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://www.google-analytics.com https://www.googletagmanager.com; connect-src 'self' https://www.google-analytics.com https://analytics.google.com https://www.googletagmanager.com https://cloudflareinsights.com;

/css/*
  Cache-Control: public, max-age=31536000, immutable

/js/*
  Cache-Control: public, max-age=31536000, immutable

/images/*
  Cache-Control: public, max-age=31536000, immutable

/fonts/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate
```

**Security Features:**
- **HSTS** - Force HTTPS for 1 year
- **CSP** - Content Security Policy (XSS protection)
- **X-Frame-Options** - Clickjacking protection
- **Caching** - HTML: no cache, Assets: 1 year immutable

---

### 5.3 GitHub Actions

**IndexNow Workflow** (`.github/workflows/indexnow.yml`):
- **Trigger:** Push to `main` with changes to `**.html` or `sitemap.xml`
- **Action:** Submit sitemap to IndexNow API for instant indexing
- **Search Engines:** Bing, Yandex, Seznam, Naver
- **API Key:** `7d7b322263d37b164568a832357c63b8` (verification file in repo root)

---

## 6. IMPORTANT CONSTRAINTS & GOTCHAS

### 6.1 ⛔ NEVER EDIT `dist/` DIRECTORY

**CRITICAL RULE:**
> **DO NOT edit files in `dist/` directory. Changes will be overwritten on next build.**

**Why:**
- `dist/` is automatically generated by Eleventy build process
- Every `npm run build` command deletes and recreates `dist/`
- `dist/` is in `.gitignore` and not tracked by git
- Cloudflare builds `dist/` from `src/` on every deployment

**ALWAYS edit source files in `src/` directory:**
- ✅ HTML templates: `src/pages/*.njk`
- ✅ CSS: `src/assets/styles/*.css`
- ✅ JavaScript: `src/assets/scripts/*.js`
- ✅ Layouts: `src/_includes/layouts/*.njk`
- ✅ Partials: `src/_includes/partials/*.njk`
- ✅ Data: `src/_data/*.json`

---

### 6.2 page.njk Critical CSS Mobile Fixes Required

**IMPORTANT:**
> Not all pages use dedicated critical CSS files! Pages using `page.njk` layout get critical CSS from `src/_includes/layouts/page.njk` hardcoded inline styles.

**Required Mobile Styles in page.njk (lines 5-69):**
```css
@media (max-width: 767px) {
    .container-large {
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }
    h1 {
        font-size: 2rem;
        line-height: 1.25;
        word-wrap: break-word;
        overflow-wrap: break-word;
        max-width: 100%;
    }
}

@media (max-width: 374px) {
    .container-large {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    h1 {
        font-size: 2rem;
        line-height: 1.1;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
}
```

**Why This Matters:**
- `page.njk` is extended by MANY pages (attorney profiles, service pages, location pages)
- Without mobile breakpoints → horizontal overflow on mobile
- Main CSS loads deferred → too late to prevent initial overflow
- Critical CSS MUST include mobile fixes for instant proper render

---

### 6.3 Attorney Photo Cropping Constraints

**Production Uses Hand-Cropped Images:**
> Production 220w images: ~14KB (hand-cropped for optimal framing)
> Auto-generated 220w images: ~4-5KB (algorithmically cropped from 400px originals)
> Different file sizes = completely different cropping

**DO NOT:**
- ❌ Auto-generate 220w images from 400px originals
- ❌ Replace production 220w images with auto-generated versions
- ❌ Change `object-position: top` CSS rule

**ALWAYS:**
- ✅ Use production 220w images from `images/` folder
- ✅ Keep `object-position: top` CSS rule in `style-core.css`
- ✅ Use 220w as default `src` in homepage template
- ✅ Verify photos match production before deploying

**Verification Command:**
```bash
ls -lh images/*-220w.avif
# Correct: Sorin 14K, Jonathan 14K
# Wrong: Sorin 4-5K, Jonathan 4-5K (auto-generated)
```

---

### 6.4 Mobile Navigation ARIA Role

**Fixed Accessibility Issue:**
> Mobile navigation previously used `role="dialog"` instead of `role="navigation"`.
> This was a WCAG Level A violation (4.1.2 Name, Role, Value).

**Correct Implementation** (`src/_includes/partials/header.njk` line 51):
```njk
<div class="mobile-nav_menu" id="mobile-nav" role="navigation" aria-label="Mobile navigation menu" aria-hidden="true">
```

**DO NOT change `role="navigation"` back to `role="dialog"`** - this is a critical accessibility fix.

---

### 6.5 Navigation Data Structure

**No About Page Exists:**
> The site does NOT have a dedicated `about.html` page.
> About/philosophy content is integrated into the homepage.

**Correct Navigation Links:**
- "About" button → `/` (homepage)
- "Our Philosophy" footer link → `/` (homepage)

**DO NOT:**
- ❌ Create an `about.html` page
- ❌ Point About navigation to any page other than homepage
- ❌ Use `/index.html` in navigation (use `/` for cleaner URLs)

---

### 6.6 PostCSS cssnano Temporarily Disabled

**From `postcss.config.js`:**
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
- Output `dist/css/main.min.css` is NOT actually minified (same size as source)
- File is still named `.min.css` for backwards compatibility with templates

**To Re-Enable:**
1. Uncomment cssnano plugin in `postcss.config.js`
2. Rebuild CSS: `npm run build:css`
3. Expected file size reduction: ~28% (based on previous minification)

---

### 6.7 Image Processing Scripts Gitignored

**Missing Scripts:**
- `process-images.mjs` - Generates responsive image variants with Sharp
- `extract-critical-css.mjs` - Extracts above-the-fold CSS from built HTML

**These scripts are gitignored** (not in repository):
- Mentioned in `package.json` scripts but files don't exist
- `npm run build:images` and `npm run build:critical` will fail
- Full production build `npm run build:prod` will fail

**Workaround:**
- Use `npm run build:cloudflare` instead (skips image/critical processing)
- Relies on pre-existing critical CSS files in `src/_data/`
- Relies on pre-existing image files in `images/` directory

---

### 6.8 Build Command Differences

**Development Build:**
```bash
npm run build
# Runs: HTML → CSS → Critical → HTML → JS
# Uses existing critical CSS files
```

**Production Build (Full):**
```bash
npm run build:prod
# Runs: Clean → Images → HTML → CSS → Critical → HTML → JS
# REQUIRES: process-images.mjs and extract-critical-css.mjs (MISSING)
# Will fail due to missing scripts
```

**Cloudflare Build (Deployment):**
```bash
npm run build:cloudflare
# Runs: Clean → CSS → HTML → JS
# SKIPS: Image processing and critical CSS extraction
# Uses pre-existing critical CSS files
# RECOMMENDED for deployment
```

**When to Use:**
- **`npm run dev`** - Local development with live reload
- **`npm run build`** - Test build locally (uses existing assets)
- **`npm run build:cloudflare`** - Cloudflare deployment (fastest, recommended)
- **`npm run build:prod`** - Will fail (requires missing scripts)

---

## 7. COMMON TASKS QUICK REFERENCE

### 7.1 Add a New Page

1. **Create Nunjucks template:**
   ```bash
   # Create new file
   src/pages/new-page.njk
   ```

2. **Add frontmatter:**
   ```njk
   ---
   layout: layouts/page.njk
   title: Page Title Here
   description: Meta description for SEO (150-160 chars)
   permalink: /new-page.html
   ---

   {% block content %}
   <section class="section">
     <div class="container-large">
       <h1>Page Content Here</h1>
     </div>
   </section>
   {% endblock %}
   ```

3. **Update navigation (if needed):**
   ```bash
   # Edit navigation data
   src/_data/navigation.json

   # Add to main[] or footer.* arrays
   ```

4. **Build and deploy:**
   ```bash
   npm run build:html
   git add src/pages/new-page.njk src/_data/navigation.json
   git commit -m "Add new page: [Page Name]"
   git push
   ```

---

### 7.2 Update Navigation

1. **Edit navigation data:**
   ```bash
   src/_data/navigation.json
   ```

2. **Add to main navigation:**
   ```json
   {
     "main": [
       { "text": "New Link", "url": "/new-page.html" }
     ]
   }
   ```

3. **Add dropdown menu:**
   ```json
   {
     "text": "Resources",
     "url": "#",
     "dropdown": [
       { "text": "Submenu Item", "url": "/submenu.html" }
     ]
   }
   ```

4. **Rebuild and deploy:**
   ```bash
   npm run build:html
   git add src/_data/navigation.json
   git commit -m "Update navigation"
   git push
   ```

**No template changes needed** - navigation is data-driven.

---

### 7.3 Update CSS Styles

**Standard CSS Update (No Above-the-Fold Changes):**
```bash
# 1. Edit CSS file
src/assets/styles/style-core.css  # Or style.css, core-brand.css, etc.

# 2. Rebuild CSS
npm run build:css

# 3. Commit and deploy
git add src/assets/styles/
git commit -m "Update styles: [description]"
git push
```

**Critical CSS Update (Above-the-Fold Changes):**
```bash
# 1. Update main CSS
Edit: src/assets/styles/style-core.css

# 2. Update ALL 3 critical CSS files
Edit: src/_data/critical-homepage.css
Edit: src/_data/critical-attorneys.css
Edit: src/_data/critical-practice-areas.css

# 3. Update page.njk layout if needed
Edit: src/_includes/layouts/page.njk (lines 5-69)

# 4. Rebuild both CSS and HTML
npm run build:css
npm run build:html:prod

# 5. Commit and deploy
git add src/assets/styles/ src/_data/critical-*.css src/_includes/layouts/page.njk
git commit -m "Update critical CSS: [description]"
git push
```

---

### 7.4 Update Firm Information

1. **Edit site data:**
   ```bash
   src/_data/site.json
   ```

2. **Change phone, email, address, etc.:**
   ```json
   {
     "phone": {
       "display": "(616) 555-1234",
       "link": "tel:+16165551234"
     },
     "email": "newemail@example.com"
   }
   ```

3. **Rebuild and deploy:**
   ```bash
   npm run build:html
   git add src/_data/site.json
   git commit -m "Update firm contact information"
   git push
   ```

**Changes propagate automatically** - all templates use `{{ site.* }}` variables.

---

### 7.5 Add JavaScript Functionality

1. **Edit existing or create new file:**
   ```bash
   src/assets/scripts/new-feature.js
   ```

2. **If new file, add to esbuild config:**
   ```javascript
   // esbuild.config.js
   entryPoints: {
     'new-feature': 'src/assets/scripts/new-feature.js'
   }
   ```

3. **Rebuild and deploy:**
   ```bash
   npm run build:js
   git add src/assets/scripts/ esbuild.config.js
   git commit -m "Add JavaScript feature: [description]"
   git push
   ```

4. **Add script tag to template:**
   ```njk
   <script src="/js/new-feature.js" defer></script>
   ```

---

### 7.6 Force Cloudflare Rebuild

**Method 1: Empty Commit**
```bash
git commit --allow-empty -m "Trigger Cloudflare rebuild"
git push
```

**Method 2: Touch Trigger File**
```bash
echo $(date) > .cloudflare-rebuild-trigger.txt
git add .cloudflare-rebuild-trigger.txt
git commit -m "Trigger rebuild"
git push
```

**Method 3: Cloudflare Dashboard**
- Go to Cloudflare Pages dashboard
- Navigate to Deployments
- Click "Retry deployment" button

---

### 7.7 Add a Blog Post

**Option 1: Markdown (Eleventy System - Recommended for Regular Blogging):**

1. **Create Markdown file:**
   ```bash
   src/blog/posts/YYYY-MM-DD-post-slug.md
   ```

2. **Add frontmatter:**
   ```markdown
   ---
   layout: layouts/blog-post.njk
   title: "Your Blog Post Title Here"
   description: "SEO meta description (150-160 chars)"
   date: 2025-10-06
   updated: 2025-10-15  # Optional
   author: "sorin"  # or "jonathan" or "firm"
   category: "legal"  # or "community", "michigan", "case"
   featuredImage: "/images/blog-post-image.avif"
   featuredImageAlt: "Descriptive alt text"
   tags:
     - criminal defense
     - DUI
     - Michigan law
   aboutPerson: "/sorin-panainte.html"  # Optional
   ---

   # Post Content

   Write your blog post content here using Markdown.

   ## Subheadings

   - Lists
   - **Bold text**
   - *Italic text*
   - [Links](https://example.com)
   ```

3. **Build and deploy:**
   ```bash
   npm run build:html
   git add src/blog/posts/YYYY-MM-DD-post-slug.md
   git commit -m "Add blog post: [Post Title]"
   git push
   ```

**Option 2: Manual HTML (blog.njk - For Occasional Posts):**

1. **Edit blog archive page:**
   ```bash
   src/pages/blog.njk
   ```

2. **Add new article to BlogPosting schema (line ~50-100):**
   ```njk
   <script type="application/ld+json">
   {
     "@context": "https://schema.org",
     "@type": "BlogPosting",
     "headline": "Post Title",
     "description": "Post description",
     "image": "{{ site.url }}/images/post-image.avif",
     "author": {
       "@type": "Person",
       "name": "Sorin Panainte",
       "url": "{{ site.url }}/sorin-panainte.html"
     },
     "datePublished": "2025-10-06",
     "articleSection": "Legal"
   }
   </script>
   ```

3. **Add article to page content:**
   ```html
   <article class="blog-post">
     <h2>Post Title</h2>
     <p class="blog-date">
       <time datetime="2025-10-06">October 6, 2025</time>
       <span class="blog-category blog-category-legal">Legal</span>
     </p>
     <p class="blog-byline">By Sorin Panainte</p>
     <img src="/images/post-image.avif" alt="Alt text" class="blog-image">
     <p>Post content here...</p>
   </article>
   ```

4. **Update OG image in frontmatter:**
   ```yaml
   ogImage: "https://www.sorinpyle.com/images/post-image.avif"
   ```

5. **Build and deploy:**
   ```bash
   npm run build:html
   git add src/pages/blog.njk
   git commit -m "Add blog post: [Post Title]"
   git push
   ```

**Blog Category Options:**
- **`community`** (green) - Pro bono work, events, volunteering
- **`legal`** (blue) - Attorney commentary, legal opinions
- **`michigan`** (purple) - New laws, court decisions
- **`case`** (orange) - High-profile case analysis

**Blog Authors (authors.json):**
- **`sorin`** - Sorin Panainte (Person schema)
- **`jonathan`** - Jonathan Pyle (Person schema)
- **`firm`** - Sorin & Pyle, Trial Lawyers (Organization schema)

---

## 8. TROUBLESHOOTING

### 8.1 Changes Not Visible on Live Site

**Checklist:**
1. ✅ **Did you commit and push?**
   ```bash
   git status  # Check if changes committed
   git push    # Push to GitHub
   ```

2. ✅ **Did Cloudflare build succeed?**
   - Go to Cloudflare Pages dashboard → View build log
   - Look for errors or failed build steps

3. ✅ **Clear browser cache**
   - Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
   - Or clear browser cache entirely

4. ✅ **Did you update BOTH main CSS and critical CSS?**
   - If changing above-the-fold styles, both must be updated
   - See Section 4.1 for dual CSS update workflow

---

### 8.2 Build Fails on Cloudflare

**Common Issues:**

1. **Syntax error in templates:**
   ```bash
   # Test build locally first
   npm run build:cloudflare
   # Fix any errors before pushing
   ```

2. **Missing dependencies:**
   - Check `package.json` matches local environment
   - Ensure all dependencies listed

3. **Missing files:**
   - Ensure all files committed to git
   - Check `.gitignore` isn't excluding needed files

4. **View build logs:**
   - Cloudflare Pages dashboard → Deployments → View logs
   - Look for specific error messages

---

### 8.3 CSS Not Loading

**Checklist:**
1. ✅ **Check CSS version query string:** `main.min.css?v=20251123`
2. ✅ **Check path in base.njk:** Correct `/css/main.min.css`?
3. ✅ **Check build succeeded:** `npm run build:css` no errors?
4. ✅ **Check file exists:** `dist/css/main.min.css` present after build?
5. ✅ **Check browser console:** F12 → Network tab for 404 errors

---

### 8.4 JavaScript Not Working

**Checklist:**
1. ✅ **Check browser console:** F12 → Console tab for errors
2. ✅ **Check file path:** `/js/main.min.js` correct in template?
3. ✅ **Check esbuild succeeded:** `npm run build:js` no errors?
4. ✅ **Check defer attribute:** `<script src="/js/main.min.js" defer></script>`
5. ✅ **Check event listeners:** Are tracking classes present (`track-phone-click`, etc.)?

---

### 8.5 Images Not Displaying

**Checklist:**
1. ✅ **Check image path:** `/images/image-name.avif` correct?
2. ✅ **Check file exists:** Is image in `images/` directory?
3. ✅ **Check passthrough copy:** `.eleventy.js` line 30 copies images
4. ✅ **Check responsive image shortcode:** Using correct syntax?
5. ✅ **Check browser console:** F12 → Network tab for 404 errors

---

### 8.6 Navigation Broken

**Checklist:**
1. ✅ **Check navigation.json syntax:** Valid JSON? Use JSON validator
2. ✅ **Check template loops:** `{% for item in navigation.main %}`
3. ✅ **Check file paths:** Relative paths correct for subfolder pages (`../`)?
4. ✅ **Check ARIA attributes:** `aria-expanded`, `aria-haspopup` set?
5. ✅ **Check JavaScript:** `main.js` loaded and dropdown listeners working?

---

## 9. OPTIMIZATION SUGGESTIONS FOR AI MAINTENANCE

### 9.1 Consolidate Critical CSS Management

**Current Issue:**
- Critical CSS spread across 4 locations (3 files + 1 inline in layout)
- Manual duplication required for every typography/layout change
- High risk of forgetting to update all 4 locations

**Recommendation:**
Create a build script to auto-extract critical CSS from compiled HTML using the `critical` package (already in dependencies):

```javascript
// scripts/extract-critical-css.mjs
import { generate } from 'critical';
import fs from 'fs';

const pages = [
  {
    input: 'dist/index.html',
    output: 'src/_data/critical-homepage.css',
    dimensions: [{ width: 375, height: 667 }, { width: 1920, height: 1080 }]
  },
  {
    input: 'dist/attorneys.html',
    output: 'src/_data/critical-attorneys.css',
    dimensions: [{ width: 375, height: 667 }, { width: 1920, height: 1080 }]
  },
  {
    input: 'dist/practice-areas.html',
    output: 'src/_data/critical-practice-areas.css',
    dimensions: [{ width: 375, height: 667 }, { width: 1920, height: 1080 }]
  }
];

for (const page of pages) {
  const { css } = await generate({
    inline: false,
    base: 'dist/',
    src: page.input.replace('dist/', ''),
    dimensions: page.dimensions,
    minify: true
  });

  fs.writeFileSync(page.output, css);
  console.log(`✓ Extracted critical CSS: ${page.output}`);
}
```

**Benefits:**
- Eliminates manual duplication
- Reduces human error
- Keeps critical CSS in sync automatically
- Single source of truth (main CSS files)

---

### 9.2 Document Missing Build Scripts

**Current Issue:**
- `process-images.mjs` and `extract-critical-css.mjs` are gitignored
- `npm run build:prod` fails due to missing scripts
- No templates or documentation to regenerate them

**Recommendation - Option A (Preferred):**
Un-gitignore scripts and commit them to repository:

```bash
# Remove from .gitignore
# Commit scripts
git add scripts/process-images.mjs scripts/extract-critical-css.mjs
git commit -m "Add image processing and critical CSS extraction scripts"
git push
```

**Recommendation - Option B:**
Create template versions in `scripts/TEMPLATES/`:

```javascript
// scripts/TEMPLATES/process-images.mjs.template
import sharp from 'sharp';
import fs from 'fs';

const images = fs.readdirSync('images/').filter(f =>
  f.endsWith('.jpg') || f.endsWith('.png')
);

const widths = [220, 400, 450, 800];
const formats = ['avif', 'webp', 'jpeg'];

// Process each image...
```

**Recommendation - Option C:**
Document expected behavior in this file (AI_CONTEXT.md):

```markdown
### Image Processing Script Expected Behavior
- Input: Images in `images/` directory (JPEG, PNG)
- Output: Multiple widths (220w, 400w, 450w, 800w)
- Formats: AVIF (primary), WebP (fallback), JPEG (legacy)
- Manifest: Updates `src/_data/images.json` with variant paths
- Sharp settings: Quality 85 for AVIF, 90 for WebP
```

**Benefits:**
- AI can regenerate missing scripts from templates/docs
- Prevents "build failed - script not found" confusion
- Makes full `npm run build:prod` functional

---

### 9.3 Add Eleventy Data Cascade Visualization

**Current Issue:**
- Navigation and site data flow is implicit, not documented
- Unclear where data comes from in templates
- Hard for AI to understand variable scope

**Recommendation:**
Add clear data cascade diagram to this file:

```markdown
## Eleventy Data Cascade Flow

```
GLOBAL DATA (src/_data/*.json)
  ↓
site.json
  → {{ site.title }}
  → {{ site.phone.display }}
  → {{ site.attorneys[0].name }}
  → Available in ALL templates
  ↓
navigation.json
  → {{ navigation.main[] }}
  → {{ navigation.footer.practiceAreas[] }}
  → Available in ALL templates
  ↓
images.json
  → Used internally by {% responsiveImage %} shortcode
  → Not directly accessible in templates
  ↓
TEMPLATE FRONTMATTER (---...---)
  → layout, title, description, permalink
  → criticalCSSFile, customData
  → Overrides global data
  → Available as {{ title }}, {{ description }}
  ↓
PAGE CONTENT ({% block content %})
  → Variables from global data and frontmatter
  → Nunjucks filters and shortcodes
  → Final rendered HTML
```
```

**Example Usage:**
```njk
{# Access global site data (available everywhere) #}
{{ site.title }}  → "Sorin & Pyle, PC"
{{ site.phone.display }}  → "(616) 227-3303"

{# Access frontmatter data (page-specific) #}
{{ title }}  → From frontmatter `title: "Page Title"`
{{ description }}  → From frontmatter `description: "..."`

{# Access navigation data (available everywhere) #}
{% for item in navigation.main %}
  {{ item.text }}  → "About", "Attorneys", etc.
{% endfor %}
```

**Benefits:**
- Clear mental model of data sources
- Reduces guesswork when adding new data fields
- Shows inheritance and precedence rules
- Easier for AI to understand variable scope

---

## 10. FILE NAMING CONVENTIONS

### 10.1 Template Files
- **Extension:** `.njk` (Nunjucks templates)
- **Style:** kebab-case (lowercase with hyphens)
- **Examples:** `dui-defense.njk`, `jonathan-pyle.njk`, `gvsu-student-defense.njk`

### 10.2 CSS Files
- **Source:** `core-brand.css`, `style-core.css`, `style.css`
- **Entry:** `main.css` (imports all other CSS)
- **Output:** `main.min.css` (in `dist/css/`)
- **Critical:** `critical-homepage.css` (in `src/_data/`)

### 10.3 JavaScript Files
- **Source:** `main.js`, `analytics.js`, `cookie-consent.js`
- **Output:** `main.min.js`, `analytics.js`, `cookie-consent.js` (in `dist/js/`)
- **Note:** esbuild minifies automatically, `.min.js` suffix only on main.js

### 10.4 Image Files
- **Original:** `attorney-name.avif`, `holland-michigan-lawyers.avif`
- **Responsive:** `attorney-name-220w.avif`, `attorney-name-400w.avif`
- **Style:** kebab-case, SEO-optimized (include location, service, name)
- **Example:** `sorin-panainte-criminal-defense-attorney-holland-mi.avif`

### 10.5 Data Files
- **Format:** JSON (`.json`)
- **Location:** `src/_data/`
- **Examples:** `site.json`, `navigation.json`, `images.json`
- **Exception:** Critical CSS stored as `.css` in `_data/` (unusual but intentional)

---

## 11. PERFORMANCE OPTIMIZATIONS

### 11.1 Critical CSS Strategy
- Inline above-the-fold CSS in `<head>` for instant render
- Defer main.min.css loading with `<link rel="preload">`
- Eliminates Flash of Unstyled Content (FOUC)
- Improves LCP (Largest Contentful Paint) Core Web Vital

### 11.2 Image Optimization
- AVIF format (30-50% smaller than WebP)
- Responsive images with srcset (220w, 400w, 450w, 800w)
- Lazy loading for below-the-fold images
- Eager loading for hero images (`loading="eager"`)

### 11.3 JavaScript Optimization
- Bundled and minified with esbuild
- Deferred loading (`<script defer>`) - non-blocking
- Tree shaking removes unused code
- IIFE format for browser compatibility

### 11.4 HTML Minification
- Remove comments and whitespace (production only)
- Minify inline CSS/JS
- Conservative collapse (preserve readability)
- Enabled via `NODE_ENV=production`

### 11.5 Caching Strategy
- **HTML:** No cache (`max-age=0, must-revalidate`)
- **CSS/JS/Images/Fonts:** 1 year cache (`max-age=31536000, immutable`)
- Cloudflare CDN edge caching globally
- Cache busting via query strings (`?v=20251123`)

---

## 12. SECURITY & COMPLIANCE

### 12.1 Security Headers
- **HSTS** - Force HTTPS for 1 year
- **CSP** - Content Security Policy (XSS protection)
- **X-Frame-Options** - Clickjacking protection
- **X-Content-Type-Options** - MIME sniffing protection
- **Referrer-Policy** - Privacy protection
- **COOP** - Cross-Origin-Opener-Policy (origin isolation)
- **Permissions-Policy** - Feature restrictions

### 12.2 Cookie Consent (GDPR/CCPA)
- Blocks Google Analytics until user accepts
- Stores consent in localStorage (version + timestamp)
- 1-second delay before banner appears
- Persistent across page visits

### 12.3 Accessibility (WCAG 2.1 Level AA)
- Semantic HTML structure
- ARIA attributes (`role`, `aria-label`, `aria-expanded`)
- Keyboard navigation support
- Skip links for screen readers
- Focus indicators on interactive elements
- Screen reader compatible navigation

### 12.4 Legal Disclaimers
- Attorney-client relationship disclaimer (all pages)
- Past results disclaimer (pages with case results)
- Privacy policy (linked from all pages)
- Accessibility statement (linked from all pages)

---

## APPENDIX: QUICK COMMAND REFERENCE

```bash
# Development
npm run dev              # Start dev server (localhost:8080)
npm run dev:watch        # Watch CSS/JS changes

# Build Individual Assets
npm run build:html       # Build HTML (dev mode)
npm run build:html:prod  # Build HTML (production with minification)
npm run build:css        # Build CSS with PostCSS
npm run build:js         # Build JavaScript with esbuild
npm run clean            # Remove dist/ directory

# Composite Builds
npm run build            # Full dev build
npm run build:cloudflare # Cloudflare deployment build (RECOMMENDED)
npm run build:prod       # Full production build (FAILS - missing scripts)

# Deployment
git add src/
git commit -m "Description"
git push                 # Auto-deploys to Cloudflare Pages
```

---

**END OF AI_CONTEXT.MD**

This document provides comprehensive context for AI agents working on the Sorin & Pyle Eleventy website. All critical systems, workflows, constraints, and gotchas are documented with examples and troubleshooting guidance.

For additional historical context and detailed implementation notes, refer to `CLAUDE.md` in the project root.
