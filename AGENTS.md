# Repository Memory: Cincinnati Chiropractic & Cincinnati Longevity

## Project Identity
- **Goal**: Premium "Technical Blueprint" clinical website for Dr. Limle.
- **Authority**: Official chiropractor for Bengals and Cyclones.
- **Hierarchy**: 4 Flagships, 8 Specialized Protocols.

## Technical Patterns
- **Tailwind CSS**: Core styling via CDN.
- **Sync System**: Use `sync_layout.py` to propagate header/footer changes from `index.html` to all other `.html` files.
- **Hero Animations**: High-intensity CSS/SVG animations in the home hero (infinite grid scroll, dual-axis lasers).
- **Button Styling**: Primary CTA buttons on dark backgrounds use `bg-white` with inline `style="color: #0047AB !important;"` to ensure visibility.

## Tool Lessons
- **Image Generation**: The `gemini-image_generate_image` tool does not accept a `path` argument. Always run it with only the `prompt` argument, then move the generated file using terminal commands.
- **Port Management**: The site serves on port 12000 (primary) or 12001 (backup).

## Active Development
- **Branch**: All work should be synchronized to `main`.
- **Images**: Local treatment images are stored in `/images/treatments/`.
- **Handoff**: Refer to `HANDOFF.md` for specific design system details.
