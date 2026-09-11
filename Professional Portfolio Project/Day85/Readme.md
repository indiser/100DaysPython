# Day 85: Image Watermarking Tool

## 📌 Project Overview
A Tkinter GUI app that lets you open an image, click to place a text watermark anywhere on it, preview the result, and save the full-resolution watermarked image.

## 🚀 Features
- **File Upload** - Opens JPG/PNG via file dialog
- **Click-to-Place** - Click anywhere on the preview to position the watermark
- **Custom Text** - Enter any watermark text via toolbar input
- **Random Font** - Randomly selects a `.ttf` font from `C:/Windows/Fonts`
- **High-Res Save** - Saves watermark at full original resolution (coordinates scaled back from preview)
- **Preview Panel** - Live preview updates on every click

## 🛠️ How It Works
1. Upload screen → select image file
2. Editor opens with a 600px-wide preview of the image
3. Type watermark text in the toolbar, click on the image to place it
4. Hit "Save Image" → file dialog to choose output path → saves full-res PNG/JPG

## 📦 Dependencies
```
Pillow
```

## ▶️ Usage
```bash
python image_watermarking.py
```

## 📁 Files
| File | Description |
|------|-------------|
| `image_watermarking.py` | Main GUI application |
| `puppy.jpg` / `pups.png` | Sample input images |
| `watermarked_puppy.jpg` | Sample output |
