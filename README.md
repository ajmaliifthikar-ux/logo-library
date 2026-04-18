# 🎨 Pro Logo & UI Icon Library (Open Source)

A high-quality, professionally categorized collection of over **10,000+ brand logos and UI icons**. Optimized for developers and designers.

## 🚀 Features
- **1,800+ Brand Logos:** Categorized by industry (Tech, Finance, Social, etc.).
- **7,000+ UI Icons:** Uniformly structured SVG icons from top-tier community packs.
- **Search-Optimized:** Includes a SQLite database (`library_index.db`) and `metadata.json` with industry tags.
- **Developer-First:** All assets are in clean, optimized SVG format with `kebab-case` naming.
- **Cloudinary CDN Sync:** Built-in scripts to sync the entire library to your own CDN.

## 📂 Structure
- `Assets/` - The core library grouped by `Category > Brand/Set`.
- `library_index.db` - SQLite database with Full-Text Search (FTS5) for instant asset lookup.
- `metadata.json` - Complete JSON manifest with search tags.

## 🔍 How to Search
You can search locally using the index file or via SQL:
```sql
SELECT brand, file_path FROM logos_fts WHERE logos_fts MATCH 'video OR messaging';
```

## 🤝 Contributing
This is a community-driven project. To add new logos:
1. Fork the repo.
2. Add your SVGs to the appropriate category in `Assets/`.
3. Run the indexing script to update the DB.
4. Open a Pull Request.

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. *Note: Brand logos are trademarks of their respective owners.*
