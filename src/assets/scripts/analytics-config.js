/**
 * Analytics Configuration for Sorin & Pyle Website
 * Update these values with your actual tracking IDs
 */

window.ANALYTICS_CONFIG = {
    // Google Analytics 4 Configuration
    GA4: {
        MEASUREMENT_ID: 'G-XXXXXXXXXX', // Replace with your GA4 Measurement ID
        ENHANCED_ECOMMERCE: false,
        CUSTOM_DIMENSIONS: {
            page_type: 'custom_parameter_1',
            practice_area: 'custom_parameter_2',
            user_type: 'custom_parameter_3'
        }
    },

    // Google Tag Manager (Optional)
    GTM: {
        CONTAINER_ID: 'GTM-XXXXXXX', // Replace with your GTM Container ID
        ENABLED: false
    },

    // Google Ads Conversion Tracking
    GOOGLE_ADS: {
        CONVERSION_ID: 'AW-XXXXXXXXX', // Replace with your Google Ads Conversion ID
        CONVERSIONS: {
            CONTACT_FORM: 'CONVERSION_LABEL_1',
            PHONE_CALL: 'CONVERSION_LABEL_2',
            EMAIL_CLICK: 'CONVERSION_LABEL_3',
            CONSULTATION_REQUEST: 'CONVERSION_LABEL_4'
        }
    },

    // Facebook Pixel (Optional)
    FACEBOOK: {
        PIXEL_ID: 'XXXXXXXXXXXXXXX', // Replace with your Facebook Pixel ID
        ENABLED: false
    },

    // Hotjar or Similar Heat Mapping (Optional)
    HEATMAP: {
        HOTJAR_ID: 'XXXXXXX', // Replace with your Hotjar ID
        ENABLED: false
    },

    // Microsoft Clarity (Optional)
    CLARITY: {
        PROJECT_ID: 'XXXXXXXXXX', // Replace with your Microsoft Clarity Project ID
        ENABLED: false
    },

    // Tracking Preferences
    TRACKING: {
        // Core Web Vitals tracking
        TRACK_WEB_VITALS: true,

        // User engagement tracking
        TRACK_SCROLL_DEPTH: true,
        TRACK_TIME_ON_PAGE: true,
        TRACK_CLICKS: true,

        // Form tracking
        TRACK_FORM_INTERACTIONS: true,
        TRACK_FORM_ABANDONMENT: true,

        // Error tracking
        TRACK_JS_ERRORS: true,
        TRACK_404_ERRORS: true,

        // Phone and email tracking
        TRACK_PHONE_CLICKS: true,
        TRACK_EMAIL_CLICKS: true,

        // Performance monitoring
        TRACK_PAGE_SPEED: true,
        TRACK_RESOURCE_ERRORS: true
    },

    // Legal Website Specific Tracking
    LEGAL_SPECIFIC: {
        // Track practice area interest
        TRACK_PRACTICE_AREAS: true,

        // Track attorney profile views
        TRACK_ATTORNEY_PROFILES: true,

        // Track location page views
        TRACK_LOCATION_INTEREST: true,

        // Track resource/FAQ usage
        TRACK_RESOURCE_USAGE: true,

        // Track case result views
        TRACK_CASE_RESULTS: true
    },

    // Debug and Development
    DEBUG: {
        CONSOLE_LOGGING: false, // Set to true for development
        VERBOSE_TRACKING: false // Set to true to see all tracked events
    }
};

/**
 * Analytics Setup Instructions
 * ============================
 *
 * 1. Google Analytics 4 Setup:
 *    - Go to https://analytics.google.com/
 *    - Create a new GA4 property for your website
 *    - Copy the Measurement ID (starts with 'G-')
 *    - Replace 'G-XXXXXXXXXX' above with your actual ID
 *
 * 2. Google Ads Conversion Tracking:
 *    - Go to https://ads.google.com/
 *    - Set up conversion actions for:
 *      * Contact form submissions
 *      * Phone calls
 *      * Email clicks
 *      * Consultation requests
 *    - Copy the Conversion ID and Labels
 *    - Replace the placeholder values above
 *
 * 3. Google Search Console:
 *    - Go to https://search.google.com/search-console/
 *    - Add your website property
 *    - Verify ownership using the HTML tag method
 *    - Submit your sitemap.xml file
 *
 * 4. Google Tag Manager (Optional but Recommended):
 *    - Go to https://tagmanager.google.com/
 *    - Create a new container
 *    - Install the GTM code on all pages
 *    - Set up tags for GA4, Google Ads, etc.
 *
 * 5. Facebook Pixel (Optional):
 *    - Go to https://business.facebook.com/
 *    - Create a Facebook Pixel
 *    - Copy the Pixel ID
 *    - Enable Facebook tracking in config above
 *
 * 6. Microsoft Clarity (Free Heat Mapping):
 *    - Go to https://clarity.microsoft.com/
 *    - Create a new project
 *    - Copy the Project ID
 *    - Enable Clarity tracking in config above
 *
 * 7. Testing Your Setup:
 *    - Enable DEBUG.CONSOLE_LOGGING = true
 *    - Open browser console and test events
 *    - Check Real-Time reports in Google Analytics
 *    - Verify conversions are tracking properly
 *
 * 8. Legal Compliance:
 *    - Update your Privacy Policy to mention analytics
 *    - Consider implementing cookie consent if required
 *    - Ensure GDPR/CCPA compliance if applicable
 */