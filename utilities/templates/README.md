# Schema Templates

JSON templates for common schema.org markup patterns used on the Sorin & Pyle website.

## Available Templates

### 1. schema-legalservice.json
**Purpose:** Legal service offering schema markup for practice area pages

**Placeholders:**
- `{{SERVICE_NAME}}` - Name of service (e.g., "DUI Defense", "Domestic Violence Defense")
- `{{DESCRIPTION}}` - Brief description (1-2 sentences)
- `{{SERVICE_TYPE_1}}`, `{{SERVICE_TYPE_2}}`, `{{SERVICE_TYPE_3}}` - Service types
- `{{IMAGE_URL}}` - Image URL for Google Rich Results

**Required Fields (Google Rich Results):**
- ✅ address (already included)
- ✅ telephone (already included)
- ✅ image (placeholder - must fill)

**Example Usage:**
```bash
node utilities/generate-schema.js --type=LegalService
# Prompts for service name, description, types, image URL
# Outputs formatted JSON-LD schema
```

---

### 2. schema-faqpage.json
**Purpose:** Frequently Asked Questions schema for FAQ sections

**Placeholders:**
- `{{QUESTION_1}}` through `{{QUESTION_5}}` - FAQ questions
- `{{ANSWER_1}}` through `{{ANSWER_5}}` - FAQ answers

**Best Practices:**
- Use 5-10+ questions for Google Rich Snippets eligibility
- Keep answers 100-200 words (detailed but concise)
- Target "People Also Ask" boxes in Google
- Natural language questions matching user search intent

**Example Usage:**
```bash
node utilities/generate-schema.js --type=FAQPage
# Prompts for number of questions and each Q&A pair
# Outputs formatted JSON-LD schema
```

---

### 3. schema-breadcrumblist.json
**Purpose:** Navigation breadcrumb schema for site hierarchy

**Placeholders:**
- `{{PARENT_PAGE}}` - Parent page name (e.g., "Practice Areas")
- `{{PARENT_URL}}` - Parent page URL (e.g., "practice-areas.html")
- `{{CURRENT_PAGE}}` - Current page name (e.g., "DUI Defense")
- `{{CURRENT_URL}}` - Current page URL (e.g., "dui-defense.html")

**Best Practices:**
- Always start with Home (position 1)
- Increment position numbers sequentially
- Use full URLs (https://www.sorinpyle.com/...)
- Maximum 3-5 levels recommended

**Example Usage:**
```bash
node utilities/generate-schema.js --type=BreadcrumbList
# Prompts for parent/current page names and URLs
# Outputs formatted JSON-LD schema
```

---

## Interactive CLI Generator

**Command:**
```bash
node utilities/generate-schema.js
```

**Features:**
- Interactive prompts for all required values
- Validates schema structure
- Outputs formatted JSON-LD ready to copy-paste
- Usage instructions included in output

**Example Session:**
```bash
$ node utilities/generate-schema.js

╔════════════════════════════════════════╗
║   Schema Markup Generator CLI         ║
╚════════════════════════════════════════╝

Available Schema Types:

  LegalService
    Legal service offering (practice areas, defense services)

  FAQPage
    Frequently Asked Questions (5-10+ Q&As)

  BreadcrumbList
    Navigation breadcrumbs (Home > Parent > Current)

Select schema type: LegalService

📋 LegalService Schema Generator

Service name (e.g., "DUI Defense"): Felony Defense
Description (1-2 sentences): Aggressive felony defense representation...
Service type 1 (e.g., "DUI Defense"): Felony Defense
...

✓ Generated Schema:

────────────────────────────────────────────────────────────
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "Felony Defense",
  ...
}
────────────────────────────────────────────────────────────
```

---

## Manual Template Usage

If you prefer manual editing:

1. Copy template file: `cp utilities/templates/schema-legalservice.json my-schema.json`
2. Replace all `{{PLACEHOLDERS}}` with actual values
3. Validate with: `npm run validate:schema` (after adding to HTML)
4. Wrap in `<script type="application/ld+json">` tags
5. Add to .njk template file

---

## Validation

After generating and adding schema to a page:

```bash
# Build HTML
npm run build:html:prod

# Validate all schemas
npm run validate:schema

# Test with Google Rich Results Test
# https://search.google.com/test/rich-results
```

---

## Adding New Templates

To add a new schema type:

1. **Create template file:**
   ```bash
   utilities/templates/schema-newtype.json
   ```

2. **Add to SCHEMA_TYPES in generate-schema.js:**
   ```javascript
   const SCHEMA_TYPES = {
     'LegalService': 'Legal service offering...',
     'FAQPage': 'Frequently Asked Questions...',
     'BreadcrumbList': 'Navigation breadcrumbs...',
     'NewType': 'Description of new type'  // Add here
   };
   ```

3. **Add generator function:**
   ```javascript
   async function generateNewType() {
     // Prompt for values
     // Load template
     // Replace placeholders
     // Return schema
   }
   ```

4. **Add to switch statement:**
   ```javascript
   case 'NewType':
     schema = await generateNewType();
     break;
   ```

---

## Related Documentation

- [SCHEMA_GUIDE.md](../docs/SCHEMA_GUIDE.md) - Schema best practices and validation
- [utilities/validate-schema.js](../validate-schema.js) - Schema validation script
- [Google Rich Results Test](https://search.google.com/test/rich-results) - Official validation tool

---

**Last Updated:** 2025-11-24
