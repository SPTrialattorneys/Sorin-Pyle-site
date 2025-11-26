# Schema Markup Guide - Sorin & Pyle Website

**⏱️ 10-minute read** | For full documentation, see [AI_CONTEXT.md](../../AI_CONTEXT.md) Section 5.3

---

## 📚 Quick Navigation

**Other Guides:**
- [Quick Start](../../QUICK_START.md) - 5-minute onboarding
- [CSS Guide](CSS_GUIDE.md) - CSS workflow and critical CSS
- [Content Guide](CONTENT_GUIDE.md) - Creating new pages (coming soon)
- [Troubleshooting](TROUBLESHOOTING.md) - Common errors (coming soon)

---

## 🎯 Schema Types Used on Site

The website uses structured data (schema.org JSON-LD) to help search engines understand content and enable Google Rich Results.

### **Schema Types by Page:**

| Schema Type | Used On | Purpose |
|------------|---------|---------|
| **LegalService** | Service pages (DUI, DV, Expungement) | Google Rich Results, local search |
| **FAQPage** | Pages with FAQ sections | Featured snippets, "People also ask" |
| **BreadcrumbList** | All service/location pages | Search result breadcrumbs |
| **Person** | Attorney profiles | Knowledge panel, author attribution |
| **WebSite** | Homepage | Sitelinks search box |
| **BlogPosting** | Blog posts | Article rich results |

---

## 🔧 LegalService Schema Template

### **Complete Template** (Copy-Paste)

Use this for **all service pages** (DUI defense, domestic violence, expungement, etc.)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "Sorin & Pyle, Trial Lawyers - [SERVICE NAME]",
  "legalName": "Sorin & Pyle, PC",
  "description": "[150-200 word description of service]",
  "url": "https://www.sorinpyle.com/[page-name].html",
  "telephone": "+16162273303",
  "email": "justice@callsbp.com",
  "logo": "https://www.sorinpyle.com/images/logo.svg",
  "image": "https://www.sorinpyle.com/images/ottawa-county-courthouse.avif",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "217 E 24th St Ste 107",
    "addressLocality": "Holland",
    "addressRegion": "MI",
    "postalCode": "49423",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 42.7875,
    "longitude": -86.1089
  },
  "areaServed": [
    {
      "@type": "AdministrativeArea",
      "name": "Ottawa County"
    },
    {
      "@type": "City",
      "name": "Holland"
    },
    {
      "@type": "City",
      "name": "Grand Rapids"
    }
  ],
  "serviceType": [
    "[Primary Service]",
    "[Secondary Service]",
    "[Tertiary Service]"
  ],
  "priceRange": "Free Consultation",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59",
    "description": "Phone consultations and messages 24/7. Office visits Mon-Fri 9 AM - 5 PM."
  },
  "founder": [
    {
      "@type": "Person",
      "@id": "https://www.sorinpyle.com/sorin-panainte.html#person",
      "name": "Sorin Panainte",
      "jobTitle": "Criminal Defense Attorney",
      "url": "https://www.sorinpyle.com/sorin-panainte.html"
    },
    {
      "@type": "Person",
      "@id": "https://www.sorinpyle.com/jonathan-pyle.html#person",
      "name": "Jonathan Pyle",
      "jobTitle": "Criminal Defense Attorney",
      "url": "https://www.sorinpyle.com/jonathan-pyle.html"
    }
  ]
}
</script>
```

### **Placeholder Instructions:**

1. **[SERVICE NAME]** - e.g., "DUI Defense", "Domestic Violence Defense", "Record Expungement"
2. **[150-200 word description]** - Brief service description mentioning key benefits
3. **[page-name].html** - Actual page filename (e.g., dui-defense.html)
4. **areaServed** - Add all relevant cities/counties served
5. **serviceType** - List 3-5 specific services offered on this page

### **Real Example from dui-defense.njk:**

```json
"serviceType": [
  "DUI Defense",
  "OWI Defense",
  "Super Drunk Defense",
  "Breathalyzer Defense",
  "Field Sobriety Test Defense"
]
```

---

## 📝 FAQPage Schema Template

### **Complete Template** (Copy-Paste)

Use this for pages with FAQ sections (5+ questions minimum).

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text here?]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Complete answer text. Can be 100-300 words. Include all relevant details from the HTML answer.]"
      }
    },
    {
      "@type": "Question",
      "name": "[Second question?]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Second answer text]"
      }
    }
  ]
}
</script>
```

### **Best Practices:**

