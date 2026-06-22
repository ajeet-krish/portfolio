# AGENTS.md

Static portfolio website for **Ajeet Krishnasamy** - Biomedical Mechanical Engineering graduate. Terminal-inspired **Dracula theme** aesthetic. Hosted on **GitHub Pages** from `main`.

## Commands
- **Preview:** `python3 -m http.server`
- **Deploy:** push to `main` branch (auto-deploys)

## Structure

```
├── index.html          # Digital CV / Homepage (static HTML/CSS)
├── projects.html       # Engineering project gallery with modal viewer (inline JS)
├── travel.html         # Leaflet.js interactive travel map (inline JS)
├── css/main.css        # All styles - Dracula theme, 665 lines, 9 sections
├── assets/
│   ├── docs/Resume.pdf
│   ├── img/
│   │   ├── profile_pic.png
│   │   └── luffy_icons.png       # Custom Leaflet marker icon
│   └── projects/
│       ├── soccer/               # velocity_comparison.mp4, formation_comparison.png, gap_2m.png, gap_4m.png
│       ├── capstone/             # EMPTY - WIP placeholder in modal
│       ├── orbital/              # outputs/ (3 GIFs: multi_orbit, hohmann, ground_track)
│       ├── airfoil/              # 3 PNGs: airfoil_comparison, cd_vs_mach, optimization_convergence
│       └── crankshaft/           # crankshaft animated.mp4 (plays on hover)
├── pyproject.toml      # Python project: folium for offline map generation (NOT web runtime)
├── uv.lock             # Lockfile for folium + deps
└── README.md
```

## Pages

### `index.html` - Digital CV
- Profile pic + bio, experience (2 CenTrak internships), skills (Python dict literal), education
- Action bar with Resume PDF, email, LinkedIn, GitHub links
- No JavaScript - purely static

### `projects.html` - Engineering Projects
- Wiki-style cards with modal-based detail viewer
- **Projects (ordered):** The Physics of Soccer (CFD, tabbed report modal), Wearable Hip Protector (capstone, tabbed report modal), 3D Orbital Trajectory Animator (gallery modal), Airfoil Optimization Dashboard (gallery modal + 3 coming-soon placeholders)
- **CAD Gallery section:** Crankshaft Assembly MP4 (plays on hover via JS)
- **Modal system (inline JS):** `projectData` object, `openProject(id)`, `switchTab(projectId, tabKey)`, `closeModal()`, click-outside-to-close
- Modal types: `gallery` (media + description) and `report` (tabbed content)

### Soccer Project (`'soccer'` entry in `projectData`)
- **Type:** `report` with 4 tabs: Overview, Shooting, Tactical, Overlap
- **Overview:** ΦFlow + SU2 pipeline description, links to live site + GitHub, key results table
- **Shooting:** `velocity_comparison.mp4` - Magnus effect vs knuckleball (ΦFlow, Re≈4×10⁴), key insight card
- **Tactical:** `formation_comparison.png` - 4-formation pressure grid (Gaussian influence fields), HTML table of lane pressures
- **Overlap:** `gap_2m.png` + `gap_4m.png` - drafting drag reduction at varying gaps, gap sweep data card

### `travel.html` - Leaflet.js Travel Map
- **Current state:** "Work in progress" notice
- Sidebar (location list) + map (flex layout)
- Leaflet.js 1.9.4 with **ÖPNVKarte** (public transport) + **OpenSeaMap** (nautical) tile layers
- Custom **Luffy icon** marker (One Piece theme)
- 7 locations: Mississauga, Ottawa, Chennai, Melbourne, Bangkok, New Delhi, Los Angeles
- Click sidebar item → `map.flyTo()` + popup after 1.5s delay
- `map.invalidateSize()` on resize

## CSS Conventions (`css/main.css`)
- **Dracula palette** via `:root` custom properties: `--background`, `--current-line`, `--foreground`, `--comment`, `--cyan`, `--green`, `--orange`, `--pink`, `--purple`
- **Accent meaning:** purple → headers/titles, cyan → links, pink → hover, green → active, orange → metadata, comment → secondary text
- Cards: dark bg `#21222c`, left border accent (section-specific color), 20px padding
- Responsive: single `@media (max-width: 768px)` breakpoint
- All class names are semantic kebab-case

## JavaScript Conventions
- **No external `.js` files** - all JS is inline in HTML
- Libraries loaded from CDN: Leaflet.js 1.9.4, Meslo LG L font

## Content Rules
- **No em dashes** (`--`, `&mdash;`, Unicode U+2014) anywhere in the project. They read as AI-generated. Use colons, semicolons, or commas instead.

## Tech Stack
- Pure HTML/CSS/JS (no build, no lint, no test)
- Leaflet.js 1.9.4 + OpenStreetMap tiles (CDN)
- Meslo LG L font (CDN)
- Python 3.14+ with folium for offline data generation only

## Deployment
- **Host:** GitHub Pages from `main`
- **URL:** https://ajeet-krish.github.io/portfolio
- **No CI/CD** - push-to-deploy via GitHub Pages branch setting
- `.gitignore`: `.DS_Store`, `.venv/`, `.idea/`, `.ruff_cache/`, `__pycache__/`, `*.pyc`, `CV/`, `assets/maps/`, `assets/projects/orbital/orbit_files/`, `assets/projects/orbital/orbit.html`, `assets/projects/orbital/orbit.css`

## Gotchas
- **Travel Map Images:** `travel.html` references 7 city images (`mississauga.jpg`, `ottawa.jpg`, `chennai.jpg`, `melbourne.jpg`, `bangkok.jpg`, `newdelhi.jpg`, `losangeles.jpg`) in `assets/img/` that are **not yet in the repo**.
- **Capstone Media:** `assets/projects/capstone/` does not exist; WIP placeholder shown in modal pending publication clearance.
- **Crankshaft Images:** The 4 PNGs (drawings, exploded_view, closeup_1/2) were 0-byte stubs and removed. Only the MP4 exists.
- **Python:** `pyproject.toml` / `uv.lock` is for offline folium map generation - **not part of the web runtime**.
- **Breadcrumb conceit:** Pages use a terminal-style path (e.g., `~ / portfolio / resume.py`) with `.py` extension as a theme, not indicating actual Python files.
