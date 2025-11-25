#!/usr/bin/env node
/**
 * Optimize CDAM conference logo using Sharp
 * Converts PNG to AVIF format with optimal compression
 */

import sharp from 'sharp';
import { readFileSync, statSync } from 'fs';

const sourcePath = 'samples/cdam.png';
const outputPath = 'images/cdam-conference-michigan-criminal-defense.avif';
const targetWidth = 800;

console.log('='.repeat(60));
console.log('Sharp AVIF Optimization - CDAM Logo');
console.log('='.repeat(60));
console.log();

console.log(`Processing: CDAM Conference Logo`);
console.log(`  Source: ${sourcePath}`);
console.log(`  Output: ${outputPath}`);
console.log(`  Target width: ${targetWidth}px`);
console.log();

// Get original file size
const originalSize = statSync(sourcePath).size / 1024;
console.log(`  Original size: ${originalSize.toFixed(1)} KB`);

// Process image
try {
  await sharp(sourcePath)
    .resize(targetWidth, targetWidth, {
      fit: 'inside',
      withoutEnlargement: true
    })
    .avif({
      quality: 85,
      effort: 6  // Higher effort = better compression (0-9)
    })
    .toFile(outputPath);

  // Get optimized file size
  const optimizedSize = statSync(outputPath).size / 1024;
  const reduction = ((originalSize - optimizedSize) / originalSize) * 100;

  console.log(`  Optimized size: ${optimizedSize.toFixed(1)} KB`);
  console.log(`  Reduction: ${reduction.toFixed(1)}%`);
  console.log();
  console.log('[OK] Optimization complete!');
  console.log();
  console.log('='.repeat(60));

} catch (error) {
  console.error(`[ERROR] Optimization failed: ${error.message}`);
  process.exit(1);
}
