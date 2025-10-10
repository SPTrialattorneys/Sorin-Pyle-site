const fs = require('fs');
const path = require('path');

// Read the shared header and footer
const header = fs.readFileSync('_includes/header.html', 'utf8');
const footer = fs.readFileSync('_includes/footer.html', 'utf8');

// Get all HTML files in current directory and locations subdirectory
const htmlFiles = [
    ...fs.readdirSync('.').filter(f => f.endsWith('.html')),
    ...fs.readdirSync('./locations').filter(f => f.endsWith('.html')).map(f => `locations/${f}`)
];

// Markers for replacement
const HEADER_START = '<a href="#main-content" class="skip-link">Skip to main content</a>';
const HEADER_END = '<main id="main-content">';
const FOOTER_START = '<!-- ▼▼▼ FOOTER (Identical on all pages) ▼▼▼ -->';
const FOOTER_END = '<script src=';

let updatedCount = 0;
let errorCount = 0;

htmlFiles.forEach(file => {
    try {
        let content = fs.readFileSync(file, 'utf8');
        let modified = false;

        // Replace header
        const headerStartIndex = content.indexOf(HEADER_START);
        const headerEndIndex = content.indexOf(HEADER_END);

        if (headerStartIndex !== -1 && headerEndIndex !== -1) {
            const before = content.substring(0, headerStartIndex);
            const after = content.substring(headerEndIndex);
            content = before + header + '\n\n    ' + after;
            modified = true;
        }

        // Replace footer
        const footerStartIndex = content.indexOf(FOOTER_START);
        const footerEndIndex = content.indexOf(FOOTER_END);

        if (footerStartIndex !== -1 && footerEndIndex !== -1) {
            const before = content.substring(0, footerStartIndex);
            const after = content.substring(footerEndIndex);
            content = before + footer + '\n    <' + after;
            modified = true;
        }

        if (modified) {
            fs.writeFileSync(file, content, 'utf8');
            console.log(`✅ Updated: ${file}`);
            updatedCount++;
        } else {
            console.log(`⚠️  Skipped: ${file} (markers not found)`);
        }
    } catch (error) {
        console.error(`❌ Error updating ${file}:`, error.message);
        errorCount++;
    }
});

console.log(`\n📊 Summary:`);
console.log(`   Updated: ${updatedCount} files`);
console.log(`   Errors: ${errorCount} files`);
console.log(`\n✨ Done! All HTML pages now use shared header/footer from _includes/`);
