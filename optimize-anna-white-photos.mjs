import sharp from 'sharp';
import { promises as fs } from 'fs';

const photos = [
    {
        input: 'samples/aw.jpg',
        output: 'images/anna-white-judicial-announcement-speaking.avif',
        alt: 'Attorney Anna White speaking at her judicial campaign announcement outside Holland District Court'
    },
    {
        input: 'samples/bh.jpg',
        output: 'images/robert-hamilton-introducing-anna-white-judge.avif',
        alt: 'Attorney Robert Hamilton introducing Anna White at judicial campaign announcement'
    },
    {
        input: 'samples/aw4j.jpg',
        output: 'images/anna-white-campaign-announcement-crowd-holland.avif',
        alt: 'Crowd gathered outside Holland District Court for Anna White judicial campaign announcement'
    }
];

console.log('🖼️  Optimizing Anna White campaign announcement photos...\n');

for (const photo of photos) {
    try {
        const info = await sharp(photo.input)
            .resize(800, null, {
                fit: 'inside',
                withoutEnlargement: true
            })
            .avif({
                quality: 85,
                effort: 6
            })
            .toFile(photo.output);

        const inputStats = await fs.stat(photo.input);
        const inputSize = (inputStats.size / 1024 / 1024).toFixed(2);
        const outputSize = (info.size / 1024).toFixed(2);
        const reduction = (((inputStats.size - info.size) / inputStats.size) * 100).toFixed(1);

        console.log(`✓ ${photo.output}`);
        console.log(`  Input:  ${photo.input} (${inputSize} MB)`);
        console.log(`  Output: ${outputSize} KB`);
        console.log(`  Size reduction: ${reduction}%`);
        console.log(`  Dimensions: ${info.width}x${info.height}`);
        console.log(`  Alt text: "${photo.alt}"`);
        console.log('');
    } catch (err) {
        console.error(`✗ Error processing ${photo.input}:`, err.message);
    }
}

console.log('✅ All photos optimized successfully!');
