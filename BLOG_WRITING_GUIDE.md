# Blog Writing Guide - Sorin & Pyle Law Firm

## Quick Start

**Goal:** This guide helps you write and publish blog posts using the Eleventy Markdown system.

**Who:** For attorneys and staff writing blog content (3-8 posts/month expected)

**Prerequisites:** Basic Markdown knowledge (headings, lists, links, bold/italic)

---

## Creating a New Blog Post

### Step 1: Create a new Markdown file

Create a new file in the `src/posts/` directory with this naming format:

```
src/posts/YYYY-MM-DD-post-title-slug.md
```

**Examples:**
- `src/posts/2025-11-24-new-michigan-dui-law.md`
- `src/posts/2025-12-15-client-success-story.md`

**Naming Rules:**
- Start with date: `YYYY-MM-DD` (2025-11-24)
- Follow with slug: lowercase, hyphens only, no spaces
- Extension: `.md` (Markdown)

---

### Step 2: Add Front Matter (Required Metadata)

Every blog post MUST start with front matter (YAML metadata between `---` markers).

**Copy this template:**

```yaml
---
title: "Your Blog Post Title Here (50-60 characters ideal)"
description: "A compelling 1-2 sentence summary for search engines and social sharing (150-160 characters recommended)"
date: 2025-11-24
author: firm
category: Community
featuredImage: /images/your-image-filename.avif
featuredImageAlt: "Descriptive alt text for screen readers and SEO"
aboutPerson: /sorin-panainte.html#attorney
layout: layouts/blog-post.njk
---
```

**Field Explanations:**

| Field | Required | Description | Example Values |
|-------|----------|-------------|----------------|
| `title` | ✅ Yes | Post headline (50-60 chars ideal for SEO) | `"New Michigan DUI Law Takes Effect"` |
| `description` | ✅ Yes | Meta description for SEO (150-160 chars) | `"Learn how Michigan's new DUI law affects first-time offenders..."` |
| `date` | ✅ Yes | Publication date (YYYY-MM-DD format) | `2025-11-24` |
| `author` | ✅ Yes | Author identifier (see Author Options below) | `sorin-panainte`, `jonathan-pyle`, or `firm` |
| `category` | ✅ Yes | Post category (see Category Options below) | `Community`, `Legal`, `Michigan Law`, `Case Analysis` |
| `featuredImage` | ✅ Yes | Path to featured image (AVIF preferred) | `/images/michigan-capitol.avif` |
| `featuredImageAlt` | ✅ Yes | Alt text for image (accessibility + SEO) | `"Michigan State Capitol building in Lansing"` |
| `aboutPerson` | ❌ Optional | Link to attorney profile if post is about someone | `/sorin-panainte.html#attorney` or `/jonathan-pyle.html#attorney` |
| `layout` | ✅ Yes | Template to use (always same value) | `layouts/blog-post.njk` |
| `draft` | ❌ Optional | Set to `true` to hide post from site | `true` or `false` (default: false) |

---

### Step 3: Write Your Content (Markdown)

After the closing `---` of front matter, write your post content in Markdown.

**Example Post:**

```markdown
---
title: "Understanding Michigan's New Expungement Law"
description: "Michigan's Clean Slate law expands expungement eligibility. Learn if you qualify to clear your criminal record in 2025."
date: 2025-11-24
author: sorin-panainte
category: Michigan Law
featuredImage: /images/michigan-clean-slate-law.avif
featuredImageAlt: "Michigan gavel and legal documents for criminal record expungement"
aboutPerson: /sorin-panainte.html#attorney
layout: layouts/blog-post.njk
---

On November 15, 2025, Michigan's expanded Clean Slate law went into effect, making it easier than ever to clear criminal records. **If you have a past conviction, you may now qualify for automatic expungement.**

## What Changed in 2025?

The new law expands eligibility in three key ways:

1. **More felonies qualify** - Up to 3 felonies (previously 1)
2. **Shorter waiting periods** - 5 years for misdemeanors (previously 7)
3. **Automatic expungements** - No application required for some convictions

## Who Qualifies Now?

You may qualify if:

- You have **1-3 felony convictions** (non-assaultive)
- You have **up to 2 misdemeanor convictions**
- At least **5 years have passed** since completion of sentence
- You have **no pending criminal charges**

**Important:** Certain serious crimes (CSC, homicide, terrorism) are **never eligible** for expungement.

## How Our Firm Can Help

Attorney Sorin Panainte has helped dozens of clients clear their records through Michigan's expungement process. We offer:

- **Free initial consultation** to review your eligibility
- **Complete petition preparation** with all required documents
- **Court representation** at expungement hearings
- **Fast turnaround** - most petitions filed within 2 weeks

## Next Steps

Ready to start over with a clean slate? [Contact us today](/contact.html) for a free consultation, or call **(616) 227-3303** to speak with an attorney.

*Disclaimer: This blog post is for general informational purposes only and does not constitute legal advice.*
```

