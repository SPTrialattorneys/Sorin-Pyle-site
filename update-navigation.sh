#!/bin/bash
# Script to update navigation dropdown across all HTML files

# Array of root HTML files (excluding index.html which is already done)
root_files=(
    "attorneys.html"
    "contact.html"
    "practice-areas.html"
    "locations.html"
    "privacy-policy.html"
    "drivers-license-restoration.html"
    "record-expungement.html"
    "sorin-panainte.html"
    "jonathan-pyle.html"
    "resources.html"
    "dui-defense.html"
    "domestic-violence-defense.html"
    "404.html"
    "500.html"
    "card.html"
)

# Array of location HTML files (with proper relative paths)
location_files=(
    "locations/ottawa-county.html"
    "locations/kent-county.html"
    "locations/allegan-county.html"
    "locations/kalamazoo-county.html"
    "locations/muskegon-county.html"
    "locations/van-buren-county.html"
    "locations/newaygo-county.html"
    "locations/other-michigan-counties.html"
    "locations/allendale-mi.html"
    "locations/calvin-university-student-defense.html"
    "locations/davenport-student-defense.html"
    "locations/ferris-student-defense.html"
    "locations/grand-haven-mi.html"
    "locations/grand-rapids-mi.html"
    "locations/grandville-mi.html"
    "locations/grcc-student-defense.html"
    "locations/gvsu-student-defense.html"
    "locations/holland-mi.html"
    "locations/hope-college-student-defense.html"
    "locations/hudsonville-mi.html"
    "locations/jenison-mi.html"
    "locations/kentwood-mi.html"
    "locations/saugatuck-mi.html"
    "locations/south-haven-mi.html"
    "locations/walker-mi.html"
    "locations/wmu-student-defense.html"
    "locations/wyoming-mi.html"
    "locations/zeeland-mi.html"
)

# Update desktop navigation for root files
for file in "${root_files[@]}"; do
    if [ -f "$file" ]; then
        echo "Updating desktop navigation in $file..."
        sed -i 's|<li role="none"><a href="resources\.html#faq" role="menuitem">Frequently Asked Questions</a></li>|<li role="none"><a href="faq.html" role="menuitem">Frequently Asked Questions</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="local-resources\.html" role="menuitem">Community Support Resources</a></li>|<li role="none"><a href="your-rights.html" role="menuitem">Know Your Rights</a></li>\n                            <li role="none"><a href="community-resources.html" role="menuitem">Community Resources</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="resources\.html#blog" role="menuitem">Firm News \& Updates</a></li>|<li role="none"><a href="blog.html" role="menuitem">Firm News \& Updates</a></li>|g' "$file"
    fi
done

# Update mobile navigation for root files
for file in "${root_files[@]}"; do
    if [ -f "$file" ]; then
        echo "Updating mobile navigation in $file..."
        sed -i 's|<li role="none"><a href="resources\.html#faq" role="menuitem">Frequently Asked Questions</a></li>|<li role="none"><a href="faq.html" role="menuitem">Frequently Asked Questions</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="local-resources\.html" role="menuitem">Community Support Resources</a></li>|<li role="none"><a href="your-rights.html" role="menuitem">Know Your Rights</a></li>\n                    <li role="none"><a href="community-resources.html" role="menuitem">Community Resources</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="resources\.html#blog" role="menuitem">Firm News \& Updates</a></li>|<li role="none"><a href="blog.html" role="menuitem">Firm News \& Updates</a></li>|g' "$file"
    fi
done

# Update footer links for root files
for file in "${root_files[@]}"; do
    if [ -f "$file" ]; then
        echo "Updating footer in $file..."
        sed -i 's|<li><a href="resources\.html">|<li><a href="faq.html">|g' "$file"
        sed -i 's|<li><a href="resources\.html">Firm Updates \& Resources</a></li>|<li><a href="faq.html">Client Resources</a></li>|g' "$file"
    fi
done

# Update location files with relative paths
for file in "${location_files[@]}"; do
    if [ -f "$file" ]; then
        echo "Updating $file with relative paths..."
        # Desktop navigation
        sed -i 's|<li role="none"><a href="\.\./resources\.html#faq" role="menuitem">Frequently Asked Questions</a></li>|<li role="none"><a href="../faq.html" role="menuitem">Frequently Asked Questions</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="\.\./local-resources\.html" role="menuitem">Community Support Resources</a></li>|<li role="none"><a href="../your-rights.html" role="menuitem">Know Your Rights</a></li>\n                            <li role="none"><a href="../community-resources.html" role="menuitem">Community Resources</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="\.\./resources\.html#blog" role="menuitem">Firm News \& Updates</a></li>|<li role="none"><a href="../blog.html" role="menuitem">Firm News \& Updates</a></li>|g' "$file"

        # Mobile navigation
        sed -i 's|<li role="none"><a href="\.\./resources\.html#faq" role="menuitem">Frequently Asked Questions</a></li>|<li role="none"><a href="../faq.html" role="menuitem">Frequently Asked Questions</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="\.\./local-resources\.html" role="menuitem">Community Support Resources</a></li>|<li role="none"><a href="../your-rights.html" role="menuitem">Know Your Rights</a></li>\n                    <li role="none"><a href="../community-resources.html" role="menuitem">Community Resources</a></li>|g' "$file"
        sed -i 's|<li role="none"><a href="\.\./resources\.html#blog" role="menuitem">Firm News \& Updates</a></li>|<li role="none"><a href="../blog.html" role="menuitem">Firm News \& Updates</a></li>|g' "$file"

        # Footer
        sed -i 's|<li><a href="\.\./resources\.html">|<li><a href="../faq.html">|g' "$file"
        sed -i 's|<li><a href="\.\./resources\.html">Firm Updates \& Resources</a></li>|<li><a href="../faq.html">Client Resources</a></li>|g' "$file"
    fi
done

echo "Navigation update complete!"
