# LogoLibrary — Portfolio Case Study

## Project Overview

**LogoLibrary** is a comprehensive open-source brand logo and UI icon collection that I created, designed, and maintain as the official repository owner. It combines a searchable web explorer with an interactive 3D Studio, allowing designers and developers to find, preview, and extrude logos into three-dimensional assets.

| | |
|:---|:---|
| **Role** | Creator, Lead Developer, Maintainer |
| **Type** | Open Source Developer Tool |
| **Live URL** | [logo-explorer.vercel.app](https://logo-explorer.vercel.app) |
| **3D Studio** | [logo-explorer.vercel.app/studio](https://logo-explorer.vercel.app/studio) |
| **GitHub** | [github.com/ajmaliifthikar-ux/logo-library](https://github.com/ajmaliifthikar-ux/logo-library) |
| **Tech Stack** | Next.js 16, TypeScript, Tailwind CSS, Three.js, Python, SQLite, Cloudinary |

---

## The Problem

Designers and developers waste hours searching through messy, unorganized logo dumps. Existing collections are:
- Unsearchable — no metadata or categorization
- Static — logos are flat files with no interactive preview
- Fixed — no way to expand the library without manual work
- Unattributed — no clear licensing or brand ownership info

## The Solution

LogoLibrary solves all four problems with a fully automated, searchable, and interactive platform.

### 1. Searchable Explorer
Instant client-side search across 1,147+ brands by name, tag, or category. Powered by SQLite FTS5 and a JSON metadata manifest.

### 2. Interactive 3D Studio
Users can select any logo and extrude it into interactive 3D with full control over materials, lighting, animation, and camera — powered by the `3dsvg` engine and Three.js.

### 3. Auto-Expanding Pipeline
A background Python pipeline listens for new Figma URLs, extracts SVGs, organizes them by category, updates the search index, commits to Git, and syncs to Cloudinary CDN — all automatically.

### 4. Attribution-First
Every copy action includes proper HTML attribution snippets. Brand ownership is clearly noted.

---

## Key Features

### Explorer Dashboard
- **1,147+ brands** across 9 categories
- **Instant search** with category filtering
- **Grid + List views** with responsive layout
- **One-click copy** — local path, CDN URL, or full HTML attribution
- **Dark mode UI** built with brand colors (#e94560 on #0a0a0a)

### 3D Studio
- **10 material presets** — plastic, metal, glass, rubber, chrome, gold, clay, emissive, holographic
- **7 animation presets** — spin, float, pulse, wobble, spinFloat, swing
- **Real-time camera control** — zoom, FOV, tilt X/Y
- **Dramatic lighting** — adjustable key light, ambient fill, contact shadows
- **Background picker** — 10 presets including transparent
- **SVG upload** — drop any `.svg` and instantly see it in 3D
- **Cinematic intro** — zoom or fade animation on load

### Auto-Pipeline
- **Figma extractor** — downloads SVGs via Figma API with rate-limit backoff
- **Smart organization** — sorts into categories automatically
- **SQLite indexer** — rebuilds full-text search on every update
- **Git auto-commit** — commits new assets every 5 minutes
- **Cloudinary sync** — uploads to CDN with automatic tagging

---

## Technical Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Figma Files    │────▶│  Python Pipeline │────▶│  Logo_Library/  │
│  (Community)    │     │  (Extractor)     │     │  (Assets + DB)  │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                          ┌──────────────────┐            │
                          │  Cloudinary CDN  │◀───────────┘
                          └──────────────────┘
                                   │
                          ┌────────▼─────────┐
                          │  Next.js App     │
                          │  - Explorer      │
                          │  - 3D Studio     │
                          │  - Static Export │
                          └──────────────────┘
```

### Frontend
- **Next.js 16** with App Router and static export
- **Tailwind CSS** for utility-first styling
- **TypeScript** for type safety
- **3dsvg + Three.js** for 3D rendering
- **React lazy + Suspense** for code splitting

### Backend / Pipeline
- **Python** orchestrator with PID-file locking
- **SQLite FTS5** for full-text search
- **Cloudinary REST API** for CDN sync
- **Figma REST API** for SVG extraction

### DevOps
- **Vercel** for frontend hosting
- **GitHub** for version control
- **Background daemons** for continuous processing

---

## My Contributions

### Design & UX
- Designed the entire dark-mode interface with custom brand identity
- Built the explorer grid, list view, modal system, and toast notifications
- Created the 3D Studio control panel with 30+ adjustable parameters

### Development
- Built the Next.js app with static generation for 1,800+ assets
- Integrated the `3dsvg` engine with custom lighting and camera presets
- Wrote the Python auto-pipeline with logging, health monitoring, and crash recovery
- Implemented SQLite FTS5 search index with automatic rebuilds

### DevOps & Maintenance
- Set up Vercel continuous deployment
- Built Cloudinary sync scripts
- Created monitoring dashboard (`./monitor.sh`)
- Wrote comprehensive documentation and improvement roadmaps

---

## Impact

| Metric | Value |
|--------|-------|
| Brands indexed | 1,147 |
| Total assets | 3,128 |
| Categories | 9 |
| GitHub stars | Growing |
| Auto-commits | Every 5 minutes |
| CDN uploads | 520+ and counting |

---

## What I Learned

- **Static site generation at scale** — deploying 1,800+ assets with Next.js static export
- **3D in the browser** — integrating Three.js via React with proper SSR guards
- **Pipeline architecture** — building resilient background workers with PID locking and log rotation
- **Open source maintenance** — writing docs, managing issues, and creating contributor-friendly code

---

## Links

- **Live Explorer:** [logo-explorer.vercel.app](https://logo-explorer.vercel.app)
- **3D Studio:** [logo-explorer.vercel.app/studio](https://logo-explorer.vercel.app/studio)
- **GitHub Repo:** [github.com/ajmaliifthikar-ux/logo-library](https://github.com/ajmaliifthikar-ux/logo-library)
- **Improvement Plan:** [IMPROVEMENT_PLAN.md](https://github.com/ajmaliifthikar-ux/logo-library/blob/main/IMPROVEMENT_PLAN.md)

---

*Built by Mohamed Ajmal Ifthikar — Multimedia Executive | AI Content Creator | Graphic Designer, Dubai, UAE*
