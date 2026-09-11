# ⌨️ Day 86: Typing Speed Test

> _How fast are your fingers? Find out in seconds._

---

## 🎯 What It Does

A clean Tkinter GUI app that challenges you to type a randomly generated word as fast as possible. Hit **Enter** and instantly see your time — or get called out for a typo.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎲 Random Words | 50-word pool generated fresh each session via `Faker` |
| ⏱️ Precision Timing | Uses `timeit.default_timer` for accurate millisecond timing |
| ✅ Instant Feedback | Correct → shows elapsed time / Wrong → clears and retries |
| ⌨️ Enter to Submit | No button clicking — just type and press `Enter` |
| 🔁 Infinite Practice | Hit Start anytime for a new word |

---

## 🖥️ App Preview

```
┌─────────────────────────────────────┐
│   Type the word shown below:        │
│                                     │
│         [ computer ]                │
│                                     │
│   Press 'Enter' to check your time  │
│   ┌─────────────────────────┐       │
│   │ computer                │       │
│   └─────────────────────────┘       │
│                                     │
│          [ Start ]                  │
│                                     │
│   ✅ Correct! Time: 1.42 seconds    │
└─────────────────────────────────────┘
```

---

## 📦 Dependencies

```bash
pip install faker
```

---

## ▶️ Run It

```bash
python TypingSpeed.py
```

1. Click **Start** — a random word appears in blue
2. Type it in the input box
3. Press **Enter** — see your time instantly

---

## 📁 Files

| File | Description |
|---|---|
| `TypingSpeed.py` | Complete app — UI, timing logic, word generation |
