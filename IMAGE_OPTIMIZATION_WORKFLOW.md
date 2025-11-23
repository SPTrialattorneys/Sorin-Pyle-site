# Image Optimization Workflow for Sorin & Pyle Website

## Quick Reference

**Goal:** All images should be < 20KB for thumbnails, < 50KB for full-size photos, < 200KB for hero/OG images

**Tools:**
- **TinyPNG API** for AVIF optimization (best compression)
- **ImageMagick** for quick local resizing (fallback)

**API Key Location:** Ask Claude or check your password manager

---

## Workflow for Adding New Images

### Step 1: Save Original to `samples/originals/`

```bash
# Always keep high-resolution originals
cp new-photo.jpg samples/originals/
```

**Why:** Originals are your master copies. Never optimize these directly.

### Step 2: Determine Target Sizes

| Use Case | Target Size | Example |
|----------|-------------|---------|
| Homepage attorney cards | 220x220 | `sorin-panainte-*-220w.avif` |
| Profile page main photo | 400x400 | `sorin-panainte-*.avif` |
| Gallery photos (portrait) | 400x500 | `jonathan-pyle-trial-attorney-*.avif` |
| Hero images (desktop) | 800x600 | `holland-michigan-*.avif` |
| Hero images (mobile) | 450x300 | `holland-michigan-*-450w.avif` |
| Blog post images | 800x600 | `sorin-panainte-gun-lake-*.avif` |
| OG/social share images | 1200x630 | `og-*.avif` |

### Step 3: Run Optimization Script

**Option A: Use existing script (recommended)**

Edit `optimize_images_tinify.py` and add your new image:

```python
{
    "name": "New Attorney Photo",
    "source": "samples/originals/new-photo.jpg",
    "crop": {"method": "cover", "width": 3200, "height": 3200},  # Square
    "outputs": [
        {"width": 220, "filename": "images/new-photo-220w.avif"},
        {"width": 400, "filename": "images/new-photo.avif"}
    ]
},
```

Then run:
```bash
python optimize_images_tinify.py
```

**Option B: Quick single image (manual)**

Go to https://tinypng.com/ and upload manually (if you need just one image quickly)

### Step 4: Use Responsive Images in HTML

```html
<!-- For attorney photos (220px displayed, 400px available for retina) -->
<img src="images/attorney-220w.avif"
     srcset="images/attorney-220w.avif 220w,
             images/attorney.avif 400w"
     sizes="220px"
     alt="Attorney Name - Description"
     loading="lazy"
     width="400"
     height="400">

<!-- For hero images (responsive mobile/desktop) -->
<img src="images/hero-450w.avif"
     srcset="images/hero-450w.avif 450w,
             images/hero.avif 800w"
     sizes="(max-width: 767px) 100vw, 800px"
     alt="Description"
     loading="eager"
     fetchpriority="high"
     width="800"
     height="600">
```

---

## Image Naming Convention

**Format:** `[subject]-[descriptor]-[location/context]-[size].avif`

**Examples:**
- `sorin-panainte-criminal-defense-attorney-holland-mi-220w.avif`
- `jonathan-pyle-trial-attorney-west-michigan.avif`
- `holland-michigan-criminal-defense-lawyers-450w.avif`

**Rules:**
- Use lowercase and hyphens (SEO friendly)
- Include attorney name for profile photos
- Include location keywords for local SEO
- Include width suffix for responsive images (`-220w`, `-450w`, `-800w`)
- Keep descriptive for accessibility and SEO

---

## Crop Parameters Guide

### Portrait Photos (Attorney Profiles)

**4:5 Ratio (400x500)** - Gallery photos, profile main photos
```python
"crop": {"method": "cover", "width": 3200, "height": 4000}
```

**Square (400x400)** - Homepage cards, attorneys page thumbnails
```python
"crop": {"method": "cover", "width": 3200, "height": 3200}
```

### Landscape Photos (Hero Images, Blog Posts)

**4:3 Ratio (800x600)** - Standard hero images
```python
"crop": {"method": "cover", "width": 3200, "height": 2400}
```

**16:9 Ratio (1200x675)** - Wide hero images
```python
"crop": {"method": "cover", "width": 3200, "height": 1800}
```

**No Crop** - Use original aspect ratio
```python
"crop": None
```

---

## File Size Targets

| Image Type | Target Size | Max Acceptable | Current Average |
|------------|-------------|----------------|-----------------|
| Thumbnail (220x220) | 5-10 KB | 15 KB | 5 KB ✓ |
| Standard (400x400) | 10-20 KB | 30 KB | 11 KB ✓ |
| Gallery (400x500) | 15-25 KB | 40 KB | 20 KB ✓ |
| Hero mobile (450x300) | 8-15 KB | 25 KB | 8 KB ✓ |
| Hero desktop (800x600) | 15-30 KB | 50 KB | 15 KB ✓ |
| Blog images (800x600) | 20-40 KB | 80 KB | 30 KB ✓ |
| OG images (1200x630) | 40-80 KB | 150 KB | - |

**If file exceeds target:** Lower quality setting or reduce dimensions

