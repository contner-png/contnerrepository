import os

pages = {
    "spinal-decompression.html": {
        "title": "Spinal Decompression",
        "image": "/images/treatments/decompression.png",
        "mechanism": "Engineering negative intradiscal pressure to facilitate nutrient exchange and disc rehydration.",
        "efficacy_title": "Precision Mechanical Traction",
        "efficacy_text": "Our advanced spinal decompression system allows for targeted, computerized axial traction designed to alleviate pressure on compromised nerve roots."
    },
    "dry-needling.html": {
        "title": "Advanced Dry Needling",
        "image": "/images/treatments/dryneedling.png",
        "mechanism": "Targeting myofascial trigger points to reset neuromuscular dysfunction and eliminate chronic tension.",
        "efficacy_title": "Intramuscular Stimulation",
        "efficacy_text": "Utilizing precision filiform needles to elicit a local twitch response, facilitating the release of deep tissue adhesions and improving blood flow."
    },
    "vagus-nerve-stimulation.html": {
        "title": "tVNS Vagus Nerve Stimulation",
        "image": "https://images.unsplash.com/photo-1559757175-570098d17869?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80",
        "mechanism": "Modulating the auricular branch of the vagus nerve to balance the autonomic nervous system and reduce systemic inflammation.",
        "efficacy_title": "Non-Invasive Neuromodulation",
        "efficacy_text": "Leveraging the gut-brain axis to improve heart rate variability (HRV), sleep quality, and immune resilience through non-invasive nerve stimulation."
    },
    "sleep-testing.html": {
        "title": "Clinical Sleep Testing",
        "image": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80",
        "mechanism": "Comprehensive at-home diagnostics to quantify sleep architecture and identify metabolic recovery barriers.",
        "efficacy_title": "Quantified Recovery Diagnostics",
        "efficacy_text": "High-fidelity biometric monitoring used to identify OSA, restless leg syndrome, and architectural disruptions that prevent cellular restoration."
    },
    "targeted-supplements.html": {
        "title": "Targeted Supplements",
        "image": "https://images.unsplash.com/photo-1584017911766-d451b3d0e843?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80",
        "mechanism": "Evidence-based nutraceutical protocols designed to optimize mitochondrial efficiency and cellular resilience.",
        "efficacy_title": "Precision Biological Support",
        "efficacy_text": "Pharmaceutical-grade supplements curated to address specific metabolic deficiencies and support your unique longevity blueprint."
    },
    "longevity-blood-panels.html": {
        "title": "Longevity Blood Panels",
        "image": "https://images.unsplash.com/photo-1579154273821-ad111f395706?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80",
        "mechanism": "Advanced biomarker analysis and estimated aging quantification to engineer your biological future.",
        "efficacy_title": "Biological Age Quantification",
        "efficacy_text": "Moving beyond standard labs to analyze inflammatory markers, nutrient levels, and hormonal profiles that dictate long-term vitality."
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Cincinnati Chiropractic & Mitoflux Longevity</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lexend:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        clinical: {{
                            blue: '#0047AB',
                            green: '#22C55E',
                            charcoal: '#333333',
                            gray: '#F9FAFB',
                            light: '#FFFFFF'
                        }}
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        display: ['Lexend', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-white text-clinical-charcoal font-sans antialiased">
    <!-- Navigation included via build process -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm">
        <nav class="container mx-auto px-6 py-4 flex items-center justify-between">
            <div class="flex items-center">
                <a href="/index.html" class="text-2xl font-display font-bold text-clinical-blue tracking-tight">
                    CINCINNATI <span class="text-clinical-charcoal font-light">CHIROPRACTIC</span>
                </a>
            </div>
            <div class="hidden lg:flex items-center space-x-8 text-sm font-medium">
                <a href="/index.html" class="nav-link text-clinical-blue">Home</a>
                <!-- Navigation items will be updated globally -->
            </div>
        </nav>
    </header>

    <main>
        <!-- Technology Hero -->
        <section class="py-24 bg-clinical-gray relative overflow-hidden">
            <div class="absolute inset-0 bg-grid-pattern opacity-10"></div>
            <div class="container mx-auto px-6 relative z-10">
                <div class="flex flex-col lg:flex-row items-center gap-16">
                    <div class="lg:w-1/2">
                        <div class="inline-flex items-center px-3 py-1 rounded-full bg-clinical-blue/10 text-clinical-blue text-xs font-bold tracking-widest uppercase mb-6">
                            Advanced Modality
                        </div>
                        <h1 class="text-5xl lg:text-7xl font-display font-bold mb-8 leading-tight">
                            {title}
                        </h1>
                        <div class="prose prose-lg text-gray-600 leading-relaxed max-w-xl">
                            <h3 class="text-2xl font-bold text-clinical-charcoal mb-4">Mechanism of Action</h3>
                            <p class="text-xl">
                                {mechanism}
                            </p>
                        </div>
                        <div class="mt-12">
                            <a href="/contact.html" class="px-8 py-4 bg-clinical-blue text-white rounded-full font-bold text-lg hover:bg-blue-700 transition-all shadow-xl shadow-blue-100 inline-block text-center">
                                Request Appointment
                            </a>
                        </div>
                    </div>
                    <div class="lg:w-1/2 relative">
                        <div class="relative z-10 rounded-[3rem] overflow-hidden shadow-2xl border-[12px] border-white">
                            <img src="{image}" alt="{title} Benefits" class="w-full h-full object-cover">
                        </div>
                        <div class="absolute -bottom-10 -left-10 w-40 h-40 bg-clinical-green/10 rounded-full blur-3xl"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Clinical Efficacy Section -->
        <section class="py-24 bg-white relative overflow-hidden">
            <div class="absolute inset-0 bg-dot-pattern opacity-10"></div>
            <div class="container mx-auto px-6 relative z-10">
                <div class="max-w-4xl mx-auto text-center">
                    <h3 class="text-4xl font-display font-bold mb-8">{efficacy_title}</h3>
                    <p class="text-2xl text-gray-600 leading-relaxed font-light">
                        {efficacy_text}
                    </p>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-clinical-charcoal text-white pt-24 pb-12">
        <div class="container mx-auto px-6 text-center">
            <p>&copy; 2026 Cincinnati Chiropractic & Mitoflux Longevity. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

base_dir = "/workspace/project/contnerrepository/treatments"
for filename, content in pages.items():
    path = os.path.join(base_dir, filename)
    with open(path, "w") as f:
        f.write(template.format(**content))
    print(f"Updated {path}")
