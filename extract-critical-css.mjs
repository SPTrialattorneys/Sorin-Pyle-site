#!/usr/bin/env node

/**
 * Extract Critical CSS
 *
 * This script extracts above-the-fold (critical) CSS for key pages using the critical npm package.
 * Critical CSS is inlined in the <head> to improve First Contentful Paint (FCP) and Largest Contentful Paint (LCP).
 *
 * Usage: node extract-critical-css.js
 */

import { generate as generateCritical } from 'critical';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const BASE_URL = 'http://localhost:8080';
const DIST_DIR = path.join(__dirname, 'dist');
const OUTPUT_DIR = path.join(__dirname, 'src/_data');

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
  console.log(`Base URL: ${BASE_URL}`);
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
