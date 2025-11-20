/**
 * Google Analytics 4 Configuration for Sorin & Pyle Website
 *
 * Features:
 * - GA4 tracking with measurement ID G-LV7PKRF2YT
 * - Core Web Vitals monitoring (CLS, FID, FCP, LCP, TTFB)
 * - User engagement tracking
 * - GDPR/CCPA compliant with consent mode defaults
 *
 * Note: This file works with js/cookie-consent.js for consent management.
 * Cookie consent script calls gtag('consent', 'update', ...) when user accepts.
 */

// Initialize dataLayer and gtag function globally
// (must be available for inline onclick handlers and cookie-consent.js)
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

// Set default consent state (blocked until user accepts)
gtag('consent', 'default', {
    'analytics_storage': 'denied',
    'ad_storage': 'denied'
});

// Initialize GA4
gtag('js', new Date());
gtag('config', 'G-LV7PKRF2YT', {
    // Enhanced tracking for legal websites
    page_title: document.title,
    page_location: window.location.href,
    // Core Web Vitals tracking
    custom_map: {
        'custom_parameter_1': 'page_type',
        'custom_parameter_2': 'practice_area'
    }
});

// Track Core Web Vitals
function trackWebVitals() {
    function sendToGoogleAnalytics({name, delta, value, id}) {
        gtag('event', name, {
            event_category: 'Web Vitals',
            event_label: id,
            value: Math.round(name === 'CLS' ? delta * 1000 : delta),
            non_interaction: true,
        });
    }

    // Load web-vitals library
    import('https://unpkg.com/web-vitals@3/dist/web-vitals.js').then(({onCLS, onFID, onFCP, onLCP, onTTFB}) => {
        onCLS(sendToGoogleAnalytics);
        onFID(sendToGoogleAnalytics);
        onFCP(sendToGoogleAnalytics);
        onLCP(sendToGoogleAnalytics);
        onTTFB(sendToGoogleAnalytics);
    }).catch(err => {
        console.warn('Web Vitals library failed to load:', err);
    });
}

// Track page engagement for legal sites
function trackEngagement() {
    let engagementTime = 0;
    let lastActiveTime = Date.now();

    const trackTime = () => {
        const now = Date.now();
        engagementTime += now - lastActiveTime;
        lastActiveTime = now;
    };

    ['mousedown', 'touchstart', 'keydown', 'scroll'].forEach(event => {
        document.addEventListener(event, trackTime, {passive: true});
    });

    // Send engagement data on page unload
    window.addEventListener('beforeunload', () => {
        gtag('event', 'engagement_time', {
            event_category: 'User Engagement',
            value: Math.round(engagementTime / 1000),
            non_interaction: true
        });
    });
}

// Initialize tracking when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        trackWebVitals();
        trackEngagement();
    });
} else {
    trackWebVitals();
    trackEngagement();
}
