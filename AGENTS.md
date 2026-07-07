# AGENTS.md

Static portfolio website for **Ajeet Krishnasamy** - Mechanical Engineering graduate specializing in aerodynamics and CFD. Terminal-inspired **Dracula theme** aesthetic. Hosted on **GitHub Pages** from `main`.

## Commands
- **Preview:** `python3 -m http.server`
- **Deploy:** push to `main` branch (auto-deploys)

## Structure

```
├── index.html          # Digital CV / Homepage (static HTML/CSS)
├── projects.html       # Engineering project gallery with modal viewer (inline JS)
├── gallery.html        # CAD gallery page (inline JS modal)
├── css/main.css        # All styles - Dracula theme, 683 lines, 9 sections
├── assets/
│   ├── docs/Resume.pdf
│   ├── img/
│   │   └── profile_pic.png
│   └── projects/
│       ├── soccer/               # velocity_comparison.mp4, formation_comparison.png, gap_2m.png, gap_4m.png
│       ├── capstone/             # EMPTY - WIP placeholder in modal
│       ├── orbital/              # outputs/ (3 GIFs: multi_orbit, hohmann, ground_track)
│       ├── airfoil/              # 3 PNGs: airfoil_comparison, cd_vs_mach, optimization_convergence
│       ├── crankshaft/           # crankshaft animated.mp4 (plays on hover)
│       ├── swarm/                # teaser_3d.png, teaser_2d.png, trajectory_facets.png, apf_path_2d.mp4
│       └── f1/                   # downforce/, ride_height/, cornering/, cfd/ PNGs
├── pyproject.toml      # Python project (NOT web runtime)
├── uv.lock
├── PROJECTS_SOURCE.md  # Master project bank (8 entries, gitignored)
├── PORTFOLIO_REVIEW.md # Hiring manager portfolio analysis (gitignored)
├── README.md
└── AGENTS.md
```

## Pages

### `index.html` - Digital CV
- Profile pic + 3-paragraph bio (cover-letter style, CDF workflow + GNC + career interests)
- Experience (2 CenTrak internships, metric-driven bullets from resume)
- Skills (clean list format, 4 categories: Aerodynamics & CFD, GNC, CAD/FEA & Programming, Manufacturing)
- Education (Degree, Major, Coursework)
- Action bar with Resume PDF, email, LinkedIn, GitHub links
- No JavaScript - purely static

### `projects.html` - Engineering Projects
- 2x2 grid of wiki-style cards with top-border accent, hover lift effect
- 6 projects (ordered): SwarmGNC, Airfoil CFD Explorer, Soccer, F1 Dashboard, Capstone, Orbital
- **Modal system (inline JS):** `projectData` object, `openProject(id)`, `switchTab(projectId, tabKey)`, `closeModal()`, click-outside-to-close
- Modal types: `gallery` (direct media + description) and `report` (tabbed content)
- Link to gallery.html at bottom

### SwarmGNC (`'swarm'` entry)
- **Type:** `report` with 3 tabs: Overview, 3D Swarm, 2D APF
- **Overview:** LQR control via CARE, APF obstacle avoidance, graph Laplacian consensus, Dryden wind turbulence, key results card
- **3D Swarm:** Three.js viewer screenshot, key metrics (formation error, connectivity, wind rejection)
- **2D APF:** Trajectory facets gain sweep comparison, corridor animation MP4, 4 behavioral regimes

### Soccer Project (`'soccer'` entry)
- **Type:** `report` with 4 tabs: Overview, Shooting, Tactical, Overlap
- **Overview:** PhiFlow + SU2 pipeline, links, key results (Strouhal, Cd, drag reduction, formation pressure)
- **Shooting:** `velocity_comparison.mp4` - Magnus vs knuckleball, key insight card
- **Tactical:** `formation_comparison.png` - 4-formation Gaussian pressure grid, HTML pressure table
- **Overlap:** `gap_2m.png` + `gap_4m.png` - drafting drag reduction, gap sweep card

### F1 Dashboard (`'f1'` entry)
- **Type:** `gallery` with 7 image figures + captions + live site link
- Downforce breakdown, drag polar, ride height contour, grip envelope, venturi CFD, front wing CFD, force scaling

### `gallery.html` - CAD Gallery
- Orange-themed gallery page
- Gallery grid (auto-fill, 300px min, 1:1 aspect ratio)
- Crankshaft Assembly MP4 (hover-play) + 5 coming-soon placeholders
- Dedicated modal with technical specs (software, component count)

## CSS Conventions (`css/main.css`)
- **Dracula palette** via `:root` custom properties: `--background`, `--current-line`, `--foreground`, `--comment`, `--cyan`, `--green`, `--orange`, `--pink`, `--purple`
- **Accent meaning:** purple → headers/titles, cyan → links, pink → hover, green → active, orange → metadata, comment → secondary text
- Cards: dark bg `#21222c`, left border accent (section-specific color), 20px padding
- Responsive: single `@media (max-width: 768px)` breakpoint
- All class names are semantic kebab-case

## JavaScript Conventions
- **No external `.js` files** - all JS is inline in HTML
- Libraries loaded from CDN: Meslo LG L font

## Content Rules
- **No em dashes** (`--`, `&mdash;`, Unicode U+2014) anywhere in the project. They read as AI-generated. Use colons, semicolons, or commas instead.

## Tech Stack
- Pure HTML/CSS/JS (no build, no lint, no test)
- Meslo LG L font (CDN)
- Python 3.14+ with folium for offline data generation only

## Deployment
- **Host:** GitHub Pages from `main`
- **URL:** https://ajeet-krish.github.io/portfolio
- **No CI/CD** - push-to-deploy via GitHub Pages branch setting
- `.gitignore`: `.DS_Store`, `.venv/`, `.idea/`, `.ruff_cache/`, `__pycache__/`, `*.pyc`, `CV/`, `assets/maps/`, `assets/projects/orbital/orbit_files/`, `assets/projects/orbital/orbit.html`, `assets/projects/orbital/orbit.css`, `PORTFOLIO_REVIEW.md`, `PROJECTS_SOURCE.md`

## Gotchas
- **Travel Page:** `travel.html` still exists on disk but is **not linked from any nav**. City images are not in the repo. Not part of the live site.
- **Capstone Media:** `assets/projects/capstone/` does not exist; WIP placeholder shown in modal pending publication clearance.
- **Crankshaft Images:** The 4 PNGs (drawings, exploded_view, closeup_1/2) were 0-byte stubs and removed. Only the MP4 exists.
- **Python:** `pyproject.toml` / `uv.lock` is for offline folium map generation - **not part of the web runtime**.
- **Breadcrumb conceit:** Pages use a terminal-style path (e.g., `~ / portfolio / resume.py`) with `.py` extension as a theme, not indicating actual Python files.
- **Card Style:** Projects use a 2-column `wiki-grid` with top-border accent, rectangular (no rounded) corners. Mobile collapses to single column with left-border accent.
