# 🎧 Day 91: PDF to Audiobook Converter

> _Turn any research paper into a listenable audiobook — powered by AI text-to-speech._

---

## 💡 The Concept

Feed it a PDF. Get back a full-length `.wav` audiobook. This project converts academic papers (or any PDF) into natural-sounding audio using the **Kokoro TTS** model — a high-quality, open-source neural text-to-speech engine.

The test subject? A NeurIPS 2025 paper on **Self-Adapting LLMs (SEAL)** — a framework where language models generate their own training data via reinforcement learning.

---

## 🔄 Pipeline

```
📄 PDF File
    │
    ▼
pymupdf4llm ──► Converts PDF pages → Markdown
    │
    ▼
mdclense / MarkdownParser ──► Strips markdown syntax → Clean plain text
    │
    ▼
Kokoro TTS (KPipeline) ──► Streams text → Audio chunks
    │
    ▼
soundfile (SoundFile) ──► Writes chunks to disk in real-time
    │
    ▼
🎵 final_audiobook.wav / .mp3
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 📄 PDF Parsing | `pymupdf4llm` extracts structured Markdown from any PDF |
| 🧹 Text Cleaning | `mdclense` strips headers, code blocks, and markdown syntax |
| 🗣️ Neural TTS | Kokoro `af_heart` voice — natural American English |
| 📡 Streaming Output | Audio written chunk-by-chunk — no RAM overflow on long docs |
| 🎵 WAV Export | 24kHz mono WAV, compatible with any audio player |
| ☁️ Google Colab | Runs on free T4 GPU for fast inference |

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| `pymupdf4llm` | PDF → Markdown extraction |
| `mdclense` | Markdown → plain text cleaning |
| `kokoro` | Neural text-to-speech (Kokoro-82M model) |
| `soundfile` | Streaming WAV file writer |
| `torch` | Model inference backend |

---

## 📦 Dependencies

```bash
pip install pymupdf4llm mdclense kokoro soundfile
apt-get install espeak-ng   # Required by Kokoro phonemizer
```

---

## ▶️ Run It

**Option 1 — Jupyter Notebook (Colab recommended):**
```
Open pdftoaudiobook.ipynb in Google Colab (T4 GPU)
Upload your PDF and run all cells
```

**Option 2 — Local script:**
```bash
python testrun.py   # Extracts and prints clean text from PDF
```

---

## 📁 Files

| File | Description |
|---|---|
| `pdftoaudiobook.ipynb` | Full pipeline — PDF → text → audio (Colab) |
| `testrun.py` | Local PDF text extraction test |
| `Self_improving_LLM.pdf` | Sample input — SEAL paper (NeurIPS 2025) |
| `AudioBook/final_audiobook.wav` | Generated audiobook output (WAV) |
| `AudioBook/final_audiobook.mp3` | Generated audiobook output (MP3) |
