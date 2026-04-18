# 🎨 LogoLibrary

> A professionally curated, auto-expanding open-source collection of brand logos and UI icons.

**Live Explorer:** [your-vercel-url.vercel.app](https://your-vercel-url.vercel.app)  
**Core Repo:** [github.com/ajmalifthikar/logo-library](https://github.com/ajmaliifthikar-ux/logo-library)

---

## 🚀 What's Inside

- **1,135+ brand logos** across 9 categories
- **1,877+ asset files** (SVG + PNG variants)
- **Instant search** by name, tag, or category
- **One-click copy** — local path or Cloudinary CDN URL
- **Auto-expanding** — paste a Figma URL, the pipeline does the rest

---

## 📁 Repositories

| Repo | Purpose | Tech |
|------|---------|------|
| [`logo-library`](./Logo_Library) | Core assets, metadata, SQLite index | Python, SQLite |
| [`logo-library-web`](./logo-explorer) | Searchable web dashboard | Next.js 16, Tailwind |

---

## 🛠 Quick Start

```bash
# 1. Clone
git clone https://github.com/ajmaliifthikar-ux/logo-library.git
cd logo-library

# 2. Install explorer deps
cd logo-explorer && npm install && npm run dev

# 3. Open http://localhost:3000
```

---

## 🤖 Auto-Pipeline

Drop a Figma community file URL into `figma_queue.txt` (or copy it to your clipboard) and run:

```bash
python3 logo_pipeline.py --daemon
```

This background process will:
1. Extract SVGs from Figma
2. Organize into categories
3. Update `metadata.json` + SQLite index
4. Auto-commit to git
5. Sync to Cloudinary CDN

---

## 📊 Pipeline Commands

```bash
# Check what's running
python3 logo_pipeline.py --status

# Run full pipeline once
python3 logo_pipeline.py --all

# Stop all background tasks
python3 logo_pipeline.py --stop

# Rebuild metadata + search index only
python3 logo_pipeline.py --index
```

---

## 🌍 Deploy

```bash
# Deploy everything (GitHub + Vercel)
./launch.sh ajmalifthikar
```

---

## 📜 License

MIT — see [LICENSE](./Logo_Library/LICENSE). Brand logos are trademarks of their respective owners.

Built by [Mohamed Ajmal Ifthikar](https://github.com/ajmalifthikar)
