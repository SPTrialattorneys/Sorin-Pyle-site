# Google Search Console "Page with Redirect" Fix

## 🔍 Issues Found

Your Search Console showed these redirect issues:

1. **HTTP → HTTPS redirects** (normal, but needs proper setup)
   - `http://sorinpyle.com/`
   - `http://www.sorinpyle.com/`

2. **Non-WWW → WWW inconsistency**
   - `https://sorinpyle.com/` (no www)
   - `https://www.sorinpyle.com/` (with www)

3. **Duplicate homepage URLs**
   - `https://www.sorinpyle.com/`
   - `https://www.sorinpyle.com/index.html`

4. **Query parameter on practice-areas**
   - `https://www.sorinpyle.com/practice-areas.html?q={search_term_string}`

---

## ✅ What Was Fixed in .htaccess

The updated .htaccess now includes these redirects (lines 80-99):

### 1. Force HTTPS
All HTTP requests redirect to HTTPS:
- `http://www.sorinpyle.com/` → `https://www.sorinpyle.com/`

### 2. Force WWW
All non-www requests redirect to www:
- `https://sorinpyle.com/` → `https://www.sorinpyle.com/`

### 3. Remove index.html from URL
- `https://www.sorinpyle.com/index.html` → `https://www.sorinpyle.com/`

**Result**: All URLs now canonicalize to:
```
https://www.sorinpyle.com/
```

---

## 🎯 Actions Required in Google Search Console

### Step 1: Set Preferred Domain (CRITICAL)

1. Go to **Google Search Console**
2. Click on **Settings** (gear icon)
3. Under **Property settings**:
   - Verify you have property for: `https://www.sorinpyle.com`
   - If not, click "Add property" and add it

4. **Remove or ignore these properties** (if you have them):
   - `http://sorinpyle.com`
   - `http://www.sorinpyle.com`
   - `https://sorinpyle.com` (no www)

**Only monitor**: `https://www.sorinpyle.com`

### Step 2: Update Sitemap.xml References

Your sitemap is already correct (uses `https://www.sorinpyle.com/`), but verify:

1. In Search Console, go to **Sitemaps**
2. Submit: `https://www.sorinpyle.com/sitemap.xml`
3. Remove any old sitemap submissions if they exist

### Step 3: Request Re-indexing

For each page showing "page with redirect":

