# Sorin & Pyle Blog System

This is the blog system for the Sorin & Pyle law firm website. It uses 11ty (Eleventy) to generate static blog pages while keeping the rest of your site as pure HTML.

## What This System Does

- Creates individual blog posts from simple Markdown files
- Generates a blog archive page at `/blog/`
- Creates an RSS feed at `/blog/feed.xml`
- Uses your existing site CSS and navigation
- Each article gets its own SEO-optimized URL

## How to Write a New Blog Post

### Step 1: Create a New Markdown File

Create a new file in the `posts/` folder with this naming format:
```
posts/YYYY-MM-DD-article-title.md
```

Example: `posts/2025-10-15-understanding-expungements.md`

### Step 2: Add the Article Header

At the top of your file, add this header (called "front matter"):

```markdown
---
layout: layouts/blog-post.html
title: "Your Article Title Here"
author: "Sorin Panainte"  or  "Jonathan Pyle"  or  "Sorin & Pyle, Trial Lawyers"
date: 2025-10-15
description: "A brief description for SEO - appears in search results"
tags: ["DUI", "Criminal Defense", "Michigan Law"]
---
```

**Author Options**:
- `"Sorin Panainte"` - Articles written by Sorin
- `"Jonathan Pyle"` - Articles written by Jonathan
- `"Sorin & Pyle, Trial Lawyers"` - Firm articles (general content from the firm)

### Step 3: Write Your Content

After the `---`, write your article in plain text with simple formatting:

```markdown
## This is a heading

This is a paragraph of text.

### This is a subheading

- Bullet point 1
- Bullet point 2
- Bullet point 3

**Bold text** and *italic text*

[Link text](https://example.com)
```

### Complete Example

Here's a complete blog post file:

```markdown
---
layout: layouts/blog-post.html
title: "5 Things to Know About Expungements in Michigan"
author: "Jonathan Pyle"
date: 2025-10-15
description: "Learn the basics of criminal record expungement in Michigan and how it can help your future."
tags: ["Expungement", "Criminal Record", "Michigan Law"]
---

Getting your criminal record expunged in Michigan can open doors to employment, housing, and education. Here's what you need to know.

## 1. Not All Crimes Are Eligible

Michigan law limits which convictions can be expunged. Generally, you can expunge:

- Most misdemeanors
- Some felonies
- Certain traffic offenses

However, serious crimes like murder, criminal sexual conduct, and child abuse cannot be expunged.

## 2. Waiting Periods Apply

You must wait:
- 3 years for misdemeanors
- 5 years for felonies
- 7 years for serious misdemeanors

## Need Help?

Contact Sorin & Pyle at **(616) 227-3303** for a free consultation about expunging your record.
```

## Building Your Blog

### Option 1: Build for Production

When you're ready to publish your blog:

1. Open Command Prompt/Terminal
2. Navigate to the blog folder:
   ```
   cd blog
   ```
3. Run the build command:
   ```
   npm run build
   ```
4. Your blog will be generated in the `_site` folder
5. Upload the contents of `_site` to your web server

### Option 2: Preview While Writing

To see your blog locally while you write:

1. Run:
   ```
   npm run dev
   ```
2. Open your browser to `http://localhost:8080`
3. The blog will automatically reload when you save changes

## File Structure

```
blog/
├── posts/                          ← Your blog articles go here
│   ├── 2025-10-06-dui-article.md
│   └── 2025-10-15-expungement.md
│
├── _includes/                      ← Templates (don't touch unless redesigning)
│   └── layouts/
│       └── blog-post.html
│
├── _site/                          ← Generated blog (upload this to server)
│   ├── blog/
│   │   ├── dui-article/
│   │   ├── expungement/
│   │   └── feed.xml
│   ├── css/
│   ├── js/
│   └── index.html
│
├── package.json                    ← Configuration
├── .eleventy.js                    ← Build settings
└── README.md                       ← This file
```

## URLs Your Blog Creates

After building, your blog will have these URLs:

- `/blog/` - Blog archive page (lists all articles)
- `/blog/understanding-dui-charges/` - Individual article
- `/blog/expungement-guide/` - Another article
- `/blog/feed.xml` - RSS feed

## Publishing Workflow

1. Write article in `posts/YYYY-MM-DD-title.md`
2. Run `npm run build`
3. Upload `_site` folder contents to your web server
4. Done! Your new article is live

## Important Notes

- **Your main site is unchanged**: All your HTML files (index.html, attorneys.html, etc.) remain exactly as they are
- **Shared CSS/JS**: The blog uses your existing styles and scripts
- **SEO Optimized**: Each article has proper meta tags, schema markup, and clean URLs
- **RSS Feed**: Automatically updated at `/blog/feed.xml`

## Troubleshooting

**Q: Build command not working?**
A: Make sure you're in the `blog` folder and ran `npm install` first

**Q: Blog looks different from main site?**
A: The blog uses `/css/style.min.css` from your main site. Any CSS changes to your main site will automatically apply to the blog.

**Q: How do I delete an article?**
A: Delete the `.md` file from `posts/` folder and rebuild

**Q: Can I edit an existing article?**
A: Yes! Edit the `.md` file and run `npm run build` again

## Need Help?

If you need to make changes to:
- Blog layout/design
- Article templates
- URL structure
- RSS feed format

Contact your developer for assistance.
