# Cloudflare Pages Deployment Configuration

## Critical Build Settings

**IMPORTANT:** Cloudflare Pages must be configured with these exact build settings.

### Build Configuration

Go to Cloudflare Pages dashboard → Your project → Settings → Build & deployments

**Build command:**
```
npm run build:cloudflare
```

**Build output directory:**
```
dist
```

**Node.js version:**
```
20.x
```

## What the Build Does

The `npm run build:cloudflare` command runs these steps in order:

1. `npm run clean` - Removes old dist/ folder
2. `npm run build:images` - Processes images with Sharp
3. `npm run build:css` - Compiles CSS with PostCSS (autoprefixer + cssnano)
4. `npm run build:html:prod` - Builds HTML with Eleventy (production mode with minification)
5. `npm run build:js` - Bundles and minifies JavaScript with esbuild

## Required Files in Build Output

After build completes, `dist/` should contain:

- ✅ `dist/_headers` - HTTP security headers configuration
- ✅ `dist/css/main.min.css` - Minified CSS bundle
- ✅ `dist/js/analytics.js` - Google Analytics script
- ✅ `dist/js/main.min.js` - Main JavaScript bundle
- ✅ `dist/js/cookie-consent.js` - Cookie banner script
- ✅ `dist/js/tracking.js` - Event tracking script
- ✅ `dist/js/business-card.js` - Digital business card script
- ✅ `dist/js/qr-campaign.js` - QR campaign script
- ✅ `dist/images/` - Optimized images
- ✅ `dist/*.html` - All HTML pages

## Security Headers

The `_headers` file configures these security headers:

- **HSTS** - Forces HTTPS for 1 year
- **Content-Security-Policy** - XSS protection
- **X-Frame-Options** - Clickjacking protection
- **X-Content-Type-Options** - MIME sniffing protection
- **Cross-Origin-Opener-Policy** - Origin isolation
- **Permissions-Policy** - Feature restrictions

## Troubleshooting

### Issue: 404 errors for /js/analytics.js or /css/cookie-consent.css

**Cause:** Cloudflare isn't running the build command

**Fix:**
1. Check build settings use `npm run build:cloudflare`
2. Check build output directory is set to `dist`
3. Verify build logs show all scripts running successfully

### Issue: Security headers not working

**Cause:** `_headers` file not in dist/

**Fix:**
1. Verify `.eleventy.js` has passthrough copy for _headers
2. Run `npm run build:html` locally and check `dist/_headers` exists
3. Push changes and rebuild on Cloudflare

### Issue: CSS or JavaScript changes not appearing

**Cause:** Browser caching

**Fix:**
1. Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
2. Check version string in base.njk matches deployment date
3. Clear Cloudflare cache if needed

## Local Testing

Test the full build locally before pushing:

```bash
# Full production build
npm run build:prod

# Serve dist/ folder locally
npx serve dist -p 8080

# Open http://localhost:8080 and test
```

## Deployment Checklist

Before deploying major changes:

- [ ] Test locally with `npm run build:prod`
- [ ] Verify all JS/CSS files exist in `dist/`
- [ ] Check `dist/_headers` exists
- [ ] Test pages load without errors
- [ ] Check browser console for errors
- [ ] Verify images load correctly
- [ ] Test navigation works
- [ ] Commit and push to main branch
- [ ] Monitor Cloudflare build logs
- [ ] Test live site after deployment

## Build Performance

Expected build times on Cloudflare Pages:

- Image processing: ~15-30 seconds (first build)
- CSS compilation: ~2-5 seconds
- HTML generation: ~1-2 seconds
- JavaScript bundling: ~1-2 seconds
- **Total:** ~25-45 seconds

## Contact

For Cloudflare Pages support: https://developers.cloudflare.com/pages/

---
Last deployment trigger: November 23, 2025
