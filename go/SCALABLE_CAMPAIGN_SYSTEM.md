# Scalable QR Campaign System

## 🎯 Problem Solved

**Before:** Each new campaign required copying 700+ lines of duplicate code
**After:** New campaigns are ~150 lines of unique content only

**Maintenance:** One brand change updates all campaigns automatically
**Scalability:** Add unlimited campaigns with minimal effort

---

## 📁 New File Structure

```
/go/
├── qr-brand.css              # Shared brand styles (fonts, colors, components)
├── qr-shared.js              # Shared JavaScript (vCard, forms, tracking)
├── _TEMPLATE.html            # Campaign template (copy & customize)
├── _header.html              # Reusable <head> resources (optional reference)
├── _page-header.html         # Reusable logo/tagline (optional reference)
├── _footer.html              # Reusable footer (optional reference)
├── _resources.html           # Reusable resources section (optional reference)
│
├── police-stops.html         # Individual campaigns
├── dui-rights.html
├── know-your-rights.html
├── drug-charges.html
├── domestic-violence.html
├── warrant-help.html
│
└── QR_CAMPAIGN_SYSTEM.md     # Marketing campaign tracking guide
```

---

## 🚀 Creating a New Campaign (5 Minutes)

### Step 1: Copy Template
```bash
cp _TEMPLATE.html [new-campaign-name].html
```

### Step 2: Customize Metadata (lines 5-18)
```html
<title>Your Campaign Title | Sorin & Pyle</title>
<meta name="description" content="Campaign description for SEO">
<meta property="og:title" content="Social media title">
<link rel="canonical" href="https://www.sorinpyle.com/go/[campaign-url]">
```

### Step 3: Set Campaign Name (line 30)
```javascript
initQRCampaign('campaign_name'); // Used for analytics tracking
```

### Step 4: Write Unique Content (lines 40-80)
```html
<div class="intro-box">
    <h1>Your Campaign Headline</h1>
    <p><strong style="color: var(--accent-orange);">Hook text</strong> Description</p>
</div>

<!-- Add campaign-specific content: charts, accordions, lists -->
```

### Step 5: Customize Form (lines 100-130)
Add campaign-specific fields if needed:
```html
<div class="form-group">
    <label for="arrest_date">Date of Arrest *</label>
    <input type="date" id="arrest_date" name="arrest_date" required>
</div>
```

### Step 6: Add Page-Specific CSS (if needed)
Only include truly unique styles (charts, special layouts):
```html
<style>
.special-chart {
    /* Your unique styling */
}
</style>
```

**Done!** Your new campaign page is ready.

---

## 🔧 Shared Components Reference

