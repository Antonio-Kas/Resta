#!/usr/bin/env python3

def fix_template(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    content = content.replace('{% blocktranslate', '{% blocktrans')
    content = content.replace('{% endblocktranslate', '{% endblocktrans')
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Fixed template: {filename}")

# Fix both templates
fix_template('restasite/templates/admin/custom_index.html')
fix_template('restasite/templates/admin/base_site.html') 