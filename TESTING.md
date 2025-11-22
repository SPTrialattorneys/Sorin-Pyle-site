# Performance Testing & Quality Assurance

## Lighthouse Audits

### Running Lighthouse Audits

**Prerequisites:**
- Google Chrome or Chromium browser
- Local or deployed site

**Method 1: Chrome DevTools (Recommended)**

1. Build the production site:
   ```bash
   npm run build:prod
   ```

2. Serve the built site locally:
   ```bash
   cd dist
   python -m http.server 9000
   ```
   OR
   ```bash
   npx serve dist -p 9000
   ```

3. Open http://localhost:9000 in Chrome
4. Open DevTools (F12 or Ctrl+Shift+I)
5. Go to "Lighthouse" tab
6. Select categories:
   - ✅ Performance
   - ✅ Accessibility
   - ✅ Best Practices
   - ✅ SEO
7. Select "Desktop" or "Mobile" mode
8. Click "Analyze page load"

**Method 2: Lighthouse CI (Automated)**

Install Lighthouse CI:
```bash
npm install --save-dev @lhci/cli
```

Run audit:
```bash
npx lhci autorun --collect.url=http://localhost:9000
```

### Performance Goals

Target Lighthouse scores (Mobile):

| Metric | Target | Description |
|--------|--------|-------------|
| **Performance** | 90+ | Overall speed and optimization |
| **Accessibility** | 95+ | WCAG compliance, screen readers |
| **Best Practices** | 95+ | Security, modern standards |
| **SEO** | 95+ | Search engine optimization |

### Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor |
|--------|------|------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s - 4.0s | > 4.0s |
| **FID** (First Input Delay) | ≤ 100ms | 100ms - 300ms | > 300ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |
| **FCP** (First Contentful Paint) | ≤ 1.8s | 1.8s - 3.0s | > 3.0s |
| **TTFB** (Time to First Byte) | ≤ 800ms | 800ms - 1800ms | > 1800ms |

### Expected Results

With current optimizations (critical CSS, responsive images, minification), expect:

**Desktop:**
- Performance: 95-100
- Accessibility: 95-100
- Best Practices: 95-100
- SEO: 95-100

**Mobile:**
- Performance: 90-95
- Accessibility: 95-100
- Best Practices: 95-100
- SEO: 95-100

---

## Browser Testing

### Supported Browsers

Test on the following browsers:

- ✅ Chrome 80+ (Primary target)
- ✅ Firefox 78+ (Secondary target)
- ✅ Safari 14+ (macOS/iOS)
- ✅ Edge 88+ (Chromium-based)

### Browser Testing Checklist

For each browser:

**Navigation:**
- [ ] Desktop navigation menu
- [ ] Mobile hamburger menu
- [ ] Client Resources dropdown
- [ ] Skip to main content link
- [ ] Footer links

**Forms:**
- [ ] Contact form validation
- [ ] Cookie consent banner
- [ ] Form submission (if implemented)

**Images:**
- [ ] Responsive images load correctly
- [ ] AVIF format supported (Chrome, Edge, Firefox 93+)
- [ ] WebP fallback works
- [ ] JPEG/PNG fallback works (older browsers)
- [ ] Lazy loading functions properly

**Interactivity:**
- [ ] Dropdown menus toggle on click
- [ ] Mobile menu opens/closes
- [ ] Scroll animations trigger
- [ ] Phone links dial correctly on mobile
- [ ] Email links open email client

**Accessibility:**
- [ ] Keyboard navigation (Tab, Enter, Esc)
- [ ] Screen reader compatible (NVDA, JAWS, VoiceOver)
- [ ] Focus indicators visible
- [ ] ARIA attributes correct

---

## Accessibility Testing

### WCAG 2.1 Level AA Compliance

**Automated Testing Tools:**

1. **axe DevTools** (Chrome Extension)
   - Install from Chrome Web Store
   - Run scan on each key page
   - Fix all Critical and Serious issues

2. **WAVE** (Web Accessibility Evaluation Tool)
   - Visit https://wave.webaim.org/
   - Enter page URL
   - Review errors, alerts, and features

