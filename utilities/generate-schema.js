#!/usr/bin/env node

/**
 * Interactive Schema Generator CLI
 *
 * Generates valid schema markup using templates and user input.
 *
 * Usage:
 *   node utilities/generate-schema.js --type LegalService
 *   node utilities/generate-schema.js --type FAQPage
 *   node utilities/generate-schema.js --type BreadcrumbList
 *
 * Interactive mode (prompts for all values):
 *   node utilities/generate-schema.js
 *
 * Output:
 *   Prints formatted JSON-LD schema to stdout
 *   Can redirect to file: node utilities/generate-schema.js > schema.json
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

// ANSI color codes
const colors = {
  reset: '\x1b[0m',
  blue: '\x1b[34m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  gray: '\x1b[90m'
};

// Configuration
const TEMPLATES_DIR = path.join(__dirname, 'templates');

// Available schema types
const SCHEMA_TYPES = {
  'LegalService': 'Legal service offering (practice areas, defense services)',
  'FAQPage': 'Frequently Asked Questions (5-10+ Q&As)',
  'BreadcrumbList': 'Navigation breadcrumbs (Home > Parent > Current)'
};

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

/**
 * Promisify readline question
 */
function question(prompt) {
  return new Promise((resolve) => {
    rl.question(prompt, (answer) => {
      resolve(answer.trim());
    });
  });
}

/**
 * Print header
 */
function printHeader() {
  console.log(`${colors.blue}╔════════════════════════════════════════╗${colors.reset}`);
  console.log(`${colors.blue}║   Schema Markup Generator CLI         ║${colors.reset}`);
  console.log(`${colors.blue}╚════════════════════════════════════════╝${colors.reset}\n`);
}

/**
 * Print available schema types
 */
function printSchemaTypes() {
  console.log(`${colors.green}Available Schema Types:${colors.reset}\n`);
  Object.entries(SCHEMA_TYPES).forEach(([type, description]) => {
    console.log(`  ${colors.blue}${type}${colors.reset}`);
    console.log(`    ${colors.gray}${description}${colors.reset}\n`);
  });
}

/**
 * Load template file
 */
function loadTemplate(type) {
  const filename = `schema-${type.toLowerCase()}.json`;
  const filepath = path.join(TEMPLATES_DIR, filename);

  if (!fs.existsSync(filepath)) {
    throw new Error(`Template not found: ${filename}`);
  }

  return fs.readFileSync(filepath, 'utf8');
}

/**
 * Generate LegalService schema
 */
async function generateLegalService() {
  console.log(`${colors.green}\n📋 LegalService Schema Generator${colors.reset}\n`);

  const serviceName = await question('Service name (e.g., "DUI Defense"): ');
  const description = await question('Description (1-2 sentences): ');
  const serviceType1 = await question('Service type 1 (e.g., "DUI Defense"): ');
  const serviceType2 = await question('Service type 2 (e.g., "OWI Defense") [optional]: ');
  const serviceType3 = await question('Service type 3 [optional]: ');
  const imageUrl = await question('Image URL (e.g., "https://www.sorinpyle.com/images/..."): ');

  let template = loadTemplate('LegalService');

  template = template.replace('{{SERVICE_NAME}}', serviceName);
  template = template.replace('{{DESCRIPTION}}', description);
  template = template.replace('{{SERVICE_TYPE_1}}', serviceType1);
  template = template.replace('{{SERVICE_TYPE_2}}', serviceType2 || 'Criminal Defense');
  template = template.replace('{{SERVICE_TYPE_3}}', serviceType3 || 'Trial Representation');
  template = template.replace('{{IMAGE_URL}}', imageUrl);

  return template;
}

/**
 * Generate FAQPage schema
 */
