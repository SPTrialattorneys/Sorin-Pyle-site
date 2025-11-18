#!/usr/bin/env python3
"""
Validate schema markup on new Client Resources pages
Checks for proper JSON-LD structured data
"""

import json
import re

pages_to_test = {
    "faq.html": ("FAQPage", "jsonld"),
    "your-rights.html": ("Article", "jsonld"),
    "blog.html": ("BlogPosting", "microdata"),  # Uses inline microdata
    "community-resources.html": (None, None)  # No schema required for this page
}

def extract_schema(filepath):
    """Extract JSON-LD schema from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all JSON-LD script tags
        schemas = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>',
            content,
            re.DOTALL
        )

        return [json.loads(schema.strip()) for schema in schemas]
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        return f"JSON Parse Error: {e}"
    except Exception as e:
        return f"Error: {e}"

def validate_faq_schema(schema):
    """Validate FAQPage schema"""
    errors = []

    if schema.get('@type') != 'FAQPage':
        errors.append(f"Expected @type 'FAQPage', got '{schema.get('@type')}'")

    main_entity = schema.get('mainEntity', [])
    if not main_entity:
        errors.append("No 'mainEntity' found (FAQ questions)")
    elif not isinstance(main_entity, list):
        errors.append("'mainEntity' should be a list")
    else:
        for i, question in enumerate(main_entity):
            if question.get('@type') != 'Question':
                errors.append(f"Question {i+1}: Expected @type 'Question'")
            if not question.get('name'):
                errors.append(f"Question {i+1}: Missing 'name' field")
            answer = question.get('acceptedAnswer', {})
            if answer.get('@type') != 'Answer':
                errors.append(f"Question {i+1}: Answer should have @type 'Answer'")
            if not answer.get('text'):
                errors.append(f"Question {i+1}: Answer missing 'text' field")

    return errors

def validate_article_schema(schema):
    """Validate Article schema"""
    errors = []

    if schema.get('@type') != 'Article':
        errors.append(f"Expected @type 'Article', got '{schema.get('@type')}'")

    required_fields = ['headline', 'author', 'datePublished']
    for field in required_fields:
        if not schema.get(field):
            errors.append(f"Missing required field: '{field}'")

    return errors

def validate_blog_posting_schema(schema):
    """Validate BlogPosting schema"""
    errors = []

    if schema.get('@type') != 'BlogPosting':
        errors.append(f"Expected @type 'BlogPosting', got '{schema.get('@type')}'")

    required_fields = ['headline', 'author', 'datePublished']
    for field in required_fields:
        if not schema.get(field):
            errors.append(f"Missing required field: '{field}'")

    return errors

def has_microdata_schema(filepath, schema_type):
    """Check if file has microdata schema (itemscope/itemtype)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for microdata schema
        pattern = rf'itemscope\s+itemtype=["\']https://schema\.org/{schema_type}["\']'
        match = re.search(pattern, content)

        if match:
            # Also check for basic required properties
            has_headline = 'itemprop="headline"' in content
            has_author = 'itemprop="author"' in content
            has_date = 'itemprop="datePublished"' in content

            missing = []
            if not has_headline:
                missing.append("headline")
            if not has_author:
                missing.append("author")
            if not has_date:
                missing.append("datePublished")

            return (True, missing)

        return (False, [])
    except Exception as e:
        return (False, [str(e)])

def test_page_schema(filepath, config):
    """Test schema markup for a single page"""
    if config == (None, None):
        return []  # No schema expected

    expected_type, format_type = config

    if format_type == "microdata":
        # Check for microdata schema
        has_schema, missing = has_microdata_schema(filepath, expected_type)

        if not has_schema:
            return [f"No microdata schema found (expected {expected_type})"]
        elif missing:
            return [f"Microdata schema missing required properties: {', '.join(missing)}"]
        else:
            return []  # Valid microdata schema

    # JSON-LD schema validation
    schemas = extract_schema(filepath)

    if schemas is None:
        return [f"File not found: {filepath}"]
    elif isinstance(schemas, str):
        return [schemas]
    elif not schemas and expected_type is not None:
        return [f"No schema markup found (expected {expected_type})"]
    elif not schemas and expected_type is None:
        return []  # No schema expected, no schema found - OK

    # Find the correct schema type
    target_schema = None
    for schema in schemas:
        if schema.get('@type') == expected_type:
            target_schema = schema
            break

    if not target_schema and expected_type:
        return [f"Schema type '{expected_type}' not found in page"]

    # Validate based on type
    if expected_type == 'FAQPage':
        return validate_faq_schema(target_schema)
    elif expected_type == 'Article':
        return validate_article_schema(target_schema)
    elif expected_type == 'BlogPosting':
        return validate_blog_posting_schema(target_schema)

    return []

def run_schema_tests():
    """Run all schema validation tests"""
    print("=" * 70)
    print("SCHEMA MARKUP VALIDATION TEST SUITE")
    print("=" * 70)
    print()

    total_pages = 0
    passed_pages = 0
    failed_pages = 0

    for filepath, config in pages_to_test.items():
        total_pages += 1
        errors = test_page_schema(filepath, config)

        if errors:
            failed_pages += 1
            print(f"[FAIL] {filepath}")
            for error in errors:
                print(f"       - {error}")
            print()
        else:
            passed_pages += 1
            if config == (None, None):
                print(f"[PASS] {filepath} - No schema required")
            else:
                expected_type, format_type = config
                print(f"[PASS] {filepath} - Valid {expected_type} schema ({format_type})")

    print()
    print("=" * 70)
    print("SCHEMA VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Total pages tested: {total_pages}")
    print(f"Passed: {passed_pages}")
    print(f"Failed: {failed_pages}")

    if failed_pages == 0:
        print()
        print("[SUCCESS] All schema validations passed!")
        return True
    else:
        print()
        print("[FAILURE] Some validations failed. See details above.")
        return False

if __name__ == "__main__":
    success = run_schema_tests()
    exit(0 if success else 1)
