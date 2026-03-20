# Repository Memory: Cincinnati Chiropractic & Cincinnati Longevity

## Project Identity
- **Goal**: Premium "Technical Blueprint" clinical website for Dr. Limle.
- **Authority**: Official chiropractor for Bengals and Cyclones.
- **Hierarchy**: 4 Flagships, 10 Specialized Protocols.
- **Protocol Pages**: Renamed key files to `chronic-fatigue-long-covid.html`, `heart-rate-variability-optimization.html`, and `balance-strength-bone-optimization.html`; added `fibromyalgia-care.html` and `flexibility-mobility-optimization.html` (displayed as Flexibility & Functional Mobility).


## Technical Patterns
- **Tailwind CSS**: Core styling via CDN.
- **Sync System**: Use `sync_layout.py` to propagate header/footer changes from `index.html` to all other `.html` files.
- **Hero Animations**: High-intensity CSS/SVG animations in the home hero (infinite grid scroll, dual-axis lasers).
- **Button Styling**: Primary CTA buttons on dark backgrounds use `bg-white` with inline `style="color: #0047AB !important;"` to ensure visibility.
- **Modern Clinical Frame**: Class `.modern-clinical-frame` provides a dark glass background (`rgba(2, 6, 23, 0.8)`) with gradient borders for images. Use `object-fit: cover` and `aspect-ratio` to ensure graphics fill the frame.
- **Protocol Card Blueprint**: Class `.protocol-card-blueprint` uses a rounded rectangular design (`rounded-[2.5rem]`) with `aspect-ratio: 4/5.2` for protocol tiles. Background images are typically zoomed (e.g., `background-size: 140%`) to focus on subjects.
- **Integrated Disclaimer**: The clinical disclaimer is now a meta-card component with class `bento-stack-item lg:col-span-12` integrated directly into the `The Arsenal` grid.
- **Header Navigation**: Primary navigation links (e.g., HOME) should be in all-caps for technical consistency.

## Tool Lessons
- **Image Generation**: The `gemini-image_generate_image` tool does not accept a `path` argument. Always run it with only the `prompt` argument, then move the generated file using terminal commands.
- **Port Management**: The site serves on port 12000 (primary) or 12001 (backup).

## Active Development
- **Branch**: All work should be synchronized to `main`.
- **Images**: Local treatment images are stored in `/images/treatments/`.
- **Handoff**: Refer to `HANDOFF.md` for specific design system details.