---

## TinyPNG API Usage

**Free Tier:** 500 compressions/month
**Current Usage:** Check with `tinify.compression_count` in scripts
**Cost:** $0.009 per image after 500 (very cheap)

**Monitor usage:**
```bash
python -c "import tinify; tinify.key='YOUR_KEY'; tinify.validate(); print(f'Used: {tinify.compression_count}/500')"
```

---

## Common Image Tasks

### Task: Add new attorney photo

1. Save original to `samples/originals/IMG_XXXX.jpg`
2. Edit `optimize_images_tinify.py`, add entry with 220w and 400w sizes
3. Run `python optimize_images_tinify.py`
4. Update HTML with new image paths and responsive srcset

### Task: Update hero image

1. Save original to `samples/originals/`
2. Create 450w (mobile) and 800w (desktop) versions via script
3. Update HTML `<img>` tag with srcset
4. Update preload links in `<head>`
5. Update OG image meta tag if used for social sharing

### Task: Add blog post image

1. Save original to `samples/` (or originals if keeping long-term)
2. Create 800w version via script
3. Add to blog post HTML with proper alt text
4. Update BlogPosting schema `image` property

### Task: Bulk re-optimize all images

```bash
python optimize_all_images_tinify.py
```

This will re-process all site images from source files.

---

## Quality Control Checklist

Before committing new images:

- [ ] File size < target (see table above)
- [ ] Responsive srcset with multiple sizes
- [ ] Descriptive, SEO-friendly filename
- [ ] Alt text is descriptive and includes keywords
- [ ] Loading="lazy" for below-fold images
- [ ] Loading="eager" + fetchpriority="high" for hero images
- [ ] Preload critical above-fold images
- [ ] Original saved to samples/originals/
- [ ] Width and height attributes specified (prevents CLS)

---

## Troubleshooting

**Problem:** Image looks blurry on retina displays
**Solution:** Provide 2x srcset (e.g., 220w + 400w for 220px display)

**Problem:** Hero image loads slowly
**Solution:** Add `<link rel="preload">` in `<head>`, use fetchpriority="high"

**Problem:** File size too large (>50KB for standard photo)
**Solution:** Re-run Tinify with smaller dimensions or check if original is unnecessarily huge

**Problem:** API quota exceeded
**Solution:** Either wait for next month or upgrade ($25 for 10,000 compressions)

**Problem:** Image not found in samples/originals/
**Solution:** Check CLAUDE.md for source file mapping (e.g., IMG_3013.jpg → sorin-panainte-*.avif)

---

## Scripts Reference

### Primary Scripts

**optimize_images_tinify.py** - Main homepage images (hero, attorney cards)
**optimize_all_images_tinify.py** - ALL site images (profile pages, gallery, blog)

### Usage

```bash
# Homepage images only (6 images)
python optimize_images_tinify.py

# All site images (20+ images)
python optimize_all_images_tinify.py

# Install tinify if needed
pip install tinify
```

### Script Structure

```python
images_to_process = [
    {
        "name": "Descriptive Name",
        "source": "samples/originals/source-file.jpg",
        "crop": {"method": "cover", "width": 3200, "height": 3200},  # or None
        "outputs": [
            {"width": 220, "filename": "images/output-220w.avif"},
            {"width": 400, "filename": "images/output.avif"}
        ]
    },
]
```

---

## Performance Impact

**Before Tinify optimization:**
- Homepage: 223 KB images (Sorin 49KB, Jonathan 42KB, Hero 45KB)
- Profile pages: 579 KB images (6 gallery photos @ 60-80KB each)
- Blog: 209 KB image (Gun Lake photo)

**After Tinify optimization:**
- Homepage: 51 KB images (77% reduction!)
- Profile pages: ~150 KB images (74% reduction!)
- Blog: ~30 KB images (86% reduction!)

**PageSpeed Impact:**
- LCP: 4.3s → 2.2-2.5s (48% improvement)
- Performance Score: 78 → 92-95 (expected)

---

## Best Practices Summary

1. **Always keep originals** in samples/originals/
2. **Use TinyPNG API** for best compression (77% smaller than ImageMagick!)
3. **Provide responsive images** with srcset and sizes attributes
4. **Target < 20KB** for thumbnails, < 50KB for standard photos
5. **Use descriptive, SEO-friendly** filenames with keywords
6. **Preload critical images** (hero, above-fold)
7. **Lazy load below-fold images** for better performance
8. **Monitor API usage** (500 free/month)
9. **Document new images** in CLAUDE.md with source file mapping
10. **Test on mobile** to ensure responsive images load correctly

---

## Future Improvements

- [ ] Consider automated image optimization on git pre-commit hook
- [ ] Create simple drag-and-drop web interface for one-off optimizations
- [ ] Set up Cloudflare image optimization (paid feature)
- [ ] Implement WebP fallback for older browsers (currently AVIF-only)
- [ ] Create separate sizes for blog thumbnails vs full blog images

---

**Last Updated:** November 21, 2025
**Maintained By:** Claude Code + Sorin & Pyle Team
