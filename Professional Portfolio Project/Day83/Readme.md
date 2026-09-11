# Day 83: Portfolio Website

## 📌 Project Overview
A personal portfolio website built with Flask, featuring a contact form that sends emails via SMTP. Includes a dark/light mode toggle and showcases projects with images and GitHub links.

## 🚀 Features
- **Home** - Profile intro section
- **Work** - Skills overview (Automation, Web Dev, Data & APIs)
- **Portfolio** - 6 project cards with images and GitHub links
- **Contact Form** - Sends formatted email to owner via Gmail SMTP
- **Dark/Light Mode** - Toggle with `localStorage` persistence
- **Input Sanitization** - Strips newlines from form fields to prevent header injection

## 🛠️ Tech Stack
- Flask (routing, templating)
- Jinja2 (template rendering, success message)
- SMTP / Gmail (contact form emails)
- Custom CSS + FontAwesome icons
- Vanilla JS (dark mode toggle)

## 📦 Dependencies
```
flask
python-dotenv
```

## ⚙️ Setup
Create a `.env` file:
```
EMAIL=your_gmail@gmail.com
EMAIL_APP_PASS=your_app_password
```

## ▶️ Usage
```bash
python app.py
```
Visit `http://127.0.0.1:5000`

## 📁 Files
| File | Description |
|------|-------------|
| `app.py` | Flask app with routes and email logic |
| `templates/index.html` | Single-page portfolio template |
| `static/css/main.css` | Stylesheet |
| `static/images/` | Project screenshots and profile photo |
| `.env` | Email credentials (not committed) |
