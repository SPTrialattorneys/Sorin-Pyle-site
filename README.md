# Sorin & Pyle Law Firm Website

Professional criminal defense law firm website built with Eleventy static site generator.

## Project Overview

**Site:** https://www.sorinpyle.com
**Firm:** Sorin & Pyle, PC - Criminal Defense Attorneys
**Location:** Holland, Michigan (serving West Michigan)
**Build System:** Eleventy 3.1.2 + PostCSS + esbuild + Sharp

---

## Quick Start

### Prerequisites
- Node.js 22+ (https://nodejs.org/)
- npm (included with Node.js)
- Git (for version control)

### Installation

```bash
# Clone repository
git clone https://github.com/SPTrialattorneys/Sorin-Pyle-site.git
cd sorin-pyle-site-html

# Install dependencies
npm install

# Start development server
npm start
# Server runs at http://localhost:8080
```

### Development

```bash
# Start dev server with live reload
npm start

# Build for production
npm run build:prod

# Run individual build steps
npm run build:images   # Process responsive images
npm run build:css      # Bundle and minify CSS
npm run build:js       # Bundle and minify JavaScript
npm run build:html     # Build HTML pages
```

---

## Project Structure

```
sorin-pyle-site-html/
├── src/                    # Source files
│   ├── _data/             # Data files & critical CSS
│   ├── _includes/         # Templates & partials
│   │   ├── layouts/       # Base templates
│   │   └── partials/      # Reusable components
│   ├── assets/            # Source assets
│   │   ├── styles/        # CSS source files
│   │   └── scripts/       # JavaScript source files
│   ├── pages/             # Page content (Nunjucks)
│   └── static/            # Static files (copied as-is)
├── dist/                   # Build output (generated)
├── images/                 # Source images
├── fonts/                  # Web fonts
├── .eleventy.js           # Eleventy configuration
├── postcss.config.js      # CSS build configuration
├── esbuild.config.js      # JavaScript build configuration
├── process-images.mjs     # Image processing script
└── package.json           # Dependencies & scripts
```

---

## Technology Stack

### Core Technologies
- **Eleventy 3.1.2** - Static site generator
- **Nunjucks** - Template engine
- **PostCSS** - CSS processing and optimization
- **esbuild** - JavaScript bundling
- **Sharp** - Responsive image processing
- **Critical** - Critical CSS extraction

### Build Features
- ✅ HTML minification (production)
- ✅ CSS bundling and minification (63% reduction)
- ✅ Critical CSS inlining for faster FCP
- ✅ JavaScript bundling and tree shaking
- ✅ Responsive images (WebP, AVIF, multiple sizes)
- ✅ Lazy loading images
- ✅ Source maps for debugging

### Performance Optimizations
- **Lighthouse Scores (Mobile):** 90-95 Performance, 95+ Accessibility, 95+ Best Practices, 95+ SEO
- **Core Web Vitals:** LCP < 2.5s, FID < 100ms, CLS < 0.1
- **Image Optimization:** AVIF format (~50-70% smaller than JPEG)
- **Critical CSS:** Above-the-fold styles inlined in HTML
- **Deferred CSS:** Full CSS loaded asynchronously

---

## Documentation

### Build & Development
- **[BUILD_SYSTEM_GUIDE.md](BUILD_SYSTEM_GUIDE.md)** - Complete build system documentation
  - Directory structure
  - Build pipeline
  - Configuration files
  - Template system
  - Development workflow
  - Troubleshooting

### Deployment
- **[CLOUDFLARE_DEPLOYMENT.md](CLOUDFLARE_DEPLOYMENT.md)** - Deployment guide
  - Cloudflare Pages configuration
  - Build commands
  - Environment variables
  - Custom domain setup
  - Rollback procedures

### Testing
- **[TESTING.md](TESTING.md)** - Performance testing & QA
  - Lighthouse audits
  - Browser testing
  - Accessibility testing (WCAG 2.1 Level AA)
  - SEO testing
  - Security testing
  - Continuous monitoring

### Maintenance
- **[MAINTENANCE.md](MAINTENANCE.md)** - Ongoing maintenance
  - Content updates
  - Deployment procedures
  - Scheduled maintenance tasks
  - Image management
  - SEO maintenance
  - Security maintenance
  - Backup procedures

---

## Build Scripts

### Development
```bash
npm start              # Start dev server (http://localhost:8080)
npm run dev            # Same as start
npm run dev:watch      # Dev server + JS watch mode
```

### Building
```bash
npm run build          # Development build (no minification)
npm run build:prod     # Production build (full optimization)
```

### Individual Steps
```bash
npm run clean          # Remove dist/ directory
npm run build:images   # Process responsive images with Sharp
npm run build:css      # Bundle and minify CSS with PostCSS
npm run build:js       # Bundle and minify JavaScript with esbuild
npm run build:html     # Build HTML pages with Eleventy
npm run build:critical # Extract critical CSS from built pages
```

---

## Performance Features

### Responsive Images

All images processed into multiple formats and sizes:

**Formats Generated:**
- AVIF (most efficient, ~50-70% smaller than JPEG)
- WebP (widely supported, ~30-40% smaller than JPEG)
- Original format (JPEG/PNG fallback)

**Sizes Generated:**
- 320px, 640px, 768px, 1024px, 1280px, 1920px

**Usage in Templates:**
```nunjucks
{% responsiveImage "/images/attorney.avif",
                   "Attorney Name - Criminal Defense Lawyer",
                   "(min-width: 768px) 400px, 100vw",
                   "lazy" %}
```

**Output:**
```html
<picture>
  <source type="image/avif" srcset="..." sizes="...">
  <source type="image/webp" srcset="..." sizes="...">
  <img src="..." alt="..." srcset="..." sizes="..." loading="lazy">
</picture>
```

### Critical CSS

Above-the-fold CSS extracted and inlined for faster First Contentful Paint:

**Pages with Critical CSS:**
- Homepage (14.06 KB)
- Attorneys (11.21 KB)
- Practice Areas (10.23 KB)

**How it Works:**
1. Build HTML pages
2. Extract critical CSS from rendered HTML
3. Rebuild HTML with critical CSS inlined in `<head>`
4. Defer full CSS loading

**Impact:**
- Faster FCP (First Contentful Paint)
- Better LCP (Largest Contentful Paint)
- Improved Lighthouse performance score

### HTML Minification

Production builds minify HTML:
- Remove comments
- Collapse whitespace
- Minify inline CSS
- Minify inline JavaScript
- ~10-15% file size reduction

**Enable/Disable:**
Controlled by `NODE_ENV` environment variable:
- `npm run build` - No minification
- `npm run build:prod` - Minification enabled

---

## Site Features

### Pages (53 Total)

**Main Pages:**
- Homepage
- Attorneys
- Practice Areas
- Locations
- Contact
- Privacy Policy
- Accessibility Statement

**Attorney Profiles:**
- Sorin Panainte
- Jonathan Pyle

**Practice Area Pages:**
- DUI/OWI Defense
- Domestic Violence Defense
- Record Expungement
- Driver License Restoration
- CDL OWI Defense
- First Offense OWI
- Repeat Offense OWI
- Super Drunk / High BAC

**Location Pages (8 Counties):**
- Ottawa County
- Kent County
- Allegan County
- Kalamazoo County
- Muskegon County
- Van Buren County
- Newaygo County
- Other Michigan Counties

**University Student Defense (7 Pages):**
- GVSU Student Defense
- GRCC Student Defense
- Hope College Student Defense
- Calvin University Student Defense
- Davenport Student Defense
- Ferris Student Defense
- WMU Student Defense

**City Pages (14 Cities):**
- Holland, Grand Rapids, Grand Haven, Allendale
- Hudsonville, Zeeland, Wyoming, Kentwood
- Jenison, Grandville, Walker, Saugatuck
- South Haven

**Resource Pages:**
- FAQ
- Know Your Rights
- Blog
- Community Resources

**Utility Pages:**
- 404 Error
- 500 Error

### SEO Features

**Schema Markup:**
- LegalService schema on main pages
- Person schema for attorneys
- FAQPage schema on FAQ page
- BlogPosting schema on blog posts
- BreadcrumbList schema on all pages

**Meta Tags:**
- Optimized title tags (< 60 characters)
- Compelling meta descriptions (155-160 characters)
- Open Graph tags for social sharing
- Twitter Card tags
- Canonical URLs

**Technical SEO:**
- XML sitemap (sitemap.xml)
- robots.txt
- Structured URLs
- Semantic HTML
- WCAG 2.1 Level AA accessibility

### Accessibility

**WCAG 2.1 Level AA Compliant:**
- Keyboard navigation
- Screen reader compatible
- ARIA attributes
- Focus indicators
- Color contrast (4.5:1+ ratio)
- Semantic HTML
- Skip to main content link

**Testing:**
- axe DevTools (Chrome extension)
- WAVE (Web Accessibility Evaluation Tool)
- Lighthouse accessibility audits
- Manual keyboard testing
- Screen reader testing (NVDA, JAWS, VoiceOver)

---

## Deployment

### Cloudflare Pages (Production)

**Automatic Deployment:**
1. Push code to GitHub main branch
2. Cloudflare Pages detects push
3. Runs `npm run build:prod`
4. Deploys to production (~2-3 minutes)

**Build Settings:**
- **Framework:** None (Custom Configuration)
- **Build command:** `npm run build:prod`
- **Build output:** `dist`
- **Node version:** 22

**Custom Domain:**
- Primary: https://www.sorinpyle.com
- Redirect: sorinpyle.com → www.sorinpyle.com

### Local Testing

```bash
# Build production version
npm run build:prod

# Serve locally
cd dist
python -m http.server 9000
# OR
npx serve -p 9000

# Open http://localhost:9000
```

---

## Browser Support

**Target Browsers:**
- Chrome 80+
- Firefox 78+
- Safari 14+
- Edge 88+ (Chromium-based)
- iOS Safari 12+

**Graceful Degradation:**
- AVIF support (modern browsers)
- WebP fallback (older modern browsers)
- JPEG/PNG fallback (all browsers)

---

## Performance Benchmarks

### Production Build Output

**HTML:**
- 53 pages generated
- Build time: ~0.40 seconds
- Minified in production

**CSS:**
- Source: ~176KB
- Bundled & minified: 65KB (63% reduction)
- Critical CSS: 14KB (homepage)

**JavaScript:**
- 5 bundles: ~10KB total
- main.min.js: 3.9KB
- cookie-consent.js: 2.8KB
- tracking.js: 1KB
- Build time: ~11ms

**Images:**
- 9 source images
- 129 responsive variants generated
- AVIF, WebP, original formats
- 6 sizes per image

### Lighthouse Scores

**Desktop (Expected):**
- Performance: 95-100
- Accessibility: 95-100
- Best Practices: 95-100
- SEO: 95-100

**Mobile (Expected):**
- Performance: 90-95
- Accessibility: 95-100
- Best Practices: 95-100
- SEO: 95-100

### Core Web Vitals

**Targets:**
- LCP (Largest Contentful Paint): < 2.5s ✅
- FID (First Input Delay): < 100ms ✅
- CLS (Cumulative Layout Shift): < 0.1 ✅
- FCP (First Contentful Paint): < 1.8s ✅
- TTFB (Time to First Byte): < 800ms ✅

---

## Contributing

### Code Style

**HTML/Nunjucks:**
- 2-space indentation
- Semantic HTML5 elements
- ARIA attributes where needed
- Descriptive class names

**CSS:**
- CSS custom properties for colors/spacing
- Mobile-first responsive design
- BEM-like naming convention
- PostCSS for vendor prefixes

**JavaScript:**
- ES2020 syntax
- IIFE format (browser compatibility)
- Event delegation patterns
- No jQuery dependency

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Description of changes"

# Test locally
npm run build:prod

# Push to GitHub
git push origin feature/new-feature

# Create pull request
# Merge after review
```

---

## License

**Proprietary** - © 2025 Sorin & Pyle, PC. All Rights Reserved.

This website and its contents are proprietary to Sorin & Pyle, PC. Unauthorized copying, modification, distribution, or use is prohibited.

---

## Contact

**Sorin & Pyle, PC**
217 E 24th St Ste 107
Holland, MI 49423

**Phone:** (616) 227-3303
**Email:** justice@callsbp.com
**Web:** https://www.sorinpyle.com

---

## Support & Resources

### Internal Documentation
- [BUILD_SYSTEM_GUIDE.md](BUILD_SYSTEM_GUIDE.md)
- [CLOUDFLARE_DEPLOYMENT.md](CLOUDFLARE_DEPLOYMENT.md)
- [TESTING.md](TESTING.md)
- [MAINTENANCE.md](MAINTENANCE.md)

### External Resources
- [Eleventy Documentation](https://www.11ty.dev/docs/)
- [Nunjucks Documentation](https://mozilla.github.io/nunjucks/)
- [PostCSS](https://postcss.org/)
- [Sharp](https://sharp.pixelplumbing.com/)
- [Cloudflare Pages](https://developers.cloudflare.com/pages/)

---

**Last Updated:** November 22, 2025
**Version:** 1.0
**Eleventy:** 3.1.2
**Node:** 22.18.0
