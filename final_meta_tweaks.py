import re

# Final tweaks for the 7 pages that are 6+ chars over limit
tweaks = {
    'dui-defense.html': 'Michigan OWI/DUI defense. Former public defender. Breathalyzer challenges, Super Drunk defense. Holland, Grand Rapids & West Michigan. (616) 227-3303',
    
    'locations/zeeland-mi.html': 'Zeeland criminal defense lawyers. DUI, domestic violence & all charges. 58th District Court. Ottawa County, Dutch community. Free consult: (616) 227-3303',
    
    'locations/calvin-university-student-defense.html': 'Calvin University student defense. MIP, fake ID & drug charges. Protect seminary plans & teaching certification. Grand Rapids. Free consult: (616) 227-3303',
    
    'locations/wyoming-mi.html': 'Wyoming criminal defense. DUI, domestic violence, retail fraud & all charges. 61st District Court. Kent County south side. Free consult: (616) 227-3303',
    
    'locations/kentwood-mi.html': 'Kentwood criminal defense. DUI, retail fraud & all charges. 61st District Court. Kent County, 28th Street corridor. Free consult: (616) 227-3303',
    
    'first-offense-owi.html': 'First offense OWI defense Michigan. Most avoid jail. Former public defender. Holland, Grand Rapids & West Michigan. Free consultation: (616) 227-3303',
    
    'sorin-panainte.html': 'Sorin Panainte: Founding partner, former public defender, tireless advocate for criminal defense clients. DUI, felonies & misdemeanors. (616) 227-3303',
}

updated = 0
for file_path, new_desc in tweaks.items():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'(<meta name="description" content=")[^"]+(")'
    content = re.sub(pattern, f'\1{new_desc}\2', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'OK {file_path} ({len(new_desc)} chars)')
    updated += 1

print(f'\nFinal tweaks complete: {updated} files updated')
