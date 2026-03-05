import os
import re

mapping = {
    "vagus-nerve-stimulation.html": "tvns.png",
    "sleep-testing.html": "sleepstudy.jpg",
    "targeted-supplements.html": "supplement.png",
    "longevity-blood-panels.html": "longevitypanel.png",
    "vo2-max-testing.html": "vo2max.png",
    "red-light-therapy.html": "redlight.png"
}

base_dir = "/workspace/project/contnerrepository/treatments"

for filename, img_name in mapping.items():
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, file does not exist.")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Look for the <img> tag inside the Technology Hero section
    # Usually it's in a <div class="lg:w-1/2 relative">
    new_img_src = f"/images/treatments/{img_name}"
    
    # Simple regex to replace whatever is in the src attribute of the first <img> tag in the hero section
    # We look for the part where it says Advanced Modality
    pattern = re.compile(r'(Advanced Modality.*?<img src=")(.*?)(")', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(rf'\1{new_img_src}\3', content)
        print(f"Updated {filename} with {new_img_src}")
    else:
        # Fallback to general <img> tag if the specific pattern fails
        print(f"Pattern failed for {filename}, trying generic search...")
        # Replace the first instance of src="..." after "Technology Hero"
        hero_start = content.find("Technology Hero")
        if hero_start != -1:
            img_start = content.find("<img", hero_start)
            src_start = content.find('src="', img_start) + 5
            src_end = content.find('"', src_start)
            content = content[:src_start] + new_img_src + content[src_end:]
            print(f"Updated {filename} with {new_img_src} via fallback")
        else:
            print(f"Could not find hero section in {filename}")

    with open(filepath, 'w') as f:
        f.write(content)