1. Go to **URL Inspection** tool
2. Enter the CANONICAL URL (with https://www and without index.html):
   - `https://www.sorinpyle.com/`
   - `https://www.sorinpyle.com/locations.html`
   - `https://www.sorinpyle.com/practice-areas.html`
   - `https://www.sorinpyle.com/resources.html`

3. Click **Request Indexing**

### Step 4: Wait for Google to Re-crawl

- Re-crawling typically takes 3-7 days
- Check back in Search Console after 1 week
- The "page with redirect" errors should disappear

---

## 📋 Verification Checklist

After uploading the new .htaccess, test these URLs:

### Test 1: HTTP redirects to HTTPS
```
http://www.sorinpyle.com/
Should redirect to → https://www.sorinpyle.com/
```

### Test 2: Non-WWW redirects to WWW
```
https://sorinpyle.com/
Should redirect to → https://www.sorinpyle.com/
```

### Test 3: index.html redirects to root
```
https://www.sorinpyle.com/index.html
Should redirect to → https://www.sorinpyle.com/
```

### Test 4: All pages use canonical URLs
Visit any page and check the address bar shows:
```
https://www.sorinpyle.com/[page-name].html
```

---

## 🔧 How to Test

### Online Tool (Easy)
1. Go to: https://httpstatus.io/
2. Enter your URLs
3. Verify you get **301 Redirect** to the canonical version

### Command Line (Advanced)
```bash
curl -I http://sorinpyle.com/
# Should show: Location: https://www.sorinpyle.com/

curl -I https://sorinpyle.com/
# Should show: Location: https://www.sorinpyle.com/

curl -I https://www.sorinpyle.com/index.html
# Should show: Location: https://www.sorinpyle.com/
```

---

## 📊 Expected Timeline

| Timeframe | What Happens |
|-----------|--------------|
| **Immediately** | .htaccess redirects active |
| **1-3 days** | Google re-crawls when you request indexing |
| **3-7 days** | Search Console updates status |
| **7-14 days** | "Page with redirect" errors clear |
| **2-4 weeks** | Full re-indexing of all pages |

---

## ⚠️ Important Notes

### 1. Canonical Tags
Verify ALL your HTML pages have canonical tags pointing to the www version:

```html
<!-- Check each page has this (with correct URL) -->
<link rel="canonical" href="https://www.sorinpyle.com/page-name.html">
```

Your pages already have this ✅

### 2. Internal Links
All internal links should use relative paths or www version:
```html
<!-- Good -->
<a href="/attorneys.html">Attorneys</a>
<a href="https://www.sorinpyle.com/attorneys.html">Attorneys</a>

<!-- Avoid -->
<a href="https://sorinpyle.com/attorneys.html">Attorneys</a>
```

### 3. External Links
Update any external profiles to use canonical URL:
- Google Business Profile
- Social media profiles
- Directory listings (Avvo, Justia, etc.)
- Citations

All should link to: `https://www.sorinpyle.com/`

---

## 🎯 Query Parameter Issue (practice-areas.html?q=)

The query parameter `?q={search_term_string}` is likely from:
- Search engines testing your site
- A search form somewhere
- Dynamic URL generation

### Option 1: Ignore It (Recommended)
Google will figure out it's the same page. No action needed.

### Option 2: Block Parameters in Search Console
1. Go to **Settings** → **Crawling**
2. Under **URL parameters**
3. Add parameter: `q`
4. Set to: "Doesn't change page content"

### Option 3: Redirect in .htaccess
Uncomment lines 96-99 in .htaccess if you want to remove all query parameters from practice-areas.html

---

## ✅ Success Criteria

You'll know this is fixed when:

1. ✅ Search Console shows 0 "page with redirect" errors
2. ✅ All pages indexed under `https://www.sorinpyle.com`
3. ✅ Visiting any URL variant redirects to canonical version
4. ✅ Coverage report shows "Valid" for all important pages

---

## 📞 What to Do After Upload

1. **Upload new .htaccess** to your web server
2. **Test the redirects** using the verification checklist above
3. **Request re-indexing** in Search Console for affected URLs
4. **Monitor Search Console** over next 1-2 weeks
5. **Update external links** to use canonical URLs

---

## 🔮 Expected Results

After 2-4 weeks, you should see:

- ✅ All pages indexed properly
- ✅ No "page with redirect" errors
- ✅ Consistent URLs in search results
- ✅ Potentially better rankings (clearer signals to Google)
- ✅ More accurate analytics (no split traffic between URL variants)

---

## ❓ Troubleshooting

### If redirects don't work:
1. Check if `.htaccess` is uploading correctly
2. Verify Apache `mod_rewrite` is enabled on your server
3. Check server error logs for issues
4. Contact hosting support if needed

### If Search Console still shows errors after 2 weeks:
1. Verify .htaccess is working with online tools
2. Check canonical tags are correct
3. Request indexing again
4. Consider submitting a sitemap update

---

## 📋 Quick Action Checklist

- [ ] Upload new .htaccess file to server
- [ ] Test HTTP → HTTPS redirect
- [ ] Test non-www → www redirect
- [ ] Test index.html → root redirect
- [ ] Verify canonical URLs in Search Console property
- [ ] Submit sitemap in Search Console
- [ ] Request indexing for affected pages
- [ ] Update Google Business Profile URL
- [ ] Update social media profile links
- [ ] Monitor Search Console for 2 weeks
- [ ] Verify all "page with redirect" errors cleared

---

**Need help?** If redirects aren't working after uploading .htaccess, your hosting provider may need to enable mod_rewrite module.
