# Quick Brand CSS Update Guide

## For Each Remaining File (5 files)

### Files to Update:
1. dui-rights.html
2. know-your-rights.html
3. drug-charges.html
4. domestic-violence.html
5. warrant-help.html

---

## Step 1: Replace CSS Link (Lines ~20-37)

**FIND:**
```html
<link rel="canonical" href="https://www.sorinpyle.com/go/[PAGE]">
<link rel="icon" type="image/png" href="../images/favicon.png">

<!-- Critical CSS for Above-the-Fold -->
<style>
    :root {
        --primary-blue: #1B3A61;
        --accent-orange: #F26522;
        --success-green: #28a745;
        --warning-red: #dc3545;
        --text-dark: #212529;
        --text-light: #6c757d;
        --white: #ffffff;
        --gray-light: #f8f9fa;
        --border-radius: 12px;
        --shadow: 0 4px 6px rgba(0,0,0,0.1);
        --shadow-lg: 0 10px 25px rgba(0,0,0,0.15);
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
        line-height: 1.6;
        color: var(--text-dark);
        background: linear-gradient(135deg, #1B3A61 0%, #2c5282 100%);
        min-height: 100vh;
    }
```

**REPLACE WITH:**
```html
<link rel="canonical" href="https://www.sorinpyle.com/go/[PAGE]">
<link rel="icon" type="image/png" href="../images/favicon.png">

<!-- Sorin & Pyle Brand Stylesheet -->
<link rel="stylesheet" href="qr-brand.css">

<!-- Page-Specific Styles -->
<style>
```

---

## Step 2: Delete Generic CSS (Keep Only Page-Specific)

**DELETE everything from line ~38 to ~470** EXCEPT:

### For dui-rights.html - KEEP:
```css
/* Intro with red warning */
.intro {
    background: var(--gray-light);
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    margin-bottom: var(--spacing-lg);
    border-left: 4px solid var(--warning-red);
}

/* BAC Chart */
.bac-chart {
    background: var(--gray-light);
    border-radius: var(--border-radius-md);
    padding: var(--spacing-lg);
    margin: var(--spacing-lg) 0;
}

.bac-chart h3 {
    text-align: center;
    margin-bottom: var(--spacing-md);
}

.bac-levels {
    display: grid;
    gap: 0.75rem;
}

.bac-level {
    background: var(--white);
    padding: 0.75rem;
    border-radius: var(--border-radius-sm);
    border-left: 4px solid var(--warning-red);
}

.bac-level strong {
    display: block;
    margin-bottom: 0.25rem;
}

.bac-level span {
    color: var(--text-light);
    font-size: 0.9rem;
}

/* Warning box */
.warning-box {
    background: #fff3cd;
    border: 2px solid #ffc107;
    border-radius: var(--border-radius-md);
    padding: var(--spacing-md);
    margin: var(--spacing-lg) 0;
}

.warning-box strong {
    color: var(--warning-red);
}

/* Critical item styling */
.right-item.critical {
    border-color: var(--warning-red);
    border-width: 2px;
}
```

### For know-your-rights.html - KEEP:
```css
/* Amendment Grid */
.amendment-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-md);
    margin: var(--spacing-lg) 0;
}

.amendment-card {
    background: linear-gradient(135deg, var(--primary-blue) 0%, var(--primary-blue-dark) 100%);
    color: var(--white);
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    text-align: center;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.amendment-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-medium);
}

.amendment-number {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.amendment-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.amendment-summary {
    font-size: 0.85rem;
    opacity: 0.9;
}

/* Magic Words boxes */
.magic-words {
    background: var(--gray-light);
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    margin: var(--spacing-md) 0;
    border-left: 4px solid var(--accent-orange);
}

.magic-words strong {
    color: var(--accent-orange);
}

.quick-action {
    background: var(--primary-blue);
    color: var(--white);
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    margin: var(--spacing-md) 0;
}

@media (max-width: 480px) {
    .amendment-grid {
        grid-template-columns: 1fr;
    }
}
```

### For drug-charges.html - KEEP:
```css
/* Drug Schedule Table */
.schedule-table {
    width: 100%;
    border-collapse: collapse;
    margin: var(--spacing-lg) 0;
    background: var(--white);
}

.schedule-table th,
.schedule-table td {
    padding: var(--spacing-sm);
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}

.schedule-table th {
    background: var(--primary-blue);
    color: var(--white);
    font-weight: 600;
}

.schedule-table tr:hover {
    background: var(--gray-light);
}

/* Penalty Levels */
.penalty-level {
    padding: var(--spacing-sm);
    margin: var(--spacing-sm) 0;
    border-radius: var(--border-radius-sm);
    border-left: 4px solid var(--accent-orange);
}

.penalty-level.severe {
    border-color: var(--warning-red);
    background: #fff3cd;
}

.penalty-level strong {
    display: block;
    margin-bottom: 0.25rem;
}

/* Consequence Section */
.consequence-section {
    background: var(--gray-light);
    padding: var(--spacing-lg);
    border-radius: var(--border-radius-md);
    margin: var(--spacing-lg) 0;
}
```

