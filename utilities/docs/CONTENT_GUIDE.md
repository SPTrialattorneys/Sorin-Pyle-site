# Content Creation Guide - Sorin & Pyle Website

**⏱️ 12-minute read** | For full documentation, see [AI_CONTEXT.md](../../AI_CONTEXT.md) Section 6

---

## 📚 Quick Navigation

**Other Guides:**
- [Quick Start](../../QUICK_START.md) - 5-minute onboarding
- [CSS Guide](CSS_GUIDE.md) - CSS workflow and critical CSS
- [Schema Guide](SCHEMA_GUIDE.md) - Schema markup templates
- [Troubleshooting](TROUBLESHOOTING.md) - Common errors (coming soon)

---

## 🎯 Overview: Creating New Pages

This guide covers creating **two main page types**:
1. **Service Pages** - DUI defense, domestic violence, expungement, etc.
2. **Location Pages** - City and county landing pages

Both follow similar workflows but have different schema and content requirements.

---

## 📄 Creating a New Service Page (Step-by-Step)

### **Example: Creating "Felony Defense" Service Page**

### **Step 1: Create Nunjucks Template File**

**Location:** `src/pages/felony-defense.njk`

**File Naming Convention:**
- All lowercase
- Hyphens (not underscores)
- Descriptive keywords
- .njk extension (Nunjucks template)

**Basic Template Structure:**

```njk
---
layout: layouts/page.njk
title: "Felony Defense Lawyer Holland MI | Serious Crime Attorney Ottawa County"
description: "Facing felony charges in Michigan? Experienced felony defense lawyers in Holland & Grand Rapids. Former public defender. Free consultation: (616) 227-3303"
permalink: "/felony-defense.html"
---

{# Page content goes here #}
<div class="container-large">
  <h1>Felony Defense Attorney in Holland & Grand Rapids</h1>

  {# Introduction section #}
  <section class="section">
    <p class="lead">[Compelling opening paragraph]</p>
  </section>

  {# Main content sections #}
  <section class="section">
    <h2>Types of Felony Charges We Defend</h2>
    {# Content #}
  </section>

  {# FAQ section #}
  <section class="section">
    <h2>Frequently Asked Questions</h2>
    {# FAQ content #}
  </section>

  {# CTA section #}
  <section class="section section_contact-cta">
    {# Call to action #}
  </section>
</div>

{# Schema markup #}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  ...
}
</script>
```

---

### **Step 2: Write Front Matter (Page Metadata)**

**Required Fields:**

```yaml
---
layout: layouts/page.njk              # Use page.njk for standard service pages
title: "Page Title 50-60 chars"       # SEO-optimized title
description: "Meta description 150-160 chars"  # Shows in search results
permalink: "/page-name.html"          # Output filename
---
```

**Title Tag Best Practices:**
- 50-60 characters max (Google truncates at ~60)
- Include primary keyword first
- Include location (Holland MI, Ottawa County)
- Include firm type or differentiator
- Format: `[Service] Lawyer [City] | [Differentiator] Attorney [County]`

**Example:**
```
"Felony Defense Lawyer Holland MI | Former Public Defender Ottawa County"
```

**Meta Description Best Practices:**
- 150-160 characters max (Google truncates at ~160)
- Include primary and secondary keywords
- Include location and phone number
- Include CTA ("Free consultation")
- Front-load important information

**Example:**
```
"Facing felony charges in Michigan? Experienced felony defense lawyers in Holland & Grand Rapids. Former public defender. Free consultation: (616) 227-3303"
```

---

### **Step 3: Write Page Content**

**Content Structure (Standard Service Page):**

1. **H1 Heading** - Primary keyword + location
   ```html
   <h1>Felony Defense Attorney in Holland & Grand Rapids</h1>
   ```

2. **Lead Paragraph** - Hook + urgency + value proposition
   ```html
   <p class="lead">Facing felony charges in Michigan? You need an experienced trial lawyer who understands the stakes. Sorin & Pyle are former public defenders who have handled hundreds of felony cases in Ottawa and Kent County courts.</p>
   ```

3. **Main Content Sections** (5-8 sections typical):
   - Types of charges we defend
   - Penalties and consequences
   - Defense strategies
   - What to do after arrest
   - Why choose us
   - FAQ (5-10 questions)
   - Common mistakes to avoid
   - Final CTA

4. **Word Count Target:** 3,000-6,000 words
   - DUI defense: 5,000+ words
   - Domestic violence: 6,500+ words
   - Expungement: 2,500+ words

**Content Writing Guidelines:**