- ✅ Include 5-10+ questions (Google recommends comprehensive FAQ sections)
- ✅ Use natural language questions (how people actually search)
- ✅ Write complete answers (100-300 words each)
- ✅ Extract text from HTML but remove formatting
- ✅ One FAQPage schema per page (don't duplicate)

### **Real Example from dui-defense.njk:**

```json
{
  "@type": "Question",
  "name": "Can I refuse field sobriety tests?",
  "acceptedAnswer": {
    "@type": "Answer",
    "text": "Yes, you can refuse field sobriety tests in Michigan. Unlike the chemical test (breathalyzer or blood test), there is no legal penalty for refusing roadside sobriety tests. These tests are voluntary and are designed to give the officer evidence to arrest you. However, your refusal can be used as evidence in court, and the officer may still arrest you based on other observations. If you refuse sobriety tests, remain polite but firm, and ask to speak with your attorney immediately."
  }
}
```

---

## 🗺️ BreadcrumbList Schema Template

### **Complete Template** (Copy-Paste)

Use this for **all service pages and location pages** to show navigation hierarchy in search results.

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.sorinpyle.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Parent Category]",
      "item": "https://www.sorinpyle.com/[parent-page].html"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Current Page Title]",
      "item": "https://www.sorinpyle.com/[current-page].html"
    }
  ]
}
</script>
```

### **Example Breadcrumbs:**

**Service Page (dui-defense.html):**
```
Home > Practice Areas > DUI Defense
```

**Location Page (holland-mi.html):**
```
Home > Locations > Holland, MI
```

**County Page (ottawa-county.html):**
```
Home > Locations > Ottawa County
```

---

## ⚠️ Common Schema Errors & Fixes

### **Error 1: Missing Required Fields (CRITICAL)**

**Problem:** Google Rich Results Test showing "Missing field 'address'" or "Missing field 'telephone'"

**Solution:** All LegalService schemas MUST include:
```json
"address": { "@type": "PostalAddress", ... },
"telephone": "+16162273303",
"image": "https://www.sorinpyle.com/images/ottawa-county-courthouse.avif"
```

**Fixed:** November 19, 2025 (see CLAUDE.md lines 1481-1521)

---

### **Error 2: Duplicate priceRange Property**

**Problem:** Homepage had `priceRange` appearing twice in LegalService schema

**Solution:** Remove duplicate, keep only one:
```json
"priceRange": "Free Consultation"
```

**Fixed:** November 19, 2025 (index.html)

---

### **Error 3: AggregateRating with Zero Reviews**

**Problem:** Homepage had `aggregateRating` with `reviewCount: 0` (invalid)

**Solution:** Remove entire `aggregateRating` block unless you have **visible reviews on your own pages**

**Important:** Embedded Google Maps reviews don't count - reviews must be on your website pages.

**Fixed:** November 19, 2025 (index.html)

---

### **Error 4: SearchAction Causing Invalid URL Crawls**

**Problem:** Google crawling `practice-areas.html?q={search_term_string}` literally

**Cause:** SearchAction schema declared but site has no search functionality

**Solution:** Remove `potentialAction` with SearchAction from WebSite schema:

```json
// ❌ REMOVE THIS if no search function
"potentialAction": {
  "@type": "SearchAction",
  "target": "https://www.sorinpyle.com/practice-areas.html?q={search_term_string}",
  "query-input": "required name=search_term_string"
}
```

**Fixed:** November 19, 2025 (index.html)

---

### **Error 5: Unnamed Item (Provider Reference)**

**Problem:** "Unnamed item" error from incorrect provider reference format

**Wrong:**
```json
"provider": {
  "@type": "LegalService",
  "@id": "https://www.sorinpyle.com/#legalservice"
}
```

**Correct:**
```json
"provider": {
  "@id": "https://www.sorinpyle.com/#legalservice"
}
```

**Fix:** Remove duplicate `@type` from provider reference - just use `@id`

---

## 🧪 Google Rich Results Testing

### **How to Test Schema Markup:**

1. **Build HTML First:**
   ```bash
   npm run build:html:prod
   ```

2. **Open Google Rich Results Test:**
   - URL: https://search.google.com/test/rich-results
   - Paste page URL or HTML code

3. **Expected Results:**
   - ✅ "Page is eligible for rich results"
   - ✅ LegalService, FAQPage, BreadcrumbList detected
   - ✅ No critical errors

4. **Common Warnings (OK to ignore):**
   - "The property X is not recognized by Google for an object of type Y" - Safe to ignore if not required

### **Pages to Test:**
- index.html (Homepage)
- dui-defense.html (Service page with all 3 schema types)
- domestic-violence-defense.html (Service page)
- faq.html (FAQPage schema)
- jonathan-pyle.html (Person schema)
- sorin-panainte.html (Person schema)

---

## ✅ Schema Validation Checklist

Use this checklist **before deploying** any page with schema markup:

### **LegalService Schema:**
- [ ] Includes `address` (required by Google)
- [ ] Includes `telephone` (required by Google)
- [ ] Includes `image` (required by Google)
- [ ] `areaServed` lists all relevant cities/counties
- [ ] `serviceType` lists 3-5 specific services
- [ ] `openingHoursSpecification` reflects 24/7 phone availability
- [ ] `founder` references both attorney profile pages
- [ ] No duplicate properties (e.g., two `priceRange` fields)
- [ ] No `aggregateRating` with `reviewCount: 0`

### **FAQPage Schema:**
- [ ] Contains 5-10+ questions
- [ ] Questions use natural language ("Can I...", "What happens if...", "How much does...")
- [ ] Answers are complete (100-300 words)
- [ ] Only one FAQPage schema per page
- [ ] All questions/answers match HTML content

### **BreadcrumbList Schema:**
- [ ] Position starts at 1 (Home)
- [ ] Each item has name and item URL
- [ ] Hierarchy matches actual navigation
- [ ] Final item is current page

### **General:**
- [ ] All URLs are absolute (https://www.sorinpyle.com/...)
- [ ] Phone number in international format (+16162273303)
- [ ] Schema placed in `<head>` section (before `</head>` closing tag)
- [ ] JSON-LD format (`<script type="application/ld+json">`)
- [ ] Valid JSON syntax (no trailing commas, proper escaping)

---

## 📋 When to Add Each Schema Type

### **LegalService Schema:**
- ✅ All service pages (DUI, domestic violence, expungement, license restoration)
- ✅ Practice area pages
- ❌ Homepage (use WebSite schema instead)
- ❌ Blog posts (use BlogPosting schema instead)

### **FAQPage Schema:**
- ✅ Pages with 5+ FAQ questions
- ✅ Dedicated FAQ page (faq.html)
- ✅ Service pages with comprehensive FAQ sections
- ❌ Pages with only 1-2 sidebar questions

### **BreadcrumbList Schema:**
- ✅ All service pages
- ✅ All location pages
- ✅ All attorney profile pages
- ❌ Homepage (no breadcrumbs on home)
- ❌ 404/500 error pages

### **Person Schema:**
- ✅ Attorney profile pages (jonathan-pyle.html, sorin-panainte.html)
- ✅ Referenced in LegalService schema `founder` field
- ❌ Standalone on homepage

---

## 🔗 Schema Cross-Referencing

Use `@id` to link schemas together:

### **Example: Attorney Profile Referenced in Service Page**

**In jonathan-pyle.html:**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://www.sorinpyle.com/jonathan-pyle.html#person",
  "name": "Jonathan Pyle",
  ...
}
```

