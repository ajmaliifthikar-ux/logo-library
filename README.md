# 🎨 LogoLibrary

> A professionally curated, open-source collection of **1,100+ brand logos and UI icons** — searchable, categorized, and production-ready.

[![Vercel](https://img.shields.io/badge/Live%20Demo-Vercel-%23e94560?style=flat-square&logo=vercel)](https://your-vercel-url.vercel.app)
[![GitHub Stars](https://img.shields.io/github/stars/YOUR_USERNAME/logo-library?style=flat-square&color=%23e94560)](https://github.com/YOUR_USERNAME/logo-library)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

---

## ✨ Why LogoLibrary?

Most logo/icon collections are messy dumps. This one is different:

- 🏷️ **Categorized by Industry** — Tech, Finance, Social, Design, and more
- 🔍 **Full-Text Searchable** — SQLite FTS5 + JSON metadata
- 📦 **Multiple Variants** — icon, wordmark, full, and default versions per brand
- ☁️ **CDN Ready** — Built-in Cloudinary sync scripts
- 🤖 **Auto-Expanding** — Add new Figma files and the pipeline extracts + organizes automatically
- ⚡ **Developer First** — Clean SVGs, kebab-case naming, copy-ready paths

---

## 📂 Repository Structure

```
Logo_Library/
├── Assets/                      # Core library by category
│   ├── Browsers_and_OS/
│   ├── Business_and_Finance/
│   ├── Design_and_Creative/
│   ├── Social_and_Communication/
│   ├── Technology_and_Development/
│   └── ...
├── metadata.json                # Full JSON manifest for API usage
├── library_index.db             # SQLite FTS5 search index
├── cloudinary_sync.py           # Upload script to Cloudinary CDN
└── README.md
```

---

## 🚀 Quick Start

### Search via JSON
```js
const metadata = require('./metadata.json');

// Find all brands tagged with "payment"
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

### Use in your project
```html
<!-- Local -->
<img src="Assets/Technology_and_Development/vercel/vercel-icon.svg" />

<!-- Cloudinary CDN -->
<img src="https://res.cloudinary.com/dldf3xftp/image/upload/logo_library/Technology_and_Development/vercel/vercel-icon" />
```

---

## 🛠 Auto-Expanding the Library

Found a new Figma community file with icons? Just copy the Figma URL to your clipboard. The background pipeline handles the rest:

1. **Clipboard Listener** detects the Figma URL
2. **Extractor** downloads all SVGs via Figma API
3. **Organizer** sorts assets into categories
4. **Indexer** updates `metadata.json` + SQLite DB
5. **Sync** uploads to Cloudinary CDN
6. **Git** auto-commits new assets

To start the pipeline:
```bash
python3 master_processor.py &
python3 master_queue_processor.py &
./cloudinary_sync.sh &
```

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| Brands | 1,135+ |
| Total Assets | 1,877+ |
| Categories | 9 |
| Source Formats | SVG, PNG |

---

## 🤝 Contributing

1. Fork the repo
2. Add your SVGs to the appropriate `Assets/` category
3. Run the indexing script to update metadata
4. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## ⚖️ License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE).

> **Note:** Brand logos are trademarks of their respective owners. This library is for educational and reference purposes.

---

Built with ❤️ by [Mohamed Ajmal Ifthikar](https://github.com/YOUR_USERNAME)