3. **Lighthouse Accessibility Audit**
   - Included in standard Lighthouse run
   - Target: 95+ score

**Manual Testing:**

1. **Keyboard Navigation**
   - Tab through entire page
   - Verify all interactive elements reachable
   - Confirm focus indicators visible
   - Test skip link functionality

2. **Screen Reader Testing**
   - **Windows:** NVDA (free) or JAWS
   - **macOS:** VoiceOver (built-in)
   - **iOS:** VoiceOver (Settings > Accessibility)
   - **Android:** TalkBack (Settings > Accessibility)

3. **Color Contrast**
   - Use WebAIM Contrast Checker
   - Verify 4.5:1 ratio for normal text
   - Verify 3:1 ratio for large text (18pt+)

4. **Zoom Testing**
   - Test at 200% zoom
   - Confirm no horizontal scrolling
   - Verify content remains readable

---

## Performance Benchmarking

### Page Load Metrics

Test on representative pages:

**Key Pages to Test:**
- Homepage (`/index.html`)
- Attorneys (`/attorneys.html`)
- Practice Areas (`/practice-areas.html`)
- Contact (`/contact.html`)
- Location Page (`/locations/ottawa-county.html`)

**Metrics to Track:**

```bash
# Use Chrome DevTools Performance tab
1. Open DevTools > Performance
2. Click "Reload" button
3. Review metrics:
   - DOMContentLoaded: Target < 1.5s
   - Load: Target < 3s
   - First Paint: Target < 1s
   - FCP: Target < 1.8s
   - LCP: Target < 2.5s
```

### Network Performance

**Test Conditions:**
- Fast 3G (simulated mobile)
- Slow 4G (realistic mobile)
- Wi-Fi (desktop)

**Throttling in Chrome DevTools:**
1. Open DevTools > Network tab
2. Select throttling profile dropdown
3. Choose "Fast 3G" or "Slow 4G"
4. Reload page and monitor:
   - Total page size (Target: < 1.5MB)
   - Number of requests (Target: < 50)
   - Time to interactive (Target: < 5s on 3G)

---

## Cross-Device Testing

### Responsive Design Breakpoints

Test at these viewport widths:

| Device | Width | Height | Notes |
|--------|-------|--------|-------|
| iPhone SE | 375px | 667px | Small mobile |
| iPhone 12/13 | 390px | 844px | Standard mobile |
| iPhone 14 Pro Max | 430px | 932px | Large mobile |
| iPad Mini | 768px | 1024px | Tablet portrait |
| iPad Pro | 1024px | 1366px | Tablet landscape |
| Desktop | 1280px | 720px | Small desktop |
| Desktop HD | 1920px | 1080px | Standard desktop |

**Chrome DevTools Device Mode:**
1. Open DevTools (F12)
2. Click "Toggle device toolbar" (Ctrl+Shift+M)
3. Select device from dropdown or enter custom dimensions

### Touch Target Testing

Verify all interactive elements meet minimum touch target size:
- Minimum: 44px × 44px (iOS HIG, Material Design)
- Ideal: 48px × 48px

**Elements to check:**
- Navigation links
- Buttons (primary, secondary)
- Form fields
- Dropdown toggles
- Mobile menu items

---

## SEO Testing

### Technical SEO Checklist

**Meta Tags:**
- [ ] Title tags < 60 characters
- [ ] Meta descriptions 150-160 characters
- [ ] Canonical URLs set correctly
- [ ] Open Graph tags for social sharing
- [ ] Twitter Card tags
- [ ] Viewport meta tag present

**Structured Data:**
- [ ] LegalService schema markup valid
- [ ] Person schema for attorneys
- [ ] BreadcrumbList schema
- [ ] FAQPage schema (if applicable)

**Validation Tools:**
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/
- Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/

**XML Sitemap:**
- [ ] sitemap.xml generated and accessible
- [ ] All pages included
- [ ] Priority and lastmod set correctly
- [ ] Submitted to Google Search Console

**Robots.txt:**
- [ ] robots.txt exists and accessible
- [ ] Allows all necessary pages
- [ ] Links to sitemap.xml

---

## Security Testing

### HTTPS & Security Headers

