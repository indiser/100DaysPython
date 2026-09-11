# 🎮 Day 87: Pygame Arcade Games

> _Two games built from scratch with Pygame — a classic Breakout and a side-scrolling runner._

---

## 🕹️ Game 1 — Breakout (`breakout.py`)

Smash through **80 bricks** across 10 rows using a mouse-controlled paddle and a bouncing ball. Clear the board to win.

```
┌──────────────────────────────────────┐
│  🟦🟥🟩🟧🟪🟦🟥🟩🟧🟪  (Row 1)   │
│  🟥🟩🟧🟪🟦🟥🟩🟧🟪🟦  (Row 2)   │
│  ...  10 rows × 8 cols = 80 bricks   │
│                                      │
│            ● (ball)                  │
│                                      │
│         ══════ (paddle)              │
└──────────────────────────────────────┘
```

### ✨ Features
| Feature | Details |
|---|---|
| 🖱️ Mouse Control | Paddle follows mouse X position |
| 🎨 Colored Bricks | 5 random brick colors per session |
| 🔊 Sound Effects | Distinct sounds for brick hits & paddle bounces |
| 🎵 Background Music | Looping pixel music via `pygame.mixer` |
| 🏆 Win / Lose Screen | Victory on all bricks cleared, Game Over on ball drop |
| 🔁 Restart | Press `SPACE` to replay |

---

## 🏃 Game 2 — Pixel Runner (`test.py`)

An endless side-scrolling runner. Jump over snails and dodge flying flies — survive as long as you can.

```
  Score: 42
 ┌────────────────────────────────────┐
 │  🌤️  Sky                           │
 │                    🪰  (fly)       │
 │  🧍 (player)                       │
 │──────────────────────────────────  │
 │  🐌 (snail)          ground        │
 └────────────────────────────────────┘
       Press SPACE to jump!
```

### ✨ Features
| Feature | Details |
|---|---|
| ⌨️ Space to Jump | Gravity-based jump with landing detection |
| 🐌 Snail Obstacle | Ground-level animated enemy |
| 🪰 Fly Obstacle | Aerial animated enemy — duck or jump over |
| ⏱️ Score System | Time-based score (seconds survived) |
| 🎬 Sprite Animation | Walk cycle + jump frame for player |
| 🔊 Jump Sound | Audio feedback on jump |
| 🔁 Restart | Press `SPACE` on game over screen |

---

## 📦 Dependencies

```bash
pip install pygame
```

---

## ▶️ Run It

```bash
# Breakout
python breakout.py

# Pixel Runner
python test.py
```

---

## 📁 Project Structure

```
Day87/
├── breakout.py          ← Breakout game
├── test.py              ← Pixel Runner game
├── Balls/               ← Ball sprites (Glass, Glossy, Shiny)
├── Bricks/              ← Brick sprites (Colored, Textured)
├── Paddles/             ← Paddle sprites (Style A/B/C)
├── graphics/            ← Player, snail, fly, sky, ground
├── audio/               ← Jump & background music
├── breakout_audio/      ← Brick hit & paddle hit sounds
└── font/                ← Pixeltype.ttf pixel font
```
