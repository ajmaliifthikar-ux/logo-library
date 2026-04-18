# 🎨 LogoLibrary

> The largest open-source collection of searchable brand logos and UI icons — with a built-in 3D Studio.

[![Live Explorer](https://img.shields.io/badge/Live%20Explorer-Vercel-%23000000?style=flat-square&logo=vercel)](https://logo-explorer.vercel.app)
[![3D Studio](https://img.shields.io/badge/3D%20Studio-Try%20Now-%23e94560?style=flat-square)](https://logo-explorer.vercel.app/studio)
[![GitHub Stars](https://img.shields.io/github/stars/ajmaliifthikar-ux/logo-library?style=flat-square&color=%23e94560)](https://github.com/ajmaliifthikar-ux/logo-library)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

---

## ✨ What is LogoLibrary?

A **professionally curated, auto-expanding** open-source collection of brand logos and UI icons. Unlike messy icon dumps, this library is:

- 🏷️ **Categorized by Industry** — Tech, Finance, Social, Design, and more
- 🔍 **Full-Text Searchable** — SQLite FTS5 + JSON metadata
- 🧊 **3D Studio** — Extrude any logo into interactive 3D with materials, animation, and lighting
- 📦 **Multiple Variants** — icon, wordmark, full, and default versions per brand
- ☁️ **CDN Ready** — Built-in Cloudinary sync scripts
- 🤖 **Auto-Expanding** — Paste a Figma URL, the pipeline does the rest

---

## 📸 Screenshots

### Explorer Dashboard
![Explorer](https://logo-explorer.vercel.app/assets/screenshots/explorer.png)
*Search 1,100+ brands instantly with category filtering and one-click copy.*

### 3D Studio
![Studio](https://logo-explorer.vercel.app/assets/screenshots/studio.png)
*Full control: materials, lighting, animation, camera, and background.*

### Logo Detail Modal
![Modal](https://logo-explorer.vercel.app/assets/screenshots/modal.png)
*Large preview, copy path/CDN/HTML, 3D preview with animation presets.*

---

## 🚀 Quick Start

### Browse the Library
```bash
# Explore live
open https://logo-explorer.vercel.app
```

### Use in Your Project
```html
<!-- Local -->
<img src="Assets/Technology_and_Development/vercel/vercel-icon.svg" />

<!-- Cloudinary CDN -->
<img src="https://res.cloudinary.com/dldf3xftp/image/upload/logo_library/Technology_and_Development/vercel/vercel-icon" />
```

### Search via JSON
```js
const metadata = require('./metadata.json');
const payments = Object.entries(metadata)
  .filter(([_, b]) => b.tags.includes('payment'));
```

### Search via SQLite
```bash
sqlite3 library_index.db
```
```sql
SELECT brand_name, path FROM logos_fts
WHERE logos_fts MATCH 'video OR messaging';
```

---

## 🛠 3D Studio Features

The [3D Studio](https://logo-explorer.vercel.app/studio) lets you turn any SVG logo into an interactive 3D object:

| Feature | Control |
|---------|---------|
| **Depth** | Extrusion thickness (0.1 – 3.0) |
| **Smoothness** | Edge bevel/roundness |
| **Materials** | Plastic, metal, glass, rubber, chrome, gold, clay, emissive, holographic |
| **Color Tint** | Override or accent the logo color |
| **Metalness / Roughness** | PBR material control |
| **Wireframe** | Toggle mesh view |
| **Animations** | Spin, float, pulse, wobble, spinFloat, swing |
| **Camera** | Zoom, FOV, tilt X/Y |
| **Reset on Idle** | Returns to default angle after inactivity |
| **Lighting** | Key light + ambient intensity |
| **Shadows** | Contact shadows on/off |
| **Background** | 10 presets including transparent |
| **Intro** | Cinematic zoom, fade, or none |
| **Texture** | Map any image URL onto the 3D surface |
| **Upload** | Drop any `.svg` file |

---

## 🤖 Auto-Pipeline

Drop a Figma community file URL into `figma_queue.txt` and run:

```bash
python3 logo_pipeline.py start
```

This background process will:
1. Extract SVGs from Figma
2. Organize into categories
3. Update `metadata.json` + SQLite index
4. Auto-commit to git
5. Sync to Cloudinary CDN

```bash
python3 logo_pipeline.py status   # Check health
python3 logo_pipeline.py logs     # Live tail all logs
python3 logo_pipeline.py stop     # Stop everything
python3 logo_pipeline.py restart  # Restart
```

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| Brands | 1,147+ |
| Total Assets | 3,128+ |
| Categories | 9 |
| Source Formats | SVG, PNG |

---

## 📁 Repository Structure

```
Logo_Library/
├── Assets/                      # Core library by category
├── metadata.json                # Full JSON manifest
├── library_index.db             # SQLite FTS5 search index
├── cloudinary_sync.py           # CDN upload script
├── logo_pipeline.py             # Auto-pipeline orchestrator
├── IMPROVEMENT_PLAN.md          # Roadmap
└── README.md

logo-explorer/                   # Next.js web dashboard
├── src/app/
│   ├── page.tsx                 # Explorer
│   └── studio/page.tsx          # 3D Studio
├── public/assets/               # Logo files
└── README.md
```

---

## 🤝 Contributing

1. Fork the repo
2. Add your SVGs to the appropriate `Assets/` category
3. Run the indexing script to update metadata
4. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## ⚖️ License

MIT — see [LICENSE](LICENSE). Brand logos are trademarks of their respective owners. This library is for educational and reference purposes.

---

Built with ❤️ by [Mohamed Ajmal Ifthikar](https://github.com/ajmaliifthikar-ux)
