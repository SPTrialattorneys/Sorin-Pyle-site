# QR Code Campaign System Documentation

## System Architecture

### URL Structure
```
sorinpyle.com/go/[campaign-name]
```

### Current Campaigns
1. **Police Stops** - `/go/police-stops.html` ✅ READY
2. **DUI Rights** - `/go/dui-rights.html` ✅ READY
3. **Know Your Rights** - `/go/know-your-rights.html` ✅ READY

## UTM Parameter Strategy

### QR Code URL Format
```
https://www.sorinpyle.com/go/police-stops?utm_source=qr&utm_medium=card&utm_campaign=ace_downtown_q3_2024
```

### Parameter Definitions
- **utm_source**: Always "qr" for QR codes
- **utm_medium**: Type of material (card, poster, sticker, flyer)
- **utm_campaign**: Specific batch identifier

### Campaign Naming Convention
```
[card-name]_[location]_[quarter]_[year]
```

Examples:
- `ace_downtown_q3_2024`
- `police_stops_holland_bars_q4_2024`
- `dui_rights_college_campus_q1_2025`

## Analytics Tracking

### Key Metrics to Track
1. **Scan Rate**: Total QR code scans by campaign
2. **Conversion Rate**: vCard downloads / form submissions
3. **Geographic Performance**: Which locations generate most scans
4. **Time Analysis**: Peak scan times (arrest patterns)
5. **Device Types**: Mobile OS breakdown

### Google Analytics Events

```javascript
// Page View (automatic on load)
gtag('event', 'page_view', {
    'campaign_source': 'qr_code',
    'campaign_name': '[specific_campaign]'
});

// vCard Download
gtag('event', 'conversion', {
    'event_category': 'QR Campaign',
    'event_label': 'vCard Download - [Card Type]',
    'value': 1
});

// Form Submission
gtag('event', 'form_submit', {
    'event_category': 'QR Campaign',
    'event_label': 'Consultation Request - [Card Type]'
});

// Phone Call Click
gtag('event', 'click', {
    'event_category': 'QR Campaign',
    'event_label': 'Phone Call - [Card Type]'
});
```

## Creating New Campaign Pages

### Step 1: Duplicate Template
```bash
cp go/police-stops.html go/new-campaign.html
```

### Step 2: Customize Content
- Update title and meta description
- Modify rights accordion content
- Adjust intro message
- Update form hidden field values

### Step 3: Generate QR Codes
Use QR generator with these settings:
- Error Correction: H (30%)
- Size: 1000x1000px minimum
- Format: SVG or PNG
- Include campaign UTM parameters

### Step 4: Test Campaign
1. Scan QR code on multiple devices
2. Verify vCard download works
3. Test form submission
4. Check analytics tracking
5. Verify mobile responsiveness

## vCard Configuration

Current vCard includes:
```vcard
BEGIN:VCARD
VERSION:3.0
FN:Sorin & Pyle Criminal Defense
ORG:Sorin & Pyle, PC
TEL;TYPE=WORK,VOICE:+16162273303
EMAIL;TYPE=WORK:justice@callsbp.com
URL:https://www.sorinpyle.com
ADR;TYPE=WORK:;;217 E 24th St Ste 107;Holland;MI;49423;USA
NOTE:Criminal Defense Attorneys - Available 24/7 for emergencies
END:VCARD
```

## Backend Integration Requirements

### Form Submission Endpoint
Create `/submit-consultation` endpoint that:
1. Validates form data
2. Stores in CRM/database
3. Sends email notification to firm
4. Sends confirmation to user
5. Triggers follow-up automation

### Recommended Fields to Capture
```json
{
    "name": "required",
    "phone": "required",
    "email": "optional",
    "issue": "required",
    "source": "qr_police_stops",
    "utm_source": "qr",
    "utm_medium": "card",
    "utm_campaign": "specific_batch",
    "timestamp": "auto",
    "ip_address": "auto",
    "user_agent": "auto"
}
```

## Card Distribution Tracking

### Batch Tracking Spreadsheet
| Batch ID | Card Type | Quantity | Location | Date Distributed | QR Scans | Conversions |
|----------|-----------|----------|----------|------------------|-----------|-------------|
| ace_downtown_q3_2024 | Police Stops | 500 | Downtown Bars | 2024-07-15 | TBD | TBD |
| police_college_q3_2024 | Police Stops | 1000 | GVSU Campus | 2024-08-01 | TBD | TBD |

## A/B Testing Opportunities

### Test Variables
1. **CTA Button Text**
   - "Save to Contacts" vs "Add Our Number"
   - "Get Help Now" vs "Free Consultation"

2. **Color Schemes**
   - Orange CTA vs Blue CTA
   - Gradient background vs Solid color