✅ **DO:**
- Write in second person ("you", "your")
- Use short paragraphs (2-4 sentences)
- Use conversational tone (firm's "WE GIVE A [EXPLETIVE]!" philosophy)
- Include specific Michigan statutes (MCL 750.xxx)
- Mention specific courts (20th Circuit, 58th District)
- Include real case examples (anonymized)
- Front-load important information
- Use bullet points and numbered lists
- Include internal links to related pages

❌ **DON'T:**
- Use legal jargon without explanation
- Make outcome guarantees ("we will win")
- Use "specializing in" (MRPC 7.4 violation)
- Include outdated information
- Bury the CTA at the bottom
- Write long walls of text
- Use passive voice excessively

---

### **Step 4: Add Schema Markup**

**Required Schema Types for Service Pages:**

1. **LegalService Schema** - Always required
2. **FAQPage Schema** - Required if 5+ FAQ questions
3. **BreadcrumbList Schema** - Always required

**Copy-Paste Templates:** See [Schema Guide](SCHEMA_GUIDE.md)

**Schema Placement:** Add before closing `</body>` tag (Eleventy handles this automatically)

---

### **Step 5: Add to Sitemap**

**File:** `src/sitemap.njk`

**Add New Entry:**

```xml
<url>
  <loc>{{ site.url }}/felony-defense.html</loc>
  <lastmod>2025-11-24</lastmod>
  <priority>0.95</priority>
</url>
```

**Priority Guidelines:**
- Homepage: 1.00
- Service pages: 0.90-0.95 (high priority)
- Location pages: 0.70-0.85
- Resource pages: 0.75-0.85
- Other pages: 0.60-0.70

---

### **Step 6: Add Internal Links**

**Link from Homepage:**

**File:** `src/pages/index.njk`

**Add to Practice Areas section:**

```html
<li><a href="felony-defense.html">Felony Defense</a></li>
```

**Link from Practice Areas Page:**

**File:** `src/pages/practice-areas.njk`

**Add to appropriate section:**

```html
<li><a href="felony-defense.html">Felony Defense</a> - [Brief description]</li>
```

---

### **Step 7: Build and Test**

```bash
# Build HTML
npm run build:html:prod

# Test locally
# Open dist/felony-defense.html in browser

# Verify:
# ✅ Page displays correctly
# ✅ Navigation links work
# ✅ Internal links work
# ✅ CTAs have phone tracking
# ✅ Mobile responsive
```

---

### **Step 8: Validate Schema**

**Use Google Rich Results Test:**

1. Go to: https://search.google.com/test/rich-results
2. Paste page URL or HTML code
3. Verify:
   - ✅ LegalService schema detected
   - ✅ FAQPage schema detected (if applicable)
   - ✅ BreadcrumbList schema detected
   - ✅ No critical errors

---

### **Step 9: Deploy**

```bash
# Commit changes
git add src/pages/felony-defense.njk src/sitemap.njk src/pages/index.njk src/pages/practice-areas.njk

# Commit with descriptive message
git commit -m "Add felony defense service page

- 5,000+ word comprehensive guide
- LegalService, FAQPage, BreadcrumbList schema
- 10 FAQ questions for featured snippets
- Internal links from homepage and practice areas
- SEO-optimized title and description"

# Push to trigger Cloudflare deployment
git push
```

**Deployment Time:** 2-3 minutes via Cloudflare Pages

---

## 🗺️ Creating a New Location Page (Step-by-Step)

### **Example: Creating "Jenison, MI" City Page**

### **Step 1: Create Nunjucks Template File**

**Location:** `src/pages/locations/jenison-mi.njk`

**Note:** Location pages go in `locations/` subfolder

---

### **Step 2: Write Front Matter**

```yaml
---
layout: layouts/page.njk
title: "Jenison MI Criminal Defense Lawyer | Ottawa County Attorney"
description: "Jenison, Michigan criminal defense lawyers. DUI, domestic violence & all charges. Former public defender. Office 6 miles away. (616) 227-3303"
permalink: "/locations/jenison-mi.html"
---
```

**Location Page Title Format:**
```
"[City] MI Criminal Defense Lawyer | [County] Attorney"
```

---

### **Step 3: Write Page Content**

**Content Structure (Standard Location Page):**

1. **H1 Heading** - City + service + location
   ```html
   <h1>Jenison Criminal Defense Lawyer</h1>
   ```

2. **Introduction** - Local positioning + proximity
   ```html
   <p class="lead">Jenison residents facing criminal charges need a lawyer who knows the Ottawa County courts. Sorin & Pyle's Holland office is just 6 miles from Jenison, and we regularly appear in the 58th District Court and 20th Circuit Court.</p>
   ```

3. **Main Content Sections** (6-8 sections typical):
   - Overview of local criminal justice system
   - Court information (58th District Court, 20th Circuit Court)
   - Common charges in Jenison
   - Local law enforcement (Ottawa County Sheriff, Georgetown Township Police)
   - Why choose local representation
   - What to do if arrested in Jenison
   - Links to DUI and domestic violence pages
   - CTA section

4. **Word Count Target:** 800-2,000 words
   - Major cities (Holland, Grand Rapids): 1,200-1,500 words
   - Smaller cities: 800-1,200 words

**Location-Specific Content Tips:**

✅ **DO:**
- Mention specific courts by name (58th District Court - Holland Division)
- Include court addresses
- Name local law enforcement agencies
- Reference local landmarks or events (if relevant)
- Mention distance from office ("6 miles from Jenison")
- Link to county page for more details

❌ **DON'T:**
- Copy-paste content from other location pages
- Make claims about being "the best" or "#1" in the city
- Include inaccurate court information
- Forget to update schema `areaServed` field

---

### **Step 4: Add Schema Markup**

**Required Schema Types for Location Pages:**

1. **LegalService Schema** - Always required
   - Update `areaServed` to include city
   - Update `description` to mention city
2. **BreadcrumbList Schema** - Always required
   - Format: Home > Locations > [City Name]

**Example `areaServed`:**

```json
"areaServed": [
  {
    "@type": "AdministrativeArea",
    "name": "Ottawa County"
  },
  {
    "@type": "City",
    "name": "Jenison"
  },
  {
    "@type": "City",
    "name": "Holland"
  }
]
```

---

### **Step 5: Add to Sitemap**

**Priority for Location Pages:**
- Major cities (Holland, Grand Rapids): 0.85-0.90
- County seats (Grand Haven): 0.85
- Smaller cities: 0.80
- University pages: 0.80-0.85

---

### **Step 6: Add Internal Links**

**Link from Locations Page:**

**File:** `src/pages/locations.njk`

**Add to Ottawa County section:**

```html
<li><a href="locations/jenison-mi.html">Jenison</a></li>
```

**Link from Ottawa County Page:**

**File:** `src/pages/locations/ottawa-county.njk`

**Add to Cities/Townships Served section:**

```html
<li><a href="jenison-mi.html">Jenison</a></li>
```

**Note:** Location pages use relative paths (`jenison-mi.html` not `locations/jenison-mi.html`) since they're already in the locations/ folder.

---

## ✅ Page Template Checklist

Use this checklist for **every new page**:

### **Front Matter:**
- [ ] `layout: layouts/page.njk` correct
- [ ] `title` is 50-60 characters
- [ ] `description` is 150-160 characters
- [ ] `permalink` matches filename

### **Content:**
- [ ] H1 heading includes primary keyword + location
- [ ] Lead paragraph hooks reader and establishes urgency
- [ ] Content is 3,000+ words (service) or 800+ words (location)
- [ ] Includes 5-8 main sections with H2 headings
- [ ] FAQ section has 5-10 questions (if applicable)
- [ ] CTA section at bottom with phone number and contact link
- [ ] No outcome guarantees or "specializing in" language
- [ ] Internal links to related pages

### **Schema Markup:**
- [ ] LegalService schema included
- [ ] FAQPage schema included (if 5+ questions)
- [ ] BreadcrumbList schema included
- [ ] All required fields present (address, telephone, image)
- [ ] `areaServed` lists correct cities/counties
- [ ] `serviceType` lists correct services
- [ ] Schema tested with Google Rich Results Test

### **Sitemap:**
- [ ] Page added to src/sitemap.njk
- [ ] Priority set correctly (0.90-0.95 service, 0.80-0.85 location)
- [ ] `lastmod` date is current

### **Internal Links:**
- [ ] Linked from homepage (if service page)
- [ ] Linked from practice-areas.html (if service page)
- [ ] Linked from locations.html (if location page)
- [ ] Linked from county page (if city page)

### **Build & Test:**
- [ ] `npm run build:html:prod` runs successfully
- [ ] Page displays correctly in dist/ folder
- [ ] Navigation links work
- [ ] Internal links work
- [ ] Phone CTAs have analytics tracking
- [ ] Mobile responsive design works
- [ ] Schema validates with no critical errors

---

## 🎯 SEO Optimization Checklist

### **On-Page SEO:**
- [ ] **Title Tag:** 50-60 chars, primary keyword first, location included
- [ ] **Meta Description:** 150-160 chars, includes phone number and CTA
- [ ] **H1 Heading:** Matches primary keyword, includes location
- [ ] **H2 Headings:** 5-8 descriptive headings with keywords
- [ ] **URL:** Descriptive, hyphenated, keyword-rich (e.g., /felony-defense.html)
- [ ] **Word Count:** 3,000+ words (service) or 800+ words (location)
- [ ] **Keyword Density:** Primary keyword appears 8-12 times naturally
- [ ] **Internal Links:** 3-5 links to related pages
- [ ] **External Links:** 0-2 links to authoritative sources (Michigan Legislature, court websites)
- [ ] **Image Alt Text:** Descriptive, includes keywords (if images used)
- [ ] **Schema Markup:** LegalService, FAQPage, BreadcrumbList

### **Content Quality:**
- [ ] **Unique Content:** No duplicate content from other pages
- [ ] **Helpful Content:** Answers user questions and provides value
- [ ] **E-A-T Signals:** Demonstrates expertise, authority, trustworthiness
- [ ] **Local Signals:** Mentions specific courts, laws, locations
- [ ] **Readability:** 8th-10th grade reading level, short paragraphs
- [ ] **Call to Action:** Clear CTA with phone number and urgency

### **Technical SEO:**
- [ ] **Canonical URL:** Matches sitemap URL
- [ ] **Mobile Responsive:** Displays correctly on mobile devices
- [ ] **Page Speed:** Loads in < 3 seconds (use Cloudflare CDN)
- [ ] **Schema Valid:** No critical errors in Google Rich Results Test
- [ ] **Breadcrumbs:** Schema matches visual breadcrumbs (if applicable)

---

## 📝 Content Writing Guidelines

### **Tone & Voice:**
- **Authentic & Bold:** "WE GIVE A [EXPLETIVE]!" philosophy
- **Empathetic:** Understanding of client stress and fear
- **Confident:** Former public defenders with trial experience
- **Direct:** No legal jargon or corporate speak
- **Judgment-Free:** Especially for substance abuse and mental health clients

### **Writing Style:**
- Use active voice ("We fight for your rights" not "Your rights are fought for")
- Write in second person ("you", "your")
- Use contractions ("don't", "can't", "we'll")
- Vary sentence length (mix short and long sentences)
- Use transitions between sections
- Front-load important information

### **Keyword Integration:**
- **Primary Keyword:** Use 8-12 times naturally throughout page
- **Secondary Keywords:** Use 4-6 times each
- **LSI Keywords:** Include related terms (e.g., "OWI" + "drunk driving" + "DUI")
- **Location Keywords:** Mention cities and counties frequently
- **Avoid Keyword Stuffing:** Write for humans first, search engines second

### **Michigan-Specific Content:**
- Reference Michigan Compiled Laws (MCL 750.xxx)
- Name specific courts (20th Circuit Court, 58th District Court)
- Mention local law enforcement (Ottawa County Sheriff, Holland Police)
- Discuss Michigan-specific penalties (driver responsibility fees until 2018)
- Reference Michigan Supreme Court cases when relevant

---

## 🔗 Internal Linking Strategy

### **Link from Every New Service Page:**
- Homepage (in Practice Areas section)
- practice-areas.html (in appropriate category)
- Related service pages (e.g., DUI page links to license restoration page)

### **Link from Every New Location Page:**
- locations.html (in appropriate county section)
- County page (e.g., ottawa-county.html)
- Related service pages (DUI, domestic violence at minimum)

### **Anchor Text Best Practices:**
- Use descriptive anchor text ("DUI defense attorney" not "click here")
- Vary anchor text (don't always use exact same phrase)
- Include location in anchor text when relevant
- Keep anchor text concise (2-5 words typically)

### **Link Placement:**
- **Within Content:** 2-3 contextual links in body text
- **CTA Section:** 1-2 links to related services
- **Footer:** Automatic via site-wide footer navigation

---

## 🚀 Quick Reference: File Locations

| Page Type | Template Location | Output Location | Sitemap Priority |
|-----------|------------------|-----------------|------------------|
| Service Page | `src/pages/[name].njk` | `dist/[name].html` | 0.90-0.95 |
| City Page | `src/pages/locations/[city]-mi.njk` | `dist/locations/[city]-mi.html` | 0.80-0.90 |
| County Page | `src/pages/locations/[county]-county.njk` | `dist/locations/[county]-county.html` | 0.70-0.75 |
| University Page | `src/pages/locations/[school]-student-defense.njk` | `dist/locations/[school]-student-defense.html` | 0.80-0.85 |

---

## 📚 Additional Resources

- **Full Documentation:** [AI_CONTEXT.md](../../AI_CONTEXT.md) Section 6 (Content Guidelines)
- **Schema Templates:** [SCHEMA_GUIDE.md](SCHEMA_GUIDE.md)
- **CSS Workflows:** [CSS_GUIDE.md](CSS_GUIDE.md)
- **Quick Start:** [QUICK_START.md](../../QUICK_START.md)

---

**Questions?** Check [AI_CONTEXT.md](../../AI_CONTEXT.md) for comprehensive documentation or review existing service pages (dui-defense.njk, domestic-violence-defense.njk) for complete examples.