---

## Markdown Formatting Reference

### Headings

```markdown
# H1 - Page Title (automatically added from front matter `title`)
## H2 - Main Section Heading
### H3 - Subsection Heading
```

**Best Practice:** Start content with `##` (H2), not `#` (H1). The page title is already H1.

---

### Text Formatting

```markdown
**Bold text** for emphasis
*Italic text* for subtle emphasis
***Bold and italic*** for strong emphasis
```

---

### Lists

**Unordered (bullet) lists:**

```markdown
- First item
- Second item
- Third item
  - Nested sub-item (indent with 2 spaces)
```

**Ordered (numbered) lists:**

```markdown
1. First step
2. Second step
3. Third step
```

---

### Links

**Internal links (to other site pages):**

```markdown
[Contact us](/contact.html)
[Read our FAQ](/faq.html)
[Learn about DUI defense](/dui-defense.html)
```

**External links (to other websites):**

```markdown
[Michigan Legislature](https://legislature.mi.gov){target="_blank" rel="noopener noreferrer"}
```

**Note:** External links should include `{target="_blank" rel="noopener noreferrer"}` to open in new tab safely.

---

### Images

**Images in Markdown:**

```markdown
![Alt text description](/images/filename.avif)
```

**Images with specific size:**

```markdown
<img src="/images/filename.avif" alt="Alt text" width="800" height="600">
```

**Best Practices:**
- Use AVIF format for best compression (smallest file size)
- Provide descriptive alt text for accessibility and SEO
- Keep images under 200 KB (optimize before uploading)

---

### Block Quotes

```markdown
> "This is a quote or callout text."
>
> - Source or attribution
```

---

### Horizontal Rules (Section Dividers)

```markdown
---
```

---

## Author Options

Set the `author` field in front matter to one of these values:

| Author Value | Display Name | Schema Type | When to Use |
|--------------|--------------|-------------|-------------|
| `sorin-panainte` | Sorin Panainte | Person | Sorin wrote the post or it's about his work |
| `jonathan-pyle` | Jonathan Pyle | Person | Jonathan wrote the post or it's about his work |
| `firm` | Sorin & Pyle, Trial Lawyers | Organization | General firm updates, both attorneys, or staff-written |

