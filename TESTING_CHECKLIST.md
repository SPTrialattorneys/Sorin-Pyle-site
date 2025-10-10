# Digital Business Card Testing Checklist

## Last Updated: October 9, 2025
## Overall Status: 0% Complete (Setup Phase)

---

## 1. Baseline Metrics (Before Changes)

### Card Pages
| Page | Lighthouse Performance | Accessibility | Best Practices | SEO | Status |
|------|----------------------|---------------|----------------|-----|--------|
| card.html | TBD | TBD | TBD | TBD | ⏸️ Pending |
| card/sorin.html | TBD | TBD | TBD | TBD | ⏸️ Pending |
| card/jonathan.html | TBD | TBD | TBD | TBD | ⏸️ Pending |

### Main Site Sample Pages
| Page | Lighthouse Performance | Accessibility | Best Practices | SEO | Status |
|------|----------------------|---------------|----------------|-----|--------|
| index.html | TBD | TBD | TBD | TBD | ⏸️ Pending |
| attorneys.html | TBD | TBD | TBD | TBD | ⏸️ Pending |
| contact.html | TBD | TBD | TBD | TBD | ⏸️ Pending |
| practice-areas.html | TBD | TBD | TBD | TBD | ⏸️ Pending |
| locations.html | TBD | TBD | TBD | TBD | ⏸️ Pending |

---

## 2. File Backups

### Backup Status
- [ ] card.html → card.html.backup
- [ ] card/sorin.html → card-sorin.html.backup
- [ ] card/jonathan.html → card-jonathan.html.backup
- [ ] css/style.css → css/style.css.backup

**Backup Location**: Same directory as originals
**Backup Date**: TBD

---

## 3. Phase 1 Testing: Visual & Structural Improvements

### 3.1 Hero Section Modernization
**Status**: ⏸️ Not Started

#### card.html Testing
- [ ] Background pattern displays correctly
- [ ] Logo sizing correct (200px+)
- [ ] Gradient overlay visible
- [ ] Mobile responsive
- [ ] Desktop display
- [ ] Tablet display

#### card/sorin.html Testing
- [ ] Photo size 220px
- [ ] Pulse animation plays once on load
- [ ] Layered box-shadow displays
- [ ] Role badge displays correctly
- [ ] Photo circular and properly cropped
- [ ] Mobile responsive

#### card/jonathan.html Testing
- [ ] Photo size 220px
- [ ] Pulse animation plays once on load
- [ ] Layered box-shadow displays
- [ ] Role badge displays correctly
- [ ] Photo circular and properly cropped
- [ ] Mobile responsive

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 3.2 Bento Grid Layout
**Status**: ⏸️ Not Started

#### Desktop Testing (1920x1080)
- [ ] Grid displays asymmetrical layout
- [ ] Large modules prominent (CTA, Form, Bio)
- [ ] Medium modules sized correctly (Services, Contact)
- [ ] Small modules sized correctly (Social, Footer)
- [ ] Spacing consistent
- [ ] Visual hierarchy clear

#### Tablet Testing (768x1024)
- [ ] Grid adapts to 2-column layout
- [ ] Content readable and accessible
- [ ] No horizontal scrolling
- [ ] Touch targets adequate size

#### Mobile Testing (375x667)
- [ ] Grid stacks to single column
- [ ] Content fully visible
- [ ] No horizontal scrolling
- [ ] Proper spacing maintained

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 3.3 Card Section Visual Enhancements
**Status**: ⏸️ Not Started

- [ ] Gradient backgrounds on alternating sections
- [ ] Hover states work on interactive sections
- [ ] Scale animations smooth (no jank)
- [ ] Scroll animations trigger correctly
- [ ] Service list items slide in
- [ ] Gradient dividers display instead of borders
- [ ] All animations performant (< 5ms)

**Issues Found**: None yet
**Issues Resolved**: None yet

---

## 4. Phase 2 Testing: Content Strategy

### 4.1 CTA Hierarchy
**Status**: ⏸️ Not Started

- [ ] Step numbering displays
- [ ] Business hours accurate (Mon-Fri 9-5)
- [ ] Weekend appointment notice present
- [ ] Social proof displays
- [ ] Visual hierarchy clear
- [ ] Mobile CTA accessible

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 4.2 Services Section
**Status**: ⏸️ Not Started

- [ ] Service icons display correctly
- [ ] Accordion expand/collapse works
- [ ] Service descriptions visible when expanded
- [ ] Process steps clear
- [ ] Success rates display
- [ ] Keyboard accessible
- [ ] Mobile friendly

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 4.3 Testimonials
**Status**: ⏸️ Not Started

- [ ] Testimonial cards display
- [ ] Carousel auto-rotates (8 sec)
- [ ] Navigation dots work
- [ ] Manual navigation works
- [ ] Quotation marks visible
- [ ] Client initials display
- [ ] Case type and outcome visible
- [ ] Accessible to keyboard users

