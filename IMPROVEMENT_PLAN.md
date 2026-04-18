# LogoLibrary — Improvement Plan

> Open-source brand logo library. Current status: 1,147 brands, 3,128 assets, live at [logo-explorer.vercel.app](https://logo-explorer.vercel.app)

---

## ✅ Completed (Apr 2026)

| Feature | Status |
|---------|--------|
| Core library with 1,100+ logos | ✅ |
| Searchable web explorer | ✅ |
| SQLite + JSON metadata index | ✅ |
| Cloudinary CDN sync | ✅ |
| Auto-pipeline (Figma → Git → CDN) | ✅ |
| Dark mode UI | ✅ |
| 3D preview with animation presets | ✅ |
| 3D Studio (full control) | ✅ |
| Copy with attribution | ✅ |
| Star & Share buttons | ✅ |

---

## 🔧 Immediate Improvements (Next 1-2 Weeks)

### 1. 3D Engine Quality
**Problem:** The current 3D extrusion via `3dsvg` doesn't produce true 3D logos — it's a flat extrude with limited depth realism.

**Reference Repos Analyzed:**
- `renatoworks/3dsvg` — Full editor with materials, lighting, animation, export
- `its-arun/svg-to-3d` — Simple Three.js extrusion to GLTF/STL

**Action Items:**
- [ ] Add **GLTF/STL export** from the Studio (using Three.js directly like svg-to-3d)
- [ ] Add **video export** (screen recording the 3D canvas)
- [ ] Add **image export** with transparent background option
- [ ] Improve **SVG path parsing** — complex paths with holes, gradients, and clipping paths fail
- [ ] Add **beveled edges** option for more realistic 3D look
- [ ] Add **environment map** support for realistic metal/glass reflections

### 2. Studio Enhancements
- [ ] **Text-to-3D** input (type any text, render as 3D logo)
- [ ] **Pixel editor** (draw simple logos, extrude to 3D)
- [ ] **Embed code generator** (copy-paste snippet for blogs/websites)
- [ ] **Preset gallery** (save/load favorite 3D configurations)
- [ ] **Undo/redo** in Studio

### 3. Library Growth
- [ ] Re-categorize 926 "Other / Uncategorized" brands into proper categories
- [ ] Add **batch Figma processing** with better rate-limit handling
- [ ] Add **duplicate detection** (same logo in multiple sources)
- [ ] Add **SVG optimization** (svgo cleanup before storing)

---

## 🚀 Medium-Term (1-2 Months)

### 4. API & Developer Experience
- [ ] REST API endpoint for logo search
- [ ] NPM package (`@ajmallibrary/logos`) for React/Vue/Angular
- [ ] Figma plugin (search & insert logos directly in Figma)
- [ ] CLI tool (`npx logolibrary search <brand>`)

### 5. Community Features
- [ ] User submissions (upload + moderation queue)
- [ ] Collections/folders (users save favorite sets)
- [ ] Rating system per logo
- [ ] Contribution leaderboard

### 6. Monetization (Optional)
- [ ] Pro tier: HD exports, batch downloads, API access
- [ ] Sponsored placements (brands pay to be featured)

---

## 📋 Technical Debt

| Issue | Priority |
|-------|----------|
| Pipeline zombie processes | High |
| Metadata category accuracy | High |
| Cloudinary sync manifest | Medium |
| GitHub Actions auto-deploy | Medium |
| Test coverage | Low |

---

## 🎯 Success Metrics

- 5,000+ GitHub stars
- 100+ daily active users on explorer
- 50+ community contributions
- Featured on Product Hunt / Hacker News

---

Maintained by [Mohamed Ajmal Ifthikar](https://github.com/ajmaliifthikar-ux)
