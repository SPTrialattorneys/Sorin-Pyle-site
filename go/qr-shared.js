/**
 * Sorin & Pyle QR Campaign Shared JavaScript
 * ============================================
 * Reusable functions for all QR landing pages
 */

// vCard Download Function (used by all campaigns)
function downloadVCard(campaignName = 'QR Campaign') {
    const vcard = `BEGIN:VCARD
VERSION:3.0
FN:Sorin & Pyle Criminal Defense
ORG:Sorin & Pyle, PC
TEL;TYPE=WORK,VOICE:+16162273303
EMAIL;TYPE=WORK:justice@callsbp.com
URL:https://www.sorinpyle.com
ADR;TYPE=WORK:;;217 E 24th St Ste 107;Holland;MI;49423;USA
NOTE:Criminal Defense Attorneys - Available 24/7 for emergencies. West Michigan's trusted defense team.
END:VCARD`;

    const blob = new Blob([vcard], { type: 'text/vcard' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'Sorin_Pyle_Criminal_Defense.vcf';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);

    // Track conversion
    if (typeof gtag !== 'undefined') {
        gtag('event', 'conversion', {
            'event_category': 'QR Campaign',
            'event_label': `vCard Download - ${campaignName}`,
            'value': 1
        });
    }
}

// Accordion Toggle (used by most campaigns)
function toggleAccordion(element) {
    const parent = element.closest('.accordion-item') || element.parentElement;
    parent.classList.toggle('active');
}

// Legacy support for old function names
function toggleRight(element) {
    toggleAccordion(element);
}

/**
 * Sanitizes user input by escaping HTML characters
 * Prevents XSS attacks via URL parameters
 * @param {string} input - The input string to sanitize
 * @returns {string} - Sanitized string with HTML entities escaped
 */
function sanitizeInput(input) {
    if (!input) return input;
    return input.replace(/[<>"'&]/g, function(char) {
        const escapeMap = {
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;',
            '&': '&amp;'
        };
        return escapeMap[char];
    });
}

// UTM Parameter Capture
function getUTMParams(defaultCampaign = 'qr_direct') {
    const params = new URLSearchParams(window.location.search);

    const utmSource = sanitizeInput(params.get('utm_source') || 'qr_direct');
    const utmMedium = sanitizeInput(params.get('utm_medium') || 'card');
    const utmCampaign = sanitizeInput(params.get('utm_campaign') || defaultCampaign);

    // Set hidden form fields if they exist
    const sourceField = document.getElementById('utm_source');
    const mediumField = document.getElementById('utm_medium');
    const campaignField = document.getElementById('utm_campaign');

    if (sourceField) sourceField.value = utmSource;
    if (mediumField) mediumField.value = utmMedium;
    if (campaignField) campaignField.value = utmCampaign;

    return { utmSource, utmMedium, utmCampaign };
}

// Form Submission Handler
function handleConsultationForm(formElement, campaignName) {
    formElement.addEventListener('submit', function(e) {
        e.preventDefault();

        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;

        submitBtn.innerHTML = '<span class="spinner"></span> Submitting...';
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;

        // Simulate submission (replace with actual backend endpoint)
        setTimeout(() => {
            alert('Thank you for your consultation request. We will contact you within 2 hours during business hours.');
            this.reset();
            submitBtn.innerHTML = originalText;
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
        }, 1500);

        // Track form submission
        if (typeof gtag !== 'undefined') {
            gtag('event', 'form_submit', {
                'event_category': 'QR Campaign',
                'event_label': `${campaignName} Consultation Request`
            });
        }
    });
}

// Scroll to Section (for know-your-rights page)
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.classList.add('active');
        element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

// Page View Tracking
function trackPageView(campaignName) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'page_view', {
            'campaign_source': 'qr_code',
            'campaign_name': campaignName
        });
    }
}

// Fade-in Animation Observer
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe common animated elements
    document.querySelectorAll('.right-item, .accordion-item, .resources, .bac-chart, .timeline, .amendment-grid').forEach(el => {
        observer.observe(el);
    });
}

// Initialize all shared functionality
function initQRCampaign(campaignName) {
    document.addEventListener('DOMContentLoaded', function() {
        // Capture UTM parameters
        getUTMParams(campaignName);

        // Track page view
        trackPageView(campaignName);

        // Setup form handler if form exists
        const consultationForm = document.getElementById('consultationForm');
        if (consultationForm) {
            handleConsultationForm(consultationForm, campaignName);
        }

        // Initialize scroll animations
        initScrollAnimations();
    });
}
