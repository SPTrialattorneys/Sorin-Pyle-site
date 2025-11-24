#!/usr/bin/env node

/**
 * Schema Markup Validation Script
 *
 * Validates JSON-LD schema markup in built HTML files to prevent Google Rich Results errors.
 *
 * Usage: node utilities/validate-schema.js
 * Or: npm run validate:schema
 */

const fs = require('fs');
const path = require('path');

// ANSI color codes for terminal output
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
const LOCATIONS_DIR = path.join(DIST_DIR, 'locations');

// Validation results
let totalFiles = 0;
let filesWithSchema = 0;
let totalSchemas = 0;
let totalErrors = 0;
let totalWarnings = 0;

/**
 * Extract all JSON-LD schema blocks from HTML content
 */
function extractSchemas(html, filename) {
  const schemas = [];
  const regex = /<script type="application\/ld\+json">([\s\S]*?)<\/script>/g;
  let match;
  let lineNumber = 1;

  // Track line numbers
  const lines = html.split('\n');

  while ((match = regex.exec(html)) !== null) {
    // Find line number of this schema block
    const beforeMatch = html.substring(0, match.index);
    lineNumber = beforeMatch.split('\n').length;

    try {
      const schemaText = match[1].trim();
      const schema = JSON.parse(schemaText);
      schemas.push({ schema, lineNumber, filename });
    } catch (error) {
      console.error(`${colors.red}✗${colors.reset} ${filename}:${lineNumber} - Invalid JSON: ${error.message}`);
      totalErrors++;
    }
  }

  return schemas;
}

/**
 * Validate LegalService schema
 */
function validateLegalService(schema, filename, lineNumber) {
  const errors = [];
  const warnings = [];

  // Required fields for Google Rich Results
  const requiredFields = {
    'address': 'Missing required field "address" (Google Rich Results requirement)',
    'telephone': 'Missing required field "telephone" (Google Rich Results requirement)',
    'image': 'Missing required field "image" (Google Rich Results requirement)'
  };

  for (const [field, errorMsg] of Object.entries(requiredFields)) {
    if (!schema[field]) {
      errors.push(errorMsg);
    }
  }

  // Check for duplicate priceRange property
  const jsonText = JSON.stringify(schema, null, 2);
  const priceRangeCount = (jsonText.match(/"priceRange":/g) || []).length;
  if (priceRangeCount > 1) {
    errors.push(`Duplicate property "priceRange" (found ${priceRangeCount} times)`);
  }

  // Check for aggregateRating with reviewCount: 0
  if (schema.aggregateRating && schema.aggregateRating.reviewCount === 0) {
    errors.push('aggregateRating has reviewCount: 0 (must be positive integer or remove aggregateRating)');
  }

  // Check address structure if present
  if (schema.address && schema.address['@type'] !== 'PostalAddress') {
    warnings.push('address should have @type: "PostalAddress"');
  }

  // Check provider reference format
  if (schema.provider && schema.provider['@type'] && schema.provider['@id']) {
    warnings.push('provider should only have @id, not @type (removes "Unnamed item" error)');
  }

  // Check areaServed has correct structure
  if (schema.areaServed) {
    const areas = Array.isArray(schema.areaServed) ? schema.areaServed : [schema.areaServed];
    areas.forEach((area, index) => {
      if (area.name && !area['@type']) {
        warnings.push(`areaServed[${index}] missing @type (should be "City" or "AdministrativeArea")`);
      }
    });
  }

  return { errors, warnings };
}

/**
 * Validate FAQPage schema
 */
function validateFAQPage(schema, filename, lineNumber) {
  const errors = [];
  const warnings = [];

  if (!schema.mainEntity || !Array.isArray(schema.mainEntity)) {
    errors.push('FAQPage must have "mainEntity" array');
    return { errors, warnings };
  }

  if (schema.mainEntity.length < 5) {
    warnings.push(`FAQPage has only ${schema.mainEntity.length} questions (Google recommends 5-10+)`);
  }

  schema.mainEntity.forEach((question, index) => {
    if (!question.name) {
      errors.push(`Question ${index + 1} missing "name" field`);
    }
    if (!question.acceptedAnswer) {
      errors.push(`Question ${index + 1} missing "acceptedAnswer"`);
    } else if (!question.acceptedAnswer.text) {
      errors.push(`Question ${index + 1} acceptedAnswer missing "text"`);
    }
  });

  return { errors, warnings };
}

/**
 * Validate BreadcrumbList schema
 */
function validateBreadcrumbList(schema, filename, lineNumber) {
  const errors = [];
  const warnings = [];

  if (!schema.itemListElement || !Array.isArray(schema.itemListElement)) {
    errors.push('BreadcrumbList must have "itemListElement" array');
    return { errors, warnings };
  }

  schema.itemListElement.forEach((item, index) => {
    if (item.position !== index + 1) {
      errors.push(`Breadcrumb item ${index + 1} has position ${item.position} (should be ${index + 1})`);
    }
    if (!item.name) {
      errors.push(`Breadcrumb item ${index + 1} missing "name"`);
    }
    if (!item.item) {
      errors.push(`Breadcrumb item ${index + 1} missing "item" (URL)`);
    }
  });

  return { errors, warnings };
}

/**
 * Validate Person schema
 */
function validatePerson(schema, filename, lineNumber) {
  const errors = [];
  const warnings = [];

  if (!schema.name) {
    errors.push('Person schema missing "name" field');
  }

  if (!schema.jobTitle) {
    warnings.push('Person schema missing "jobTitle" (recommended)');
  }

  return { errors, warnings };
}

