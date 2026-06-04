# AGENTS.md

Static portfolio website (HTML/CSS/JS) hosted on GitHub Pages from `main`.

## Commands
- Preview: `python3 -m http.server`
- Deploy: push to `main` branch

## Structure
- index.html — Entry point / Digital CV
- projects.html — Engineering projects (inline tab JS)
- travel.html — Leaflet.js travel map
- css/main.css — Dracula theme styles

## Tech & Conventions
- Leaflet.js 1.9.4 + OpenStreetMap (CDN)
- Dracula theme via CSS custom properties (`--background`, `--cyan`, etc.)
- Meslo LG L font (CDN)
- No build, lint, or test step

## Gotchas
- **Travel Map Images**: `travel.html` may reference images in `assets/img/` that are not yet in the repo.
- **Python**: `pyproject.toml` is for offline data generation (folium), not part of the web runtime.
- **Capstone Media**: `assets/projects/capstone/` is empty; WIP placeholder shown in modal.
- **Crankshaft Images**: The 4 PNGs (drawings, exploded_view, closeup_1/2) were 0-byte stubs and removed. Only the MP4 exists.
