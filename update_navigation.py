import os
import re

new_treatments_links = """
                        <a href="/treatments/class-iv-laser.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Class IV Laser</a>
                        <a href="/treatments/shockwave-therapy.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Shockwave Therapy</a>
                        <a href="/treatments/pemf-therapy.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">PEMF Therapy</a>
                        <a href="/treatments/hyperbaric-oxygen.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Hyperbaric Oxygen</a>
                        <a href="/treatments/spinal-decompression.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Spinal Decompression</a>
                        <a href="/treatments/dry-needling.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Dry Needling</a>
                        <a href="/treatments/vagus-nerve-stimulation.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">tVNS (Vagus Nerve)</a>
                        <a href="/treatments/sleep-testing.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Sleep Testing</a>
                        <a href="/treatments/targeted-supplements.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Targeted Supplements</a>
                        <a href="/treatments/longevity-blood-panels.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">Longevity Blood Panels</a>
                        <a href="/treatments/vo2-max-testing.html" class="block px-4 py-2 hover:bg-clinical-gray hover:text-clinical-blue transition-colors text-sm text-clinical-charcoal">VO2 Max Testing</a>
"""

new_mobile_treatments = """
                    <div class="space-y-2">
                        <span class="text-[10px] uppercase tracking-widest text-gray-400 block mb-2">Treatments</span>
                        <div class="grid grid-cols-2 gap-2">
                            <a href="/treatments/class-iv-laser.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Class IV Laser</a>
                            <a href="/treatments/shockwave-therapy.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Shockwave</a>
                            <a href="/treatments/pemf-therapy.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">PEMF Therapy</a>
                            <a href="/treatments/hyperbaric-oxygen.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">HBOT</a>
                            <a href="/treatments/spinal-decompression.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Decompression</a>
                            <a href="/treatments/dry-needling.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Dry Needling</a>
                            <a href="/treatments/vagus-nerve-stimulation.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">tVNS</a>
                            <a href="/treatments/sleep-testing.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Sleep Testing</a>
                            <a href="/treatments/targeted-supplements.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Supplements</a>
                            <a href="/treatments/longevity-blood-panels.html" class="block text-sm hover:text-clinical-blue text-clinical-charcoal">Blood Panels</a>
                        </div>
                    </div>
"""

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Update Treatments dropdown
    dropdown_pattern = re.compile(r'<span>Treatments</span>\s*<svg.*?>\s*</button>\s*<div class="absolute left-0 mt-0 w-64 bg-white border border-gray-100 shadow-xl rounded-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50">.*?</div>', re.DOTALL)
    
    dropdown_replacement = f"""<span>Treatments</span>
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="absolute left-0 mt-0 w-64 bg-white border border-gray-100 shadow-xl rounded-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 py-4 z-50">
                        {new_treatments_links}
                    </div>"""
    
    content = dropdown_pattern.sub(dropdown_replacement, content)

    # Update Mobile Menu
    mobile_pattern = re.compile(r'(<div class="space-y-2">\s*<span class="text-\[10px\] uppercase tracking-widest text-gray-400 block mb-2">Specialized Protocols</span>.*?</div>)', re.DOTALL)
    content = mobile_pattern.sub(r'\1' + new_mobile_treatments, content)

    with open(filepath, 'w') as f:
        f.write(content)

for root, dirs, files in os.walk("/workspace/project/contnerrepository"):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            update_file(filepath)
            print(f"Updated {filepath}")
