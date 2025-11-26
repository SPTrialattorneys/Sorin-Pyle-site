#!/usr/bin/env node

/**
 * HTML Validation Script
 *
 * Validates built HTML files for common issues:
 * 1. Broken internal links (href="#...", href="page.html", src="...")
 * 2. Missing alt text on images
 * 3. Duplicate IDs
 * 4. Missing meta descriptions
 * 5. Canonical URL consistency with sitemap.xml
 *
 * Usage: node utilities/validate-html.js
 * Or: npm run validate:html
 */

const fs = require('fs');
const path = require('path');
const { parse } = require('node-html-parser');

// ANSI color codes
const colors = {
  reset: '\x1b[0m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  gray: '\x1b[90m'
};

// Configuration
const DIST_DIR = path.join(__dirname, '..', 'dist');
const SITEMAP_PATH = path.join(__dirname, '..', 'sitemap.xml');
const BASE_URL = 'https://www.sorinpyle.com';

// Error and warning trackers
let errors = [];
let warnings = [];

/**
 * Get all HTML files from dist/
 */
function getHtmlFiles(dir = DIST_DIR, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });

  return fileList;
}

/**
 * Parse sitemap.xml and extract canonical URLs
 */
function parseSitemap() {
  if (!fs.existsSync(SITEMAP_PATH)) {
    warnings.push({
      type: 'sitemap',
      message: 'sitemap.xml not found - skipping canonical URL validation'
    });
    return new Map();
  }

  const sitemapContent = fs.readFileSync(SITEMAP_PATH, 'utf8');
  const urlMap = new Map();

  // Simple regex to extract URLs from sitemap
  const urlRegex = /<loc>(.*?)<\/loc>/g;
  let match;

  while ((match = urlRegex.exec(sitemapContent)) !== null) {
    const url = match[1];
    // Convert URL to relative path (e.g., https://www.sorinpyle.com/attorneys.html -> attorneys.html)
    const relativePath = url.replace(BASE_URL + '/', '').replace(BASE_URL, 'index.html');
    urlMap.set(relativePath, url);
  }

  return urlMap;
}

/**
 * Check 1: Validate internal links
 */
function checkInternalLinks(htmlFile, root) {
  const relativePath = path.relative(DIST_DIR, htmlFile);
  const dir = path.dirname(htmlFile);

  // Find all links
  const links = root.querySelectorAll('a[href], link[href], script[src], img[src]');

  links.forEach(element => {
    const attr = element.hasAttribute('href') ? 'href' : 'src';
    const link = element.getAttribute(attr);

    if (!link) return;

    // Skip external links, mailto, tel, javascript, data URIs
    if (
      link.startsWith('http://') ||
      link.startsWith('https://') ||
      link.startsWith('mailto:') ||
      link.startsWith('tel:') ||
      link.startsWith('javascript:') ||
      link.startsWith('data:') ||
      link.startsWith('#') // Anchor-only links checked separately
    ) {
      return;
    }

    // Handle anchor links (href="page.html#section")
    const [linkPath, anchor] = link.split('#');
    if (!linkPath) return; // Pure anchor link (#section)

    // Strip query strings (e.g., ?v=20251123 for cache busting)
    const linkPathWithoutQuery = linkPath.split('?')[0];

    // Resolve relative path
    let targetPath;
    if (linkPathWithoutQuery.startsWith('/')) {
      // Absolute path from root
      targetPath = path.join(DIST_DIR, linkPathWithoutQuery);
    } else {
      // Relative path
      targetPath = path.resolve(dir, linkPathWithoutQuery);
    }

    // Check if file exists
    if (!fs.existsSync(targetPath)) {
      errors.push({
        file: relativePath,
        type: 'broken-link',
        message: `Broken ${attr}: ${link}`,
        element: element.toString().substring(0, 100)
      });
    }

    // Check anchor exists (if specified)
    if (anchor && fs.existsSync(targetPath)) {
      try {
        const targetContent = fs.readFileSync(targetPath, 'utf8');
        const targetRoot = parse(targetContent);

        // Check for id or name matching anchor
        const anchorTarget = targetRoot.querySelector(`#${anchor}, [name="${anchor}"]`);
        if (!anchorTarget) {
          warnings.push({
            file: relativePath,
            type: 'missing-anchor',
            message: `Anchor not found: ${link} (target element #${anchor} missing)`
          });
        }
      } catch (error) {
        // Silently skip if can't parse target file
      }
    }
  });
}

