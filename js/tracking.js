/**
 * Event Tracking for Sorin & Pyle Website
 *
 * Handles conversion tracking for:
 * - Phone click events (90+ instances across site)
 * - CTA button clicks
 * - Form interactions
 *
 * This file replaces inline onclick="gtag(...)" handlers for CSP compliance.
 */

// Wait for gtag to be available before initializing tracking
function waitForGtag(callback) {
    if (typeof gtag !== 'undefined') {
        callback();
    } else {
        setTimeout(() => waitForGtag(callback), 100);
    }
}

// Initialize all tracking when DOM is ready and gtag is available
waitForGtag(function() {
    document.addEventListener('DOMContentLoaded', function() {

        // Phone Click Tracking
        // Uses class="track-phone-click" and data-event-label="label" attributes
        document.querySelectorAll('.track-phone-click').forEach(link => {
            link.addEventListener('click', function() {
                const label = this.dataset.eventLabel || 'unknown';
                gtag('event', 'phone_click', {
                    'event_category': 'contact',
                    'event_label': label
                });
            });
        });

        // CTA Button Click Tracking
        // Uses class="track-cta-click" and data-cta-type="type" attributes
        document.querySelectorAll('.track-cta-click').forEach(button => {
            button.addEventListener('click', function() {
                const ctaType = this.dataset.ctaType || 'unknown';
                const ctaLabel = this.dataset.ctaLabel || 'CTA Click';
                gtag('event', 'cta_click', {
                    'event_category': 'conversion',
                    'event_label': ctaLabel,
                    'cta_type': ctaType
                });
            });
        });

        // Generic Click Event Tracking
        // Uses class="track-click" with data-event-category, data-event-label, data-event-action
        document.querySelectorAll('.track-click').forEach(element => {
            element.addEventListener('click', function() {
                const category = this.dataset.eventCategory || 'Unspecified';
                const label = this.dataset.eventLabel || 'Unspecified';
                const action = this.dataset.eventAction || 'click';

                gtag('event', 'click', {
                    'event_category': category,
                    'event_label': label,
                    'event_action': action
                });
            });
        });

    });
});
