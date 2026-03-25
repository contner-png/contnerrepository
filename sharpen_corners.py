import os
import re

def sharpen_corners(content):
    # CSS border-radius replacements
    content = re.sub(r'border-radius:\s*[^;!]+', 'border-radius: 0', content)
    
    # Tailwind rounded class replacements
    rounded_patterns = [
        r'rounded-xl',
        r'rounded-2xl',
        r'rounded-lg',
        r'rounded-md',
        r'rounded-sm',
        r'rounded-\[[^\]]+\]',
        r'rounded-full' 
    ]
    
    for pattern in rounded_patterns:
        content = re.sub(pattern, 'rounded-none', content)
        
    return content

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = sharpen_corners(content)
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Sharpened corners in {filepath}")
