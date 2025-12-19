import sharp from 'sharp';
import { promises as fs } from 'fs';

const input = 'samples/originals/IMG_3013.jpg';
const output = 'samples/originals/spheadshot.jpg';

console.log('🖼️  Optimizing Sorin headshot for web...\n');

try {
    // Get original image info
    const metadata = await sharp(input).metadata();
    console.log(`Original: ${metadata.width}x${metadata.height} (${(metadata.size / 1024 / 1024).toFixed(2)} MB)`);

    // Resize to max 4096x4096, optimize quality
    const info = await sharp(input)
        .resize(4096, 4096, {
            fit: 'inside',
            withoutEnlargement: true
        })
        .jpeg({
            quality: 90,
            mozjpeg: true  // Use mozjpeg for better compression
        })
        .toFile(output);

    const outputStats = await fs.stat(output);
    const outputSize = (outputStats.size / 1024 / 1024).toFixed(2);
    const reduction = (((metadata.size - outputStats.size) / metadata.size) * 100).toFixed(1);

    console.log(`\n✓ ${output}`);
    console.log(`  Dimensions: ${info.width}x${info.height}`);
    console.log(`  Output size: ${outputSize} MB`);
    console.log(`  Size reduction: ${reduction}%`);
    console.log(`  Format: JPEG (quality 90, mozjpeg)`);

} catch (err) {
    console.error(`✗ Error processing ${input}:`, err.message);
}
