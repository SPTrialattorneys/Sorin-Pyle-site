#!/usr/bin/env node

/**
 * Blog Image Optimizer using Sharp
 *
 * Optimizes IMG_2786.jpg from samples/originals/ for use in blog post
 * Output: images/sorin-panainte-trial-attorney.avif
 *
 * Target specs:
 * - Format: AVIF (best compression)
 * - Size: 800x600 (4:3 ratio for full article, CSS crops for preview)
 * - Quality: 85 (good balance)
 */

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const inputFile = 'samples/originals/IMG_2786.jpg';
const outputFile = 'images/sorin-panainte-trial-attorney.avif';

console.log('🖼️  Blog Image Optimizer');
console.log('========================\n');

// Check if input file exists
if (!fs.existsSync(inputFile)) {
    console.error(`❌ Error: Input file not found: ${inputFile}`);
    process.exit(1);
}

// Get input file stats
const inputStats = fs.statSync(inputFile);
console.log(`📁 Input: ${inputFile}`);
console.log(`📊 Original size: ${(inputStats.size / 1024 / 1024).toFixed(2)} MB\n`);

// Optimize image
console.log('🔧 Processing...');

sharp(inputFile)
    .extract({
        left: 0,
        top: 50,               // Start 50px from top - maximum headroom
        width: 3405,           // Full width
        height: 2554           // 4:3 ratio (3405 * 0.75)
    })
    .resize(800, 600, {
        fit: 'cover'
    })
    .avif({
        quality: 85,            // Good quality/size balance
        effort: 6               // Compression effort (0-9, 6 is good balance)
    })
    .toFile(outputFile)
    .then(info => {
        const outputStats = fs.statSync(outputFile);
        const savings = ((1 - outputStats.size / inputStats.size) * 100).toFixed(1);

        console.log('✅ Optimization complete!\n');
        console.log(`📁 Output: ${outputFile}`);
        console.log(`📊 Optimized size: ${(outputStats.size / 1024).toFixed(2)} KB`);
        console.log(`📐 Dimensions: ${info.width}x${info.height}`);
        console.log(`💾 Savings: ${savings}% reduction`);
        console.log(`\n✨ Ready for blog post use!`);
    })
    .catch(err => {
        console.error('❌ Error during optimization:', err);
        process.exit(1);
    });
