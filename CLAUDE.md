# Sorin & Pyle Law Firm Website - Claude Code Reference

## Project Overview
**Purpose**: Professional criminal defense law firm website for Sorin & Pyle, PC
**Location**: Holland, Michigan (serving West Michigan)
**Attorneys**: Sorin Panainte & Jonathan Pyle
**Site Type**: Static HTML/CSS/JS website with advanced SEO optimization

## Project Structure

### Core Files
- `index.html` - Homepage with hero, attorney cards, philosophy, results
- `attorneys.html` - Attorney listing page
- `contact.html` - Contact information and forms
- `practice-areas.html` - Legal practice areas
- `locations.html` - Service locations overview
- `resources.html` - Firm updates, blog, and resources
- `privacy-policy.html` - Privacy policy page
- `404.html` - Custom error page

### Attorney Profiles
- `jonathan-pyle.html` - Jonathan's individual profile
- `sorin-panainte.html` - Sorin's individual profile

### Location Pages (8 counties served)
- `locations/ottawa-county.html`
- `locations/kent-county.html`
- `locations/allegan-county.html`
- `locations/kalamazoo-county.html`
- `locations/muskegon-county.html`
- `locations/van-buren-county.html`
- `locations/newaygo-county.html`
- `locations/other-michigan-counties.html`

### Assets & Configuration
- `css/style.css` - Main stylesheet
- `css/style.min.css` - Minified version
- `js/main.js` - Core JavaScript functionality
- `js/analytics.js` - Analytics and tracking
- `js/analytics-config.js` - Analytics configuration
- `images/` - Image assets (AVIF optimized for performance)
- `fonts/` - Custom web fonts
- `.htaccess` - Apache server configuration
- `robots.txt` - Search engine crawler instructions
- `sitemap.xml` - XML sitemap for SEO

## Key Features & Technologies

### Performance Optimization
- **Image Format**: Primary use of AVIF images for superior compression
- **Critical CSS**: Inline critical styles for above-the-fold content
- **Lazy Loading**: Images and non-critical resources
- **Preloading**: Hero images and critical resources
- **Web Vitals Tracking**: Core Web Vitals monitoring via Google Analytics

### SEO & Schema Markup
- **Enhanced Schema**: LegalService and Person schemas on most pages
- **Location Schema**: Detailed geographic coverage markup
- **Structured Data**: Professional service offerings, hours, contact info
- **Meta Optimization**: Title tags, descriptions, Open Graph, Twitter Cards

### Accessibility Features
- **ARIA Labels**: Navigation menus with proper roles and states
- **Skip Links**: Keyboard navigation support
- **Screen Reader**: Optimized content structure
- **Mobile Navigation**: Accessible hamburger menu implementation

### Analytics & Tracking
- **Google Analytics 4**: Enhanced tracking for legal websites
- **Event Tracking**: CTA clicks, engagement time, form submissions
- **Core Web Vitals**: Performance monitoring
- **Custom Events**: Legal-specific tracking (consultation requests)

## Content Strategy

### Firm Philosophy
- "WE GIVE A [EXPLETIVE]!" - Bold, authentic messaging
- Judgment-free representation
- Focus on mental health and substance abuse clients
- Client-centered advocacy approach

### Service Areas
- **Geographic**: 7+ Michigan counties (Ottawa, Kent, Allegan, Kalamazoo, Muskegon, Van Buren, Newaygo)
- **Practice Areas**: Criminal defense, DUI, felonies, misdemeanors, expungements, license restoration
- **Specialties**: Pre-charge investigations, trial representation

### Recent Results Highlighted
- Felonious Assault: Dismissed
- CCW: Dismissed
- Domestic Violence: Not Guilty
- OWI: Dismissed
- Resisting and Opposing: Not Guilty
- Aggravated Assault: Not Guilty

## Development Commands

### Build & Test Commands
*Note: No package.json found - this appears to be a static HTML site*

**Image Optimization**: Uses ImageMagick for AVIF conversion
```bash
magick "source-image.png" -quality 90 "optimized-image.avif"
```

**Local Development**: Serve via any static file server
```bash
# Example with Python
python -m http.server 8000

# Example with Node.js serve
npx serve .
```

### Git Workflow
- **Main Branch**: `main` (for production deployments)
- **Current Status**: Multiple modified files, recent AVIF image optimizations
- **Recent Commits**: v1.1 revisions, blog post additions, live version updates

## File Modification Patterns

### When updating HTML files:
1. **Preserve Schema Markup**: Maintain enhanced LegalService schemas
2. **Keep Accessibility**: Don't remove ARIA labels or roles
3. **Image Optimization**: Use AVIF format with WebP/JPG fallbacks
4. **Analytics**: Preserve gtag event tracking on CTAs

