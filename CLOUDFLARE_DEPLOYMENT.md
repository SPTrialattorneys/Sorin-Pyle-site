# Cloudflare Pages Deployment Guide

## Quick Deploy

This project is configured for automatic deployment to Cloudflare Pages.

### Cloudflare Pages Settings

**Framework preset:** None (Custom Configuration)

**Build command:**
```bash
npm run build:prod
```

**Build output directory:**
```
dist
```

**Root directory:**
```
/ (project root)
```

**Node version:**
```
22
```

### Environment Variables

No environment variables required for build.

### Build Process

The `build:prod` script performs the following steps:

1. **Clean**: Removes existing `dist` directory
2. **Images**: Processes responsive images with Sharp (WebP, AVIF variants)
3. **HTML (Production)**: Builds HTML with minification enabled
4. **CSS**: Bundles and minifies CSS with PostCSS
5. **Critical CSS**: Extracts above-the-fold CSS for key pages
6. **HTML (Rebuild)**: Rebuilds HTML with inlined critical CSS
7. **JavaScript**: Bundles and minifies JavaScript with esbuild

**Total build time:** ~30-45 seconds

### Deployment Workflow

1. Push code to your GitHub repository main branch
2. Cloudflare Pages automatically detects the push
3. Cloudflare runs `npm install` and `npm run build:prod`
4. Site deployed to `https://[project-name].pages.dev`

### Custom Domain Setup

1. Go to Cloudflare Pages dashboard
2. Navigate to your project > Custom domains
3. Add `www.sorinpyle.com` and `sorinpyle.com`
4. Update DNS records as instructed by Cloudflare
5. Enable automatic HTTPS

### Performance Features

The site includes:

- **HTML Minification**: Removes comments, whitespace (production only)
- **CSS Optimization**: PostCSS with cssnano (63% file size reduction)
- **Critical CSS**: Inlined for faster First Contentful Paint
- **JavaScript Bundling**: esbuild with tree shaking (~10KB total)
- **Responsive Images**: WebP, AVIF, multiple sizes via Sharp
- **Lazy Loading**: Images load on scroll for better performance

### Cache Control

Cloudflare Pages automatically caches static assets with optimal headers:

- HTML: Short cache (1 hour), revalidate frequently
- CSS/JS: Long cache (1 year) with hash-based filenames
- Images: Long cache (1 year) for processed responsive variants

### Rollback

To rollback to a previous deployment:

1. Go to Cloudflare Pages dashboard
2. Navigate to your project > Deployments
3. Find the deployment you want to restore
4. Click "⋮" menu > "Rollback to this deployment"

### Build Troubleshooting

**Build fails on `npm run build:prod`:**
- Verify Node v22 is set in Cloudflare Pages settings
- Check build logs for specific error messages
- Test build locally with `npm run build:prod`

**CSS not applying:**
- Verify critical CSS extraction completed successfully
- Check browser console for CSS load errors
- Confirm PostCSS plugins are installed

**Images not loading:**
- Verify Sharp successfully processed images (check build logs)
- Confirm `images.json` manifest was generated
- Check responsive image shortcode syntax in templates

### Local Testing

To test production build locally:

```bash
# Build for production
npm run build:prod

# Serve dist directory
cd dist
python -m http.server 8000
# OR
npx serve

# Open http://localhost:8000
```

### Continuous Deployment

Cloudflare Pages automatically deploys:

- **Production deployments**: Commits to `main` branch
- **Preview deployments**: Pull requests (optional)

### Performance Monitoring

Monitor site performance:

- **Cloudflare Analytics**: Dashboard > Analytics
- **Lighthouse CI**: Run periodic audits (see TESTING.md)
- **Core Web Vitals**: Google Search Console

---

## Advanced Configuration

### Build Optimization

For faster builds on Cloudflare Pages, consider:

1. **Incremental Builds**: Eleventy supports incremental rebuilds
2. **Image Caching**: Pre-process images locally, commit to repo
3. **Parallel Processing**: Already enabled in build scripts

### Custom Build Commands

**Development build** (no minification):
```bash
npm run build
```

**Production build** (full optimization):
```bash
npm run build:prod
```

**Individual steps:**
```bash
npm run build:images  # Process responsive images
npm run build:css     # Bundle CSS
npm run build:html    # Build HTML
npm run build:js      # Bundle JavaScript
```

### Debugging

Enable verbose logging by modifying `.eleventy.js`:

```javascript
// Change quiet mode to false
eleventyConfig.setQuietMode(false);
```

Then rebuild to see detailed Eleventy output.

---

**Last Updated:** November 22, 2025
**Eleventy Version:** 3.1.2
**Node Version:** 22.18.0
