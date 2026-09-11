# 🎨 Day 92: Color Palette Generator

> _Drop in an image. Get back its soul — the dominant colors that define it._

---

## 💡 The Concept

Every image has a hidden color story. This tool extracts the **top 10 dominant colors** from any image, converts them to HEX codes, and renders a beautiful visual palette strip — plus an inverted version of the original image for fun.

---

## 🔄 Pipeline

```
🖼️ Input Image (PNG/JPG)
      │
      ▼
PIL resize → 150×150  (fast processing)
      │
      ▼
NumPy reshape → flat pixel array  [N × 3]
      │
      ▼
np.unique → count every unique RGB color
      │
      ▼
Sort by frequency → Top 10 dominant colors
      │
      ▼
RGB → HEX conversion
      │
      ▼
┌─────────────────────────────────────────┐
│  Matplotlib palette strip with HEX labels│
└─────────────────────────────────────────┘
      +
🔄 Inverted image saved to disk
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎨 Dominant Colors | Extracts top 10 most frequent RGB colors |
| 🔢 HEX Codes | Converts every color to `#RRGGBB` format |
| 🖼️ Visual Palette | Matplotlib color strip with labels overlaid |
| 🔆 Smart Text | Label color auto-switches black/white based on brightness |
| 🔄 Color Inversion | Saves a pixel-inverted version of the image (`255 - RGB`) |
| ⚡ Fast Processing | Image resized to 150×150 before analysis for speed |

---

## 🖥️ Output Preview

```
┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
│      │      │      │      │      │      │      │      │      │      │
│1a2b3c│ff8c42│e2d9c5│3d5a80│98c1d9│ffffff│2b2d42│ef233c│8d99ae│d90429│
│      │      │      │      │      │      │      │      │      │      │
└──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
              Dominant Color Palette
```

---

## 🛠️ How It Works

```python
# 1. Load & resize for speed
img = Image.open(path).resize((150, 150))

# 2. Flatten to pixel list
pixels = np.array(img).reshape(-1, 3)

# 3. Count unique colors, sort by frequency
unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
top_colors = unique_colors[np.argsort(counts)[::-1]][:10]

# 4. Convert to HEX
hex_code = '%02x%02x%02x' % (r, g, b)

# 5. Invert
inverted = 255 - np.array(img)
```

---

## 📦 Dependencies

```bash
pip install pillow numpy matplotlib
```

---

## ▶️ Run It

```bash
python colorpalette.py
```

Outputs:
- Palette strip displayed via Matplotlib
- `Inverted.png` saved to the same directory
- RGB and HEX values printed to console

---

## 📁 Files

| File | Description |
|---|---|
| `colorpalette.py` | Main script — extraction, inversion, visualization |
| `Gemini_Generated_Image_7omm3k7omm3k7omm.png` | Sample input image |
| `Inverted.png` | Color-inverted output image |