**Using securityheaders.com:**
1. Visit https://securityheaders.com/
2. Enter deployed site URL
3. Review grade and recommendations

**Expected Headers:**
- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)
- X-Content-Type-Options: nosniff
- X-Frame-Options: SAMEORIGIN
- Referrer-Policy: strict-origin-when-cross-origin

### Content Security Policy (CSP)

Test CSP implementation:
1. Open DevTools Console
2. Look for CSP violation errors
3. Verify no `unsafe-inline` or `unsafe-eval`
4. Confirm all scripts/styles whitelisted

---

## Regression Testing

### Visual Regression Testing

**Manual Visual QA:**
- [ ] Homepage hero section layout
- [ ] Navigation alignment (desktop/mobile)
- [ ] Attorney cards layout
- [ ] Practice areas grid
- [ ] Footer columns alignment
- [ ] Form styling

**Screenshot Comparison:**
1. Before updates: Save screenshots
2. After updates: Compare new screenshots
3. Flag any unintended visual changes

### Functional Testing

**Core User Flows:**
1. **Find attorney information:**
   - Homepage → Attorneys page → Individual profile

2. **Contact firm:**
   - Any page → Contact link → Contact page → Form

3. **Learn about services:**
   - Homepage → Practice Areas → Individual service page

4. **Find location information:**
   - Homepage → Locations → County page

---

## Continuous Monitoring

### Production Monitoring

**Tools:**
- **Cloudflare Analytics:** Traffic, performance, threats
- **Google Analytics 4:** User behavior, Core Web Vitals
- **Google Search Console:** Search performance, indexing, errors
- **Uptime monitoring:** Pingdom, UptimeRobot, or StatusCake

**Weekly Checks:**
- [ ] Review GA4 Core Web Vitals report
- [ ] Check Google Search Console for errors
- [ ] Verify site uptime (target: 99.9%)
- [ ] Review Cloudflare analytics for anomalies

**Monthly Audits:**
- [ ] Run Lighthouse audit on key pages
- [ ] Review and update outdated content
- [ ] Check for broken links
- [ ] Verify forms still functional
- [ ] Review accessibility compliance

---

## Testing Automation

### Lighthouse CI Integration

Create `.lighthouserc.js`:

```javascript
module.exports = {
  ci: {
    collect: {
      startServerCommand: 'npm run build:prod && cd dist && python -m http.server 9000',
      url: ['http://localhost:9000'],
      numberOfRuns: 3
    },
    assert: {
      preset: 'lighthouse:recommended',
      assertions: {
        'categories:performance': ['error', {minScore: 0.9}],
        'categories:accessibility': ['error', {minScore: 0.95}],
        'categories:best-practices': ['error', {minScore: 0.95}],
        'categories:seo': ['error', {minScore: 0.95}]
      }
    },
    upload: {
      target: 'temporary-public-storage'
    }
  }
};
```

Run automated tests:
```bash
npx lhci autorun
```

---

## Troubleshooting Common Issues

### Performance Issues

**Problem:** Low Lighthouse performance score

**Solutions:**
1. Verify critical CSS extracted and inlined
2. Check for render-blocking resources
3. Optimize images (WebP, AVIF formats)
4. Review JavaScript bundle sizes
5. Enable caching headers

**Problem:** High Cumulative Layout Shift (CLS)

**Solutions:**
1. Set width/height on images
2. Reserve space for dynamic content
3. Avoid inserting content above existing content
4. Use `aspect-ratio` CSS property

### Accessibility Issues

**Problem:** Low accessibility score

**Solutions:**
1. Add missing ARIA labels
2. Ensure sufficient color contrast
3. Verify keyboard navigation works
4. Add alt text to all images
5. Fix heading hierarchy

### SEO Issues

**Problem:** Pages not indexing

**Solutions:**
1. Check robots.txt allows page
2. Verify sitemap.xml includes page
3. Submit sitemap to Google Search Console
4. Check for noindex meta tag
5. Ensure canonical URL set correctly

---

**Last Updated:** November 22, 2025
**Testing Framework:** Manual + Lighthouse + Browser DevTools
**Target Compliance:** WCAG 2.1 Level AA, Core Web Vitals