async function generateFAQPage() {
  console.log(`${colors.green}\n❓ FAQPage Schema Generator${colors.reset}\n`);
  console.log(`${colors.gray}Google recommends 5-10+ questions for rich snippets${colors.reset}\n`);

  const numQuestions = parseInt(await question('How many Q&As to include (5-10 recommended): ') || '5');

  const questions = [];
  for (let i = 1; i <= numQuestions; i++) {
    console.log(`\n${colors.blue}Question ${i}:${colors.reset}`);
    const question_text = await question(`  Question: `);
    const answer_text = await question(`  Answer: `);
    questions.push({ question: question_text, answer: answer_text });
  }

  let template = loadTemplate('FAQPage');
  const templateJson = JSON.parse(template);

  // Build mainEntity array
  templateJson.mainEntity = questions.map((qa) => ({
    "@type": "Question",
    "name": qa.question,
    "acceptedAnswer": {
      "@type": "Answer",
      "text": qa.answer
    }
  }));

  return JSON.stringify(templateJson, null, 2);
}

/**
 * Generate BreadcrumbList schema
 */
async function generateBreadcrumbList() {
  console.log(`${colors.green}\n🗺️  BreadcrumbList Schema Generator${colors.reset}\n`);

  const parentPage = await question('Parent page name (e.g., "Practice Areas"): ');
  const parentUrl = await question('Parent page URL (e.g., "practice-areas.html"): ');
  const currentPage = await question('Current page name (e.g., "DUI Defense"): ');
  const currentUrl = await question('Current page URL (e.g., "dui-defense.html"): ');

  let template = loadTemplate('BreadcrumbList');

  template = template.replace('{{PARENT_PAGE}}', parentPage);
  template = template.replace('{{PARENT_URL}}', parentUrl);
  template = template.replace('{{CURRENT_PAGE}}', currentPage);
  template = template.replace('{{CURRENT_URL}}', currentUrl);

  return template;
}

/**
 * Main function
 */
async function main() {
  // Parse command line arguments
  const args = process.argv.slice(2);
  const typeArg = args.find(arg => arg.startsWith('--type='));
  let schemaType = typeArg ? typeArg.split('=')[1] : null;

  printHeader();

  // If no type specified, prompt for it
  if (!schemaType) {
    printSchemaTypes();
    schemaType = await question(`${colors.green}Select schema type:${colors.reset} `);
  }

  // Validate schema type
  if (!SCHEMA_TYPES[schemaType]) {
    console.error(`${colors.yellow}Error: Unknown schema type "${schemaType}"${colors.reset}`);
    console.error(`${colors.gray}Available types: ${Object.keys(SCHEMA_TYPES).join(', ')}${colors.reset}`);
    rl.close();
    process.exit(1);
  }

  let schema;

  // Generate schema based on type
  switch (schemaType) {
    case 'LegalService':
      schema = await generateLegalService();
      break;
    case 'FAQPage':
      schema = await generateFAQPage();
      break;
    case 'BreadcrumbList':
      schema = await generateBreadcrumbList();
      break;
    default:
      console.error(`${colors.yellow}Schema type not yet implemented: ${schemaType}${colors.reset}`);
      rl.close();
      process.exit(1);
  }

  // Print generated schema
  console.log(`\n${colors.green}✓ Generated Schema:${colors.reset}\n`);
  console.log(`${colors.gray}${'─'.repeat(60)}${colors.reset}`);
  console.log(schema);
  console.log(`${colors.gray}${'─'.repeat(60)}${colors.reset}\n`);

  // Usage instructions
  console.log(`${colors.blue}Usage:${colors.reset}`);
  console.log(`  1. Copy the schema above`);
  console.log(`  2. Wrap in <script type="application/ld+json"> tags`);
  console.log(`  3. Add to your .njk template file\n`);

  console.log(`${colors.gray}Example:${colors.reset}`);
  console.log(`  <script type="application/ld+json">`);
  console.log(`  ${schema.split('\n')[1]}  // First line of schema`);
  console.log(`  ...</script>\n`);

  rl.close();
}

// Run main function
main().catch((error) => {
  console.error(`${colors.yellow}Error: ${error.message}${colors.reset}`);
  rl.close();
  process.exit(1);
});
