# QR Campaign Migration Summary

## ✅ Police-Stops.html - MIGRATED

**Changes Made:**
1. ✅ Added `<script src="qr-shared.js"></script>` in `<head>`
2. ✅ Replaced ~100 lines of JavaScript with `initQRCampaign('police_stops')`
3. ✅ Updated vCard button: `onclick="downloadVCard('Police Stops')"`
4. ✅ Simplified Google Analytics setup
5. ✅ File reduced from ~530 to ~427 lines

**Result:** Fully functional with shared system

---

## 🔄 Remaining 5 Files - Quick Migration Pattern

For each remaining file, apply these 3 edits:

### Step 1: Add Shared JS (in <head>, after qr-brand.css)
```html
<!-- Sorin & Pyle Brand Stylesheet -->
<link rel="stylesheet" href="qr-brand.css">

<!-- ADD THIS LINE: -->
<script src="qr-shared.js"></script>
```

### Step 2: Replace ALL JavaScript (near end of file)
**FIND** (~100 lines starting with):
```javascript
<script>
    // Download vCard
    function downloadVCard() {
        const vcard = `BEGIN:VCARD
        ...
        [lots of code]
        ...
    </script>

    <!-- Google Analytics -->
    <script async src="..."></script>
    <script>
        window.dataLayer = ...
        ...
    </script>
```

**REPLACE WITH** (just 15 lines):
```javascript
<!-- Initialize Campaign -->
<script>
    initQRCampaign('[campaign_name]'); // police_stops, dui_rights, etc.
</script>

<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'YOUR-GA-ID');
</script>
```

### Step 3: Update vCard Button
**FIND**:
```html
<button onclick="downloadVCard()" class="...">
```

**REPLACE WITH**:
```html
<button onclick="downloadVCard('[Campaign Display Name]')" class="...">
```

---

## Campaign Name Mapping

| File | Campaign Name (for initQRCampaign) | Display Name (for downloadVCard) |
|------|-----------------------------------|----------------------------------|
| ✅ police-stops.html | `'police_stops'` | `'Police Stops'` |
| dui-rights.html | `'dui_rights'` | `'DUI Rights'` |
| know-your-rights.html | `'know_your_rights'` | `'Know Your Rights'` |
| drug-charges.html | `'drug_charges'` | `'Drug Charges'` |
| domestic-violence.html | `'domestic_violence'` | `'Domestic Violence'` |
| warrant-help.html | `'warrant_help'` | `'Warrant Help'` |

---

## Expected File Size Reductions

| File | Before | After | Reduction |
|------|--------|-------|-----------|
| ✅ police-stops.html | ~530 lines | ~427 lines | -103 lines |
| dui-rights.html | ~750 lines | ~650 lines | -100 lines |
| know-your-rights.html | ~850 lines | ~750 lines | -100 lines |
| drug-charges.html | ~800 lines | ~700 lines | -100 lines |
| domestic-violence.html | ~775 lines | ~675 lines | -100 lines |
| warrant-help.html | ~800 lines | ~700 lines | -100 lines |

**Total Reduction:** ~600 lines of duplicate JavaScript removed

---

## Testing Checklist (After Each Migration)

- [ ] Page loads without errors
- [ ] vCard download works
- [ ] Form submission works
- [ ] UTM parameters captured
- [ ] Analytics tracking fires
- [ ] Accordions toggle correctly
- [ ] Scroll animations work

---

## Quick Apply Instructions

### For dui-rights.html:
1. Find line ~23: Add `<script src="qr-shared.js"></script>` after qr-brand.css
2. Find line ~610: Replace ALL `<script>` blocks with initQRCampaign pattern
3. Find `onclick="downloadVCard()"`: Change to `onclick="downloadVCard('DUI Rights')"`

### For know-your-rights.html:
1. Find line ~23: Add `<script src="qr-shared.js"></script>` after qr-brand.css
2. Find line ~720: Replace ALL `<script>` blocks with initQRCampaign pattern
3. Find `onclick="downloadVCard()"`: Change to `onclick="downloadVCard('Know Your Rights')"`

### For drug-charges.html:
1. Find line ~23: Add `<script src="qr-shared.js"></script>` after qr-brand.css
2. Find line ~680: Replace ALL `<script>` blocks with initQRCampaign pattern
3. Find `onclick="downloadVCard()"`: Change to `onclick="downloadVCard('Drug Charges')"`

### For domestic-violence.html:
1. Find line ~23: Add `<script src="qr-shared.js"></script>` after qr-brand.css
2. Find line ~660: Replace ALL `<script>` blocks with initQRCampaign pattern
3. Find `onclick="downloadVCard()"`: Change to `onclick="downloadVCard('Domestic Violence')"`

### For warrant-help.html:
1. Find line ~23: Add `<script src="qr-shared.js"></script>` after qr-brand.css
2. Find line ~690: Replace ALL `<script>` blocks with initQRCampaign pattern
3. Find `onclick="downloadVCard()"`: Change to `onclick="downloadVCard('Warrant Help')"`

---

## Verification Command

After all migrations, verify shared JS is linked:
```bash
grep -l "qr-shared.js" go/*.html
```

Should return all 6 campaign files.

---

## Benefits Achieved

✅ **One Source of Truth:** All JavaScript in qr-shared.js
✅ **Easier Maintenance:** Update tracking logic once, affects all pages
✅ **Smaller Files:** ~600 fewer lines total
✅ **Consistent Behavior:** All campaigns use same functions
✅ **Scalability:** New campaigns automatically get all functionality

---

**Status:** 1 of 6 complete
**Next:** Apply pattern to remaining 5 files
