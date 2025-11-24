#!/usr/bin/env node

/**
 * CRITICAL CSS EXTRACTION SYSTEM
 *
 * Purpose: Automatically extracts above-the-fold CSS from rendered HTML
 *
 * When to re-run:
 * - After changing any CSS in src/assets/styles/
 * - After modifying page layouts (navbar, hero, footer)
 * - Automatically runs during npm run build:cloudflare
 *
 * Configuration:
 * - PAGES array (line 26): Add new pages for extraction
 * - dimensions: Viewport sizes to analyze (mobile/tablet/desktop)
 *
 * Output:
 * - src/_data/critical-homepage.css (~28KB)
 * - src/_data/critical-attorneys.css (~22KB)
 * - src/_data/critical-practice-areas.css (~19KB)
 * - src/_data/critical-page-layout.css (~15KB)
 *
 * Debugging:
 * - Check dist/ folder exists before running
 * - Verify HTML files rendered correctly
 * - Run npm run build:html:prod first if extraction fails
 *
 * DO NOT manually edit critical-*.css files - they are auto-generated
 *
 * Usage: node utilities/extract-critical-css.mjs
 */

import { generate as generateCritical } from 'critical';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const PROJECT_ROOT = path.join(__dirname, '..');
const DIST_DIR = path.join(PROJECT_ROOT, 'dist');
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'src', '_data');

// Pages to extract critical CSS for
const PAGES = [
  {
    name: 'homepage',
    url: '/index.html',
    output: 'critical-homepage.css',
    dimensions: [
      { width: 375, height: 667 },   // Mobile
      { width: 768, height: 1024 },  // Tablet
      { width: 1920, height: 1080 }  // Desktop
    ]
  },
  {
    name: 'attorneys',
    url: '/attorneys.html',
    output: 'critical-attorneys.css',
    dimensions: [
      { width: 375, height: 667 },
      { width: 1920, height: 1080 }
    ]
  },
  {
    name: 'practice-areas',
    url: '/practice-areas.html',
    output: 'critical-practice-areas.css',
    dimensions: [
      { width: 375, height: 667 },
      { width: 1920, height: 1080 }
    ]
  },
  {
    name: 'page-layout',
    url: '/dui-defense.html',
    output: 'critical-page-layout.css',
    dimensions: [
      { width: 375, height: 667 },   // Mobile
      { width: 768, height: 1024 },  // Tablet
      { width: 1920, height: 1080 }  // Desktop
    ]
  }
];

/**
 * Extract critical CSS for a single page
 */
async function extractCriticalCSS(page) {
  console.log(`\n📄 Extracting critical CSS for ${page.name}...`);

  const src = path.join(DIST_DIR, page.url);
  const outputPath = path.join(OUTPUT_DIR, page.output);

  try {
    const { css } = await generateCritical({
      src: src,
      target: {
        css: outputPath
      },
      dimensions: page.dimensions,
      inline: false,  // We'll inline manually in the template
      extract: false, // Don't remove critical CSS from main stylesheet
      penthouse: {
        timeout: 60000,
        renderWaitTime: 1000
      }
    });

    console.log(`✅ Critical CSS extracted: ${outputPath}`);
    console.log(`   Size: ${(css.length / 1024).toFixed(2)} KB`);

    return css;
  } catch (error) {
    console.error(`❌ Error extracting critical CSS for ${page.name}:`, error.message);
    throw error;
  }
}

/**
 * Main function
 */
async function main() {
  console.log('🚀 Starting critical CSS extraction...\n');
  console.log(`Project root: ${PROJECT_ROOT}`);
  console.log(`Dist directory: ${DIST_DIR}`);
  console.log(`Output directory: ${OUTPUT_DIR}\n`);

  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Check if dist directory exists
  if (!fs.existsSync(DIST_DIR)) {
    console.error('❌ dist directory not found. Run "npm run build:html" first.');
    process.exit(1);
  }

  // Extract critical CSS for each page
  const results = [];
  for (const page of PAGES) {
    try {
      const css = await extractCriticalCSS(page);
      results.push({
        page: page.name,
        success: true,
        size: css.length
      });
    } catch (error) {
      results.push({
        page: page.name,
        success: false,
        error: error.message
      });
    }
  }

  // Summary
  console.log('\n📊 Summary:');
  console.log('─'.repeat(50));
  results.forEach(result => {
    if (result.success) {
      console.log(`✅ ${result.page}: ${(result.size / 1024).toFixed(2)} KB`);
    } else {
      console.log(`❌ ${result.page}: ${result.error}`);
    }
  });
  console.log('─'.repeat(50));

  const successCount = results.filter(r => r.success).length;
  console.log(`\n✨ Extracted critical CSS for ${successCount}/${results.length} pages`);
}

// Run main function
main().catch(error => {
  console.error('❌ Fatal error:', error);
  process.exit(1);
});