3. **Content Order**
   - vCard first vs Rights first
   - Form prominent vs Form at bottom

4. **Rights Presentation**
   - Accordion (current) vs All visible
   - Icons vs No icons
   - Detailed vs Summary only

## Mobile Optimization Checklist

- [x] Viewport meta tag with safe areas
- [x] Touch-friendly button sizes (44px minimum)
- [x] No horizontal scrolling
- [x] Readable font sizes (16px minimum)
- [x] Fast loading (< 3 seconds)
- [x] Offline-capable (service worker potential)
- [x] Click-to-call phone numbers
- [x] Apple Wallet pass integration (future)

## SEO Considerations

### Schema Markup for Landing Pages
```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "Sorin & Pyle, PC",
  "description": "Know your rights during police stops",
  "url": "https://www.sorinpyle.com/go/police-stops",
  "telephone": "+16162273303",
  "areaServed": "Michigan"
}
```

### Meta Tags Strategy
- Unique title for each campaign
- Campaign-specific descriptions
- Open Graph tags for social sharing
- No-index tag (optional) to keep landing pages out of search

## Security & Privacy

### Data Protection
- SSL certificate required
- Form submissions encrypted
- No sensitive data in URL parameters
- Clear privacy policy link
- Attorney-client privilege notice

### Rate Limiting
- Implement form submission limits
- Block spam submissions
- CAPTCHA for suspicious activity

## Performance Monitoring

### Core Web Vitals Targets
- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1

### Optimization Techniques
- Inline critical CSS
- Lazy load images
- Minimize JavaScript
- Enable compression
- Browser caching headers

## Campaign ROI Calculation

### Cost Factors
- Card printing: $0.20/card
- Design time: $500/campaign
- Distribution labor: $15/hour
- QR code generation: $0

### Value Metrics
- Cost per scan
- Cost per vCard download
- Cost per consultation
- Client acquisition cost
- Lifetime client value

### Sample ROI Formula
```
ROI = (Client Value × Conversion Rate × Scans) - Total Campaign Cost
     ------------------------------------------------
                    Total Campaign Cost
```

## Future Enhancements

### Phase 2 Features
1. **Apple Wallet Pass**: Digital business card in wallet
2. **SMS Auto-responder**: Immediate text confirmation
3. **Geo-targeting**: Location-based content
4. **Progressive Web App**: Installable app experience
5. **Offline Mode**: Service worker for offline access
6. **Multi-language**: Spanish language option
7. **Video Explainers**: Short rights explanation videos
8. **Chat Widget**: Live chat integration

### Phase 3 Features
1. **AI Chatbot**: Immediate Q&A responses
2. **Document Upload**: Secure document submission
3. **Appointment Booking**: Calendar integration
4. **Push Notifications**: Re-engagement campaigns
5. **Referral Program**: Share incentives

## Testing Protocol

### Pre-Launch Testing
1. **Device Testing**
   - iPhone (Safari, Chrome)
   - Android (Chrome, Samsung Browser)
   - iPad/Tablets

2. **Network Testing**
   - 4G/5G cellular
   - Slow 3G simulation
   - Offline behavior

3. **Functionality Testing**
   - vCard download on all devices
   - Form submission validation
   - Analytics event firing
   - UTM parameter capture

### Post-Launch Monitoring
- Daily: Check form submissions
- Weekly: Review analytics data
- Monthly: ROI analysis
- Quarterly: Campaign optimization

## Support & Maintenance

### Regular Updates Needed
- Phone number changes
- Address updates
- Attorney information
- Legal disclaimer updates
- Privacy policy compliance

### Backup Strategy
- Regular HTML backups
- Form submission data exports
- Analytics data archives
- QR code image backups

## Success Metrics

### KPIs to Track
1. **Engagement Rate**: Scans / Cards Distributed
2. **Conversion Rate**: Actions / Scans
3. **Cost Per Acquisition**: Campaign Cost / New Clients
4. **Response Time**: Time from scan to contact
5. **Geographic Heat Map**: Best performing locations

### Reporting Schedule
- Weekly: Scan and conversion counts
- Monthly: Full campaign analysis
- Quarterly: ROI assessment and optimization

---

## Quick Start Commands

### Create New Campaign
```bash
# Copy template
cp go/police-stops.html go/new-campaign.html

# Edit content
nano go/new-campaign.html

# Test locally
python -m http.server 8000
```

### Generate QR Code URL
```
Base: https://www.sorinpyle.com/go/[page]
Add: ?utm_source=qr&utm_medium=card&utm_campaign=[batch_id]
```

### Track Campaign
```javascript
// Add to each QR landing page
gtag('config', 'GA-ID', {
    'campaign': {
        'source': 'qr_code',
        'medium': 'card',
        'name': 'campaign_name'
    }
});
```