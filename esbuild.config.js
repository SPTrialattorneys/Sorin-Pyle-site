const esbuild = require('esbuild');
const path = require('path');

// Build configuration
const buildConfig = {
  entryPoints: {
    'main.min': 'src/assets/scripts/main.js',
    'cookie-consent': 'src/assets/scripts/cookie-consent.js',
    'tracking': 'src/assets/scripts/tracking.js',
    'business-card': 'src/assets/scripts/business-card.js',
    'qr-campaign': 'src/assets/scripts/qr-campaign.js'
  },
  bundle: true,
  minify: true,
  sourcemap: true,
  target: ['es2020', 'chrome80', 'firefox78', 'safari14', 'edge88'],
  outdir: 'dist/js',
  format: 'iife', // Immediately Invoked Function Expression for browser compatibility
  splitting: false, // Not supported with IIFE format
  platform: 'browser',
  treeShaking: true,
  legalComments: 'none',
  logLevel: 'info'
};

// Build function
async function build() {
  try {
    console.log('Building JavaScript with esbuild...');
    const result = await esbuild.build(buildConfig);
    console.log('JavaScript build complete!');
    return result;
  } catch (error) {
    console.error('Build failed:', error);
    process.exit(1);
  }
}

// Watch mode for development
async function watch() {
  try {
    console.log('Starting esbuild watch mode...');
    const context = await esbuild.context(buildConfig);
    await context.watch();
    console.log('Watching for JavaScript changes...');
  } catch (error) {
    console.error('Watch mode failed:', error);
    process.exit(1);
  }
}

// Run build if executed directly
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.includes('--watch')) {
    watch();
  } else {
    build();
  }
}

module.exports = { build, watch, buildConfig };
