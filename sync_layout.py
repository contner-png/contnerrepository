import os
import re

with open("/workspace/project/contnerrepository/index.html", 'r') as f:
    index_content = f.read()

header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in index.html")
    exit(1)

header_content = header_match.group(1)
footer_content = footer_match.group(1)

def sync_file(filepath):
    if "index.html" in filepath:
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Sync Header
    content = re.sub(r'<header.*?</header>', header_content, content, flags=re.DOTALL)
    
    # Sync Footer
    content = re.sub(r'<footer.*?</footer>', footer_content, content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

for root, dirs, files in os.walk("/workspace/project/contnerrepository"):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            sync_file(filepath)
            print(f"Synced {filepath}")
