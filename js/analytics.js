/**
 * Advanced Analytics and Performance Monitoring for Sorin & Pyle Website
 * Includes: GA4 Events, Core Web Vitals, Error Tracking, Conversion Tracking
 */

// Analytics Configuration
const ANALYTICS_CONFIG = {
    // Replace with actual Google Analytics 4 Measurement ID
    GA_ID: 'G-LV7PKRF2YT',
    // Replace with actual Google Tag Manager ID if using GTM
    GTM_ID: 'GTM_CONTAINER_ID'
};

/**
 * Enhanced Event Tracking for Legal Website
 */
class LegalSiteAnalytics {
    constructor() {
        this.init();
    }

    init() {
        this.setupEventTracking();
        this.setupFormTracking();
        this.setupPhoneTracking();
        this.setupScrollTracking();
        this.setupErrorTracking();
        this.setupConversionTracking();
    }

    /**
     * Track button clicks and important interactions
     */
    setupEventTracking() {
        // Track all CTA buttons
        document.querySelectorAll('.button-primary').forEach(button => {
            button.addEventListener('click', (e) => {
                const buttonText = e.target.textContent.trim();
                const pageType = this.getPageType();

                gtag('event', 'cta_click', {
                    event_category: 'User Interaction',
                    event_label: buttonText,
                    page_type: pageType,
                    button_location: this.getElementLocation(e.target)
                });
            });
        });

        // Track navigation clicks
        document.querySelectorAll('.navbar_link, .mobile-nav_link').forEach(link => {
            link.addEventListener('click', (e) => {
                const linkText = e.target.textContent.trim();
                const destination = e.target.getAttribute('href');

                gtag('event', 'navigation_click', {
                    event_category: 'Navigation',
                    event_label: linkText,
                    destination_page: destination
                });
            });
        });

        // Track attorney profile clicks
        document.querySelectorAll('.card_attorney a').forEach(link => {
            link.addEventListener('click', (e) => {
                const attorneyName = e.target.closest('.card_attorney').querySelector('.attorney_name')?.textContent;

                gtag('event', 'attorney_profile_click', {
                    event_category: 'Content Engagement',
                    event_label: attorneyName || 'Unknown Attorney',
                    engagement_type: 'profile_view'
                });
            });
        });
    }

    /**
     * Track form interactions and submissions
     */
    setupFormTracking() {
        // Track form starts
        document.querySelectorAll('form input, form textarea').forEach(field => {
            field.addEventListener('focus', (e) => {
                const form = e.target.closest('form');
                const formName = form?.getAttribute('name') || form?.id || 'contact_form';

                gtag('event', 'form_start', {
                    event_category: 'Form Interaction',
                    event_label: formName,
                    field_name: e.target.name || e.target.id
                });
            }, { once: true });
        });

        // Track form submissions
        document.querySelectorAll('form').forEach(form => {
            form.addEventListener('submit', (e) => {
                const formName = e.target.getAttribute('name') || e.target.id || 'contact_form';

                gtag('event', 'form_submit', {
                    event_category: 'Conversion',
                    event_label: formName,
                    value: 1
                });

                // Track as conversion goal
                gtag('event', 'conversion', {
                    send_to: 'AW-CONVERSION_ID/CONVERSION_LABEL'
                });
            });
        });
    }

    /**
     * Track phone number clicks (mobile)
     */
    setupPhoneTracking() {
        document.querySelectorAll('a[href^="tel:"]').forEach(phoneLink => {
            phoneLink.addEventListener('click', (e) => {
                const phoneNumber = e.target.getAttribute('href').replace('tel:', '');
                const location = this.getElementLocation(e.target);

                gtag('event', 'phone_call', {
                    event_category: 'Conversion',
                    event_label: phoneNumber,
                    phone_location: location,
                    value: 1
                });

                // Track as conversion
                gtag('event', 'conversion', {
                    send_to: 'AW-CONVERSION_ID/PHONE_CONVERSION_LABEL'
                });
            });
        });
    }

