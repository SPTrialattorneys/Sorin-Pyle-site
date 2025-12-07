import sharp from 'sharp';

const inputFile = 'samples/acba.png';
const outputFile = 'images/allegan-county-bar-association-logo.avif';

sharp(inputFile)
    .resize(800, 600, {
        fit: 'cover',
        position: 'center'
    })
    .avif({
        quality: 85,
        effort: 6
    })
    .toFile(outputFile)
    .then(info => {
        console.log('✓ ACBA logo optimized successfully');
        console.log(`  Input:  samples/acba.png`);
        console.log(`  Output: ${outputFile}`);
        console.log(`  Size:   ${Math.round(info.size / 1024)} KB`);
        console.log(`  Dimensions: ${info.width}x${info.height}`);
    })
    .catch(err => {
        console.error('Error optimizing image:', err);
        process.exit(1);
    });