/**
 * Check 2: Validate alt text on images
 */
function checkImageAltText(htmlFile, root) {
  const relativePath = path.relative(DIST_DIR, htmlFile);
  const images = root.querySelectorAll('img');

  images.forEach(img => {
    const alt = img.getAttribute('alt');
    const src = img.getAttribute('src');

    // Skip if no src (malformed img tag)
    if (!src) return;

    // Alt attribute must exist (can be empty for decorative images)
    if (alt === null || alt === undefined) {
      errors.push({
        file: relativePath,
        type: 'missing-alt',
        message: `Image missing alt attribute: ${src}`,
        element: img.toString().substring(0, 100)
      });
    }
    // Warn if alt is empty (should only be for decorative images)
    else if (alt.trim() === '' && !src.includes('logo') && !src.includes('icon')) {
      warnings.push({
        file: relativePath,
        type: 'empty-alt',
        message: `Image has empty alt text (OK if decorative): ${src}`
      });
    }
  });
}

/**
 * Check 3: Validate for duplicate IDs
 */
function checkDuplicateIds(htmlFile, root) {
  const relativePath = path.relative(DIST_DIR, htmlFile);
  const elementsWithId = root.querySelectorAll('[id]');
  const idMap = new Map();

  elementsWithId.forEach(element => {
    const id = element.getAttribute('id');
    if (!id) return;

    if (idMap.has(id)) {
      errors.push({
        file: relativePath,
        type: 'duplicate-id',
        message: `Duplicate ID found: "${id}"`,
        elements: [idMap.get(id), element.toString().substring(0, 80)]
      });
    } else {
      idMap.set(id, element.toString().substring(0, 80));
    }
  });
}

/**
 * Check 4: Validate meta descriptions
 */
function checkMetaDescription(htmlFile, root) {
  const relativePath = path.relative(DIST_DIR, htmlFile);

  // Skip error pages
  if (relativePath.includes('404.html') || relativePath.includes('500.html')) {
    return;
  }

  const metaDesc = root.querySelector('meta[name="description"]');

  if (!metaDesc) {
    errors.push({
      file: relativePath,
      type: 'missing-meta-desc',
      message: 'Missing meta description'
    });
  } else {
    const content = metaDesc.getAttribute('content');
    if (!content || content.trim().length === 0) {
      errors.push({
        file: relativePath,
        type: 'empty-meta-desc',
        message: 'Meta description is empty'
      });
    } else if (content.length > 160) {
      warnings.push({
        file: relativePath,
        type: 'long-meta-desc',
        message: `Meta description too long (${content.length} chars, recommended: 150-160)`
      });
    }
  }
}

/**
 * Check 5: Validate canonical URLs match sitemap
 */
function checkCanonicalUrls(htmlFile, root, sitemapUrls) {
  const relativePath = path.relative(DIST_DIR, htmlFile);

  // Skip error pages
  if (relativePath.includes('404.html') || relativePath.includes('500.html')) {
    return;
  }

  const canonical = root.querySelector('link[rel="canonical"]');

  if (!canonical) {
    warnings.push({
      file: relativePath,
      type: 'missing-canonical',
      message: 'Missing canonical URL (recommended for SEO)'
    });
    return;
  }

  const canonicalUrl = canonical.getAttribute('href');
  const expectedUrl = sitemapUrls.get(relativePath);

  if (expectedUrl && canonicalUrl !== expectedUrl) {
    errors.push({
      file: relativePath,
      type: 'canonical-mismatch',
      message: `Canonical URL mismatch:\n    Found: ${canonicalUrl}\n    Expected (from sitemap): ${expectedUrl}`
    });
  }
}