**Issues Found**: None yet
**Issues Resolved**: None yet

---

## 5. Phase 3 Testing: Interactive Features

### 5.1 Video Integration Placeholder
**Status**: ⏸️ Not Started

- [ ] Placeholder section displays
- [ ] "Coming Soon" message visible
- [ ] YouTube embed structure ready
- [ ] Play button overlay styled
- [ ] Only on attorney cards (not firm card)

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 5.2 Enhanced Lead Capture Form
**Status**: ⏸️ Not Started

#### Functionality
- [ ] Progress indicator displays
- [ ] Real-time validation works
- [ ] Error messages helpful and clear
- [ ] Privacy reassurance visible
- [ ] Lock icon displays
- [ ] Appointment type dropdown works
- [ ] Contact time selector works
- [ ] Business hours notice visible

#### Mobile Testing
- [ ] Form inputs mobile-optimized
- [ ] Tel input shows number keyboard
- [ ] Email input shows email keyboard
- [ ] Form submits correctly
- [ ] Success message displays

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 5.3 Smart Contact Saving
**Status**: ⏸️ Not Started

#### vCard Download
- [ ] vCard file downloads
- [ ] Works on iOS Safari
- [ ] Works on Android Chrome
- [ ] Contact info accurate
- [ ] Opens native contact app

#### QR Code
- [ ] QR code generates dynamically
- [ ] QR code scannable
- [ ] Links to correct URL
- [ ] Mobile optimized

#### Wallet Passes
- [ ] Apple Wallet button displays
- [ ] Google Wallet button displays
- [ ] Wallet pass generates
- [ ] Pass contains correct info

#### Share Functionality
- [ ] Share link button works
- [ ] Copy to clipboard works
- [ ] Success notification shows
- [ ] Analytics tracks shares

**Issues Found**: None yet
**Issues Resolved**: None yet

---

## 6. Phase 4 Testing: Performance & Accessibility

### 6.1 Image Optimization
**Status**: ⏸️ Not Started

- [ ] Lazy loading implemented
- [ ] Lazy loading works correctly
- [ ] srcset attributes present
- [ ] Responsive images load
- [ ] Attorney photos optimized (< 100KB)
- [ ] Blur-up effect displays
- [ ] Performance improved

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 6.2 Accessibility Audit
**Status**: ⏸️ Not Started

#### Color Contrast
- [ ] All text meets 4.5:1 ratio minimum
- [ ] Headings contrast checked
- [ ] Body text contrast checked
- [ ] Button text contrast checked
- [ ] Link text contrast checked

#### ARIA & Semantics
- [ ] aria-labels on all interactive elements
- [ ] Heading hierarchy logical (h1→h2→h3)
- [ ] Alt text on all images
- [ ] Form labels properly associated
- [ ] Skip links present

#### Keyboard Navigation
- [ ] All elements tabbable
- [ ] Tab order logical
- [ ] Focus indicators visible
- [ ] No keyboard traps
- [ ] Enter/Space activate buttons

#### Screen Reader Testing (NVDA)
- [ ] Page structure announced correctly
- [ ] All content accessible
- [ ] Forms navigable
- [ ] Images described
- [ ] Links descriptive

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 6.3 Mobile-First Optimization
**Status**: ⏸️ Not Started

#### Tap Targets
- [ ] All buttons 48x48px minimum
- [ ] All links 48x48px minimum
- [ ] Form inputs adequate size
- [ ] Proper spacing between targets

#### Form Inputs
- [ ] Tel input type set
- [ ] Email input type set
- [ ] Autocomplete attributes present

#### Mobile Features
- [ ] Sticky CTA bar displays on scroll
- [ ] Sticky CTA positioned correctly
- [ ] Touch actions optimized

#### Device Testing
- [ ] Tested on iPhone SE (small screen)
- [ ] Tested on iPhone 14 Pro (large screen)
- [ ] Tested on Samsung Galaxy (Android)

**Issues Found**: None yet
**Issues Resolved**: None yet

---

## 7. Site-Wide Regression Testing

### 7.1 CSS Isolation Verification
**Status**: ⏸️ Not Started
**Pass Rate**: 0/18 tests

| Page | Header | Footer | Buttons | Forms | Navigation | Hero | Cards | Hover | Overall |
|------|--------|--------|---------|-------|------------|------|-------|-------|---------|
| index.html | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| attorneys.html | ⏸️ | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| practice-areas.html | ⏸️ | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| locations.html | ⏸️ | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ |
| contact.html | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ | N/A | N/A | ⏸️ | ⏸️ |
| resources.html | ⏸️ | ⏸️ | ⏸️ | N/A | ⏸️ | N/A | N/A | ⏸️ | ⏸️ |
| ottawa-county.html | ⏸️ | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ |
| kent-county.html | ⏸️ | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ | N/A | ⏸️ | ⏸️ |

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 7.2 JavaScript Conflict Testing
**Status**: ⏸️ Not Started

