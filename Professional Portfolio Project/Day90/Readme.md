# 🖊️ Day 90: Disappearing Text Editor

> _Write or lose it. Every keystroke resets the clock — stop typing for 10 seconds and your words vanish forever._

---

## 💡 The Concept

Inspired by the "write or die" productivity technique — this editor **deletes everything** if you go idle for more than **10 seconds**. It forces you to keep writing without second-guessing yourself.

---

## ✨ Features

| Feature | Details |
|---|---|
| ⏳ Auto-Delete Timer | 10-second idle countdown resets on every keystroke |
| 🔄 Timer Reset | Each keypress cancels and restarts the countdown |
| ⌫ Backspace Tracking | Correctly tracks deletions in the internal buffer |
| 💾 Save Functionality | Saves content to a `.txt` file named from first 5 characters |
| 🎨 Modern UI | `ttkbootstrap` **Superhero** dark theme |
| ⚠️ Error Handling | Shows info/error dialogs on save success or failure |

---

## 🖥️ App Preview

```
┌──────────────────────────────────────────────────┐
│                                                  │
│       WRITE WITH DISAPPEARING INK.               │
│                                                  │
│   Text will disappear if idle for 10 seconds...  │
│                                                  │
│  ┌────────────────────────────────────────────┐  │
│  │ The quick brown fox jumps over the lazy    │  │
│  │ dog and then...                            │  │
│  │                                            │  │
│  │                          ⏳ 10s countdown  │  │
│  └────────────────────────────────────────────┘  │
│                                                  │
│  [              Save              ]              │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## ⚙️ How It Works

```
Keystroke detected
      │
      ▼
Cancel existing timer ──► Restart 10s countdown
      │
      ▼
Still typing? → Timer keeps resetting ✅
      │
Idle for 10s?
      │
      ▼
💥 All text deleted — editor wiped clean
```

---

## 💾 Save Behaviour

- Click **Save** at any time to rescue your writing
- File is saved as `<first 5 chars of text>.txt` in the same directory
- Timer is cancelled and editor is cleared after saving

---

## 📦 Dependencies

```bash
pip install ttkbootstrap
```

---

## ▶️ Run It

```bash
python disapperingText.py
```

---

## 📁 Files

| File | Description |
|---|---|
| `disapperingText.py` | Complete app — UI, timer logic, save functionality |
| `*.txt` | Output files saved from the editor |