/**
 * Main validation function
 */
function validateHtml() {
  console.log(`${colors.blue}HTML Validation${colors.reset}\n`);

  // Check if dist/ exists
  if (!fs.existsSync(DIST_DIR)) {
    console.log(`${colors.yellow}⚠ dist/ directory not found${colors.reset}`);
    console.log(`${colors.gray}Run build first: npm run build:html:prod${colors.reset}\n`);
    return true; // Not an error - just skip validation
  }

  // Get all HTML files
  const htmlFiles = getHtmlFiles();
  if (htmlFiles.length === 0) {
    console.log(`${colors.yellow}⚠ No HTML files found in dist/${colors.reset}\n`);
    return true;
  }

  console.log(`${colors.gray}Found ${htmlFiles.length} HTML files${colors.reset}\n`);

  // Parse sitemap for canonical URL validation
  const sitemapUrls = parseSitemap();

  // Validate each file
  htmlFiles.forEach(htmlFile => {
    try {
      const content = fs.readFileSync(htmlFile, 'utf8');
      const root = parse(content);

      checkInternalLinks(htmlFile, root);
      checkImageAltText(htmlFile, root);
      checkDuplicateIds(htmlFile, root);
      checkMetaDescription(htmlFile, root);
      checkCanonicalUrls(htmlFile, root, sitemapUrls);
    } catch (error) {
      warnings.push({
        file: path.relative(DIST_DIR, htmlFile),
        type: 'parse-error',
        message: `Could not parse HTML: ${error.message}`
      });
    }
  });

  // Print results
  console.log('─'.repeat(60));

  if (errors.length > 0) {
    console.log(`${colors.red}✗ Found ${errors.length} error(s):${colors.reset}\n`);

    // Group errors by type
    const errorsByType = {};
    errors.forEach(error => {
      if (!errorsByType[error.type]) {
        errorsByType[error.type] = [];
      }
      errorsByType[error.type].push(error);
    });

    Object.keys(errorsByType).forEach(type => {
      const typeErrors = errorsByType[type];
      console.log(`${colors.red}${type.toUpperCase()} (${typeErrors.length}):${colors.reset}`);
      typeErrors.forEach(error => {
        console.log(`  ${colors.red}•${colors.reset} ${error.file}`);
        console.log(`    ${error.message}`);
        if (error.element) {
          console.log(`    ${colors.gray}${error.element}${colors.reset}`);
        }
      });
      console.log();
    });
  }

  if (warnings.length > 0) {
    console.log(`${colors.yellow}⚠ Found ${warnings.length} warning(s):${colors.reset}\n`);

    warnings.slice(0, 10).forEach(warning => {
      console.log(`  ${colors.yellow}•${colors.reset} ${warning.file || 'general'}`);
      console.log(`    ${warning.message}`);
    });

    if (warnings.length > 10) {
      console.log(`${colors.gray}  ... and ${warnings.length - 10} more warnings${colors.reset}`);
    }
    console.log();
  }

  console.log('─'.repeat(60));

  if (errors.length > 0) {
    console.log(`${colors.red}✗ HTML validation FAILED${colors.reset}`);
    console.log(`\n${colors.gray}Fix errors above before committing.${colors.reset}`);
    return false;
  } else if (warnings.length > 0) {
    console.log(`${colors.yellow}⚠ HTML validation passed with ${warnings.length} warning(s)${colors.reset}`);
    console.log(`${colors.gray}Review warnings above (not blocking commit).${colors.reset}`);
    return true;
  } else {
    console.log(`${colors.green}✓ HTML validation passed - no issues found!${colors.reset}`);
    return true;
  }
}

// Run validation if called directly
if (require.main === module) {
  const success = validateHtml();
  process.exit(success ? 0 : 1);
}

// Export for use in other scripts
module.exports = { validateHtml };
