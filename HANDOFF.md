# Cincinnati Chiropractic & Cincinnati Longevity: Technical Handoff

## **1. Project Overview**
Recreation of the "Cincinnati Chiropractic & Cincinnati Longevity" website with a premium **"Technical Blueprint"** clinical aesthetic. The site establishes Dr. Limle’s authority as the official chiropractor for the Cincinnati Bengals and Cyclones while implementing a rigorous 2-tier service hierarchy.

---

## **2. Design System & Aesthetic**
- **Core Theme**: High-Performance Clinical Engineering / Technical Blueprint.
- **Typography**: 
  - Display: `Lexend` (Massive, authoritative scales: 8xl - 9xl).
  - Body: `Inter` (Clean, technical legibility).
- **Color Palette**:
  - **Clinical Blue**: `#0047AB` (Foundational authority).
  - **Clinical Green**: `#22C55E` (Biological optimization & recovery).
  - **Bengals Orange**: `#FB4F14` (Pro-level accents & urgent notices).
  - **Background**: `#020617` (Cinematic deep charcoal).
- **Key UI Patterns**:
  - `blueprint-bg`: Dark blue grid with CSS scanning laser animations.
  - `glassmorphism`: Used for technical strategy modules and protocol headers.
  - `dot-matrix`: Subtle radial patterns behind specialized treatment heroes.

---

## **3. Technical Architecture**
- **Frontend**: Vanilla HTML5, Tailwind CSS (via CDN), Heroicons.
- **Animations**:
  - **Home Hero**: High-intensity CSS/SVG animation featuring dual-axis lasers, an infinite scrolling blueprint grid, and pulsing energy orbs.
  - **Technical HUD**: Floating geospatial coordinates and status readouts in the hero section.
- **Maintenance Scripting**:
  - `sync_layout.py`: A Python utility located in the root directory. Use this to automatically propagate changes from `index.html` (header/footer) to every other page in the repository.

---
## **3.5. Local Preview / Rehost**
- **Command**: `pkill -f "http.server"; nohup python3 -m http.server 12000 --directory /workspace/project/contnerrepository > /workspace/project/server.log 2>&1 &`
- **Primary Preview URL**: https://work-1-opgiuonvtishlphi.prod-runtime.all-hands.dev/
- **Backup Preview URL**: https://work-2-opgiuonvtishlphi.prod-runtime.all-hands.dev/
- If port 12000 is already in use, switch to 12001 and use the backup URL.

---


## **4. Site Hierarchy**
### **Tier 1: The Flagships (4)**
1. Precision Chiropractic
2. Integrative Physical Therapy
3. Personalized Medicine
4. Cincinnati Longevity

### **Tier 2: Specialized Protocols (10)**
- Neuropathy Care
- Cardiometabolic Repair
- Chronic Fatigue & Long Covid
- Fibromyalgia Care
- Sleep Optimization
- Heart Rate Variability Optimization
- Balance, Strength, and Bone Optimization
- Flexibility & Functional Mobility
- Golf Performance
- Longevity & Healthspan

---

## **5. Key Functional Elements**
- **Same-Day Notice**: Pulsing orange indicator on Chiropractic and Spinal Decompression pages for acute pain cases.
- **Treatment Hero Design**: Integrated green accent bars and circular technical overlays to unify modality pages.
- **Strategic CTA**: "Request Appointment" buttons are forced to high-contrast blue (`#0047AB`) against white backgrounds to ensure visibility.

---

## **6. Future Development Notes**
- **Adding New Pages**: When adding a new treatment or protocol, use the `vagus-nerve-stimulation.html` or `shockwave-therapy.html` as templates to maintain the hero aesthetic.
- **Header/Footer Updates**: Always update the master versions in `index.html` or the standalone text files, then run `python3 sync_layout.py` to update the entire site.
- **Image Management**: Ensure all treatment images are placed in `/images/treatments/` and use the `object-contain` class within the white frames to prevent clipping of clinical diagrams.
- **Mobile Layout (Homepage)**: Mobile-only spacing and typography tweaks live in `index.html` for the hero, Cincinnati Legacy, and Flagships cards. Preserve the `sm:` breakpoints when adjusting desktop layout.

