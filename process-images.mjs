#!/usr/bin/env node

/**
 * Image Processing with Sharp
 *
 * Generates responsive image sizes and modern formats (WebP, AVIF) from source images.
 * Creates a manifest file for the responsive image shortcode to reference.
 */

import sharp from 'sharp';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const CONFIG = {
  inputDir: path.join(__dirname, 'images'),
  outputDir: path.join(__dirname, 'dist', 'images'),

  // Responsive image widths to generate
  widths: [320, 640, 768, 1024, 1280, 1920],

  // Formats to generate (in addition to source format)
  formats: ['webp', 'avif'],

  // Quality settings
  quality: {
    jpeg: 85,
    webp: 85,
    avif: 80,
    png: 90
  },

  // File extensions to process
  extensions: ['.jpg', '.jpeg', '.png'],

  // Files to skip (already optimized or special purpose)
  skipFiles: [
    'logo.svg',
    'logo-icon.svg',
    'logo-icon-white-ship.svg',
    'favicon.png'
  ],

  // Skip files that already have size suffixes (manually optimized)
  skipPattern: /-\d+w\.(avif|webp|jpg|jpeg|png)$/
};

/**
 * Get all image files to process
 */
function getImageFiles() {
  const files = fs.readdirSync(CONFIG.inputDir);

  return files.filter(file => {
    const ext = path.extname(file).toLowerCase();
    const isProcessable = CONFIG.extensions.includes(ext);
    const isSkipped = CONFIG.skipFiles.includes(file);
    const hasSkipPattern = CONFIG.skipPattern.test(file);

    return isProcessable && !isSkipped && !hasSkipPattern;
  });
}

/**
 * Process a single image file
 */
async function processImage(filename) {
  const inputPath = path.join(CONFIG.inputDir, filename);
  const basename = path.basename(filename, path.extname(filename));

  console.log(`\n📸 Processing: ${filename}`);

  // Get image metadata
  const metadata = await sharp(inputPath).metadata();
  const originalWidth = metadata.width;
  const originalFormat = metadata.format;

  console.log(`   Original: ${originalWidth}x${metadata.height} (${originalFormat})`);

  // Determine which widths to generate (don't upscale)
  const widthsToGenerate = CONFIG.widths.filter(w => w <= originalWidth);

  const results = [];

  // Process each width
  for (const width of widthsToGenerate) {
    // Generate WebP
    if (CONFIG.formats.includes('webp')) {
      const outputPath = path.join(CONFIG.outputDir, `${basename}-${width}w.webp`);
      await sharp(inputPath)
        .resize(width, null, { withoutEnlargement: true })
        .webp({ quality: CONFIG.quality.webp })
        .toFile(outputPath);

      const stats = fs.statSync(outputPath);
      results.push({ format: 'webp', width, size: stats.size });
    }

    // Generate AVIF
    if (CONFIG.formats.includes('avif')) {
      const outputPath = path.join(CONFIG.outputDir, `${basename}-${width}w.avif`);
      await sharp(inputPath)
        .resize(width, null, { withoutEnlargement: true })
        .avif({ quality: CONFIG.quality.avif })
        .toFile(outputPath);

      const stats = fs.statSync(outputPath);
      results.push({ format: 'avif', width, size: stats.size });
    }

    // Generate original format (JPEG/PNG)
    const originalExt = path.extname(filename);
    const outputPath = path.join(CONFIG.outputDir, `${basename}-${width}w${originalExt}`);

    let sharpPipeline = sharp(inputPath).resize(width, null, { withoutEnlargement: true });

    if (originalFormat === 'jpeg' || originalFormat === 'jpg') {
      sharpPipeline = sharpPipeline.jpeg({ quality: CONFIG.quality.jpeg });
    } else if (originalFormat === 'png') {
      sharpPipeline = sharpPipeline.png({ quality: CONFIG.quality.png });
    }

    await sharpPipeline.toFile(outputPath);

    const stats = fs.statSync(outputPath);
    results.push({ format: originalFormat, width, size: stats.size });
  }

  // Summary
  console.log(`   Generated ${results.length} images:`);
  const byFormat = results.reduce((acc, r) => {
    acc[r.format] = (acc[r.format] || 0) + 1;
    return acc;
  }, {});

  Object.entries(byFormat).forEach(([format, count]) => {
    const totalSize = results
      .filter(r => r.format === format)
      .reduce((sum, r) => sum + r.size, 0);
    console.log(`   - ${count} ${format.toUpperCase()} files (${(totalSize / 1024).toFixed(1)} KB total)`);
  });

  return results;
}

