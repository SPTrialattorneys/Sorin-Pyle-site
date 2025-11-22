/**
 * Cookie Consent Banner for Sorin & Pyle Website
 * GDPR & CCPA Compliant
 *
 * Features:
 * - Blocks GA4 until consent given
 * - Stores consent preference in localStorage
 * - Lightweight (no external dependencies)
 * - Accessible (keyboard navigation, screen reader friendly)
 */

(function() {
    'use strict';

    // Configuration
    const CONSENT_KEY = 'sp-cookie-consent';
    const CONSENT_VERSION = '1.0';

    // Check if consent has already been given
    function hasConsent() {
        const consent = localStorage.getItem(CONSENT_KEY);
        if (!consent) return false;

        try {
            const data = JSON.parse(consent);
            return data.version === CONSENT_VERSION && data.accepted === true;
        } catch (e) {
            return false;
        }
    }

    // Save consent preference
    function saveConsent(accepted) {
        const data = {
            version: CONSENT_VERSION,
            accepted: accepted,
            timestamp: new Date().toISOString()
        };
        localStorage.setItem(CONSENT_KEY, JSON.stringify(data));
    }

    // Initialize Google Analytics (called after consent)
    function initializeAnalytics() {
        // GA4 is already loaded in the page head, but we need to trigger it
        if (typeof gtag === 'function') {
            // Update consent mode
            gtag('consent', 'update', {
                'analytics_storage': 'granted'
            });

            // Track consent given event
            gtag('event', 'cookie_consent_given', {
                event_category: 'Privacy',
                event_label: 'Cookie Consent Banner',
                non_interaction: true
            });
        }
    }

    // Create and show the banner
    function showConsentBanner() {
        // Create banner HTML
        const banner = document.createElement('div');
        banner.id = 'cookie-consent-banner';
        banner.className = 'cookie-consent-banner';
        banner.setAttribute('role', 'dialog');
        banner.setAttribute('aria-labelledby', 'cookie-consent-title');
        banner.setAttribute('aria-describedby', 'cookie-consent-description');
        banner.innerHTML = `
            <div class="cookie-consent-container">
                <div class="cookie-consent-content">
                    <h2 id="cookie-consent-title" class="cookie-consent-title">We Value Your Privacy</h2>
                    <p id="cookie-consent-description" class="cookie-consent-text">
                        We use cookies to analyze website traffic and optimize your experience. By accepting,
                        you consent to our use of cookies for analytics purposes. Your data will never be sold
                        or shared with third parties.
                        <a href="privacy-policy.html" target="_blank" rel="noopener">Learn more in our Privacy Policy</a>.
                    </p>
                </div>
                <div class="cookie-consent-actions">
                    <button id="cookie-accept" class="cookie-btn cookie-btn-accept" type="button">
                        Accept Cookies
                    </button>
                    <button id="cookie-decline" class="cookie-btn cookie-btn-decline" type="button">
                        Decline
                    </button>
                </div>
            </div>
        `;

        // Add to page
        document.body.appendChild(banner);

        // Focus trap for accessibility
        const firstFocusable = banner.querySelector('#cookie-accept');
        const lastFocusable = banner.querySelector('#cookie-decline');

        firstFocusable.focus();

        // Handle Tab key for focus trap
        banner.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                if (e.shiftKey && document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                } else if (!e.shiftKey && document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        });

        // Accept button
        document.getElementById('cookie-accept').addEventListener('click', function() {
            saveConsent(true);
            initializeAnalytics();
            removeBanner();
        });

        // Decline button
        document.getElementById('cookie-decline').addEventListener('click', function() {
            saveConsent(false);
            removeBanner();
        });
    }

    // Remove banner from DOM
    function removeBanner() {
        const banner = document.getElementById('cookie-consent-banner');
        if (banner) {
            banner.classList.add('cookie-consent-banner-fadeout');
            setTimeout(function() {
                banner.remove();
            }, 300);
        }
    }

    // Initialize on page load
    function init() {
        // Check if consent already given
        if (hasConsent()) {
            // User already consented, initialize analytics
            initializeAnalytics();
        } else {
            // Show banner after a short delay for better UX
            setTimeout(showConsentBanner, 1000);
        }
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