### When updating CSS:
1. **Critical CSS**: Update inline styles in HTML head if modifying above-the-fold
2. **Performance**: Maintain lazy loading and preload strategies
3. **Responsive**: Test on mobile navigation and grid layouts

### When updating JavaScript:
1. **Analytics**: Preserve event tracking functionality
2. **Performance**: Maintain Web Vitals tracking
3. **Mobile Menu**: Preserve hamburger menu accessibility

## Important Notes

### Contact Information
- **Phone**: (616) 227-3303
- **Email**: justice@callsbp.com
- **Address**: 217 E 24th St Ste 107, Holland, MI 49423
- **Client Portal**: Clio integration for payments and case management

### SEO Considerations
- **Primary Keywords**: "criminal defense attorney", "Holland MI lawyer", "West Michigan criminal lawyer"
- **Location Focus**: Ottawa County primary, expanding to surrounding counties
- **Content Strategy**: Results-focused, empathetic messaging for criminal defense clients

### Performance Targets
- **Core Web Vitals**: Optimized for LCP, FID, CLS
- **Image Loading**: Hero images prioritized, others lazy loaded
- **CSS Delivery**: Critical path optimized with inline styles

## Current Project Status
Based on git status and SITE_INVENTORY.md:
- ✅ **Schema & SEO**: Enhanced markup on main pages
- ✅ **Accessibility**: Navigation updated on high-traffic pages
- ✅ **Performance**: AVIF image optimization completed
- ✅ **Attorney Cards Fix**: Removed skeleton loading delay (Sept 2024)
- ✅ **Practice Areas Redesign**: Complete 50/50 layout with enhanced content (Sept 19, 2025)
- ✅ **Spacing Consistency**: Site-wide spacing utilities and section classes (Sept 19, 2025)
- ✅ **Record Expungement Redesign**: Complete page overhaul with minimal design (Sept 20, 2025)
- ✅ **Visual Design System**: Unified color theme and clean aesthetic (Sept 20, 2025)
- ⚠️ **In Progress**: Location page accessibility updates
- 📋 **Tracked**: Systematic approach via SITE_INVENTORY.md, HANDOFF_SUMMARY.md, and RECORD_EXPUNGEMENT_SESSION_NOTES.md

## Recent Changes Log

### September 19, 2025 - Practice Areas Section Redesign & Spacing Consistency
**Major Feature**: Complete redesign of homepage practice areas section
**Files Modified**:
- `index.html`: Redesigned practice areas section (lines 252-322) with 50/50 layout
- `css/style.css`: Added enhanced practice area cards, spacing utilities, new section classes
- `css/style.min.css`: Synchronized with main CSS
- `locations.html`: Replaced inline styles with CSS classes
- `sitemap.xml`: Updated homepage lastmod date

**Key Changes**:
1. **Practice Areas Redesign**:
   - Replaced 4-column basic layout with enhanced 2-column cards
   - Left: Criminal charges (felonies & misdemeanors with examples)
   - Right: Specialized services (expungements, license restoration, etc.)
   - Added clickable heading link to practice-areas.html
   - Removed CTA buttons for cleaner design

2. **Spacing Consistency Fixes**:
   - Created dedicated `.section_results` class (separate from philosophy)
   - Added `.section_contact-cta` with blue gradient styling
   - Added complete utility class system: `.margin-top-xl`, `.padding-top-sm`, etc.
   - Fixed responsive spacing and mobile padding

3. **CSS Enhancements**:
   - Added `.practice-areas-heading-link` with hover effects
   - Enhanced `.card_practice-area-enhanced` with min-height constraints
   - Improved accessibility with border hover indicators
   - Added `.line-height-relaxed` utility class

**Impact**:
- Better content organization and visual hierarchy
- Improved mobile responsive design
- Enhanced accessibility and user experience
- Consistent spacing system across all pages
- Professional design with better conversion potential

### September 2024 - Attorney Cards Performance Fix
**Issue**: Homepage attorney section had unnecessary 1.5-second skeleton loading delay
**Files Modified**:
- `index.html`: Removed skeleton loading HTML, removed `attorney-card-hidden` class
- `js/main.js`: Deleted skeleton loading JavaScript function (lines 121-149)

**Impact**: Attorney cards (Sorin & Jonathan) now display immediately on page load
**Affected Pages**: Homepage only - no other pages use skeleton loading

### Legacy Code Notes
- CSS classes `.skeleton*` and `.attorney-card-hidden` remain in stylesheets but are unused
- Safe to remove in future cleanup if desired
- No other pages depend on skeleton loading functionality