**In dui-defense.html:**
```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "founder": [
    {
      "@type": "Person",
      "@id": "https://www.sorinpyle.com/jonathan-pyle.html#person"
    }
  ]
}
```

**Benefits:**
- Google understands relationship between service and attorney
- Improves Knowledge Graph connections
- Better author attribution

---

## 🎯 Schema Best Practices

1. **Be Accurate:** Schema must match visible page content
2. **Be Complete:** Include all recommended fields, not just required
3. **Be Consistent:** Use same format across all pages (international phone, absolute URLs)
4. **Test Before Deploy:** Use Google Rich Results Test
5. **Update Regularly:** If page content changes, update schema
6. **Don't Over-Optimize:** Avoid keyword stuffing in descriptions
7. **Don't Lie:** False information can result in manual penalties

---

## 📚 Additional Resources

- **Schema.org Documentation:** https://schema.org/LegalService
- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **Google Search Central:** https://developers.google.com/search/docs/appearance/structured-data
- **W3C JSON-LD Validator:** https://json-ld.org/playground/

---

## 🔍 Quick Reference: Schema by File

| File | LegalService | FAQPage | BreadcrumbList | Person |
|------|--------------|---------|----------------|--------|
| index.html | ❌ | ❌ | ❌ | ❌ |
| dui-defense.html | ✅ | ✅ | ✅ | ❌ |
| domestic-violence-defense.html | ✅ | ✅ | ✅ | ❌ |
| record-expungement.html | ✅ | ✅ | ✅ | ❌ |
| drivers-license-restoration.html | ✅ | ❌ | ✅ | ❌ |
| faq.html | ❌ | ✅ | ❌ | ❌ |
| jonathan-pyle.html | ❌ | ❌ | ❌ | ✅ |
| sorin-panainte.html | ❌ | ❌ | ❌ | ✅ |

---

**Questions?** Check [AI_CONTEXT.md](../../AI_CONTEXT.md) Section 5.3 (Schema Markup) or [CLAUDE.md](../../CLAUDE.md) November 19, 2025 schema fixes for detailed examples.
