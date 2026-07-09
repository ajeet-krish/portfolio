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
├── css/main.css        # All styles - Dracula theme, 862 lines, 9 sections
├── assets/
│   ├── docs/Resume.pdf
│   ├── img/
│   │   └── profile_pic.png
│   └── projects/
│       ├── soccer/               # velocity_comparison.mp4, formation_comparison.png, gap_2m.png, gap_4m.png
│       ├── capstone/             # media/ (10 files: CAD, FEA, layout, GUI images)
│       ├── orbital/              # outputs/ (3 GIFs: multi_orbit, hohmann, ground_track)
│       ├── airfoil/              # 2D_CFD/ + Optimization/ (airfoil-cfd explorer media)
│       ├── crankshaft/           # crankshaft animated.mp4 (plays on hover)
│       ├── swarm/                # *.mov videos, trajectory.png, monte_carlo.png
│       └── f1/                   # downforce/, ride_height/, cornering/, cfd/ PNGs
├── pyproject.toml      # Python project (offline map generation only)
├── uv.lock
├── CPP_PROJECT_PLAN.md # C++ project roadmap (5 projects, gitignored)
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
- **Type:** `report` with 3 tabs: Overview, 2D, 3D
- **Overview:** Purpose-focused narrative, key results card (formation error, connectivity, optimal gain, Monte Carlo envelope, control effort)
- **2D:** APF corridor simulation with gain sweep, trajectory overlay, Monte Carlo failure probability map
- **3D:** Seven-drone figure-8 through 15 obstacles, decentralized consensus, leader-velocity wedge rotation

### Soccer Project (`'soccer'` entry)
- **Type:** `report` with 4 tabs: Overview, Shooting, Tactical, Overlap
- **Overview:** PhiFlow + SU2 pipeline, links, key results (Strouhal, Cd, drag reduction, formation pressure)
- **Shooting:** `velocity_comparison.mp4` - Magnus vs knuckleball, key insight card
- **Tactical:** `formation_comparison.png` - 4-formation Gaussian pressure grid, HTML pressure table
- **Overlap:** `gap_2m.png` + `gap_4m.png` - drafting drag reduction, gap sweep card

### F1 Dashboard (`'f1'` entry)
- **Type:** `gallery` with 7 image figures + captions + live site link
- Downforce breakdown, drag polar, ride height contour, grip envelope, venturi CFD, front wing CFD, force scaling

### Capstone (`'capstone'` entry)
- **Type:** `report` with 2 tabs: Gallery, Full Report
- **Gallery:** Design overview CAD, layer sectional/exploded views, harness integration, static FEA, MATLAB GUI, optimization loop
- **Full Report:** Markdown-rendered (marked.js) design document from `assets/projects/capstone/PROJECT_CAPSTONE.md`
- Horseshoe-shaped multilayer pad (STF core + TPU shell), MATLAB parametrization tool, 35% attenuation target

### `gallery.html` - CAD Gallery
- Orange-themed gallery page
- Gallery grid (auto-fill, 300px min, 1:1 aspect ratio)
- Crankshaft Assembly MP4 (hover-play) + 5 coming-soon placeholders
- Dedicated modal with technical specs (software, component count)

### Airfoil CFD Explorer (`'airfoil-cfd'` entry)
- **Type:** `report` with 3 tabs: Overview, 2D CFD, Optimization
- **Overview:** Automated RANS pipeline, NACA 0012 validation vs Ladson 1988, CST shape optimization
- **2D CFD:** Velocity/pressure fields at AoA=0-16°, drag polar benchmark
- **Optimization:** CST parameterization (16 weights), NeuralFoil, IPOPT convergence history

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
- `.gitignore`: `.DS_Store`, `.venv/`, `.idea/`, `.ruff_cache/`, `__pycache__/`, `*.pyc`, `CV/`, `assets/maps/`, `assets/projects/orbital/orbit_files/`, `assets/projects/orbital/orbit.html`, `assets/projects/orbital/orbit.css`, `PORTFOLIO_REVIEW.md`, `PROJECTS_SOURCE.md`, `CPP_PROJECT_PLAN.md`

## Gotchas
- **Travel Page:** `travel.html` still exists on disk but is **not linked from any nav**. City images are not in the repo. Not part of the live site.
- **Capstone Media:** `assets/projects/capstone/media/` exists with 10 files (CAD, FEA, layout, GUI images). `PROJECT_CAPSTONE.md` is at `assets/projects/capstone/PROJECT_CAPSTONE.md`.
- **Crankshaft Images:** The 4 PNGs (drawings, exploded_view, closeup_1/2) were 0-byte stubs and removed. Only the MP4 exists.
- **Python:** `pyproject.toml` / `uv.lock` is for offline folium map generation - **not part of the web runtime**.
- **Breadcrumb conceit:** Pages use a terminal-style path (e.g., `~ / portfolio / resume.py`) with `.py` extension as a theme, not indicating actual Python files.
- **Card Style:** Projects use a 2-column `wiki-grid` with top-border accent, rectangular (no rounded) corners. Mobile collapses to single column with left-border accent.
- **Airfoil Dashboard removed:** The standalone `'airfoil'` gallery entry (Airfoil Optimization Dashboard) was removed from `projects.html`. Only `'airfoil-cfd'` (Airfoil CFD Explorer) remains. The top-level `assets/projects/airfoil/` images are orphaned from the dashboard but the `2D_CFD/` and `Optimization/` subdirs serve the CFD explorer.
- **No dates on projects:** Year labels stripped from all non-capstone project cards and modal metas to avoid the "all built in one semester" appearance. Only capstone retains `Capstone 2026`.
- **C++ Plan:** `CPP_PROJECT_PLAN.md` is gitignored. Contains implementation plans for 5 C++ projects (6-DOF flight sim, CFD solver, LQR port, ROS 2 EKF, trajectory optimizer) with portfolio positioning for each.