    /**
     * Track scroll depth for engagement measurement
     */
    setupScrollTracking() {
        let maxScroll = 0;
        const scrollThresholds = [25, 50, 75, 90, 100];
        const triggeredThresholds = new Set();

        const trackScroll = () => {
            const scrollPercent = Math.round(
                (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100
            );

            maxScroll = Math.max(maxScroll, scrollPercent);

            scrollThresholds.forEach(threshold => {
                if (scrollPercent >= threshold && !triggeredThresholds.has(threshold)) {
                    triggeredThresholds.add(threshold);

                    gtag('event', 'scroll_depth', {
                        event_category: 'User Engagement',
                        event_label: `${threshold}%`,
                        value: threshold,
                        page_type: this.getPageType()
                    });
                }
            });
        };

        let ticking = false;
        const requestScroll = () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    trackScroll();
                    ticking = false;
                });
                ticking = true;
            }
        };

        window.addEventListener('scroll', requestScroll, { passive: true });

        // Send final scroll depth on page unload
        window.addEventListener('beforeunload', () => {
            gtag('event', 'max_scroll_depth', {
                event_category: 'User Engagement',
                value: maxScroll,
                non_interaction: true
            });
        });
    }

    /**
     * Track JavaScript errors and performance issues
     */
    setupErrorTracking() {
        // Track JavaScript errors
        window.addEventListener('error', (e) => {
            gtag('event', 'js_error', {
                event_category: 'Technical',
                event_label: e.message,
                error_file: e.filename,
                error_line: e.lineno,
                non_interaction: true
            });
        });

        // Track unhandled promise rejections
        window.addEventListener('unhandledrejection', (e) => {
            gtag('event', 'promise_rejection', {
                event_category: 'Technical',
                event_label: e.reason?.message || 'Unknown Promise Rejection',
                non_interaction: true
            });
        });

        // Track resource loading errors
        document.addEventListener('error', (e) => {
            if (e.target !== window) {
                gtag('event', 'resource_error', {
                    event_category: 'Technical',
                    event_label: e.target.src || e.target.href || 'Unknown Resource',
                    resource_type: e.target.tagName.toLowerCase(),
                    non_interaction: true
                });
            }
        }, true);
    }

    /**
     * Track conversion goals and lead generation
     */
    setupConversionTracking() {
        // Track page views by type
        const pageType = this.getPageType();
        gtag('event', 'page_view', {
            event_category: 'Page View',
            page_type: pageType,
            page_title: document.title
        });

        // Track time to first interaction
        let firstInteraction = false;
        const startTime = performance.now();

        ['click', 'keydown', 'touchstart'].forEach(eventType => {
            document.addEventListener(eventType, () => {
                if (!firstInteraction) {
                    firstInteraction = true;
                    const timeToInteraction = Math.round(performance.now() - startTime);

                    gtag('event', 'time_to_first_interaction', {
                        event_category: 'User Engagement',
                        value: timeToInteraction,
                        non_interaction: true
                    });
                }
            }, { once: true, passive: true });
        });

        // Track session duration
        const sessionStart = Date.now();
        window.addEventListener('beforeunload', () => {
            const sessionDuration = Math.round((Date.now() - sessionStart) / 1000);

            gtag('event', 'session_duration', {
                event_category: 'User Engagement',
                value: sessionDuration,
                non_interaction: true
            });
        });
    }

    /**
     * Helper Functions
     */
    getPageType() {
        const path = window.location.pathname;

        if (path === '/' || path.includes('index')) return 'homepage';
        if (path.includes('attorneys')) return 'attorneys';
        if (path.includes('practice-areas')) return 'practice_areas';
        if (path.includes('locations')) return 'locations';
        if (path.includes('contact')) return 'contact';
        if (path.includes('resources')) return 'resources';
        if (path.includes('privacy')) return 'privacy_policy';

        return 'other';
    }

    getElementLocation(element) {
        if (element.closest('header')) return 'header';
        if (element.closest('.section_home-hero')) return 'hero';
        if (element.closest('footer')) return 'footer';
        if (element.closest('.mobile-nav_menu')) return 'mobile_menu';

        return 'content';
    }
}

/**
 * Performance Monitoring
 */
class PerformanceMonitor {
    constructor() {
        this.init();
    }

    init() {
        this.trackPageLoadMetrics();
        this.trackResourceMetrics();
        this.setupPerformanceObserver();
    }

    trackPageLoadMetrics() {
        window.addEventListener('load', () => {
            setTimeout(() => {
                const navigation = performance.getEntriesByType('navigation')[0];
                const paint = performance.getEntriesByType('paint');

                // Track page load timing
                gtag('event', 'page_load_time', {
                    event_category: 'Performance',
                    value: Math.round(navigation.loadEventEnd - navigation.fetchStart),
                    non_interaction: true
                });

                // Track First Contentful Paint
                const fcp = paint.find(entry => entry.name === 'first-contentful-paint');
                if (fcp) {
                    gtag('event', 'first_contentful_paint', {
                        event_category: 'Performance',
                        value: Math.round(fcp.startTime),
                        non_interaction: true
                    });
                }

                // Track DOM Content Loaded
                gtag('event', 'dom_content_loaded', {
                    event_category: 'Performance',
                    value: Math.round(navigation.domContentLoadedEventEnd - navigation.fetchStart),
                    non_interaction: true
                });
            }, 0);
        });
    }

    trackResourceMetrics() {
        window.addEventListener('load', () => {
            const resources = performance.getEntriesByType('resource');
            const slowResources = resources.filter(resource => resource.duration > 1000);

            slowResources.forEach(resource => {
                gtag('event', 'slow_resource', {
                    event_category: 'Performance',
                    event_label: resource.name,
                    value: Math.round(resource.duration),
                    non_interaction: true
                });
            });
        });
    }

    setupPerformanceObserver() {
        if ('PerformanceObserver' in window) {
            // Monitor Long Tasks
            try {
                const longTaskObserver = new PerformanceObserver((list) => {
                    list.getEntries().forEach((entry) => {
                        gtag('event', 'long_task', {
                            event_category: 'Performance',
                            value: Math.round(entry.duration),
                            non_interaction: true
                        });
                    });
                });
                longTaskObserver.observe({ entryTypes: ['longtask'] });
            } catch (e) {
                // Long Task API not supported
            }

            // Monitor Layout Shifts
            try {
                const clsObserver = new PerformanceObserver((list) => {
                    let clsScore = 0;
                    list.getEntries().forEach((entry) => {
                        if (!entry.hadRecentInput) {
                            clsScore += entry.value;
                        }
                    });

                    if (clsScore > 0.1) { // Only track significant shifts
                        gtag('event', 'layout_shift', {
                            event_category: 'Performance',
                            value: Math.round(clsScore * 1000),
                            non_interaction: true
                        });
                    }
                });
                clsObserver.observe({ entryTypes: ['layout-shift'] });
            } catch (e) {
                // Layout Shift API not supported
            }
        }
    }
}

// Initialize analytics when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new LegalSiteAnalytics();
        new PerformanceMonitor();
    });
} else {
    new LegalSiteAnalytics();
    new PerformanceMonitor();
}

// Export for external use
window.LegalSiteAnalytics = LegalSiteAnalytics;
window.PerformanceMonitor = PerformanceMonitor;