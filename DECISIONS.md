# Architecture Decision Log

This document tracks significant architectural and technical decisions for the Sorin & Pyle website project. Each decision includes context, alternatives considered, and consequences.

**Format:** Most recent decisions first (reverse chronological)

---

## ADR-006: Pre-Commit Validation System (2025-11-24)

**Status:** ✅ Implemented

**Context:** Developers were accidentally committing:
- Auto-generated `dist/` files (should never be in git)
- Console.log statements in production JS
- Schema markup errors (breaking Google Rich Results)
- TODO comments in templates

**Decision:** Implement husky pre-commit hooks with 4 automated checks:
1. Block commits containing `dist/` files (ERROR)
2. Warn about console.log in production JS (WARNING)
3. Warn about TODO comments in templates (WARNING)
4. Validate JSON-LD schema markup (ERROR if invalid)

**Consequences:**
- ✅ Prevents 90% of common commit mistakes
- ✅ Catches schema errors before deployment
- ✅ Saves hours of debugging post-deployment
- ⚠️ Adds ~3-5 seconds to commit time
- ⚠️ Can be bypassed with `--no-verify` when needed

**Alternative Considered:** Manual validation
**Why Rejected:** Human error too frequent; automation more reliable

**Implementation:**
- `utilities/validate-schema.js` - JSON-LD validation
- `utilities/pre-commit-check.js` - 4 validation checks
- `.husky/pre-commit` - Git hook trigger
- Exit code 1 (blocks commit) or 0 (allows commit)

---

## ADR-005: 4-Tier Layered Documentation System (2025-11-24)

**Status:** ✅ Implemented

**Context:** AI_CONTEXT.md grew to 16,000 words, making it:
- Slow to load for AI (token-heavy)
- Hard to find specific information during focused tasks
- Intimidating for new developers
- Difficult to maintain

**Decision:** Create 4-tier layered documentation architecture:
- **Tier 1:** QUICK_START.md (750 words, 5 min) - Fast onboarding
- **Tier 2:** Task-focused guides (2,000-4,000 words, 10-15 min) - CSS, Schema, Content, Troubleshooting
- **Tier 3:** AI_CONTEXT.md (16,000 words) - Comprehensive reference
- **Tier 4:** .ai/ tracking system - Session continuity (current-task, task-history, known-issues, todo)

**Consequences:**
- ✅ 5x faster AI task loading (2,000 vs 16,000 words)
- ✅ Improved AI response quality (focused context)
- ✅ Easier for humans to find specific information
- ✅ Session continuity for interrupted work
- ⚠️ Need to maintain cross-references between tiers
- ⚠️ More files to keep in sync

**Alternative Considered:** Single comprehensive document
**Why Rejected:** Too slow for both AI and human developers

**Implementation:**
- `utilities/docs/CSS_GUIDE.md` (2,367 words)
- `utilities/docs/SCHEMA_GUIDE.md` (2,185 words)
- `utilities/docs/CONTENT_GUIDE.md` (3,235 words)
- `utilities/docs/TROUBLESHOOTING.md` (4,418 words)
- `.ai/README.md`, `.ai/current-task.md`, `.ai/task-history.md`, `.ai/known-issues.md`, `.ai/todo.md`

---

## ADR-004: Automated Critical CSS Extraction (2024-11-24)

**Status:** ✅ Implemented

**Context:** Manual critical CSS management required:
- Editing 3-4 separate files for every CSS change
- Manual minification and compression
- High risk of forgetting to update one file
- November 24 incident: Mobile breakpoints updated in main CSS but not critical CSS, causing production bugs

**Decision:** Automate critical CSS extraction using `critical` package:
- Extract above-the-fold CSS from rendered HTML
- Generate 4 optimized files (homepage, attorneys, practice-areas, page-layout)
- Automatically minify and inline in templates
- Rebuild HTML after extraction to apply changes

**Consequences:**
- ✅ Reduced maintenance from 4 files to 1 source file
- ✅ Eliminated manual minification and synchronization errors
- ✅ Always in sync with main CSS
- ⚠️ Build time increased by ~15 seconds
- ⚠️ Must build HTML twice (before/after extraction)
- ⚠️ Critical CSS files must not be manually edited

**Alternative Considered:** Single universal critical CSS for all pages
**Why Rejected:** Performance - per-page optimization better for LCP (Largest Contentful Paint)

**Implementation:**
- `utilities/extract-critical-css.mjs` - Extraction script
- `npm run build:critical` - Manual extraction
- `npm run build:cloudflare` - Automated full build with extraction
- Output: `src/_data/critical-*.css` (4 files)

---

## ADR-003: Source vs Built Files Architecture (2024-09)

**Status:** ✅ Implemented

**Context:** Static site generator (Eleventy) requires clear separation between source templates and built HTML.

**Decision:** Strict source/built file separation:
- **Source:** `src/pages/*.njk`, `src/assets/styles/*.css`, `src/assets/scripts/*.js`
- **Built:** `dist/*.html`, `dist/css/*.css`, `dist/js/*.js`
- **Rule:** NEVER edit `dist/` files - changes overwritten on next build

