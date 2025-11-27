# Quick Start - Sorin & Pyle Website

**⏱️ 5-minute read** | Full docs: [AI_CONTEXT.md](AI_CONTEXT.md) • [CLAUDE.md](CLAUDE.md) • [BUILD_PROCESS.md](BUILD_PROCESS.md)

---

## 🚀 Essential Commands

```bash
# Development (live reload)
npm run dev                    # http://localhost:8080

# Production build (use this for deployment)
npm run build:cloudflare       # Full automated build (CSS → HTML → JS)
                                # Note: Critical CSS extraction runs LOCALLY only

# Individual steps (for troubleshooting)
npm run build:css              # Build CSS from src/assets/styles/
npm run build:html:prod        # Build HTML from src/pages/*.njk
npm run build:critical         # Extract critical CSS (requires dist/ to exist)
npm run build:js               # Bundle JavaScript
```

---

## 📁 File Locations

### ✅ Edit These (Source Files)
```
src/pages/*.njk              → Page templates (HTML source)
src/assets/styles/*.css      → Stylesheets (main CSS)
src/assets/scripts/*.js      → JavaScript files
src/_includes/layouts/*.njk  → Page layouts
src/_data/*.json            → Global site data
```

### ❌ Never Edit These (Auto-Generated)
```
dist/                        → Built files (overwritten on every build)
src/_data/critical-*.css     → Critical CSS (auto-extracted)
```

---

## ⚠️ Critical Rules

### **1. NEVER Edit Built Files**
- `dist/` folder is **auto-generated** on every build
- Editing `dist/*.html` directly = changes lost on next build
- **Always edit** `.njk` files in `src/pages/`

### **2. CSS Updates = Single File**
- Edit **only** `src/assets/styles/*.css`
- Critical CSS auto-extracts during build
- **Don't manually edit** `src/_data/critical-*.css`

### **3. Build Order Matters**
For above-the-fold CSS changes (critical CSS):
```bash
npm run build:css              # 1. Build main CSS
npm run build:html:prod        # 2. Build HTML to dist/
npm run build:critical         # 3. Extract critical CSS (LOCAL ONLY)
npm run build:dedupe-critical  # 4. Remove duplicate CSS rules
npm run build:html:prod        # 5. Rebuild HTML with new critical CSS
```
Or use `npm run build:prod` (includes critical CSS extraction, local only)

**Note:** `npm run build:cloudflare` does NOT extract critical CSS (Puppeteer unavailable). Use locally extracted critical CSS (committed to git).

---

## 📝 Common Workflows

### **Add a New Page**
```bash
# 1. Create template
src/pages/new-page.njk

# 2. Add to sitemap
src/sitemap.njk

# 3. Build
npm run build:html:prod
```

### **Update CSS Styling**
```bash
# 1. Edit main CSS only
src/assets/styles/style-core.css

# 2. Run local build with critical CSS extraction
npm run build:prod

# 3. Commit both main CSS and auto-generated critical CSS
git add src/assets/styles/style-core.css src/_data/critical-*.css
git commit -m "Update styling"
git push

# Cloudflare auto-deploys using committed critical CSS files
```

### **Fix a Typo on a Page**
```bash
# 1. Find and edit the .njk source file
src/pages/attorneys.njk   # NOT dist/attorneys.html

# 2. Rebuild HTML
npm run build:html:prod

# 3. Verify in dist/ folder
# Open dist/attorneys.html in browser
```

### **Add a Blog Post**
```bash
# Option 1: Markdown (Recommended for regular blogging)
# 1. Create Markdown file
src/blog/posts/2025-10-06-post-slug.md

# 2. Add frontmatter + content
---
layout: layouts/blog-post.njk
title: "Post Title"
description: "SEO description"
date: 2025-10-06
author: "sorin"  # or "jonathan" or "firm"
category: "legal"  # or "community", "michigan", "case"
featuredImage: "/images/post-image.avif"
---

# Post content in Markdown...

# 3. Build and deploy
npm run build:html:prod
git add src/blog/posts/2025-10-06-post-slug.md
git commit -m "Add blog post: Post Title"
git push

# Option 2: Manual HTML (For occasional posts)
# Edit src/pages/blog.njk directly (see AI_CONTEXT.md Section 7.7)
```

---

## 🔍 Project Structure

```
sorin-pyle-site-html/
├── src/                        # Source files (edit these)
│   ├── pages/                  # Page templates (*.njk)
│   ├── blog/
│   │   └── posts/              # Markdown blog posts (*.md)
│   ├── assets/
│   │   ├── styles/             # CSS files
│   │   └── scripts/            # JavaScript files
│   ├── _includes/
│   │   ├── layouts/            # Page layouts (base.njk, page.njk, blog-post.njk)
│   │   └── partials/           # Reusable components
│   └── _data/
│       ├── site.json           # Global site data
│       ├── navigation.json     # Navigation structure
│       ├── authors.json        # Blog author data
│       └── critical-*.css      # Critical CSS (auto-generated)
│
├── dist/                       # Built files (auto-generated, don't edit)
│
├── utilities/
│   └── extract-critical-css.mjs   # Critical CSS automation
│
├── .eleventy.js                # Eleventy configuration
├── package.json                # Build scripts
├── esbuild.config.js           # JavaScript bundler config
└── postcss.config.cjs          # CSS processing config
```

---

## 🐛 Common Issues

### **Issue: CSS changes not showing up**
```bash
# Solution: Run local build with critical CSS extraction
npm run build:prod  # Extracts critical CSS from dist/ folder
# Then commit and push critical CSS files to deploy
```

### **Issue: "Cannot find dist/ directory"**
```bash
# Solution: Build HTML first, then extract critical CSS
npm run build:html:prod
npm run build:critical
```

### **Issue: Changes not appearing in browser**
```bash
# Solution: Hard refresh (bypass cache)
Ctrl + Shift + R  (Windows/Linux)
Cmd + Shift + R   (Mac)
```

---

## 🔗 Deployment

**Automatic via Cloudflare Pages:**
1. Push to `main` branch on GitHub
2. Cloudflare detects push and runs `npm run build:cloudflare`
3. Site auto-deploys to https://www.sorinpyle.com (2-3 minutes)

**Build Command:** `npm run build:cloudflare`
**Output Directory:** `dist`
**Node Version:** 20.x

---

## 📚 Next Steps

- **Full Documentation:** [AI_CONTEXT.md](AI_CONTEXT.md) (~16,000 words)
- **Project Instructions:** [CLAUDE.md](CLAUDE.md) (critical systems + recent changes)
- **Build System Guide:** [BUILD_PROCESS.md](BUILD_PROCESS.md) (all npm scripts explained)
- **Schema Guide:** See AI_CONTEXT.md Section 5.3 (Schema Markup)
- **Troubleshooting:** See AI_CONTEXT.md Section 10 (Common Issues)

---

## 🎯 Key Takeaways

1. **Edit `.njk` files**, never `.html` files in `dist/`
2. **Update CSS once**, critical CSS auto-extracts (local builds only)
3. **For above-the-fold CSS**: Use `npm run build:prod` locally, commit critical CSS files
4. **For deployment**: `npm run build:cloudflare` (uses committed critical CSS)
5. **Push to GitHub** triggers automatic Cloudflare deployment
6. **Blog posts**: Use Markdown in `src/blog/posts/` for easy authoring + RSS feed

**Questions?** Check [BUILD_PROCESS.md](BUILD_PROCESS.md), [AI_CONTEXT.md](AI_CONTEXT.md), or [CLAUDE.md](CLAUDE.md) for detailed explanations.