### September 19, 2025 - Mobile CTA Button & Accessibility Fixes
**Major Features**: Mobile conversion optimization and critical accessibility improvements

**Files Modified**:
- `index.html`: Added mobile sticky CTA button HTML with analytics tracking
- `css/style.css`: Added comprehensive mobile CTA styling with responsive design
- `css/style.min.css`: Synchronized minified version with mobile CTA styles
- `js/main.js`: Added mobile CTA scroll logic, fixed mobile menu & FAQ accessibility

**Key Changes**:
1. **Mobile Sticky CTA Button**:
   - Single "Call Now - Free Consultation" button for mobile conversion
   - Appears after 300px scroll, hidden on desktop (>768px)
   - Direct dial to (616) 227-3303 with analytics tracking
   - Touch-optimized 44px target with smooth animations
   - Safe area support for notched devices

2. **Critical Accessibility Fixes**:
   - Mobile menu: Fixed `aria-hidden` synchronization with visibility state
   - FAQ accordion: Added proper `aria-expanded` and `aria-hidden` management
   - Screen reader compatibility improved for navigation and interactive elements

3. **Technical Implementation**:
   - JavaScript screen size detection prevents desktop display
   - Throttled scroll events for performance optimization
   - Resize handling for responsive behavior
   - Complete analytics integration for conversion tracking

**Impact**:
- Addresses mobile conversion gap for emergency legal consultations
- Removes critical accessibility barriers for screen reader users
- Maintains clean desktop design while optimizing mobile experience
- Provides essential ADA compliance improvements for legal website
- Enhanced mobile UX for clients in crisis situations

### September 2024 - Attorney Cards Performance Fix
**Issue**: Homepage attorney section had unnecessary 1.5-second skeleton loading delay
**Files Modified**:
- `index.html`: Removed skeleton loading HTML, removed `attorney-card-hidden` class
- `js/main.js`: Deleted skeleton loading JavaScript function (lines 121-149)

**Impact**: Attorney cards (Sorin & Jonathan) now display immediately on page load
**Affected Pages**: Homepage only - no other pages use skeleton loading

### Legacy Code Notes
- CSS classes `.skeleton*` and `.attorney-card-hidden` remain in stylesheets but are unused
- Safe to remove in future cleanup if desired
- No other pages depend on skeleton loading functionality

### September 20, 2025 - Record Expungement Page Complete Redesign
**Major Feature**: Complete visual and structural overhaul of record expungement page

**Files Modified**:
- `record-expungement.html`: Complete structural redesign, content updates, section reorganization
- `css/style.css`: New design system, color theme updates, responsive layout improvements
- `css/style.min.css`: Synchronized with main CSS file
- `drivers-license-restoration.html`: Fixed button height consistency issues

**Key Changes**:
1. **Single-Column Narrative Design**:
   - Replaced confusing two-column layout with guided single-column flow
   - Eliminated sidebar in favor of linear user journey
   - Primary CTA elevated immediately after introduction
   - Removed "See If You Qualify" section to eliminate barriers

2. **Unified Blue Color Theme**:
   - Fixed visual chaos from competing colors (green, blue, orange)
   - Eligibility section changed from bright green to subtle blue
   - CTA section simplified from blue gradient to clean light gray
   - Consistent blue accent throughout page

3. **Minimal Clean Design Implementation**:
   - Removed ALL background colors and borders creating visual noise
   - Eliminated box shadows and colored containers
   - Typography-driven hierarchy instead of box-based separation
   - Simple horizontal dividers for clean section breaks

