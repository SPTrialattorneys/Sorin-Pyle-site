module.exports = {
  plugins: [
    // MUST be first - resolves @import statements and bundles CSS files together
    require('postcss-import'),

    // Add vendor prefixes for browser compatibility
    require('autoprefixer')({
      overrideBrowserslist: [
        '>= 0.5%',
        'last 2 major versions',
        'not dead',
        'Chrome >= 60',
        'Firefox >= 60',
        'Edge >= 79',
        'Safari >= 12',
        'iOS >= 12'
      ]
    }),

    // Minify and optimize CSS for production
    require('cssnano')({
      preset: ['default', {
        discardComments: {
          removeAll: true  // Remove all comments
        },
        normalizeWhitespace: true,  // Minimize whitespace
        minifyFontValues: true,     // Optimize font declarations
        minifyGradients: true,      // Optimize gradients
        mergeLonghand: true,        // Merge longhand properties
        mergeRules: true,           // Merge duplicate rules
        colormin: true,             // Minimize color values
        reduceIdents: false,        // Keep animation/keyframe names
        zindex: false               // Don't modify z-index values
      }]
    })
  ]
};