/**
 * Copy SVG and already-optimized files
 */
function copyStaticImages() {
  console.log('\n📋 Copying SVG and optimized files...');

  const files = fs.readdirSync(CONFIG.inputDir);
  let copiedCount = 0;

  files.forEach(file => {
    const ext = path.extname(file).toLowerCase();

    // Copy SVG files
    if (ext === '.svg') {
      fs.copyFileSync(
        path.join(CONFIG.inputDir, file),
        path.join(CONFIG.outputDir, file)
      );
      copiedCount++;
    }

    // Copy already-optimized AVIF/WebP files
    if ((ext === '.avif' || ext === '.webp') && CONFIG.skipPattern.test(file)) {
      fs.copyFileSync(
        path.join(CONFIG.inputDir, file),
        path.join(CONFIG.outputDir, file)
      );
      copiedCount++;
    }

    // Copy favicon and special files
    if (CONFIG.skipFiles.includes(file)) {
      fs.copyFileSync(
        path.join(CONFIG.inputDir, file),
        path.join(CONFIG.outputDir, file)
      );
      copiedCount++;
    }
  });

  console.log(`   Copied ${copiedCount} files`);
}

/**
 * Generate image manifest for shortcode
 */
function generateManifest(processedImages) {
  const manifest = {};

  processedImages.forEach(({ filename, results }) => {
    const basename = path.basename(filename, path.extname(filename));

    manifest[basename] = {
      original: filename,
      variants: results.map(r => ({
        format: r.format,
        width: r.width,
        size: r.size,
        url: `/images/${basename}-${r.width}w.${r.format}`
      }))
    };
  });

  const manifestPath = path.join(__dirname, 'src', '_data', 'images.json');
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));

  console.log(`\n📝 Generated manifest: ${manifestPath}`);
  console.log(`   ${Object.keys(manifest).length} images catalogued`);
}

/**
 * Main function
 */
async function main() {
  console.log('🚀 Starting image processing with Sharp...\n');

  // Ensure output directory exists
  if (!fs.existsSync(CONFIG.outputDir)) {
    fs.mkdirSync(CONFIG.outputDir, { recursive: true });
  }

  // Get images to process
  const imageFiles = getImageFiles();
  console.log(`📂 Found ${imageFiles.length} images to process\n`);

  if (imageFiles.length === 0) {
    console.log('ℹ️  No images to process. All images are already optimized or skipped.');
    copyStaticImages();
    return;
  }

  // Process each image
  const processedImages = [];

  for (const file of imageFiles) {
    try {
      const results = await processImage(file);
      processedImages.push({ filename: file, results });
    } catch (error) {
      console.error(`❌ Error processing ${file}:`, error.message);
    }
  }

  // Copy static files
  copyStaticImages();

  // Generate manifest
  generateManifest(processedImages);

  // Summary
  console.log('\n✨ Image processing complete!');
  console.log(`   Processed: ${processedImages.length} images`);
  console.log(`   Generated: ${processedImages.reduce((sum, img) => sum + img.results.length, 0)} variants`);
}

// Run
main().catch(error => {
  console.error('❌ Fatal error:', error);
  process.exit(1);
});
