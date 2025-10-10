# QR Campaign Pages - Brand Compliance Update Instructions

## Overview
This document provides instructions for updating the remaining 5 QR campaign pages to match official Sorin & Pyle brand guidelines.

## ✅ Completed
- `qr-brand.css` - Shared brand stylesheet created with official colors and fonts
- `police-stops.html` - **UPDATED** to use brand CSS and ship logo

## 🔄 Remaining Pages to Update
1. `dui-rights.html`
2. `know-your-rights.html`
3. `drug-charges.html`
4. `domestic-violence.html`
5. `warrant-help.html`

## Update Steps for Each Page

### Step 1: Replace CSS Link Section

**FIND** (around lines 20-24):
```html
<link rel="canonical" href="https://www.sorinpyle.com/go/[PAGE-NAME]">
<link rel="icon" type="image/png" href="../images/favicon.png">

<!-- Critical CSS for Above-the-Fold -->
<style>
    :root {
        --primary-blue: #1B3A61;
        --accent-orange: #F26522;
        /* ... many more lines of CSS ... */
    }
```

**REPLACE WITH**:
```html
<link rel="canonical" href="https://www.sorinpyle.com/go/[PAGE-NAME]">
<link rel="icon" type="image/png" href="../images/favicon.png">

<!-- Sorin & Pyle Brand Stylesheet -->
<link rel="stylesheet" href="qr-brand.css">

<!-- Page-Specific Styles -->
<style>
```

### Step 2: Keep Only Page-Specific CSS

After the `<style>` tag, **DELETE** all the generic/shared CSS and **KEEP ONLY** page-specific styles like:

- Intro box custom styling
- Page-specific layouts (charts, grids, timelines)
- Custom animations specific to that page
- Loading states
- Any unique visual elements

**Example of what to KEEP** (varies by page):
```css
/* Intro box styling */
.intro-box h1 {
    color: var(--white);
}

/* vCard button with icon */
.btn svg {
    width: 24px;
    height: 24px;
}

/* Page-specific elements like BAC chart, timeline, etc. */
.bac-chart { /* DUI page only */ }
.timeline { /* Warrant page only */ }
.amendment-grid { /* Know Your Rights page only */ }
```

### Step 3: Update HTML Classes

Replace old CSS classes with brand-compliant classes from `qr-brand.css`:

**Button Classes**:
- `class="cta-primary"` → `class="btn btn-primary btn-block"`
- `class="submit-btn"` → `class="btn btn-primary btn-block"`

**Intro Section**:
- `class="intro"` → `class="intro-box"`

**Logo is already correct**:
- Keep: `<img src="../images/logo-icon.svg" alt="Sorin & Pyle">`

### Step 4: Verify Brand Colors

Ensure NO hardcoded colors remain that conflict with brand:
- ❌ Remove: `#1B3A61` (old blue)
- ❌ Remove: `#F26522` (old orange)
- ❌ Remove: Purple gradients
- ✅ Use: `var(--primary-blue)` = `#4076b4`
- ✅ Use: `var(--accent-orange)` = `#ff8a28`
- ✅ Use: `var(--background-color)` = `#FDFBF6`

## Page-Specific Notes

### dui-rights.html
**Keep these unique elements**:
- `.bac-chart` - BAC levels display
- `.bac-level` - Individual BAC cards
- Arrest date form field styling

### know-your-rights.html
**Keep these unique elements**:
- `.amendment-grid` - 4th/5th/6th Amendment cards
- `.amendment-card` - Interactive cards
- `.magic-words` - Rights statement boxes
- `scrollToSection()` JavaScript function

### drug-charges.html
**Keep these unique elements**:
- `.schedule-table` - Drug schedule table
- `.penalty-level` - Severity indicators
- `.consequence-section` - Collateral consequences
- Substance selection dropdown styling

### domestic-violence.html
**Keep these unique elements**:
- `.consequence-grid` - Impact cards
- `.do-dont-grid` - Two-column do/don't layout
- Safe contact preference styling
- No-contact order warnings

### warrant-help.html
**Keep these unique elements**:
- `.timeline` - 5-step surrender process
- `.timeline-item::before` - Timeline dots
- `.pulse` animation - Urgent CTA
- `.warrant-types` - Warrant explanation cards
- Urgency-based form logic

## Testing Checklist

After updating each page, verify:

- [ ] Page loads without console errors
- [ ] Ship logo appears in header
- [ ] Colors match brand (#4076b4 blue, #ff8a28 orange)
- [ ] Fonts are Lora (headings) and Inter (body)
- [ ] Background is cream (#FDFBF6), not purple gradient
- [ ] vCard download button works
- [ ] Form submission works
- [ ] All links work correctly
- [ ] Responsive design works on mobile
- [ ] Accordion/interactive elements function
- [ ] Page-specific features work (charts, grids, etc.)

## Brand Compliance Checklist

- [ ] Official brand colors used throughout
- [ ] Ship logo visible in header
- [ ] Inter font for body text
- [ ] Lora font for headings
- [ ] Subtle shadows (not heavy)
- [ ] Clean, professional appearance
- [ ] Matches main site aesthetic
- [ ] No purple gradients
- [ ] Touch targets >= 44px
- [ ] Accessible contrast ratios

## Files Reference

- **Brand Guidelines**: `Sorin & Pyle Brand Guidelines.pdf`
- **Main Site CSS**: `../css/style.css` (for reference)
- **Brand QR CSS**: `qr-brand.css` (shared stylesheet)
- **Ship Logo**: `../images/logo-icon.svg`

## Questions?

Contact information:
- Sorin & Pyle, PC
- (616) 227-3303
- justice@callsbp.com
- 217 E 24th St Ste 107, Holland, MI 49423

---

**Last Updated**: October 8, 2025
**Status**: police-stops.html completed, 5 pages remaining