4. **Content Strategy Improvements**:
   - Enhanced FAQ with comprehensive eligibility information
   - Focused exclusively on petition-based expungement (firm's actual service)
   - Removed automatic expungement references
   - Simplified user journey from interest to consultation

5. **Responsive Layout Optimization**:
   - Fixed width consistency issues across all sections
   - Desktop 2-column layout for "Why Choose Us" section
   - Mobile single-column maintained for readability
   - Consistent 900px content width with proper breakpoints

**Impact**:
- Dramatically reduced visual chaos and information overload
- Professional, clean appearance appropriate for legal services
- Improved conversion path with direct consultation focus
- Better mobile and desktop experiences
- Accurate representation of firm's expungement services
- Enhanced user experience with simplified decision-making process

This is a well-optimized, professional legal website with strong technical foundations, mobile conversion optimization, complete accessibility compliance, and now a completely redesigned expungement page that provides an excellent user experience.

### October 9, 2025 - Modern Card Design System & Footer Refinements
**Major Feature**: Complete modernization of card designs across the entire website

**Files Modified**:
- `css/core-brand.css`: Added modern CSS variables for shadows, gradients, border radius
- `css/style.css`: Comprehensive card styling updates (homepage, attorneys, practice areas, digital business cards)
- `_includes/footer.html`: Added spacing classes and separated hours into paragraphs
- `index.html`: Fixed CSS loading (removed async preload)
- 20 HTML files: Updated via `node update-includes.cjs`

**Key Changes**:

1. **Modern Card Design System**:
   - Added CSS variables: `--shadow-layered`, `--shadow-deep`, `--shadow-hover`
   - Border radius increased: 8px → 16px (20px for digital cards)
   - Photo rings: 10px white borders with deep shadows
   - Pill-shaped buttons: 50px border-radius with scale hover effects
   - Gradient headers: Blue gradients on practice area cards

2. **Circular Attorney Photos**:
   - Homepage attorney cards: 220px circular photos with white ring borders
   - Digital business cards: 200px circular photos with gradient overlays
   - attorneys.html: Fixed photo cropping issue (removed aspect-ratio constraint)
   - Added modern hover effects (scale 1.02-1.03)

3. **Enhanced Card Components**:
   - **Homepage attorney cards**: 4px blue gradient top accent bar, 64px padding, layered shadows
   - **Practice area cards**: Gradient headers with white text, orange checkmarks, enhanced hover
   - **Digital business cards**: Gradient overlay backgrounds, deep shadows, modern spacing
   - **CTA buttons**: Pill shapes (50px radius), gradient backgrounds, scale hover

4. **Footer Spacing Refinements** (Professional critique implementation):
   - Hours column: Split weekday/weekend into separate paragraphs (8px gap)
   - Footer lists: Increased spacing from 8px to 10px
   - Address block: Tight cohesive spacing (4px after firm name, 8px after address)
   - Line heights: Improved readability (1.5 for address, 1.8 for contact)
   - Footer divider: Balanced spacing (64px top and bottom)
   - Wide screen optimization: 80px column gap on screens >1600px

5. **Footer Heading Underlines**:
   - Added white underlines (2px, 30% opacity) to footer column headings
   - Underlines match text width using `display: inline-block`
   - Firm name excluded from underline treatment
   - Visual hierarchy improvement for footer navigation

6. **CSS Variables Added** (`core-brand.css`):
   ```css
   --shadow-layered: 0 2px 4px rgba(0,0,0,0.05), 0 8px 16px rgba(0,0,0,0.1), 0 16px 32px rgba(0,0,0,0.08);
   --shadow-deep: 0 4px 8px rgba(0,0,0,0.08), 0 12px 24px rgba(0,0,0,0.12);
   --shadow-hover: 0 8px 16px rgba(0,0,0,0.12), 0 16px 32px rgba(0,0,0,0.15);
   --border-radius-card: 16px;
   --border-radius-card-lg: 20px;
   --gradient-blue-subtle: linear-gradient(135deg, rgba(64, 118, 180, 0.05) 0%, rgba(64, 118, 180, 0.02) 100%);
   --gradient-blue-header: linear-gradient(135deg, #5a8bc7 0%, #4076B4 100%);
   --photo-ring-width: 10px;
   ```

**Technical Fixes**:
- Fixed photo cropping on attorneys.html (removed aspect-ratio, added height: auto)
- Fixed CSS loading issues (changed from preload to standard link tags)
- Fixed CSS specificity for footer spacing (added !important declarations)
- Fixed include system workflow (updated `_includes/` then ran update-includes.cjs)

**Design Research**:
- Analyzed modern card platforms: Bitly, CardPage, Linktree, Royal Primary
- Implemented layered shadows, pill buttons, circular photos, gradient headers
- Maintained legal industry professionalism while modernizing aesthetic

**Impact**:
- Modern, professional card design consistent across all 4 card types
- Improved visual hierarchy and user experience
- Enhanced footer readability and spacing consistency
- Better mobile and desktop responsive behavior
- Stronger trust signals through polished, contemporary design
- Maintained accessibility while improving aesthetics

## Design Review System

### Design Principles for Legal Website
Our design system follows professional legal industry standards while maintaining modern usability:

#### Core Design Philosophy
1. **Trust & Credibility First**: Every design decision must reinforce professional competence and trustworthiness
2. **Accessibility is Non-Negotiable**: Legal services must be accessible to all users, including those with disabilities
3. **Performance Equals Professionalism**: Fast loading times demonstrate respect for clients' time
4. **Mobile-First Legal Experience**: Many clients access legal services via mobile during stressful situations

#### Visual Design Standards
- **Color Palette**:  accessible contrast ratios (WCAG AA compliance)
- **Typography**: Clear, readable fonts optimized for legal content consumption
- **Imagery**: Professional attorney photos in AVIF format for performance
- **Whitespace**: Generous spacing to reduce cognitive load during stressful legal situations

#### Interaction Design
- **Call-to-Action Hierarchy**: Clear priority on consultation requests and contact forms
- **Navigation**: Intuitive service area and location-based navigation
- **Forms**: Simplified contact forms with clear privacy messaging
- **Error States**: Compassionate error messaging appropriate for legal context

#### Content Strategy Integration
- **Messaging Tone**: "WE GIVE A [EXPLETIVE]!" approach - authentic, bold, judgment-free
- **Service Areas**: Clear geographic and practice area organization
- **Results Display**: Tasteful presentation of case outcomes without overpromising
- **Contact Information**: Multiple contact methods prominently displayed

#### Performance & Technical Standards
- **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1
- **Image Optimization**: AVIF with WebP/JPG fallbacks
- **Schema Markup**: Enhanced LegalService and Person schemas
- **Analytics**: Privacy-conscious tracking with legal industry compliance

### Design Review Agent Configuration

Use the `@agent-design-reviewer` for comprehensive UI/UX evaluation with these specifications:

**Review Phases**:
1. **Professional Trust Assessment**: Does the design convey legal competence and trustworthiness?
2. **Legal Accessibility Review**: WCAG compliance and inclusive design principles
3. **Client Journey Optimization**: Contact form flows and consultation request processes
4. **Mobile Legal Experience**: Touch targets, readability, emergency contact accessibility
5. **Performance Validation**: Core Web Vitals and image optimization verification
6. **Schema & SEO Health**: Legal service markup and local search optimization

**Testing Environments**:
- Desktop: 1920x1080 (primary professional consultation viewport)
- Tablet: 768x1024 (secondary research and contact device)
- Mobile: 375x667 (primary emergency and mobile consultation device)

**Legal Industry Specific Checks**:
- Contact information prominence and accessibility
- Service area geographic clarity
- Attorney profile professional presentation
- Case results ethical display standards
- Privacy policy and data handling transparency
- Emergency contact accessibility on mobile devices

### Usage Commands

#### Manual Design Review
Use the `/design-review` slash command to trigger comprehensive design evaluation:
```
/design-review [page-name] [focus-area]
```

Examples:
- `/design-review homepage trust-credibility`
- `/design-review contact-form accessibility`
- `/design-review attorney-profiles mobile-experience`

#### Automated Review Triggers
The design review agent automatically evaluates changes to:
- Homepage hero and attorney sections
- Contact forms and CTAs
- Navigation and mobile menu
- Attorney profile pages
- Location and service area pages

## September 21, 2025 - Address & Email Standardization + Content Updates

### Address Standardization (SEO Consistency)
**Major Update**: Standardized all address references across the entire website for SEO consistency

**Files Modified**: 21 HTML files (all site pages)
**Changes Made**:
- Updated from `217 E. 24th St. Suite 107` to `217 E 24th St Ste 107`
- Removed period after "E" and abbreviated "Suite" to "Ste"
- **Total instances updated**: 78 address references
- **Schema markup**: All JSON-LD structured data updated
- **Google Maps URLs**: Verified working with existing format

**SEO Benefits Achieved**:
- Consistent NAP (Name, Address, Phone) across all pages
- Standardized schema markup for enhanced search engine recognition
- Improved local search rankings with uniform address formatting
- Better Google My Business alignment using standard abbreviations

### Email Address Update
**Major Update**: Changed primary contact email across entire website

**Files Modified**: 21 HTML files (all site pages)
**Changes Made**:
- Updated from `Justice@SorinPyle.com` to `justice@callsbp.com`
- **Total instances updated**: 42 email references
- **Updated locations**: Footer contact links, contact page sections, schema markup, privacy policy content
- **All mailto links**: Updated for proper functionality

### Content Updates
**Ottawa County Page**: Updated claim language from "Ottawa County's premier criminal defense firm" to "one of Ottawa County's premier criminal defense firms" for more modest positioning

**Homepage Practice Areas**: Removed "Learn more about..." links for Record Expungement and Driver License Restoration sections, as those individual pages are not ready to go live yet

### Technical Verification
- ✅ All address references now use consistent format
- ✅ All email references updated successfully
- ✅ Schema markup remains valid
- ✅ Google Maps functionality verified
- ✅ No broken links or display issues

**Impact**: Enhanced SEO consistency, updated contact information, and prepared site for launch by removing links to incomplete pages.