/**
 * Validate WebSite schema
 */
function validateWebSite(schema, filename, lineNumber) {
  const errors = [];
  const warnings = [];

  // Check for SearchAction if no search functionality exists
  if (schema.potentialAction && schema.potentialAction['@type'] === 'SearchAction') {
    warnings.push('SearchAction present but site has no search functionality (Google will crawl invalid URLs)');
  }

  return { errors, warnings };
}

/**
 * Validate a single schema
 */
function validateSchema(schemaData) {
  const { schema, lineNumber, filename } = schemaData;
  const schemaType = schema['@type'];

  let result = { errors: [], warnings: [] };

  switch (schemaType) {
    case 'LegalService':
      result = validateLegalService(schema, filename, lineNumber);
      break;
    case 'FAQPage':
      result = validateFAQPage(schema, filename, lineNumber);
      break;
    case 'BreadcrumbList':
      result = validateBreadcrumbList(schema, filename, lineNumber);
      break;
    case 'Person':
      result = validatePerson(schema, filename, lineNumber);
      break;
    case 'WebSite':
      result = validateWebSite(schema, filename, lineNumber);
      break;
    case 'BlogPosting':
      // Basic validation - BlogPosting is usually fine
      break;
    default:
      result.warnings.push(`Unknown schema type: ${schemaType}`);
  }

  return result;
}

/**
 * Process a single HTML file
 */
function processFile(filepath) {
  totalFiles++;

  const filename = path.relative(DIST_DIR, filepath);
  const html = fs.readFileSync(filepath, 'utf8');

  const schemas = extractSchemas(html, filename);

  if (schemas.length === 0) {
    console.log(`${colors.gray}○${colors.reset} ${filename} - No schema found`);
    return;
  }

  filesWithSchema++;
  totalSchemas += schemas.length;

  let fileHasErrors = false;
  let fileHasWarnings = false;

  schemas.forEach(schemaData => {
    const schemaType = schemaData.schema['@type'];
    const result = validateSchema(schemaData);

    if (result.errors.length > 0) {
      fileHasErrors = true;
      totalErrors += result.errors.length;
      console.log(`${colors.red}✗${colors.reset} ${filename}:${schemaData.lineNumber} - ${schemaType} schema`);
      result.errors.forEach(error => {
        console.log(`  ${colors.red}ERROR:${colors.reset} ${error}`);
      });
    }

    if (result.warnings.length > 0) {
      fileHasWarnings = true;
      totalWarnings += result.warnings.length;
      if (!fileHasErrors) {
        console.log(`${colors.yellow}⚠${colors.reset} ${filename}:${schemaData.lineNumber} - ${schemaType} schema`);
      }
      result.warnings.forEach(warning => {
        console.log(`  ${colors.yellow}WARNING:${colors.reset} ${warning}`);
      });
    }

    if (!fileHasErrors && !fileHasWarnings) {
      console.log(`${colors.green}✓${colors.reset} ${filename}:${schemaData.lineNumber} - ${schemaType} schema`);
    }
  });
}

/**
 * Recursively find all HTML files in a directory
 */
function findHtmlFiles(dir) {
  const files = [];

  if (!fs.existsSync(dir)) {
    return files;
  }

  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      files.push(...findHtmlFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }

  return files;
}

/**
 * Main function
 */
function main() {
  console.log(`${colors.blue}🔍 Schema Markup Validation${colors.reset}\n`);
  console.log(`Scanning: ${DIST_DIR}\n`);

  // Check if dist directory exists
  if (!fs.existsSync(DIST_DIR)) {
    console.error(`${colors.red}✗ dist/ directory not found. Run "npm run build:html:prod" first.${colors.reset}`);
    process.exit(1);
  }

  // Find all HTML files
  const htmlFiles = findHtmlFiles(DIST_DIR);

  if (htmlFiles.length === 0) {
    console.error(`${colors.red}✗ No HTML files found in dist/ directory.${colors.reset}`);
    process.exit(1);
  }

  // Process each file
  htmlFiles.forEach(processFile);

  // Summary
  console.log('\n' + '─'.repeat(60));
  console.log(`${colors.blue}📊 Summary${colors.reset}`);
  console.log('─'.repeat(60));
  console.log(`Files scanned:        ${totalFiles}`);
  console.log(`Files with schema:    ${filesWithSchema}`);
  console.log(`Total schemas found:  ${totalSchemas}`);

  if (totalErrors > 0) {
    console.log(`${colors.red}Errors:               ${totalErrors}${colors.reset}`);
  } else {
    console.log(`${colors.green}Errors:               0${colors.reset}`);
  }

  if (totalWarnings > 0) {
    console.log(`${colors.yellow}Warnings:             ${totalWarnings}${colors.reset}`);
  } else {
    console.log(`Warnings:             0`);
  }

  console.log('─'.repeat(60));

  if (totalErrors > 0) {
    console.log(`\n${colors.red}✗ Validation failed with ${totalErrors} error(s)${colors.reset}`);
    console.log(`\n${colors.gray}See utilities/docs/SCHEMA_GUIDE.md for schema templates and fixes.${colors.reset}`);
    process.exit(1);
  } else if (totalWarnings > 0) {
    console.log(`\n${colors.yellow}⚠ Validation passed with ${totalWarnings} warning(s)${colors.reset}`);
    console.log(`\n${colors.gray}Warnings are non-critical but should be reviewed.${colors.reset}`);
    process.exit(0);
  } else {
    console.log(`\n${colors.green}✓ All schema markup is valid!${colors.reset}`);
    process.exit(0);
  }
}

// Run validation
main();