### For domestic-violence.html - KEEP:
```css
/* Consequence Grid */
.consequence-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--spacing-md);
    margin: var(--spacing-lg) 0;
}

.consequence-card {
    background: var(--white);
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    text-align: center;
    border: 2px solid var(--warning-red);
}

.consequence-icon {
    font-size: 2rem;
    margin-bottom: var(--spacing-sm);
}

.consequence-title {
    font-weight: 600;
    color: var(--primary-blue);
}

/* Do/Don't Grid */
.do-dont-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--spacing-md);
    margin: var(--spacing-lg) 0;
}

.do-section {
    background: #d4edda;
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    border-left: 4px solid var(--success-green);
}

.dont-section {
    background: #f8d7da;
    padding: var(--spacing-md);
    border-radius: var(--border-radius-md);
    border-left: 4px solid var(--warning-red);
}

.do-section h4 {
    color: var(--success-green);
}

.dont-section h4 {
    color: var(--warning-red);
}

/* Emergency box */
.emergency-box {
    background: #f8d7da;
    border: 2px solid var(--warning-red);
    border-radius: var(--border-radius-md);
    padding: var(--spacing-md);
    margin: var(--spacing-lg) 0;
    text-align: center;
}

.emergency-box strong {
    color: var(--warning-red);
}

@media (max-width: 480px) {
    .consequence-grid,
    .do-dont-grid {
        grid-template-columns: 1fr;
    }
}
```

### For warrant-help.html - KEEP:
```css
/* Timeline */
.timeline {
    position: relative;
    padding-left: 2rem;
    margin: var(--spacing-lg) 0;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0.5rem;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--accent-orange);
}

.timeline-item {
    position: relative;
    margin-bottom: var(--spacing-lg);
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -1.75rem;
    top: 0.5rem;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--accent-orange);
    border: 2px solid var(--white);
}

.timeline-item h4 {
    margin-bottom: var(--spacing-sm);
}

/* Pulse Animation */
.pulse {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(242, 101, 34, 0.7);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(242, 101, 34, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(242, 101, 34, 0);
    }
}

/* Warrant Types */
.warrant-types {
    background: var(--gray-light);
    padding: var(--spacing-lg);
    border-radius: var(--border-radius-md);
    margin: var(--spacing-lg) 0;
}

.warrant-type {
    background: var(--white);
    padding: var(--spacing-sm);
    margin-bottom: var(--spacing-sm);
    border-radius: var(--border-radius-sm);
    border-left: 4px solid var(--accent-orange);
}

.warrant-type strong {
    display: block;
    margin-bottom: 0.25rem;
}

.warrant-type span {
    color: var(--text-light);
    font-size: 0.9rem;
}

/* Danger box */
.danger-box {
    background: #f8d7da;
    border: 2px solid var(--warning-red);
    border-radius: var(--border-radius-md);
    padding: var(--spacing-md);
    margin: var(--spacing-lg) 0;
}

.danger-box strong {
    color: var(--warning-red);
}
```

---

## Step 3: Update HTML Classes

### Change button classes:
```html
<!-- OLD -->
<button onclick="downloadVCard()" class="cta-primary">

<!-- NEW -->
<button onclick="downloadVCard()" class="btn btn-primary btn-block">
```

### Verify intro class exists:
```html
<!-- Should be: -->
<div class="intro">
    <p><strong style="color: var(--accent-orange);">...</strong> ...</p>
</div>
```

---

## Step 4: Verify & Test

After updating each file, check:
- [ ] Page loads without errors
- [ ] Ship logo appears
- [ ] Colors are brand compliant (#4076b4 blue, #ff8a28 orange)
- [ ] Background is cream, not purple gradient
- [ ] All interactive elements work
- [ ] Page-specific features display correctly

---

## Quick Status Check

Run this to see which pages still have old CSS:
```bash
grep -l "#1B3A61" go/*.html
```

Should return nothing when all updates are complete.

---

**Note**: All pages already have contrast fixes and orange call buttons applied. This update is just to link the shared brand CSS file and remove duplicate code.