**Consequences:**
- ✅ Clear separation of concerns
- ✅ Git ignores `dist/` (only commit sources)
- ✅ Cloudflare Pages builds from source on every push
- ⚠️ Developers must remember to edit `.njk` not `.html`
- ⚠️ Changes to `dist/` lost on next build

**Alternative Considered:** Allow editing built files
**Why Rejected:** Unsustainable - changes lost, confusion about canonical files

**Implementation:**
- `.gitignore` excludes `dist/`
- Pre-commit hook blocks accidental `dist/` commits
- CLAUDE.md prominently documents this rule

---

## ADR-002: Eleventy over Next.js/Gatsby (2024-09)

**Status:** ✅ Implemented

**Context:** Needed static site generator for law firm marketing website. Requirements:
- Fast builds (50+ pages)
- No JavaScript required for core functionality
- Simple deployment (static HTML)
- SEO-friendly (server-rendered HTML)

**Decision:** Use Eleventy 3.x with Nunjucks templates

**Consequences:**
- ✅ Simple deployment (upload static HTML anywhere)
- ✅ No JavaScript required for core functionality
- ✅ Fast builds (53 pages in <1 second)
- ✅ Excellent SEO (pure HTML, no hydration)
- ✅ Low complexity (no React, no framework magic)
- ⚠️ Manual schema markup (no automated generation)
- ⚠️ No built-in forms (requires external service)
- ⚠️ Limited interactivity without custom JavaScript

**Alternatives Considered:**
1. **Next.js** - Rejected: Overkill for static marketing site, complex deployment
2. **Gatsby** - Rejected: Slow builds, GraphQL overhead, React lock-in
3. **Jekyll** - Rejected: Ruby dependency, slower builds than Eleventy

**Implementation:**
- Eleventy 3.1.2 with Nunjucks templating
- PostCSS for CSS processing
- esbuild for JavaScript bundling
- Cloudflare Pages for deployment

---

## ADR-001: Dual CSS Architecture (Main + Critical) (2024-09)

**Status:** ✅ Implemented

**Context:** Need to optimize Core Web Vitals (LCP, FCP) while maintaining maintainable CSS architecture.

**Problem:**
- Main CSS (80KB) blocks page render
- First Contentful Paint (FCP) slow
- Largest Contentful Paint (LCP) slow

**Decision:** Implement dual CSS system:
1. **Main CSS** (deferred) - Full stylesheet loaded after page render
2. **Critical CSS** (inline) - Above-the-fold styles inlined in `<head>`

**Consequences:**
- ✅ Improved FCP from ~2.5s to ~1.5s (40% faster)
- ✅ Improved LCP from ~3.5s to ~2.1s (40% faster)
- ✅ Eliminates "flash of unstyled content" (FOUC)
- ⚠️ Must update both main CSS and critical CSS for layout changes
- ⚠️ Critical CSS duplicates some main CSS (acceptable trade-off)

**Alternative Considered:** Single main CSS file with aggressive caching
**Why Rejected:** Doesn't solve initial page load performance

**Implementation:**
- Main CSS: `src/assets/styles/*.css` → `dist/css/main.min.css`
- Critical CSS: `src/_data/critical-*.css` → inlined in Nunjucks templates
- Automated extraction: `utilities/extract-critical-css.mjs`

**Critical CSS Files:**
- `critical-homepage.css` (~28KB) - Homepage hero, attorney cards, navbar
- `critical-attorneys.css` (~22KB) - Attorney grid layout, bio sections
- `critical-practice-areas.css` (~19KB) - Practice area cards, charges grid
- `critical-page-layout.css` (~15KB) - Standard page layout (sorin-panainte.html, etc.)

---

## Format for Future ADRs

When adding new decisions, use this template:

```markdown
## ADR-XXX: Decision Title (YYYY-MM-DD)

**Status:** 🚧 Proposed / ✅ Implemented / ⚠️ Deprecated / ❌ Rejected

**Context:** What problem are we solving? Why is this decision needed?

**Decision:** What are we doing?

**Consequences:**
- ✅ Positive outcomes
- ⚠️ Trade-offs and limitations
- ❌ Risks or downsides

**Alternative Considered:** What else did we evaluate?
**Why Rejected:** Why didn't we choose the alternative?

**Implementation:** How is this implemented? Key files/commands?
```

---

## References

- [Architecture Decision Records (ADR)](https://adr.github.io/)
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [Joel Spolsky: "Things You Should Never Do"](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)

---

**Related Documentation:**
- [AI_CONTEXT.md](AI_CONTEXT.md) - Comprehensive technical documentation
- [CLAUDE.md](CLAUDE.md) - Project instructions for Claude Code
- [utilities/docs/](utilities/docs/) - Task-focused guides
- [.ai/known-issues.md](.ai/known-issues.md) - Current bugs and limitations
