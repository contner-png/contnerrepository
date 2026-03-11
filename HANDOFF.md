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
- **Command**: `python3 -m http.server 12000 --directory /workspace/project/contnerrepository`
- **Primary Preview URL**: https://work-1-euiuochaancxlqpb.prod-runtime.all-hands.dev
- **Backup Preview URL**: https://work-2-euiuochaancxlqpb.prod-runtime.all-hands.dev
- If port 12000 is already in use, switch to 12001 and use the backup URL.

---


## **4. Site Hierarchy**
### **Tier 1: The Flagships (4)**
1. Precision Chiropractic
2. Integrative Physical Therapy
3. Personalized Medicine
4. Cincinnati Longevity

### **Tier 2: Specialized Protocols (8)**
- Neuropathy Care
- Cardiometabolic Repair
- Bio-Energy Recovery
- Sleep Optimization
- Balance, Strength, and Bone Optimization
- Golf Optimization
- HRV Optimization
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

**Status**: Active development.
**Branch**: `main`
**Repository**: [contner-png/contnerrepository](https://github.com/contner-png/contnerrepository)