---
## **7. Recent Updates**
- **2026-03-11**: Refreshed global footer layout with tightened spacing, updated clinic hours, and same-day evaluation callout across all pages.
- **2026-03-11**: Updated footer with official Cincinnati Chiropractic logo, relocated CTA into a full-width callout band, and added a richer gradient/blueprint glow background.

- **2026-03-11**: Added Patient Resources to desktop nav, added Red Light Therapy to treatments menus, and expanded the footer into a four-column navigation hub with blueprint overlay and updated social placeholders.


- **2026-03-11**: Tuned homepage hero badge spacing and added extra margin between “Dr. Andrew Limle” and “Official Team Chiropractor” in the Cincinnati Legacy section.
- **2026-03-11**: Switched the Performance Continuum section background to clinical green and adjusted heading colors for contrast.
- **2026-03-11**: Merged hero and clinical philosophy/diagnostic sections on all flagship program pages to reduce vertical scroll.
- **2026-03-11**: Applied clinical green background styling to the "A New Standard of Care" tiles on flagship pages.
- **2026-03-11**: Renamed the homepage Cincinnati Longevity references to "Longevity Care" in the flagship tile and related section copy.
- **2026-03-11**: Rebuilt the Cincinnati Longevity flagship hero into the standard two-column flagship layout with green highlight tile styling.
- **2026-03-11**: Added longevity-specific "Our Core Strategies" and "What We Treat & Optimize" sections to the Longevity Care flagship page.
- **2026-03-11**: Renamed specialized protocols (Chronic Fatigue & Long Covid, Heart Rate Variability Optimization) and added new Fibromyalgia Care + Flexibility & Functional Mobility pages; updated homepage bento grids, navigation, and contact form options.
- **2026-03-11**: Swapped homepage order so Specialized Protocols appear before the Performance Continuum.
- **2026-03-11**: Renamed Flexibility & Mobility protocol to Flexibility & Functional Mobility across navigation, program metadata, and schema.
- **2026-03-11**: Renamed Golf Optimization to Golf Performance across navigation, tiles, and program metadata.
- **2026-03-11**: Reworked the Specialized Protocols homepage section into two structured columns (Chronic Management + Performance & Structure) to replace the staggered multi-row bento layout.
- **2026-03-11**: Added a homepage Meet the Team preview section with hover bios and six placeholder portraits.
- **2026-03-11**: Removed temporary flagship pillar graphics and restored placeholder labels.

- **2026-03-11**: Refreshed Cincinnati-focused SEO meta descriptions/JSON-LD (mitochondria + diabetes in cardiometabolic, heart rate variability spelled out, cold laser naming, golf swing speed/distance) and regenerated sitemap.xml after removing deprecated pages.

- **2026-03-11**: Updated flagship core strategy tiles to white cards and removed corner numbering.
- **2026-03-11**: Added SEO metadata (descriptions, canonical URLs, OG/Twitter tags), structured data, trust strip near the hero, cleaned mobile nav duplication, and generated sitemap.xml/robots.txt.

- **2026-03-13**: Finalized **Fibromyalgia** and **Mobility** protocol pages with high-resolution PNG assets and blueprint-aligned layouts.
- **2026-03-13**: Replaced all flagship program graphics with new PNG images (`chiro.png`, `longevitycare.png`, etc.) and introduced `modern-clinical-frame` CSS for a dark-themed, edge-to-edge technical aesthetic.
- **2026-03-13**: Integrated **Chiropractic**, **Physical Therapy**, and **Medical Services** into the clinical stack grid of every specialized protocol page with context-specific details.
- **2026-03-13**: Redesigned the clinical disclaimer as an integrated full-width "meta-card" within the Arsenal grid on all protocol pages, removing it from isolated sections.
- **2026-03-13**: Updated global navigation header: Changed "Home" link text to all-caps "**HOME**" and synced across the entire site.
- **2026-03-13**: Removed protocol graphics from the homepage bento tiles to maintain exclusivity for specialized landing pages.

- **2026-03-16**: Updated Dr. Alex Contner's professional bio and transitioned headshot to PNG format (`alexcontnerheadshot.png`) across homepage and team page clinical rosters.





---



**Status**: Active development.
**Branch**: `main`
**Repository**: [contner-png/contnerrepository](https://github.com/contner-png/contnerrepository)
