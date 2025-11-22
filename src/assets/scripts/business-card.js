/**
 * Digital Business Card Functionality
 *
 * Handles interactions on card.html and card/*.html pages:
 * - vCard download functionality
 * - vCard download tracking
 * - Consultation form tracking
 *
 * This file replaces inline onclick handlers and inline function definitions for CSP compliance.
 */

document.addEventListener('DOMContentLoaded', function() {

    // vCard Download Tracking
    // Uses class="track-vcard-download" and data-card-type="firm|sorin|jonathan" attributes
    document.querySelectorAll('.track-vcard-download').forEach(button => {
        button.addEventListener('click', function() {
            const cardType = this.dataset.cardType || 'firm';
            if (typeof gtag !== 'undefined') {
                gtag('event', 'vcard_download', {
                    event_category: 'Digital Business Card',
                    event_label: cardType.charAt(0).toUpperCase() + cardType.slice(1) + ' Card',
                    card_type: cardType
                });
            }
        });
    });

    // Consultation Form Submit Tracking
    // Automatically tracks all form submissions on card pages
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const formName = this.dataset.formName || this.id || 'consultation';
            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submit', {
                    event_category: 'Business Card',
                    event_label: 'Consultation Form - ' + formName,
                    event_action: 'submit'
                });
            }
        });
    });

});

/**
 * vCard Download Function
 * Creates and downloads a .vcf file with firm contact information
 * @param {string} campaignName - Campaign name for analytics tracking (default: 'Business Card')
 */
function downloadVCard(campaignName = 'Business Card') {
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

    // Create blob and download link
    const blob = new Blob([vcard], { type: 'text/vcard' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'Sorin_Pyle_Criminal_Defense.vcf';

    // Trigger download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);

    // Track conversion
    if (typeof gtag !== 'undefined') {
        gtag('event', 'conversion', {
            event_category: 'QR Campaign',
            event_label: 'vCard Download - ' + campaignName,
            value: 1
        });
    }
}

// Make downloadVCard globally available for backwards compatibility
window.downloadVCard = downloadVCard;
