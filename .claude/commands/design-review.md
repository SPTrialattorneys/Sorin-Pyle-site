# Design Review Slash Command

## Command
`/design-review [page] [focus-area]`

## Description
Triggers comprehensive design evaluation for legal website components using the specialized design review agent.

## Parameters
- `page` (optional): Specific page to review (homepage, contact, attorneys, etc.)
- `focus-area` (optional): Specific area to focus on (trust-credibility, accessibility, mobile-experience, performance)

## Usage Examples

### General Reviews
```
/design-review
/design-review homepage
/design-review contact-form
/design-review attorney-profiles
```

### Focused Reviews
```
/design-review homepage trust-credibility
/design-review contact-form accessibility
/design-review attorney-profiles mobile-experience
/design-review all performance
```

## Implementation

When this command is triggered, the system should:

1. **Start Local Server** (if not running):
   ```bash
   python -m http.server 8000
   ```

2. **Launch Design Review Agent** with the specialized legal website configuration:
   ```
   @agent-design-reviewer Please conduct a comprehensive design review of the Sorin & Pyle law firm website focusing on [focus-area] for [page].

   Use the design principles and standards defined in CLAUDE.md and follow the 6-phase review process:
   1. Professional Trust Assessment
   2. Legal Accessibility Review
   3. Client Journey Optimization
   4. Mobile Legal Experience
   5. Performance Validation
   6. Legal Industry Compliance

   Test URL: http://localhost:8000/[page].html

   Provide structured feedback following the legal industry feedback format.
   ```

3. **Agent Testing Process**:
   - Navigate to specified page at localhost:8000
   - Test across Desktop (1920x1080), Tablet (768x1024), Mobile (375x667)
   - Capture screenshots for documentation
   - Run performance and accessibility audits
   - Generate structured feedback report

## Focus Areas

### trust-credibility
- Professional presentation assessment
- Attorney credibility signals
- Firm branding consistency
- Contact prominence and trust indicators

### accessibility
- WCAG AA compliance verification
- Screen reader compatibility
- Keyboard navigation testing
- Color contrast validation
- Touch target sizing

### mobile-experience
- Mobile-first design evaluation
- Touch interaction testing
- Mobile contact accessibility
- Responsive behavior validation
- Emergency access assessment

### performance
- Core Web Vitals measurement
- Image optimization verification
- Critical CSS analysis
- Loading strategy evaluation
- AVIF/WebP implementation check

### client-journey
- Contact form flow testing
- CTA hierarchy assessment
- Service discovery paths
- Navigation optimization
- Conversion funnel analysis

### compliance
- Schema markup verification
- Local SEO optimization
- Privacy policy compliance
- Legal industry standards
- Ethical presentation standards

## Output Format

The design review agent will provide structured feedback including:

- **Executive Summary**: Overall design health assessment
- **Critical Issues**: Must-fix items affecting trust/accessibility/functionality
- **Improvements**: Should-fix enhancements for better UX
- **Recommendations**: Consider items for future optimization
- **Legal Industry Notes**: Professional presentation and compliance observations

## Integration Notes

This command works in conjunction with:
- Design principles defined in CLAUDE.md
- Legal website-specific agent configuration
- Playwright MCP for browser automation
- Local development server for live testing

The system prioritizes legal industry requirements including professional trust, accessibility compliance, and client experience optimization.