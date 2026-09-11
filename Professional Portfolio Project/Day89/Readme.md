# ✅ Day 89: Todo List App

> _A clean, minimal task manager — add tasks, mark them done, delete them. No fluff._

---

## 🌐 What It Does

A Flask web app backed by SQLite that lets you manage a persistent todo list. Every task has a live status badge that flips from **In Progress** → **Finished** with one click.

---

## 🗺️ App Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Home — displays all tasks |
| `/add` | POST | Add a new task (status: `In Progress`) |
| `/finish?task_id=<id>` | POST | Mark a task as `Finished` |
| `/delete?task_id=<id>` | POST | Permanently remove a task |

---

## ✨ Features

| Feature | Details |
|---|---|
| ➕ Add Tasks | Type in the input field and hit **Save** |
| ✅ Finish Tasks | Green **Finished** button updates status in DB |
| 🗑️ Delete Tasks | Red **Delete** button removes task permanently |
| 💾 Persistence | SQLite database — tasks survive server restarts |
| 📱 Responsive UI | Bootstrap 5.3 card layout, centered on all screens |

---

## 🖥️ App Preview

```
┌──────────────────────────────────────────────────┐
│               ✅  To Do App                      │
│                                                  │
│   [ Enter a task here...        ] [ Save ]       │
│                                                  │
│  ┌────┬──────────────────┬────────────┬────────┐ │
│  │ No.│ Todo Item        │  Status    │Actions │ │
│  ├────┼──────────────────┼────────────┼────────┤ │
│  │ 1  │ Buy groceries    │ In Progress│[❌][✅]│ │
│  │ 2  │ Read a book      │ Finished   │[❌][✅]│ │
│  │ 3  │ Push to GitHub   │ In Progress│[❌][✅]│ │
│  └────┴──────────────────┴────────────┴────────┘ │
└──────────────────────────────────────────────────┘
```

---

## 🗃️ Database Model

```
TODOLIST
├── id      (Integer, PK)
├── task    (String, unique)
└── status  (String → "In Progress" | "Finished")
```

---

## 📦 Dependencies

```bash
pip install flask flask-sqlalchemy
```

---

## ▶️ Run It

```bash
python app.py
```

Visit `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
Day89/
├── app.py               ← Flask app, routes, SQLAlchemy model
├── instance/
│   └── todo.db          ← SQLite database
├── static/
│   └── styles.css       ← Custom styles
└── templates/
    └── index.html       ← Bootstrap 5 task table UI
```
