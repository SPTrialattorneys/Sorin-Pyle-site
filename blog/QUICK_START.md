# Blog System - Quick Start Guide

## ✅ System is Ready!

Your blog system is installed and working. Your main website (all HTML files) remains completely unchanged.

## 📝 To Write a New Blog Post

### 1. Create File
Create: `blog/posts/2025-10-15-my-article-title.md`

### 2. Add Header
```markdown
---
layout: layouts/blog-post.html
title: "Your Article Title"
author: "Sorin Panainte"
date: 2025-10-15
description: "Brief description for SEO"
---
```

### 3. Write Content
```markdown
Write your content here using plain text...

## Headings are easy

Just write naturally. Use **bold** and *italics* as needed.
```

## 🚀 To Publish

```bash
cd blog
npm run build
```

Upload the `blog/_site` folder contents to your server.

## 👀 To Preview

```bash
cd blog
npm run dev
```

Visit: http://localhost:8080

## 📍 What You Get

- **Blog Archive**: `/blog/` - Lists all articles
- **Individual Articles**: `/blog/article-name/` - Each post gets its own URL
- **RSS Feed**: `/blog/feed.xml` - Automatic feed for SEO

## ✨ Benefits

✅ Each article has its own URL (better SEO)
✅ Automatic RSS feed
✅ Automatic sitemap
✅ Schema markup for Google
✅ Uses your existing site design
✅ Main site unchanged (pure HTML)

## 💡 Tips

- Use descriptive filenames: `understanding-dui-law.md` not `post1.md`
- Write good descriptions - they appear in Google search results
- Date format must be: YYYY-MM-DD
- Author must match: "Sorin Panainte" or "Jonathan Pyle"

## 📚 Need More Help?

See the full README.md in this folder for detailed instructions.
