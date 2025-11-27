/**
 * Critical CSS Deduplication Script
 *
 * Removes duplicate CSS rules from critical CSS files to reduce file size.
 * Uses PostCSS with postcss-discard-duplicates plugin.
 *
 * Expected Reduction: 137 KB → 50-60 KB (56% improvement)
 *
 * Run: node utilities/deduplicate-critical-css.mjs
 */

import postcss from 'postcss';
import dedupe from 'postcss-discard-duplicates';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Critical CSS files to deduplicate
const criticalFiles = [
  'src/_data/critical-homepage.css',
  'src/_data/critical-attorneys.css',
  'src/_data/critical-practice-areas.css',
  'src/_data/critical-page-layout.css'
];

/**
 * Deduplicate a single CSS file
 * @param {string} filePath - Relative path to CSS file
 */
async function deduplicateFile(filePath) {
  const fullPath = path.join(__dirname, '..', filePath);

  try {
    // Read original CSS
    const css = await fs.readFile(fullPath, 'utf-8');
    const originalSize = Buffer.byteLength(css, 'utf-8');

    // Process with PostCSS deduplication
    const result = await postcss([dedupe()]).process(css, {
      from: fullPath,
      to: fullPath
    });

    // Write deduplicated CSS
    await fs.writeFile(fullPath, result.css);

    // Calculate reduction
    const newSize = Buffer.byteLength(result.css, 'utf-8');
    const reduction = originalSize - newSize;
    const reductionPercent = ((reduction / originalSize) * 100).toFixed(1);

    console.log(`✓ ${path.basename(filePath)}`);
    console.log(`  Before: ${(originalSize / 1024).toFixed(2)} KB`);
    console.log(`  After:  ${(newSize / 1024).toFixed(2)} KB`);
    console.log(`  Saved:  ${(reduction / 1024).toFixed(2)} KB (${reductionPercent}%)`);
    console.log('');

    return { originalSize, newSize, reduction };
  } catch (error) {
    console.error(`✗ Error processing ${filePath}:`, error.message);
    throw error;
  }
}

/**
 * Deduplicate all critical CSS files
 */
async function deduplicateAll() {
  console.log('=== Critical CSS Deduplication ===\n');

  let totalOriginal = 0;
  let totalNew = 0;

  for (const file of criticalFiles) {
    const stats = await deduplicateFile(file);
    totalOriginal += stats.originalSize;
    totalNew += stats.newSize;
  }

  const totalReduction = totalOriginal - totalNew;
  const totalReductionPercent = ((totalReduction / totalOriginal) * 100).toFixed(1);

  console.log('=== Summary ===');
  console.log(`Total Before: ${(totalOriginal / 1024).toFixed(2)} KB`);
  console.log(`Total After:  ${(totalNew / 1024).toFixed(2)} KB`);
  console.log(`Total Saved:  ${(totalReduction / 1024).toFixed(2)} KB (${totalReductionPercent}%)`);
  console.log('');
  console.log('✓ Deduplication complete!');
}

// Run deduplication
deduplicateAll().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