**Examples:**
- Sorin volunteers at expungement fair → `author: firm` (general firm news)
- Sorin's legal opinion on new law → `author: sorin-panainte` (Sorin's expertise)
- Jonathan wins trial → `author: firm` (firm news) OR `author: jonathan-pyle` (Jonathan's achievement)

**Default:** Use `author: firm` unless the post is specifically Sorin's or Jonathan's individual voice/achievement.

---

## Category Options

Choose ONE category that best fits your post:

| Category | When to Use | Example Posts |
|----------|-------------|---------------|
| `Community` | Pro bono work, volunteering, events, community involvement | "Attorney Sorin Volunteers at Expungement Fair" |
| `Legal` | Attorney opinions, legal analysis, practice tips, commentary | "Understanding Your Miranda Rights" |
| `Michigan Law` | New laws, court rulings, legislative updates, statutory changes | "Michigan Legalizes Marijuana for Medical Use" |
| `Case Analysis` | High-profile case breakdowns, trial strategies (NO client cases!) | "Analyzing the State v. Smith Verdict" |

**Important:** NEVER write about active client cases. All case analysis must be:
- Public court cases (news coverage)
- Anonymized examples (no real names/details)
- General patterns (not specific cases)

**Category displays as colored tag:**
- Community = Green
- Legal = Blue
- Michigan Law = Purple
- Case Analysis = Orange

---

## Featured Images

### Image Requirements

- **Format:** AVIF preferred (best compression), fallback to WebP or JPG
- **Size:** 800x600 pixels (landscape)
- **File Size:** Under 200 KB (optimize before uploading)
- **Location:** Upload to `images/` directory
- **Naming:** Use SEO-friendly filenames (e.g., `michigan-expungement-law-2025.avif` NOT `IMG_1234.avif`)

### Where to Find Images

**Free Stock Photos (Legal/Professional):**
- [Unsplash](https://unsplash.com) - Free high-quality photos
- [Pexels](https://pexels.com) - Free stock photos and videos
- [Pixabay](https://pixabay.com) - Free images and vectors

**Search Terms:**
- "courthouse" "gavel" "legal documents"
- "handshake" "scales of justice"
- "Michigan" "Detroit" "Grand Rapids"
- "community" "volunteers" "helping"

**Image Optimization:**
- Use [TinyPNG](https://tinypng.com) to compress images
- Use [Squoosh](https://squoosh.app) to convert to AVIF format

### Alt Text Guidelines

**Good alt text:**
- `"Attorney Sorin Panainte speaking at Gun Lake Tribe expungement fair"`
- `"Michigan State Capitol building in Lansing"`
- `"Hands holding expungement petition paperwork"`

**Bad alt text:**
- `"Image"` (too vague)
- `"IMG_1234"` (not descriptive)
- `"Click here"` (not an image description)

**Format:** `featuredImageAlt: "Description here"` (use quotes if description contains special characters)

---

## Building and Previewing Your Post

### Local Preview (Before Publishing)

1. **Save your Markdown file** to `src/posts/`

2. **Run the development server:**
   ```bash
   npm run dev
   ```

3. **Open in browser:**
   ```
   http://localhost:8080/blog.html
   ```

4. **View your post:**
   - Archive page: `http://localhost:8080/blog.html`
   - Individual post: `http://localhost:8080/blog/your-post-title-slug.html`

5. **Check for issues:**
   - Images load correctly
   - Links work
   - Formatting looks good
   - Category tag displays
   - Author attribution correct

### Production Build (Before Deploying)

```bash
npm run build:cloudflare
```

**What this does:**
- Builds CSS (minified)
- Builds HTML (all pages + blog posts)
- Builds JavaScript (minified)

**Check for errors:** Build should complete without errors. If you see errors, read the message and fix the Markdown file.

---

## Publishing Workflow

### Option A: Direct to Production (Small Updates)

1. Save post to `src/posts/YYYY-MM-DD-title.md`
2. Test locally (`npm run dev`)
3. Build for production (`npm run build:cloudflare`)
4. Commit changes:
   ```bash
   git add src/posts/your-post.md
   git add src/_data/authors.json  # If you added a new author
   git commit -m "Add blog post: Your Title Here"
   git push origin main
   ```
5. Cloudflare auto-deploys to production (3-5 minutes)

### Option B: Test Branch (Recommended for New Posts)

1. Create test branch:
   ```bash
   git checkout -b blog-post-test
   ```

2. Save post, build, commit:
   ```bash
   git add src/posts/your-post.md
   git commit -m "Add blog post: Your Title Here"
   git push origin blog-post-test
   ```

3. Cloudflare creates preview URL:
   ```
   https://blog-post-test.sorinpyle.pages.dev
   ```

4. Review preview, fix issues, push updates

5. When satisfied, merge to main:
   ```bash
   git checkout main
   git merge blog-post-test
   git push origin main
   ```

6. Production deploys automatically

---

## Troubleshooting Common Issues

### Build Fails with "filter not found" Error

**Cause:** Using unsupported Nunjucks filter in Markdown

**Fix:** Avoid using `{{` or `{%` in blog content. If you need to show code examples, use backticks:

```markdown
\`\`\`
{{ example.code }}
\`\`\`
```

### Post Not Showing on /blog.html

**Possible Causes:**
1. `draft: true` in front matter (remove or set to `false`)
2. Date is in the future (Eleventy may skip future posts)
3. File not in `src/posts/` directory
4. Filename doesn't match `*.md` pattern
5. Front matter is malformed (missing `---` markers)

**Fix:** Check front matter, filename, and rebuild.

### Images Not Loading

**Possible Causes:**
1. Image path wrong (should start with `/images/` not `images/`)
2. Image file not in `images/` directory
3. Filename case mismatch (use lowercase filenames)

**Fix:** Verify image exists at `images/filename.avif` and path is `/images/filename.avif`

### Schema Validation Errors

**Run validation:**
```bash
npm run validate:schema
```

**Common Issues:**
- Missing required front matter fields
- Invalid date format (must be YYYY-MM-DD)
- Invalid author (must be `sorin-panainte`, `jonathan-pyle`, or `firm`)
- Invalid category (must be `Community`, `Legal`, `Michigan Law`, or `Case Analysis`)

### Categories Not Showing Correct Color

**Check:** Category value is EXACT match (case-sensitive):
- ✅ `Community` (green)
- ✅ `Legal` (blue)
- ✅ `Michigan Law` (purple) - note the space!
- ✅ `Case Analysis` (orange) - note the space!
- ❌ `community` (won't match)
- ❌ `legal` (won't match)
- ❌ `MichiganLaw` (won't match, needs space)

---

## SEO Best Practices

### Title Optimization

**Good Titles:**
- `"New Michigan DUI Law: What First-Time Offenders Need to Know"` (58 chars)
- `"Attorney Sorin Volunteers at Gun Lake Tribe Expungement Fair"` (61 chars)

**Bad Titles:**
- `"Update"` (too vague, no keywords)
- `"Everything You Ever Wanted to Know About Michigan DUI Laws But Were Afraid to Ask"` (82 chars, too long)

**Format:** `50-60 characters` | Include primary keyword | Be specific

---

### Meta Description Optimization

**Good Descriptions:**
- `"Learn how Michigan's new DUI law affects first-time offenders and what penalties to expect in 2025."` (103 chars)
- `"Attorney Sorin Panainte recently volunteered at the Free Expungement Fair hosted by the Gun Lake Tribe in Shelbyville, Michigan."` (131 chars)

**Bad Descriptions:**
- `"Read our blog post."` (too vague, no value proposition)
- `"This extremely long description goes on and on about every single detail mentioned in the article and includes way too much information that won't fit in Google search results anyway"` (too long, gets cut off)

**Format:** `150-160 characters` | Include primary keyword | Compelling call-to-action or value proposition

---

### Keyword Guidelines

**Target Keywords Per Post:**
- **Primary keyword:** Main topic (e.g., "Michigan DUI law")
- **Secondary keywords:** Related terms (e.g., "first-time DUI", "OWI penalties")

**Keyword Placement:**
1. Title (most important)
2. Meta description
3. First paragraph
4. At least one H2 heading
5. Alt text for featured image
6. URL slug (auto-generated from filename)

**Avoid:** Keyword stuffing (repeating same phrase 10+ times)

---

## Compliance & Legal Disclaimers

### Required Disclaimers

**Every post should include this footer:**

```markdown
*Disclaimer: The information on this website is for general information purposes only. Nothing on this site should be taken as legal advice for any individual case or situation. This information is not intended to create, and receipt or viewing does not constitute, an attorney-client relationship.*
```

**For posts mentioning case results:**

```markdown
*Past results do not guarantee or predict a similar outcome in future cases. Each case is unique and must be evaluated on its own merits.*
```

### MRPC 7.1 Compliance (Attorney Advertising)

**DO NOT:**
- ❌ Guarantee outcomes ("We will get your case dismissed")
- ❌ Make unsubstantiated claims ("Best DUI lawyer in Michigan")
- ❌ Mislead about attorney credentials
- ❌ Promise results based on past cases

**DO:**
- ✅ Provide general legal information
- ✅ Share community involvement
- ✅ Explain legal processes and rights
- ✅ Use phrases like "may qualify," "potential," "we fight for"

### Client Confidentiality (MRPC 1.6)

**NEVER write about:**
- ❌ Specific client cases (even anonymized)
- ❌ Client details or stories without written permission
- ❌ Confidential communications

**OK to write about:**
- ✅ General case types ("We handle DUI cases")
- ✅ Public court cases (news coverage)
- ✅ Pro bono work (with permission)
- ✅ Legal trends and statistics

---

## Content Ideas & Topics

### Community Category Ideas
- Pro bono events (expungement fairs, legal clinics)
- Volunteer work (Gun Lake Tribe, Christian Neighbors)
- Local partnerships (public defender office, AG office)
- Community resources (mental health, substance abuse)
- Firm milestones (anniversaries, awards, recognition)

### Legal Category Ideas
- "Know Your Rights" guides (Miranda rights, search & seizure)
- Legal process explainers (arraignment, plea bargaining, trial)
- FAQ expansions (detailed answers to common questions)
- Attorney opinions on legal issues (DUI checkpoints, expungement)
- Practice area deep dives (domestic violence defense, license restoration)

### Michigan Law Category Ideas
- New legislation (DUI laws, expungement reforms, marijuana)
- Court rulings (Michigan Supreme Court decisions)
- Legislative updates (bills in progress, proposed changes)
- County-specific rules (Ottawa County, Kent County differences)
- Statute explanations (MCL 750.81, MCL 257.625, etc.)

### Case Analysis Category Ideas
- High-profile trials (public cases only)
- Legal strategy breakdowns (defense tactics, prosecution patterns)
- Jury verdict analysis (trends, patterns, predictions)
- Appellate decisions (impact on criminal defense)

**Note:** Check with attorney before publishing any case analysis to ensure accuracy and ethics compliance.

---

## RSS Feed & Syndication

**Automatic RSS Feed:** All posts are automatically added to the RSS feed at `/feed.xml`

**RSS Features:**
- Shows 15 most recent posts
- Includes full post content
- Updates on every build
- Includes author, category, and publish date

**Subscribers:** Readers can subscribe via RSS reader (Feedly, Inoreader, etc.) to get notified of new posts.

**Submit Feed To:**
- Google (via Search Console)
- Bing (via Webmaster Tools)
- Legal directories (Avvo, Justia, Lawyers.com)

---

## Writing Tips for Law Firm Blogs

### Tone & Voice
- **Professional but approachable** (not stuffy legalese)
- **Empathetic** (understand client stress and fear)
- **Action-oriented** (tell reader what to do next)
- **Confident** (expertise and experience)

**Example (Good):**
> "If you've been arrested for DUI, you're probably scared and unsure what happens next. That's normal. Here's what you need to know to protect your rights."

**Example (Bad):**
> "Pursuant to MCL 257.625, individuals charged with operating while intoxicated are subject to judicial proceedings wherein..."

### Structure
1. **Hook** (first sentence grabs attention)
2. **Problem** (what reader is facing)
3. **Solution** (how you can help)
4. **Call-to-Action** (contact us, call, schedule)

### Length
- **Ideal:** 800-1,200 words
- **Minimum:** 500 words (for SEO)
- **Maximum:** 2,000 words (readers lose attention)

### Readability
- **Short paragraphs** (2-4 sentences max)
- **Bullet points** (scan-friendly)
- **Headings** (break up text)
- **Active voice** ("We fight for you" not "Your case is fought for by us")

---

## Questions?

**Technical Issues:**
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for build errors
- Review [CLAUDE.md](CLAUDE.md) for project documentation

**Content Questions:**
- Ask Sorin or Jonathan for legal accuracy review
- Check MRPC 7.1 and 7.4 for advertising compliance

**Need Help?**
- File location issues → Check this guide Section: "Creating a New Blog Post"
- Markdown formatting → Check Section: "Markdown Formatting Reference"
- SEO questions → Check Section: "SEO Best Practices"
- Legal compliance → Ask attorney before publishing

---

**Last Updated:** November 24, 2025
**Version:** 1.0
