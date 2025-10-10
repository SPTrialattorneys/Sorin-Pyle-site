# CSS Architecture Analysis: Shared vs Separate

## 📊 Current Situation

### Main Site CSS (`/css/style.css`)
- **Size:** 1,949 lines
- **Purpose:** Full website (main nav, hero, attorney cards, practice areas, etc.)
- **Scope:** Complex multi-page site with many components

### QR Campaign CSS (`/go/qr-brand.css`)
- **Size:** 447 lines
- **Purpose:** Mobile-first landing pages only
- **Scope:** Simplified single-column layouts

### Duplication Analysis
**Duplicated (~200 lines):**
- ✅ CSS Variables (colors, fonts, spacing) - IDENTICAL
- ✅ Font-face declarations - IDENTICAL
- ✅ Base typography - IDENTICAL
- ✅ Button styles - VERY SIMILAR
- ✅ Form styles - VERY SIMILAR
- ✅ Utility classes - SIMILAR

**Unique to Main Site (~1,700 lines):**
- Main navigation & hamburger menu
- Hero sections
- Attorney cards
- Practice area grids
- Complex page layouts
- Footer complex styling
- Many page-specific components

**Unique to QR Pages (~250 lines):**
- Accordion components
- Timeline visualizations
- Mobile-optimized single column
- Campaign-specific charts/grids
- vCard button styling

---

## 🎯 Three Architecture Options

### Option 1: Keep Separate (Current State)
```
/css/style.css          (1,949 lines - main site)
/go/qr-brand.css        (447 lines - QR campaigns)
```

**Pros:**
- ✅ Complete independence - no conflicts
- ✅ QR pages load faster (smaller CSS)
- ✅ Easy to maintain separately
- ✅ No risk of breaking main site when updating QR
- ✅ Clear separation of concerns

**Cons:**
- ❌ ~200 lines duplicated (colors, fonts, variables)
- ❌ Brand changes need 2 file updates
- ❌ Inconsistency risk if one file updated without the other

**File Structure:**
```
/css/
  style.css           ← Main site
/go/
  qr-brand.css        ← QR campaigns (separate)
  qr-shared.js
```

---

### Option 2: Shared Core + Page-Specific Layers
```
/css/core-brand.css     (200 lines - variables, fonts, base)
/css/main-site.css      (1,750 lines - main site components)
/go/qr-campaigns.css    (250 lines - QR-specific components)
```

**Pros:**
- ✅ Zero duplication - DRY principle
- ✅ Brand changes in ONE place (`core-brand.css`)
- ✅ Guaranteed consistency
- ✅ Each file focused on specific purpose
- ✅ Scalable - add more layers as needed

**Cons:**
- ⚠️ Two HTTP requests for QR pages (core + qr)
- ⚠️ Refactoring work needed (2-3 hours)
- ⚠️ More complex file structure
- ⚠️ Need to test all pages after refactor

**File Structure:**
```
/css/
  core-brand.css      ← Variables, fonts, base (SHARED)
  main-site.css       ← Main site only
/go/
  qr-campaigns.css    ← QR-specific (imports core-brand.css)
  qr-shared.js
```

**Implementation:**
```html
<!-- Main site pages -->
<link rel="stylesheet" href="/css/core-brand.css">
<link rel="stylesheet" href="/css/main-site.css">

<!-- QR campaign pages -->
<link rel="stylesheet" href="../css/core-brand.css">
<link rel="stylesheet" href="qr-campaigns.css">
```

---

### Option 3: Single Shared CSS (Import Pattern)
```
/css/style.css          (All main site)
/go/qr-brand.css        (Imports relevant parts from main)
```

**Using CSS @import:**
```css
/* /go/qr-brand.css */
@import url('../css/style.css') layer(base);

/* Then override/add QR-specific styles */
.qr-specific-component { ... }
```

**Pros:**
- ✅ Main site CSS reused completely
- ✅ No duplication
- ✅ QR pages get brand updates automatically