| Functionality | Test Result | Notes |
|---------------|-------------|-------|
| Mobile hamburger menu | ⏸️ | |
| FAQ accordions | ⏸️ | |
| Contact form validation | ⏸️ | |
| Smooth scrolling | ⏸️ | |
| Analytics events | ⏸️ | |
| Console errors check | ⏸️ | |
| Mobile sticky CTA | ⏸️ | |

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 7.3 Shared Asset Testing
**Status**: ⏸️ Not Started

| Asset | Test Result | Notes |
|-------|-------------|-------|
| core-brand.css unchanged | ⏸️ | |
| style.css card styles scoped | ⏸️ | |
| style.min.css regenerated | ⏸️ | |
| main.js no breaking changes | ⏸️ | |
| HTML validation (W3C) | ⏸️ | |
| CSS validation | ⏸️ | |

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 7.4 Performance Regression Testing
**Status**: ⏸️ Not Started

| Metric | Baseline | After Changes | Impact | Pass/Fail |
|--------|----------|---------------|--------|-----------|
| Homepage Lighthouse | TBD | TBD | TBD | ⏸️ |
| CSS file size | TBD | TBD | Target: <10% | ⏸️ |
| JS file size | TBD | TBD | Target: <15% | ⏸️ |
| Homepage load time | TBD | TBD | Should match | ⏸️ |
| FCP (First Contentful Paint) | TBD | TBD | Should match | ⏸️ |
| LCP (Largest Contentful Paint) | TBD | TBD | Should match | ⏸️ |
| CLS (Cumulative Layout Shift) | TBD | TBD | Should match | ⏸️ |
| TBT (Total Blocking Time) | TBD | TBD | Should match | ⏸️ |

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 7.5 Cross-Page Navigation Testing
**Status**: ⏸️ Not Started

| Navigation Path | Result | Notes |
|-----------------|--------|-------|
| Card page → Main site (footer links) | ⏸️ | |
| Main site → Card pages | ⏸️ | |
| Attorney pages → Attorney cards | ⏸️ | |
| Card pages → Attorney profile pages | ⏸️ | |
| All footer links functional | ⏸️ | |

**Issues Found**: None yet
**Issues Resolved**: None yet

---

### 7.6 Browser & Device Compatibility
**Status**: ⏸️ Not Started

| Browser/Device | card.html | sorin.html | jonathan.html | Main Site (5 pages) | Overall |
|----------------|-----------|------------|---------------|---------------------|---------|
| Chrome Desktop | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| Chrome Mobile | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| Safari Desktop | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| Safari iOS | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| Firefox Desktop | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| Firefox Mobile | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |
| Edge Desktop | ⏸️ | ⏸️ | ⏸️ | ⏸️ | ⏸️ |

**Issues Found**: None yet
**Issues Resolved**: None yet

---

## 8. Final Pre-Launch Checklist

### Code Quality
- [ ] No console errors on card pages
- [ ] No console errors on main site
- [ ] HTML validated (W3C)
- [ ] CSS validated
- [ ] All links functional
- [ ] All images display
- [ ] Forms submit correctly

### Performance
- [ ] Card pages: Lighthouse 90+ score
- [ ] Main site: Scores unchanged
- [ ] Load time < 2 seconds (3G)
- [ ] Images optimized
- [ ] CSS minified
- [ ] JS minified

### Accessibility
- [ ] WCAG AA compliance
- [ ] Zero violations in audit
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Color contrast passes

### Brand & Content
- [ ] Brand colors correct (#4076B4, #FF8A28)
- [ ] Fonts correct (Lora, Inter)
- [ ] Business hours accurate (Mon-Fri 9-5)
- [ ] Weekend appointment notice present
- [ ] No "24/7" messaging
- [ ] Logo sizing correct
- [ ] Content reviewed

### Testing
- [ ] All 3 card pages tested
- [ ] Main site regression complete
- [ ] Cross-browser testing done
- [ ] Mobile device testing done
- [ ] Analytics verified
- [ ] Forms tested

### Documentation
- [ ] Session notes complete
- [ ] Change log detailed
- [ ] Testing checklist 100% complete
- [ ] Screenshots captured
- [ ] Git commits descriptive

### Client Approval
- [ ] Client review scheduled
- [ ] Feedback incorporated
- [ ] Final approval received
- [ ] Ready for deployment

---

## Legend
- ⏸️ Pending / Not Started
- ✓ Passed
- ✗ Failed
- ⚠️ Issues Found (see notes)

---

## Summary

**Total Tests**: TBD
**Tests Passed**: 0
**Tests Failed**: 0
**Tests Pending**: TBD

**Overall Status**: Setup Phase - Ready to Begin Testing

---