### 1. **qr-brand.css** - Universal Styles
All campaigns automatically get:
- ✅ Official brand colors (#4076b4 blue, #ff8a28 orange)
- ✅ Brand fonts (Lora headings, Inter body)
- ✅ Buttons, forms, accordions, cards
- ✅ Responsive mobile design
- ✅ Accessibility compliance

**When to update:**
- Brand color changes
- New reusable components needed
- Design system updates

### 2. **qr-shared.js** - Universal Functions
All campaigns automatically get:
- ✅ `downloadVCard()` - Contact saving
- ✅ `toggleAccordion()` - Expandable sections
- ✅ `getUTMParams()` - Campaign tracking
- ✅ `handleConsultationForm()` - Form submission
- ✅ `trackPageView()` - Analytics
- ✅ `initQRCampaign()` - Initialize everything

**When to update:**
- Backend form endpoint changes
- New tracking requirements
- Shared functionality needed

### 3. **Component Files** (Optional Reference)
These files show reusable patterns but aren't imported directly:

- `_header.html` - Standard `<head>` resources
- `_page-header.html` - Logo and tagline markup
- `_footer.html` - Contact footer markup
- `_resources.html` - Standard resource links

Copy/paste these into new campaigns for consistency.

---

## 📊 Campaign-Specific Customizations

### Example: BAC Chart (DUI Page)
```html
<div class="bac-chart">
    <h3>Michigan BAC Legal Limits</h3>
    <div class="bac-levels">
        <div class="bac-level">
            <strong>0.08% BAC</strong>
            <span>Legal limit for drivers 21 and over</span>
        </div>
    </div>
</div>
```

```css
<style>
.bac-chart {
    background: var(--gray-light);
    padding: var(--spacing-lg);
    border-radius: var(--border-radius-md);
    margin: var(--spacing-lg) 0;
}
.bac-level {
    background: var(--white);
    padding: 0.75rem;
    border-left: 4px solid var(--warning-red);
}
</style>
```

### Example: Timeline (Warrant Page)
```html
<div class="timeline">
    <div class="timeline-item">
        <h4>Step 1: Contact Attorney</h4>
        <p>We verify warrant and develop strategy</p>
    </div>
</div>
```

```css
<style>
.timeline {
    position: relative;
    padding-left: 2rem;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 0.5rem;
    width: 2px;
    height: 100%;
    background: var(--accent-orange);
}
</style>
```

---

## 🎨 Available CSS Variables

Use these in your page-specific styles:

### Colors
```css
var(--primary-blue)         /* #4076b4 - Main brand blue */
var(--primary-blue-light)   /* #5a8bc7 */
var(--primary-blue-dark)    /* #2d5a92 */
var(--accent-orange)        /* #ff8a28 - Brand orange */
var(--accent-orange-dark)   /* #e67a1e */
var(--background-color)     /* #FDFBF6 - Cream */
var(--text-color)           /* #212529 - Dark gray */
var(--success-green)        /* #28a745 */
var(--warning-red)          /* #dc3545 */
var(--white)                /* #ffffff */
var(--gray-light)           /* #f8f9fa */
```

### Spacing
```css
var(--spacing-xs)   /* 8px */
var(--spacing-sm)   /* 16px */
var(--spacing-md)   /* 24px */
var(--spacing-lg)   /* 32px */
var(--spacing-xl)   /* 48px */
```

### Shadows & Radius
```css
var(--shadow-subtle)        /* Light shadow */
var(--shadow-soft)          /* Medium shadow */
var(--shadow-medium)        /* Strong shadow */
var(--border-radius-sm)     /* 8px */
var(--border-radius-md)     /* 12px */
var(--border-radius-lg)     /* 16px */
```

---

## 🔄 Updating Existing Campaigns

### Option 1: Leave As-Is (Working Fine)
Current 6 campaigns work perfectly with embedded styles. No migration required unless:
- Making frequent brand changes
- Adding many new campaigns
- Need easier maintenance

### Option 2: Migrate to Shared System
For each file:
1. Replace `<style>` block with `<link rel="stylesheet" href="qr-brand.css">`
2. Add `<script src="qr-shared.js"></script>`
3. Keep only page-specific CSS (~50-100 lines)
4. Update JavaScript to use shared functions

**Effort:** ~15 minutes per campaign
**Benefit:** Centralized updates, smaller files

---

## 📈 Scaling Strategy

### Current: 6 Campaigns
- Manual updates manageable
- Embedded styles work fine
- Limited brand changes

### Growth: 10-20 Campaigns
- **Must migrate** to shared system
- Brand updates become too difficult
- File size adds up (10MB+ of duplicate CSS)

### Growth: 20+ Campaigns
- Consider **build system** (Eleventy, 11ty)
- True templating with includes
- Automated deployment

---

## 🛠️ Maintenance Workflows

### Updating Brand Colors
**Old way:** Edit 6 files × multiple lines = 30+ changes
**New way:** Edit `qr-brand.css` once = 1 change

```css
/* In qr-brand.css */
:root {
    --primary-blue: #4076b4;  /* Change here, updates everywhere */
    --accent-orange: #ff8a28;
}
```

### Adding New Shared Feature
**Example:** Add urgency banner to all campaigns

1. Add to `qr-brand.css`:
```css
.urgency-banner {
    background: var(--warning-red);
    color: var(--white);
    padding: var(--spacing-sm);
    text-align: center;
}
```

2. Use in any campaign:
```html
<div class="urgency-banner">⚠️ Call within 24 hours!</div>
```

### Tracking New Analytics Event
Add to `qr-shared.js`:
```javascript
function trackSpecialAction(actionName) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'special_action', {
            'event_label': actionName
        });
    }
}
```

Use in any campaign:
```html
<button onclick="trackSpecialAction('emergency_call')">Call Now</button>
```

---

## ✅ Quality Checklist for New Campaigns

Before launching a new QR campaign:

### Content
- [ ] Unique, compelling headline
- [ ] Orange-colored hook text for contrast
- [ ] Campaign-specific value proposition
- [ ] Relevant legal information (rights, deadlines, consequences)

### Technical
- [ ] Canonical URL set correctly
- [ ] Campaign name in `initQRCampaign()`
- [ ] UTM parameters in QR code URL
- [ ] Form submission works
- [ ] vCard download works
- [ ] Analytics tracking fires

### Brand Compliance
- [ ] Uses official colors (#4076b4, #ff8a28)
- [ ] Ship logo appears in header
- [ ] Lora headings, Inter body text
- [ ] Cream background, not gradients
- [ ] Touch targets ≥ 44px

### Mobile Optimization
- [ ] Responsive on 375px width
- [ ] Text readable without zoom
- [ ] Buttons easy to tap
- [ ] Forms work on mobile
- [ ] No horizontal scroll

### Accessibility
- [ ] WCAG AA contrast ratios
- [ ] Alt text on images
- [ ] Semantic HTML structure
- [ ] Keyboard navigation works

---

## 🎯 Next-Level Scaling (Future)

When you hit 20+ campaigns, consider:

### 1. Static Site Generator (Eleventy)
```javascript
// campaigns.json
[
  { "slug": "police-stops", "title": "Police Stops Rights" },
  { "slug": "dui-rights", "title": "DUI Rights" }
]

// campaign.njk template
{% for campaign in campaigns %}
  <html>...</html>
{% endfor %}
```

### 2. Build Process
```bash
npm run build  # Generates all campaign pages
npm run deploy # Pushes to server
```

### 3. CMS Integration
- Add campaigns via admin panel
- Generate QR codes automatically
- Track campaign performance dashboard

---

## 📝 Summary

**You now have:**
1. ✅ **qr-brand.css** - One source of truth for all styling
2. ✅ **qr-shared.js** - Reusable JavaScript functions
3. ✅ **_TEMPLATE.html** - Quick-start for new campaigns
4. ✅ **Component references** - Consistent patterns
5. ✅ **This guide** - Complete scaling documentation

**To create a new campaign:**
1. Copy template (1 min)
2. Customize content (3 min)
3. Test & deploy (1 min)

**Total time: ~5 minutes per campaign** (down from 2+ hours)

**Maintenance:** Update shared files once, all campaigns update automatically.

---

**Questions or need help?** Reference this guide or the working examples in existing campaign files.
