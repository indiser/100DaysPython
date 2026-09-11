# ☕ Day 88: Cafe Finder Website

> _A full-stack cafe directory — find your perfect work spot with WiFi, sockets, and good vibes._

---

## 🌐 What It Does

A Flask web app that lets you browse, add, and delete cafes from a persistent SQLite database. Each cafe entry tracks all the amenities that matter to remote workers.

---

## 🗺️ App Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Landing / home page |
| `/listings` | GET | Browse all cafes in a table |
| `/add` | GET, POST | Submit a new cafe via form |
| `/delete/<id>` | POST | Remove a cafe from the database |
| `/styles_listing` | GET | Style reference page |

---

## ✨ Features

| Feature | Details |
|---|---|
| 📋 Cafe Listings | Dark-themed Bootstrap table with all cafe details |
| ➕ Add Cafe | Flask-WTF validated form with CSRF protection |
| 🗑️ Delete Cafe | One-click delete with flash confirmation message |
| 🔗 Map Links | Clickable Google Maps URL per cafe |
| ✅ Amenity Flags | WiFi · Sockets · Toilets · Can Take Calls |
| 💾 Persistence | SQLite database via SQLAlchemy ORM |
| 📱 Responsive | Bootstrap 5 layout — works on all screen sizes |

---

## 🗃️ Database Model

```
Cafe
├── id            (Integer, PK)
├── name          (String, unique)
├── location      (String)
├── map_url       (String)
├── seats         (String)
├── has_wifi      (Boolean)
├── has_sockets   (Boolean)
├── has_toilet    (Boolean)
└── can_take_calls (Boolean)
```

---

## 🖥️ Page Preview

```
┌──────────────────────────────────────────────────────────┐
│  Cafe Info                                               │
│  ┌────────┬──────────┬──────┬──────┬────────┬────────┐  │
│  │ Name   │ Location │Seats │ WiFi │Sockets │ Action │  │
│  ├────────┼──────────┼──────┼──────┼────────┼────────┤  │
│  │ Brews  │ London   │  40  │ Yes  │  Yes   │[Delete]│  │
│  │ Grind  │ Shoreditch│ 20  │ Yes  │  No    │[Delete]│  │
│  └────────┴──────────┴──────┴──────┴────────┴────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

## 📦 Dependencies

```bash
pip install flask flask-sqlalchemy flask-wtf flask-bootstrap
```

---

## ▶️ Run It

```bash
python app.py
```

Then visit `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
Day88/
├── app.py                ← Flask app, routes, DB model, WTForms
├── instance/
│   └── cafes.db          ← SQLite database
└── templates/
    ├── index.html        ← Home page
    ├── list.html         ← All cafes table
    ├── add.html          ← Add cafe form
    └── styles.html       ← Style reference
```
