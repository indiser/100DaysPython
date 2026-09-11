# 🔬 Day 93: ArXiv Paper Scraper

> _Batch-scrape 2000+ cutting-edge AI research papers from ArXiv in one run._

---

## 💡 The Concept

A production-grade web scraper that harvests the latest **cs.AI** papers from ArXiv in batches of 250, extracting rich metadata for each paper — title, authors, subjects, and all available format links — then dumps everything into a structured JSON database.

---

## 🔄 Pipeline

```
arxiv.org/list/cs.AI/recent
         │
         ▼
  Batch Request (skip=0, show=250)
         │
         ▼
  BeautifulSoup HTML Parsing
         │
    ┌────┴────┐
    dt tags   dd tags
  (links)   (metadata)
    └────┬────┘
         ▼
  Per-paper extraction:
  ├── Paper Number  (arXiv ID)
  ├── Title
  ├── Authors       (list)
  ├── Subjects      (list)
  ├── Direct Link   (abstract page)
  ├── PDF Link
  ├── HTML Link
  └── Other Formats
         │
         ▼
  Random delay (2–5s) ──► Next batch
         │
         ▼
  📄 Paper_data.json  (2000+ entries)
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 📦 Batch Scraping | 250 papers per request, 8 batches = 2000+ papers |
| 🔗 Full Link Set | PDF · HTML · Abstract · Other Formats per paper |
| 👥 Author Extraction | Full author list per paper |
| 🏷️ Subject Tags | All subject categories, split into clean list |
| ⏱️ Rate Limiting | Random 2–5s delay between batches (polite scraping) |
| 🛡️ Error Handling | Try/except per batch — partial data saved on failure |
| 💾 JSON Export | Structured output with `indent=4`, UTF-8 encoded |
| 🧠 Browser Spoofing | Chrome User-Agent header to avoid bot detection |

---

## 📄 Output Format

Each paper entry in `Paper_data.json` looks like:

```json
{
    "Paper Number": "arXiv:2506.12345",
    "Paper Title": "Self-Adapting Language Models via Reinforcement Learning",
    "Direct Link": "https://arxiv.org/abs/2506.12345",
    "Pdf Link": "https://arxiv.org/pdf/2506.12345",
    "Html Link": "https://arxiv.org/html/2506.12345",
    "Other Formats": "https://arxiv.org/format/2506.12345",
    "Authors": ["Alice Smith", "Bob Zhang", "Carol Lee"],
    "Subjects": ["Artificial Intelligence (cs.AI)", "Machine Learning (cs.LG)"]
}
```

---

## ⚙️ Configuration

```python
total_papers_needed = 2000   # Total target
batch_size          = 250    # Papers per request
base_url = "https://arxiv.org/list/cs.AI/recent"
```

Change `cs.AI` to any ArXiv category (e.g. `cs.LG`, `cs.CV`, `stat.ML`).

---

## 📦 Dependencies

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Run It

```bash
python scraper.py
```

Progress is printed per batch:
```
Scraping papers 0 to 250...
Batch complete. Total collected so far: 247
Scraping papers 250 to 500...
...
Done. Successfully caught 2000 Papers.
```

---

## 📁 Files

| File | Description |
|---|---|
| `scraper.py` | Full scraper — batching, parsing, rate limiting, export |
| `Paper_data.json` | Output database of 2000+ scraped papers |
