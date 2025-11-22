# Maintenance Guide

## Overview

This guide covers ongoing maintenance, content updates, and operational procedures for the Sorin & Pyle law firm website.

---

## Content Updates

### Updating Page Content

**HTML Content Pages** (`src/pages/*.njk`):

1. Open the page file in text editor
2. Find the content section
3. Update text, headings, or HTML
4. Save file
5. Build and deploy:
   ```bash
   npm run build:prod
   # Deploy via Cloudflare Pages (automatic on git push)
   ```

**Example - Update Attorneys Page:**

```nunjucks
<!-- src/pages/attorneys.njk -->
---
layout: layouts/page.njk
title: "Criminal Defense Attorneys in Holland, MI"
---

<section class="section">
  <div class="container-large">
    <h1>Our Attorneys</h1>
    <p>Meet the experienced criminal defense attorneys...</p>
    <!-- Update bio content here -->
  </div>
</section>
```

### Adding New Attorneys

1. **Add photo to images/**:
   - Save as `attorney-name.jpg` or `.png`
   - High resolution (min 800px width)

2. **Process image**:
   ```bash
   npm run build:images
   ```

3. **Update attorneys page**:
   ```nunjucks
   <div class="attorney-card">
     {% responsiveImage "/images/attorney-name.avif",
                        "Attorney Name - Criminal Defense Lawyer",
                        "(min-width: 768px) 400px, 100vw" %}
     <h3>Attorney Name</h3>
     <p>Bio content...</p>
   </div>
   ```

4. **Create individual attorney page** (`src/pages/attorney-name.njk`):
   ```nunjucks
   ---
   layout: layouts/page.njk
   title: "Attorney Name | Criminal Defense Lawyer Holland MI"
   description: "..."
   permalink: /attorney-name.html
   ---

   <section class="section">
     <!-- Attorney profile content -->
   </section>
   ```

### Updating Contact Information

**Phone Number:**
1. Search project for current phone number
2. Replace in:
   - Header template (`src/_includes/partials/header.njk`)
   - Footer template (`src/_includes/partials/footer.njk`)
   - Contact page (`src/pages/contact.njk`)
   - Schema markup (all pages with LegalService schema)

**Office Address:**
1. Update in:
   - Footer template
   - Contact page
   - Schema markup (all pages)
   - Google Business Profile (external)

**Email Address:**
1. Update in:
   - Footer template
   - Contact page
   - mailto links across site

**Office Hours:**
1. Update in:
   - Footer template
   - Contact page
   - Schema markup (openingHoursSpecification)

### Adding Blog Posts

**Method 1: Manual HTML** (Current approach):

1. Open `blog.html`
2. Add new post section:
   ```html
   <article class="blog-post">
     <h2>Post Title</h2>
     <p class="blog-byline">
       <span class="blog-category blog-category-legal">Legal</span>
       By Sorin & Pyle, Trial Lawyers | November 22, 2025
     </p>
     <p>Post content...</p>
   </article>
   ```

3. Add schema markup:
   ```html
   <script type="application/ld+json">
   {
     "@context": "https://schema.org",
     "@type": "BlogPosting",
     "headline": "Post Title",
     "author": { "@type": "Organization", "name": "Sorin & Pyle, PC" },
     "datePublished": "2025-11-22",
     "description": "...",
     "image": "https://www.sorinpyle.com/images/post-image.jpg"
   }
   </script>
   ```

**Method 2: Markdown** (Future - requires Eleventy blog setup):

See BLOG_SYSTEM_GUIDE.md for Markdown-based blog implementation.

---

## Deployment Procedures

### Standard Deployment (Git Push)

1. **Test locally**:
   ```bash
   npm run build:prod
   cd dist
   python -m http.server 8000
   # Test at http://localhost:8000
   ```

2. **Commit changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. **Push to main branch**:
   ```bash
   git push origin main
   ```

4. **Automatic deployment**:
   - Cloudflare Pages detects push
   - Runs `npm run build:prod`
   - Deploys to production (~2-3 minutes)

5. **Verify deployment**:
   - Visit https://www.sorinpyle.com
   - Check updated content
   - Test navigation and functionality

### Emergency Hotfix

**For critical bugs (site down, broken functionality):**

1. **Identify issue**:
   - Check Cloudflare Pages build logs
   - Review browser console errors
   - Test locally to reproduce

2. **Fix locally**:
   ```bash
   # Fix the issue
   npm run build:prod
   # Test thoroughly
   ```

3. **Fast-track deployment**:
   ```bash
   git add .
   git commit -m "HOTFIX: Description"
   git push origin main
   ```

4. **Monitor deployment**:
   - Watch Cloudflare Pages dashboard
   - Verify fix deployed successfully
   - Test production site

5. **Rollback if needed**:
   - Cloudflare Pages > Deployments
   - Find previous working deployment
   - Click "Rollback to this deployment"

### Content-Only Updates

**For content changes without code changes:**

1. Edit page content in `src/pages/`
2. Run `npm run build:prod` locally (test build)
3. Commit and push
4. Automatic deployment to production

**No need to:**
- Run image processing (unless new images added)
- Update CSS/JS (unless styles/scripts changed)
- Rebuild critical CSS (unless layout changed)

---

## Scheduled Maintenance

### Weekly Tasks

**Monday:**
- [ ] Review Google Analytics (traffic, errors)
- [ ] Check Google Search Console (indexing issues)
- [ ] Review Cloudflare Analytics (threats, performance)
- [ ] Verify site uptime (should be 99.9%+)

**Friday:**
- [ ] Review and respond to contact form submissions
- [ ] Check for any browser console errors
- [ ] Verify all CTAs working (phone links, forms)

### Monthly Tasks

**First Monday of Month:**
- [ ] Run Lighthouse audit on key pages (homepage, attorneys, practice areas)
- [ ] Review Core Web Vitals (LCP < 2.5s, CLS < 0.1, FID < 100ms)
- [ ] Check for broken links (use online checker or Screaming Frog)
- [ ] Review and update meta descriptions if needed
- [ ] Update copyright year in footer (if new year)

**Third Monday of Month:**
- [ ] Review site security (securityheaders.com scan)
- [ ] Check for outdated npm dependencies (`npm outdated`)
- [ ] Review and update practice area content
- [ ] Verify schema markup valid (Google Rich Results Test)

### Quarterly Tasks

**Every 3 Months:**
- [ ] Update dependencies (`npm update`)
- [ ] Run full accessibility audit (axe DevTools, WAVE)
- [ ] Review and optimize images (check for unoptimized files)
- [ ] Update blog with firm news or legal updates
- [ ] Review and update attorney bios
- [ ] Backup website files and database (if applicable)
- [ ] Test contact form submission process
- [ ] Review and update privacy policy if laws changed

### Annual Tasks

**January:**
- [ ] Update copyright year in footer template
- [ ] Review and update all attorney credentials
- [ ] Conduct comprehensive SEO audit
- [ ] Review and update service area pages
- [ ] Plan content calendar for the year

**July:**
- [ ] Mid-year performance review (analytics, conversions)
- [ ] Update case results (if new wins)
- [ ] Review and refresh blog content
- [ ] Check for Google algorithm updates affecting site

---

## Monitoring & Analytics

### Google Analytics 4 (GA4)

**Access:** https://analytics.google.com

**Key Metrics to Monitor:**

**Traffic:**
- Users (unique visitors)
- Sessions (total visits)
- Page views
- Bounce rate (high bounce = poor UX)

**Acquisition:**
- Traffic sources (Organic, Direct, Referral, Social)
- Top landing pages
- Search keywords (via Search Console integration)

**Behavior:**
- Top pages (most visited)
- Average session duration
- Pages per session
- Exit pages (where users leave)

**Conversions:**
- Phone clicks (tracked via GA4 events)
- Contact form submissions
- CTA button clicks

**Core Web Vitals:**
- LCP (Largest Contentful Paint)
- FID (First Input Delay)
- CLS (Cumulative Layout Shift)

**Setting Up Alerts:**
1. GA4 > Admin > Property > Alerts
2. Create custom alert:
   - Traffic drops > 20% week-over-week
   - Conversion rate drops > 30%
   - Error rate increases > 5%

### Google Search Console

**Access:** https://search.google.com/search-console

**Weekly Reviews:**

**Performance Tab:**
- Total clicks (traffic from Google)
- Total impressions (search appearances)
- Average CTR (click-through rate)
- Average position (ranking)

**Coverage Tab:**
- Errors (pages not indexed)
- Warnings (partial indexing)
- Valid pages (successfully indexed)
- Excluded pages (intentionally not indexed)

**Enhancements Tab:**
- Mobile usability issues
- Core Web Vitals (LCP, FID, CLS)
- Structured data errors

**Submit New URLs:**
1. Search Console > URL Inspection
2. Enter new page URL
3. Click "Request Indexing"
4. Wait 1-7 days for indexing

### Cloudflare Analytics

**Access:** Cloudflare Dashboard > Analytics & Logs

**Monitor:**
- **Web Analytics:** Traffic, page views, top pages
- **Performance:** Cache hit rate, bandwidth saved
- **Security:** Threats blocked, security level
- **Bots:** Good bots (Google) vs bad bots

**Optimize:**
- Review cache hit rate (target: >90%)
- Identify slow-loading pages
- Monitor bandwidth usage
- Check threat activity

---

## Image Management

### Adding New Images

1. **Prepare image**:
   - Save in high resolution (min 1920px width for full-width images)
   - Use descriptive filename: `attorney-name-portrait.jpg`
   - Optimize with TinyPNG or similar (optional, Sharp will re-optimize)

2. **Add to images/ directory**:
   ```bash
   cp ~/Downloads/attorney-photo.jpg images/
   ```

3. **Process responsive variants**:
   ```bash
   npm run build:images
   ```

4. **Verify manifest updated**:
   ```bash
   cat src/_data/images.json | grep "attorney-photo"
   ```

5. **Use in templates**:
   ```nunjucks
   {% responsiveImage "/images/attorney-photo.jpg",
                      "Attorney Name - Criminal Defense Lawyer",
                      "(min-width: 768px) 400px, 100vw" %}
   ```

### Replacing Existing Images

1. **Delete old image**:
   ```bash
   rm images/old-photo.jpg
   ```

2. **Add new image** (same filename for easy replacement):
   ```bash
   cp ~/Downloads/new-photo.jpg images/old-photo.jpg
   ```

3. **Regenerate responsive variants**:
   ```bash
   npm run build:images
   ```

4. **Rebuild site**:
   ```bash
   npm run build:prod
   ```

### Image Optimization Best Practices

**File Formats:**
- **AVIF**: Automatically generated for modern browsers
- **WebP**: Automatically generated for older modern browsers
- **JPEG**: Use for photos (fallback format)
- **PNG**: Use for graphics with transparency
- **SVG**: Use for logos, icons (vector graphics)

**File Sizes:**
- Original source: < 5MB
- Displayed size: ~100-300KB after processing
- Hero images: Prioritize quality (higher AVIF quality)

**Alt Text:**
- Descriptive: "Attorney John Doe - Criminal Defense Lawyer Holland MI"
- Includes keywords naturally
- Helps accessibility and SEO

---

## SEO Maintenance

### Updating Meta Tags

**Title Tags** (60 characters max):

```nunjucks
---
title: "Primary Keyword | Secondary Keyword | Firm Name"
---
```

**Meta Descriptions** (155-160 characters):

```nunjucks
---
description: "Clear, compelling description with primary keyword and call-to-action. Include phone number."
---
```

**Open Graph Tags** (Social sharing):

```html
<meta property="og:title" content="Page Title">
<meta property="og:description" content="...">
<meta property="og:image" content="https://www.sorinpyle.com/images/og-image.jpg">
<meta property="og:url" content="https://www.sorinpyle.com/page.html">
```

### Schema Markup Updates

**When to update:**
- Office address changes
- Phone number changes
- Office hours change
- New attorney added
- Services change

**Where to find:**
All pages with LegalService schema (typically in `<script type="application/ld+json">` tags)

**Validation:**
1. Update schema markup
2. Test with Google Rich Results Test: https://search.google.com/test/rich-results
3. Fix any errors
4. Deploy to production

### Sitemap Updates

**Automatic Updates:**
Eleventy automatically includes all pages in sitemap (via configuration)

**Manual sitemap.xml Updates:**
1. Add new page to sitemap:
   ```xml
   <url>
     <loc>https://www.sorinpyle.com/new-page.html</loc>
     <lastmod>2025-11-22</lastmod>
     <priority>0.80</priority>
   </url>
   ```

2. Rebuild and deploy
3. Ping Google Search Console:
   - Search Console > Sitemaps
   - Enter `sitemap.xml`
   - Click "Submit"

---

## Security Maintenance

### SSL/HTTPS Certificate

**Automatic Renewal:**
Cloudflare handles SSL certificate renewal automatically.

**Verification:**
1. Visit https://www.sorinpyle.com
2. Click padlock icon in address bar
3. Verify "Certificate valid" message
4. Check expiration date (should renew 30 days before expiry)

### Security Headers

**Review Quarterly:**
1. Visit https://securityheaders.com/
2. Enter `https://www.sorinpyle.com`
3. Review grade (target: A or A+)
4. Fix any missing headers

**Update headers** in .htaccess (if needed):
```apache
# Example security headers
Header set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
Header set Content-Security-Policy "default-src 'self'; ..."
```

### Dependency Security Updates

**Check for vulnerabilities:**
```bash
npm audit
```

**Fix vulnerabilities:**
```bash
npm audit fix
```

**Manual update if auto-fix fails:**
```bash
npm install package-name@latest --save-dev
```

**Test after updates:**
```bash
npm run build:prod
# Test thoroughly before deploying
```

---

## Backup Procedures

### Code Backup

**Primary Backup:** Git repository (GitHub)
- All code versioned and backed up
- Can restore any previous version
- Accessible from anywhere

**Local Backup:**
```bash
# Create timestamped backup
tar -czf sorinpyle-backup-$(date +%Y%m%d).tar.gz \
  --exclude=node_modules \
  --exclude=dist \
  .
```

**Cloud Backup:**
- GitHub repository (automatic)
- Optional: Google Drive or Dropbox for extra redundancy

### Content Backup

**Automated:**
Cloudflare Pages maintains deployment history (50 most recent)

**Manual Snapshot:**
1. Download dist/ directory:
   ```bash
   zip -r dist-backup-$(date +%Y%m%d).zip dist/
   ```

2. Store in secure location (Google Drive, Dropbox)

### Database Backup (if applicable)

**Note:** Current static site has no database

**If you add a database (contact forms, user accounts):**
- Set up automatic daily backups
- Test restore procedure quarterly
- Store encrypted backups offsite

---

## Troubleshooting Common Issues

### Site Not Loading

**Check:**
1. Cloudflare Pages status (dashboard)
2. DNS settings (Cloudflare DNS tab)
3. SSL certificate status
4. Recent deployments for errors

**Fix:**
1. Rollback to previous deployment if recent change caused issue
2. Check Cloudflare status page: https://www.cloudflarestatus.com/
3. Contact Cloudflare support if hosting issue

### Forms Not Working

**Check:**
1. Form action URL correct
2. Required fields marked properly
3. JavaScript errors in browser console
4. Email configuration (if using server-side processing)

**Fix:**
1. Test form locally
2. Check network tab in DevTools
3. Verify form submission endpoint
4. Check spam folder for test submissions

### Images Not Displaying

**Check:**
1. Image file exists in images/ directory
2. Filename matches reference in HTML
3. File extension correct (.avif, .webp, .jpg)
4. Responsive image manifest includes image

**Fix:**
```bash
# Regenerate responsive images
npm run build:images

# Rebuild site
npm run build:prod

# Check dist/images/ for generated files
```

### Slow Page Load

**Diagnose:**
1. Run Lighthouse audit
2. Check Network tab in DevTools
3. Identify slow-loading resources

**Fix:**
1. Optimize images (reduce size, increase compression)
2. Review and minimize third-party scripts
3. Check Cloudflare cache hit rate
4. Consider adding CDN for heavy assets

---

## Contact & Support

### Internal Resources

- **Build System Guide:** BUILD_SYSTEM_GUIDE.md
- **Testing Guide:** TESTING.md
- **Deployment Guide:** CLOUDFLARE_DEPLOYMENT.md
- **Project Documentation:** CLAUDE.md (historical record)

### External Resources

- **Eleventy Docs:** https://www.11ty.dev/docs/
- **Nunjucks Docs:** https://mozilla.github.io/nunjucks/
- **PostCSS:** https://postcss.org/
- **Sharp:** https://sharp.pixelplumbing.com/
- **Cloudflare Pages:** https://developers.cloudflare.com/pages/

### Getting Help

**Eleventy Issues:**
- GitHub Issues: https://github.com/11ty/eleventy/issues
- Discord: https://www.11ty.dev/blog/discord/

**Cloudflare Pages Issues:**
- Community Forum: https://community.cloudflare.com/
- Support Ticket: Cloudflare Dashboard > Support

**General Web Development:**
- Stack Overflow: https://stackoverflow.com/
- MDN Web Docs: https://developer.mozilla.org/

---

## Change Log Template

When making significant updates, document changes:

```markdown
## [Date] - [Change Type]

### Changed
- Updated attorney bio on attorneys.html
- Added new practice area page: family-law.html

### Fixed
- Fixed broken link on contact page
- Corrected phone number in footer

### Added
- New blog post: "Understanding DUI Laws in Michigan"
- Added schema markup to location pages

### Removed
- Removed outdated case results
- Deleted unused images from images/ directory
```

---

**Last Updated:** November 22, 2025
**Maintainer:** Development Team
**Review Cycle:** Quarterly
