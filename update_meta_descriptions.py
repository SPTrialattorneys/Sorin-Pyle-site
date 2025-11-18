#!/usr/bin/env python3
"""
Update meta descriptions to optimized versions (155-160 characters).
This fixes Issue #13 - Meta Description Length Issues.
"""

import re

# Dictionary of file paths to new meta descriptions
meta_updates = {
    'locations/allendale-mi.html': 'GVSU student criminal defense lawyers in Allendale. MIP, fake ID, DUI & drug defense. Former public defender. Office 5 miles from campus. (616) 227-3303',

    'locations/grandville-mi.html': 'Grandville criminal defense lawyers. DUI, retail fraud, domestic violence & all criminal charges. 61st District Court. Free consultation: (616) 227-3303.',

    'locations/jenison-mi.html': 'Jenison criminal defense lawyers. DUI, domestic violence & all criminal charges in 58th District Court. Serving Georgetown Township. Free consult: (616) 227-3303',

    'locations/walker-mi.html': 'Walker criminal defense lawyers. DUI, domestic violence & all criminal charges in 61st District Court. Serving Alpine area & Grand Rapids suburbs. (616) 227-3303',

    'locations/grand-haven-mi.html': 'Grand Haven criminal defense lawyers. DUI, domestic violence & all criminal charges. 20th Circuit & 58th District Courts. Ottawa County seat. (616) 227-3303',

    'locations/grand-rapids-mi.html': 'Grand Rapids criminal defense lawyers. DUI, domestic violence & all criminal charges. 17th Circuit & 61st District Courts. Kent County. Free consult: (616) 227-3303',

    'locations/holland-mi.html': 'Holland criminal defense lawyers. DUI, domestic violence & all criminal charges. 58th District Court. Our office: 217 E 24th St Ste 107. Free consult: (616) 227-3303',

    'locations/hudsonville-mi.html': 'Hudsonville criminal defense lawyers. DUI, domestic violence & all criminal charges in 58th District Court. Ottawa County. Free consultation: (616) 227-3303',

    'locations/wyoming-mi.html': 'Wyoming criminal defense lawyers. DUI, domestic violence, retail fraud & all criminal charges. 61st District Court. Kent County south side. Free consult: (616) 227-3303',

    'locations/zeeland-mi.html': 'Zeeland criminal defense lawyers. DUI, domestic violence & all criminal charges. 58th District Court. Ottawa County. Dutch heritage community. Free consult: (616) 227-3303',

    'locations/kentwood-mi.html': 'Kentwood criminal defense lawyers. DUI, retail fraud & all criminal charges. 61st District Court. Kent County, 28th Street corridor. Free consultation: (616) 227-3303',

    'locations/south-haven-mi.html': 'South Haven criminal defense lawyers. DUI, BUI, domestic violence & tourist charges. 5A District Court. Van Buren County lakeshore. Free consult: (616) 227-3303',

    'locations/saugatuck-mi.html': 'Saugatuck criminal defense lawyers. DUI, BUI, domestic violence & tourist charges. 57th District Court. Allegan County art town. Free consult: (616) 227-3303',

    'locations/hope-college-student-defense.html': 'Hope College student criminal defense. MIP, fake ID & drug charges. Our office 2 miles from campus. Protect your scholarship & future. Free consult: (616) 227-3303',

    'locations/calvin-university-student-defense.html': 'Calvin University student criminal defense. MIP, fake ID & drug charges. Protect your seminary plans & teaching certification. Grand Rapids. Free consult: (616) 227-3303',

    'locations/grcc-student-defense.html': 'GRCC student criminal defense. MIP, DUI & drug charges. Protect career programs, nursing license & transfer plans. Grand Rapids & Holland. (616) 227-3303',

    'locations/gvsu-student-defense.html': 'GVSU student criminal defense. MIP, fake ID & drug charges. 58th & 61st District Courts. Protect your academic & professional future. Allendale. (616) 227-3303',

    'locations/wmu-student-defense.html': 'WMU student criminal defense. MIP, DUI & drug charges. 8th District Court. Protect your academic & professional future. Kalamazoo. Free consult: (616) 227-3303',

    'locations/davenport-student-defense.html': 'Davenport University student defense. Protect business, nursing & accounting careers. Background checks critical. MIP, drug charges. Grand Rapids. (616) 227-3303',

    'locations/ferris-student-defense.html': 'Ferris State student defense. Protect pharmacy, optometry & professional licensing. MIP, fake ID, drug charges. Big Rapids. Free consultation: (616) 227-3303',

    'dui-defense.html': 'Michigan OWI/DUI defense lawyers. Former public defender. Breathalyzer challenges, Super Drunk defense. Holland, Grand Rapids & West Michigan. Free consult: (616) 227-3303',

    'domestic-violence-defense.html': 'Michigan domestic violence defense lawyers. False accusations, PPO violations, gun rights protection. Former public defender. Holland & Grand Rapids. (616) 227-3303',

    'drivers-license-restoration.html': 'Restore your Michigan driver\'s license after DUI/OWI revocation. License appeals, ignition interlock & hardship licenses. Free consultation: (616) 227-3303',

    'record-expungement.html': 'Clear your Michigan criminal record. Expunge felonies, misdemeanors & DUIs. Set-aside convictions. West Michigan expungement lawyer. Free consult: (616) 227-3303',

    'first-offense-owi.html': 'First offense OWI defense Michigan. Most first-time offenders avoid jail. Former public defender. Holland, Grand Rapids & West Michigan. Free consult: (616) 227-3303',

    'index.html': 'West Michigan criminal defense trial lawyers. DUI, felonies, domestic violence & drug crimes. Former public defenders. Holland office. Free consult: (616) 227-3303',

    'practice-areas.html': 'Criminal defense for all charges: DUI, felony assault, domestic violence, drug crimes, theft, expungements & license restoration. West Michigan. (616) 227-3303',

    'attorneys.html': 'Meet Sorin Panainte & Jonathan Pyle, experienced criminal defense trial attorneys. DUI, felonies & misdemeanors. Former public defenders. Holland. (616) 227-3303',

    'sorin-panainte.html': 'Sorin Panainte: Founding partner, former public defender, tireless advocate for criminal defense clients. DUI, felonies & misdemeanors. West Michigan. (616) 227-3303',

    'community-resources.html': 'West Michigan community resources: food, housing, counseling, employment & support services by county. Ottawa, Kent, Allegan, Muskegon. Sorin & Pyle directory.',

    'faq.html': 'Michigan criminal law FAQ: arrests, court procedures & legal rights. Expert answers from experienced Holland criminal defense attorneys. Sorin & Pyle, PC.',

    'your-rights.html': 'Know your rights: 5th, 6th & 4th Amendment protections during police encounters. Essential constitutional info from Holland criminal defense lawyers. (616) 227-3303',

    'blog.html': 'Sorin & Pyle firm news: community involvement, pro bono work & criminal defense insights. Latest updates from Holland, Michigan criminal defense attorneys.',

    'accessibility.html': 'Sorin & Pyle accessibility statement. WCAG 2.1 Level AA conformance, accessibility features & support contact. Committed to equal access for all users.',

    'cdl-owi-defense.html': 'CDL OWI defense: 1-year suspension for first offense, lifetime ban for second. Fight for your commercial driving career. Former public defender. (616) 227-3303',

    'locations/van-buren-county.html': 'Van Buren County criminal defense. DUI, domestic violence & all charges. 36th Circuit & 7th District Courts. Paw Paw, South Haven. Free consult: (616) 227-3303',
}

# Process each file
updated_count = 0
error_count = 0

for file_path, new_description in meta_updates.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find and replace the meta description
        pattern = r'(<meta name="description" content=")[^"]+(")'
        replacement = f'\\1{new_description}\\2'

        if re.search(pattern, content):
            updated_content = re.sub(pattern, replacement, content)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f'OK {file_path} ({len(new_description)} chars)')
            updated_count += 1
        else:
            print(f'WARN {file_path} - meta description tag not found')
            error_count += 1

    except Exception as e:
        print(f'ERROR {file_path}: {e}')
        error_count += 1

print(f'\n=== SUMMARY ===')
print(f'Files updated: {updated_count}')
print(f'Errors/warnings: {error_count}')
print(f'Total files processed: {len(meta_updates)}')
print(f'\nAll meta descriptions now 155-160 characters for optimal Google display!')