**Cons:**
- ❌ QR pages load ENTIRE main site CSS (2,000 lines they don't need)
- ❌ Performance hit - slower load times
- ❌ Potential style conflicts
- ❌ @import blocks parallel loading

---

## 📈 Performance Comparison

### Current (Separate Files)
**Main Site:**
- 1 request: `style.css` (1,949 lines ≈ 45KB minified)
- **Load Time:** Fast ✅

**QR Pages:**
- 1 request: `qr-brand.css` (447 lines ≈ 10KB minified)
- **Load Time:** Very Fast ✅✅

### Option 2 (Shared Core)
**Main Site:**
- 2 requests: `core-brand.css` (200 lines ≈ 5KB) + `main-site.css` (1,750 lines ≈ 40KB)
- **Load Time:** Fast ✅ (parallel loading)

**QR Pages:**
- 2 requests: `core-brand.css` (200 lines ≈ 5KB) + `qr-campaigns.css` (250 lines ≈ 6KB)
- **Load Time:** Fast ✅ (parallel loading, cached core)

### Option 3 (Import)
**QR Pages:**
- 2 requests: `style.css` (1,949 lines ≈ 45KB) + `qr-brand.css` (250 lines ≈ 6KB)
- **Load Time:** Slower ❌ (serial loading, unnecessary CSS)

---

## 🏆 RECOMMENDATION: **Option 2 - Shared Core Layer**

### Why This is Best:

#### 1. **Guaranteed Brand Consistency**
- Change orange color once → updates everywhere
- Update font weights once → updates everywhere
- Add new brand colors once → available everywhere

#### 2. **Zero Duplication**
- DRY principle properly applied
- ~200 lines exist in one place only
- Easier to maintain long-term

#### 3. **Performance Optimized**
```
Main site:     5KB (core) + 40KB (main) = 45KB total
QR pages:      5KB (core) + 6KB (qr)    = 11KB total
```
- QR pages stay lightweight
- Core file caches across all pages
- Parallel loading maintains speed

#### 4. **Scalable for Future**
- Add blog section → create `blog.css` importing core
- Add client portal → create `portal.css` importing core
- Each section independent but brand-consistent

#### 5. **Easy Maintenance**
```
Brand update workflow:
1. Edit /css/core-brand.css (colors, fonts, spacing)
2. Done - all pages updated ✅
```

---

## 📋 Implementation Plan for Option 2

### Step 1: Create Core Brand File
**Create `/css/core-brand.css`:**
```css
/* Extract from style.css lines 1-90 */
/* Font faces */
@font-face { ... }

/* CSS Variables */
:root {
  --primary-blue: #4076B4;
  --accent-orange: #FF8A28;
  /* ... all brand variables */
}

/* Base Typography */
body { font-family: var(--font-body); }
h1, h2, h3 { font-family: var(--font-headings); }

/* Base Button Styles */
.btn { ... }

/* Base Form Styles */
input, textarea, select { ... }
```

### Step 2: Update Main Site CSS
**Update `/css/style.css`:**
```css
/* Remove duplicated core (lines 1-90) */
/* Keep only main site specific styles */

/* Main Navigation */
.nav { ... }

/* Hero Section */
.hero { ... }

/* Attorney Cards */
.attorney-card { ... }

/* etc. */
```

### Step 3: Update QR CSS
**Update `/go/qr-brand.css`:**
```css
/* Remove duplicated core */
/* Keep only QR-specific components */

/* Accordion */
.accordion-item { ... }

/* Timeline */
.timeline { ... }

/* Campaign-specific */
.bac-chart { ... }
```

### Step 4: Update HTML Files
**Main site pages:**
```html
<link rel="stylesheet" href="/css/core-brand.css">
<link rel="stylesheet" href="/css/main-site.css">
```

**QR campaign pages:**
```html
<link rel="stylesheet" href="../css/core-brand.css">
<link rel="stylesheet" href="qr-campaigns.css">
```

### Step 5: Test Everything
- [ ] Main site pages load correctly
- [ ] QR campaign pages load correctly
- [ ] All styles apply properly
- [ ] No visual regressions
- [ ] Performance metrics maintained

---

## 🔄 Alternative: Keep Current + Sync Script

If you want to **avoid refactoring** but still prevent drift:

### Create Sync Script
```javascript
// sync-brand-vars.js
// Copies variables from main CSS to QR CSS

const fs = require('fs');

const mainCSS = fs.readFileSync('./css/style.css', 'utf8');
const qrCSS = fs.readFileSync('./go/qr-brand.css', 'utf8');

// Extract :root variables from main
const rootVars = mainCSS.match(/:root\s*{[^}]+}/s)[0];

// Replace in QR CSS
const updatedQR = qrCSS.replace(/:root\s*{[^}]+}/s, rootVars);

fs.writeFileSync('./go/qr-brand.css', updatedQR);
console.log('✅ Brand variables synced');
```

**Run after brand changes:**
```bash
node sync-brand-vars.js
```

---

## 📊 Decision Matrix

| Factor | Separate (Current) | Shared Core (Recommended) | Import (Not Recommended) |
|--------|-------------------|---------------------------|--------------------------|
| **Duplication** | ❌ ~200 lines | ✅ Zero | ✅ Zero |
| **Consistency** | ⚠️ Manual sync | ✅ Automatic | ✅ Automatic |
| **Performance (Main)** | ✅ 45KB, 1 request | ✅ 45KB, 2 requests | ✅ 45KB, 1 request |
| **Performance (QR)** | ✅ 11KB, 1 request | ✅ 11KB, 2 requests | ❌ 51KB, 2 requests |
| **Maintenance** | ⚠️ Update 2 files | ✅ Update 1 file | ✅ Update 1 file |
| **Setup Effort** | ✅ Done | ⚠️ 2-3 hours | ❌ Complex |
| **Conflict Risk** | ✅ None | ⚠️ Low | ❌ High |
| **Scalability** | ⚠️ Moderate | ✅ Excellent | ❌ Poor |

---

## 🎯 FINAL RECOMMENDATION

### **Implement Option 2: Shared Core Architecture**

**When to do it:**
- **Now:** If you plan 10+ QR campaigns
- **Soon:** If making frequent brand changes
- **Later:** If only minor tweaks ahead

**Effort vs Benefit:**
- **Time:** 2-3 hours of refactoring
- **Benefit:** Permanent consistency, easier maintenance, zero duplication

**Alternative (Easier):**
Keep current setup + create sync script for brand variables only

---

## 💡 Quick Decision Helper

**Choose Shared Core (Option 2) if:**
- ✅ You'll create 10+ QR campaigns
- ✅ Brand changes happen frequently
- ✅ Multiple people update the site
- ✅ Long-term maintenance matters

**Keep Separate (Current) if:**
- ✅ Only 6-10 campaigns planned
- ✅ Brand is stable (rare changes)
- ✅ You're the only maintainer
- ✅ Want to avoid refactoring work

**My Verdict:** **Option 2 (Shared Core)** is the professional, scalable solution. Worth the 2-3 hour investment for long-term benefits.
