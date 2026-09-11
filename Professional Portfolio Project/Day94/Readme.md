# 🦕 Day 94: Chrome Dino Bot

> _A computer vision bot that plays the Chrome Dino game forever — no human required._

---

## 💡 The Concept

No internet? No problem — and no hands needed either. This bot captures the screen in real-time, scans specific pixel rows for obstacles, and fires the correct keypress in milliseconds. It distinguishes between **flying birds** (duck) and **ground cacti** (jump) using raw pixel brightness detection.

---

## 🧠 How It Sees

The game runs in grayscale. The bot scans two horizontal scan lines ahead of the dino:

```
Screen (grayscale)
│
│   🦕 ──────────────────────────────────────────►
│                        │              │
│                   y=271-273      y=305-308
│                  (Bird zone)   (Cactus zone)
│                        │              │
│              x: 720─850        x: 720─820
│
▼
If pixel brightness > 100 in bird zone  → press DOWN (duck)
If pixel brightness > 100 in cactus zone → press UP  (jump)
```

---

## 🔄 Bot Loop

```
3 second delay (time to focus browser)
        │
        ▼
Press SPACE ──► Start game
        │
        ▼
┌──────────────────────────────┐
│  Grab full screen (PIL)      │  ◄──┐
│  Convert to Grayscale        │     │
│  Load pixel data             │     │
│  Scan bird zone (y=271-273)  │     │
│    → brightness > 100? DUCK  │     │
│  Scan cactus zone (y=305-308)│     │
│    → brightness > 100? JUMP  │     │
└──────────────────────────────┘     │
        │                            │
        └────────────────────────────┘
              (infinite loop)
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 👁️ Real-Time Vision | Full screen captured every frame via `PIL.ImageGrab` |
| 🎯 Pixel Detection | Scans hardcoded scan lines for brightness spikes |
| 🐦 Bird Detection | Detects flying pterodactyls at y=271–273 → ducks |
| 🌵 Cactus Detection | Detects ground cacti at y=305–308 → jumps |
| ⚡ Zero Latency | No ML model — pure pixel math, instant reaction |
| ⌨️ PyAutoGUI Control | Sends `UP` / `DOWN` keypresses directly to the OS |
| 🕒 Startup Delay | 3-second window to alt-tab into the browser |

---

## ⚙️ Detection Logic

```python
# Bird — duck under it
for i in range(720, 850):
    for j in range(271, 273):
        if data[i, j] > 100:      # bright pixel = obstacle
            gui.press("down")

# Cactus — jump over it
for i in range(720, 820):
    for j in range(305, 308):
        if data[i, j] > 100:
            gui.press("up")
```

> Pixel coordinates are calibrated for a **1920×1080** display with the Chrome Dino game open in the browser.

---

## 📦 Dependencies

```bash
pip install pyautogui pillow
```

---

## ▶️ Run It

1. Open Chrome → go to `chrome://dino` (or disconnect internet)
2. Run the script:
```bash
python dinobot.py
```
3. Switch to the Chrome window within **3 seconds**
4. Watch the dino play forever 🦕

---

## 📁 Files

| File | Description |
|---|---|
| `dinobot.py` | Main bot — screen capture, pixel scan, keypress loop |
| `quads.py` | Helper script for screenshot capture & coordinate testing |
| `screenshot.png` / `screenshot2.png` / `screenshot3.png` | Calibration screenshots used to find pixel coordinates |
