# 🎌 Day 96: Manga Website

> **Part of 100 Days of Python Challenge - Professional Portfolio Projects (Days 82-100)**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Day 96/100](https://img.shields.io/badge/Day-96%2F100-success?style=for-the-badge)](https://github.com)
[![Professional Level](https://img.shields.io/badge/Level-Professional-red?style=for-the-badge)](https://github.com)

## 📖 Table of Contents (Because I'm Organized... Sometimes)

- [What Even Is This?](#what-even-is-this)
- [Features That'll Make You Go "Wait, What?"](#features-thatll-make-you-go-wait-what)
- [Tech Stack (AKA My Resume Keywords)](#tech-stack-aka-my-resume-keywords)
- [Installation (The "It Works on My Machine" Guide)](#installation-the-it-works-on-my-machine-guide)
- [Usage (For Research Purposes Only)](#usage-for-research-purposes-only)
- [API Endpoints (RESTful and Respectful)](#api-endpoints-restful-and-respectful)
- [Project Structure (Organized Chaos)](#project-structure-organized-chaos)
- [The Journey (A Developer's Diary)](#the-journey-a-developers-diary)
- [FAQ (Frequently Awkward Questions)](#faq-frequently-awkward-questions)
- [Legal Disclaimer](#legal-disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## 🤔 What Even Is This?

**Day 96 of 100 Days of Python** - A production-ready **Content Aggregation API** that demonstrates advanced web scraping, REST API design, and Cloudflare bypass techniques.

### 🎯 Learning Objectives (Day 96)
- ✅ Master advanced web scraping with BeautifulSoup
- ✅ Implement Cloudflare bypass using curl_cffi
- ✅ Build RESTful API with Flask and CORS
- ✅ Handle image processing and PDF generation
- ✅ Implement multi-threaded file cleanup
- ✅ Create responsive single-page application
- ✅ Practice async operations and session management

### 📍 Position in 100 Days Journey
- **Section:** Professional Portfolio Projects (Days 82-100)
- **Day:** 96/100
- **Difficulty:** Advanced
- **Project Type:** Full-Stack Web API + Scraper
- **Previous Day:** Day 95 - Custom FastAPI Manga Scraper
- **Next Day:** Day 97 - E-Commerce Platform (The Fake Shop)

---

## 🚀 Features That'll Make You Go "Wait, What?"

### Core Features (The Stuff That Actually Works)

- 🔍 **Smart Search Engine** - Search by ID, title, tags, artists, or that one thing you can't remember
- 📚 **Infinite Scroll Homepage** - Like TikTok, but for manga (equally addictive)
- 🖼️ **Lightbox Reader** - Arrow key navigation because we're not savages
- 📥 **PDF Generator** - Downloads entire galleries as PDFs (RIP your storage)
- 🎨 **Responsive UI** - Looks good on desktop, mobile, and your smart fridge
- 🌐 **Language Flags** - English, Japanese, Chinese detection (I'm basically Google Translate now)
- 🏷️ **Tag System** - Click any tag to search (it's like Wikipedia rabbit holes, but different)
- 💾 **Single Page Downloads** - For when you only need *that one* page
- 🔄 **Recommendations** - "If you liked this, you'll love..." (I'm not judging)

### Technical Flexes (The Stuff I'm Proud Of)

- ⚡ **Cloudflare Bypass** - Using `curl_cffi` because regular requests is for quitters
- 🎯 **BeautifulSoup Parsing** - Extracting JSON from JavaScript like a surgeon
- 🖼️ **Image Optimization** - Converts RGBA/PNG to RGB/JPEG (because img2pdf is picky)
- 🧵 **Threaded Cleanup** - Auto-deletes PDFs after download (covering my tracks)
- 🎭 **Browser Impersonation** - Pretends to be Chrome (method acting for APIs)
- 📱 **Progressive Loading** - Thumbnails first, full images later (I care about your bandwidth)
- 🔗 **Deep Linking** - Shareable URLs with query params (SEO-friendly... kinda)

---

## 🛠️ Tech Stack (AKA My Resume Keywords)

### Backend (Core Technologies)
```python
Flask          # Web framework for REST API
BeautifulSoup4 # HTML parsing and data extraction
curl_cffi      # Cloudflare bypass with browser impersonation
Pillow         # Image processing (RGBA to RGB conversion)
img2pdf        # PDF generation from images
Flask-CORS     # Cross-origin resource sharing
```

### Frontend (Single Page Application)
```javascript
Vanilla JS     # Pure JavaScript (no frameworks)
Tailwind CSS   # Utility-first CSS framework
HTML5          # Semantic markup
```

### Skills Demonstrated (Day 96)
```bash
✅ Advanced web scraping techniques
✅ REST API design and implementation
✅ Cloudflare protection bypass
✅ Image format conversion and optimization
✅ PDF generation from web content
✅ Multi-threaded file operations
✅ Session management and cleanup
✅ Responsive UI design
✅ Error handling and edge cases
```

---

## 📦 Installation (The "It Works on My Machine" Guide)

### Prerequisites (Things You Should Already Have)

- Python 3.8+ (If you're still on Python 2, we need to talk)
- pip (Python's package manager, not the British insult)
- A sense of humor (Non-negotiable)
- Coffee (Optional but highly recommended)

### Step 1: Navigate to Day 96 Project

```bash
cd "100Days Python/Professional Portfolio Project/Day96"
```

### Step 2: Create a Virtual Environment (Isolation is Key)

```bash
python -m venv venv

# On Windows (Because you're probably on Windows)
venv\Scripts\activate

# On Mac/Linux (Look at you, fancy pants)
source venv/bin/activate
```

**Pro Tip:** If you forget to activate the venv, you'll install packages globally and your future self will hate you. Don't be that person.

### Step 3: Install Dependencies (Pray to the Pip Gods)

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed flask-2.x.x ...
```

**Actual output:**
```
ERROR: Could not find a version that satisfies...
*5 hours of Stack Overflow later*
Successfully installed flask-2.x.x ...
```

### Step 4: Run the Server (Moment of Truth)

```bash
python api.py
```

**If you see:**
```
* Running on http://127.0.0.1:5000
```
🎉 **Congratulations!** You can follow instructions!

**If you see:**
```
ModuleNotFoundError: No module named 'flask'
```
😭 You forgot Step 3, didn't you?

### Step 5: Open Your Browser

Navigate to `http://localhost:5000` and witness the glory.

---

## 🎮 Usage (For Research Purposes Only)

### Basic Search

1. **By ID:** Type `177013` (if you know, you know 💀)
2. **By Title:** Type `"Metamorphosis"` (why would you do this to yourself?)
3. **By Tags:** Type `tag:"vanilla"` (the wholesome route)

### Advanced Search Queries

```
artist:"shadman"           # Find by artist
parody:"naruto"            # Find parodies
character:"hinata"         # Find specific characters
language:"english"         # Filter by language
tag:"wholesome" -tag:"ntr" # Wholesome content only (the good ending)
```

### Keyboard Shortcuts (Because Mice Are Overrated)

- `→` Next page
- `←` Previous page  
- `Esc` Close reader (for when your mom walks in)
- `Alt+F4` Close everything (nuclear option)

---

## 🌐 API Endpoints (RESTful and Respectful)

### `GET /api?manga_id={id}`
Fetches complete manga metadata.

**Response:**
```json
{
  "id": 177013,
  "title": "Emergence",
  "tags": ["depression", "life_choices", "regret"],
  "num_pages": 225,
  "page_urls": ["https://..."],
  "favorites": 50000,
  "recommendations": [...]
}
```

### `GET /api/search?q={query}&page={page}`
Searches the entire database.

**Example:**
```bash
curl "http://localhost:5000/api/search?q=vanilla&page=1"
```

### `GET /api/homepage?page={page}`
Loads the discovery feed.

**Returns:** 18 latest uploads (because 18 is the magic number)

### `GET /api/download?manga_id={id}`
Generates and downloads a PDF.

**Warning:** This endpoint is SLOW. Like, "go make coffee" slow. Like, "question your life choices" slow.

### `GET /api/download_page?url={url}&filename={name}`
Downloads a single page as PNG.

**Pro Tip:** Use this for your "homework" folder.

---

## 📁 Project Structure (Organized Chaos)

```
nhentai-website/
│
├── api.py                 # The brain (500+ lines of spaghetti)
├── requirements.txt       # Dependency hell manifest
├── README.md             # You are here (congrats on reading this far)
│
└── templates/
    └── index.html        # The face (1000+ lines of HTML/JS/CSS)
```

**What I planned:**
```
├── models/
├── controllers/
├── services/
├── utils/
└── tests/
```

**What I actually did:**
```
├── api.py  # Everything lives here
└── index.html  # And here
```

*"I'll refactor it later"* - Lies I tell myself

---

## 🎢 Day 96 Development Journey

### Hour 1-2: "Flask API Setup"
- Set up Flask application structure
- Implemented basic routing and CORS
- Created initial API endpoints

### Hour 3-4: "The Cloudflare Challenge"
- Discovered standard requests library blocked
- Researched Cloudflare bypass techniques
- Implemented curl_cffi with browser impersonation
- Successfully bypassed protection

### Hour 5-6: "BeautifulSoup Parsing"
- Analyzed target website HTML structure
- Extracted JSON data from JavaScript
- Implemented metadata parsing
- Built recommendation scraper

### Hour 7-8: "Image Processing Hell"
- img2pdf rejected PNG with alpha channels
- Learned about RGBA vs RGB color modes
- Implemented Pillow conversion pipeline
- Fixed transparency issues

### Hour 9-10: "Frontend Integration"
- Built responsive UI with Tailwind CSS
- Implemented lightbox reader
- Added keyboard navigation
- Created infinite scroll

### Hour 11-12: "Polish & Optimization"
- Added threaded file cleanup
- Implemented error handling
- Optimized image loading
- Final testing and deployment

## 📚 What I Learned (Day 96)

### Technical Skills
1. **Advanced Web Scraping** - Bypassing anti-bot protections
2. **REST API Design** - Building production-ready endpoints
3. **Image Processing** - Format conversion and optimization
4. **PDF Generation** - Creating documents from web content
5. **Threading** - Async file operations and cleanup
6. **Session Management** - Handling browser impersonation

### Problem-Solving
- Cloudflare bypass requires browser-like behavior
- Image format matters for PDF generation
- Cleanup operations should be non-blocking
- Error handling is critical for scrapers

### Best Practices
- Use curl_cffi for Cloudflare-protected sites
- Convert images to RGB before PDF generation
- Implement proper cleanup for temporary files
- Add rate limiting to avoid IP bans
- Handle edge cases gracefully

## 🔗 Related Projects in 100 Days Journey

- **Day 45:** BeautifulSoup basics (100 Greatest Movies)
- **Day 47:** Web scraping with requests (Amazon Price Tracker)
- **Day 48:** Selenium automation (Cookie Clicker Bot)
- **Day 66:** REST API fundamentals (Cafe API)
- **Day 93:** Batch scraping (ArXiv Paper Scraper)
- **Day 95:** FastAPI implementation (Custom Manga API)
- **Day 96:** Advanced scraping + API (This Project)
- **Day 97:** Full-stack application (The Fake Shop)

## 🎯 Skills Progression

**Before Day 96:**
- Basic web scraping with BeautifulSoup
- Simple Flask APIs
- Standard HTTP requests

**After Day 96:**
- Advanced anti-bot bypass techniques
- Production-ready REST APIs
- Image processing pipelines
- PDF generation from web content
- Multi-threaded operations

## 🏆 Day 96 Achievements

✅ Built complete REST API with 5 endpoints
✅ Implemented Cloudflare bypass successfully
✅ Created image-to-PDF conversion pipeline
✅ Designed responsive single-page application
✅ Added threaded cleanup operations
✅ Handled 10+ edge cases and errors
✅ Integrated search and recommendation systems
✅ Optimized for production deployment

## 📈 Complexity Metrics

- **Lines of Code:** ~800+ (api.py + index.html)
- **API Endpoints:** 5
- **Technologies Used:** 8+
- **Time to Complete:** ~12 hours
- **Difficulty:** Advanced ⭐⭐⭐⭐⭐
- **Reusability:** High (scraping patterns applicable to many sites)

## 🚀 Next Steps (Day 97)

After mastering web scraping and API development in Day 96, Day 97 takes it further with **The Fake Shop** - a production-ready e-commerce platform featuring:
- User authentication and authorization
- Shopping cart and checkout system
- Admin dashboard with analytics
- Database relationships (7 tables)
- Payment processing
- Email notifications
- Cloud image hosting

---

## 📝 Original Project Documentation

### The Thumbnail Optimization"
- Homepage loading 18 full images
- Users: "Why is this so slow?"
- Me: "Oh right, bandwidth exists"
- Implemented thumbnail URLs
- Users: "Wow, so fast!"

### Day 6: "The Language Detection Incident"
- Hardcoded tag IDs for languages
- Worked 90% of the time
- The other 10%: chaos
- Added title parsing fallback
- Now works 99% of the time
- The other 1%: still chaos

### Day 7: "Deployment Hell"
- "It works on my machine"
- Tried to deploy
- Everything broke
- Added Gunicorn
- Still broke
- Gave up, runs on localhost
- Just kidding. Programmers never Give up. <a href="https://hentai-manga.onrender.com">Link</a>

---

## 🔮 Future Enhancements (AKA My Procrastination List)

### Features I'll "Definitely" Add (Narrator: He Won't)

#### 🎯 High Priority (Translation: Maybe Someday)

- **🗄️ Database Integration**
  - *Current Status:* Everything lives in memory like it's 1995
  - *Plan:* Add PostgreSQL or MongoDB
  - *Reality:* "But it works fine without it..."
  - *ETA:* When I run out of RAM (so, never)

- **🔐 User Authentication**
  - *Current Status:* Everyone is admin (democracy!)
  - *Plan:* JWT tokens, OAuth, the whole nine yards
  - *Reality:* "Do I really need to track who downloads what?"
  - *ETA:* When my mom asks for a login

- **⚡ Redis Caching**
  - *Current Status:* Hitting the API like it owes me money
  - *Plan:* Cache everything, be smart about it
  - *Reality:* "The API is fast enough... right?"
  - *ETA:* After the 429 Too Many Requests incident

- **🧪 Unit Tests**
  - *Current Status:* "It works on my machine" IS the test
  - *Plan:* 80% code coverage, pytest, the works
  - *Reality:* "Testing is for people who make mistakes"
  - *ETA:* After the first production bug (so, tomorrow)

#### 🌟 Medium Priority (Translation: Probably Never)

- **🌙 Dark/Light Mode Toggle**
  - Because apparently dark mode isn't dark enough for some people
  - Will add 47 shades of gray
  - ETA: When someone complains about eye strain

- **📊 Analytics Dashboard**
  - Track what people search for (for science)
  - Realize everyone searches the same 5 things
  - Question humanity
  - ETA: When I want to feel like a data scientist

- **🔔 Notification System**
  - "New upload in your favorite tag!"
  - Realize I'm building a social network
  - Have an existential crisis
  - ETA: Never, I have enough notifications in my life

- **💬 Comment System**
  - Let users leave reviews
  - Immediately regret it
  - Spend 90% of time moderating
  - ETA: When I hate myself

#### 🎨 Low Priority (Translation: In Another Universe)

- **🤖 AI-Powered Recommendations**
  - Train a neural network on user behavior
  - Realize I need a PhD for this
  - Use a random number generator instead
  - Call it "AI-powered"
  - ETA: When AI becomes sentient and does it for me

- **📱 Native Mobile App**
  - React Native? Flutter? SwiftUI?
  - Spend 6 months deciding
  - Realize the mobile web works fine
  - Add `<meta name="viewport">` and call it a day
  - ETA: When I learn mobile development (so, 2050)

- **🎮 Gamification**
  - Achievement badges for reading
  - Leaderboards for... something
  - Realize I'm not building Duolingo
  - ETA: April 1st (as a joke)

- **🌍 Multi-Language Support**
  - i18n for the UI
  - Translations for 47 languages
  - Realize 99% of users speak English
  - ETA: When I'm fluent in 47 languages

---
### 🐛 Known Issues (That I'm Choosing to Ignore)

- **The PDF download is slower than my grandma's internet**
  - *Solution:* Make better life choices
  - *Actual Solution:* Implement async processing with Celery
  - *My Solution:* Add a loading spinner and hope people are patient

- **No error handling for when the source site is down**
  - *Current Behavior:* App explodes spectacularly
  - *Planned Fix:* Graceful error messages
  - *Actual Fix:* "Have you tried turning it off and on again?"

- **Memory leaks somewhere (probably)**
  - *Evidence:* My laptop sounds like a jet engine
  - *Investigation Status:* Pending
  - *Workaround:* Restart the server daily
  - *Real Solution:* Buy more RAM

- **The code needs refactoring**
  - *Current State:* Spaghetti code with meatballs
  - *Plan:* Clean architecture, SOLID principles
  - *Reality:* "If it ain't broke, don't fix it"
  - *Counter-argument:* "But it IS broke"
  - *Response:* "But it WORKS"

---

### 💡 Ideas From 3 AM Me (Probably Bad)

- Blockchain integration (for some reason)
- NFT support (because why not make it worse)
- Cryptocurrency mining in the background (kidding... unless?)
- VR reader mode (for the future)
- Integration with smart home devices ("Alexa, read me manga")
- Smell-o-vision support (technology isn't there yet)
- Time travel feature (still debugging)

---

### 🎯 Realistic Roadmap

- **Q1 2026:** Fix that one annoying bug  
- **Q2 2026:** Add the feature I promised  
- **Q3 2026:** Refactor (lol jk)  
- **Q4 2026:** Start a new project and abandon this one  
- **Q1 2069:** Come back because someone opened an issue  
- **Q2 2069:** "I should really update the dependencies"  
- **Q3 2069:** Update dependencies, everything breaks  
- **Q4 2069:** Revert to old dependencies  

---

### 📝 Contributing to Future Enhancements

Want to implement any of these features? Please do! I'll be here, cheering you on from the sidelines while I:
- Start 5 new projects
- Learn a new framework
- Rewrite my portfolio for the 47th time
- Question my career choices
- Browse memes on Reddit

**Seriously though,** PRs are welcome. I promise to review them faster than I implement my own features (low bar, I know).

---

## ❓ FAQ (Frequently Awkward Questions)

### Q: Is this legal?
**A:** It's a web scraper. It's like a browser, but automated. You tell me. (Consult a lawyer, not a README)

### Q: Why did you build this?
**A:** For my portfolio. And science. Mostly science.

### Q: Can I use this for commercial purposes?
**A:** Sure, if you want to explain to investors why your startup is a manga scraper.

### Q: Will this get me hired?
**A:** It demonstrates:
- Web scraping expertise ✅
- API development ✅
- Frontend skills ✅
- Problem-solving ✅
- Questionable decision-making ✅

So... maybe?

### Q: Why is the download so slow?
**A:** Because I'm downloading 200+ images, converting them, and compiling a PDF. What did you expect, magic?

### Q: Can you add [feature]?
**A:** Sure! Submit a PR. I'll review it in 3-5 business years.

### Q: Why is the code so messy?
**A:** It's not messy, it's "organically structured." Also, it's 3 AM code. Don't judge me.

### Q: What's with all the comments in the code?
**A:** Future me needs to understand what past me was thinking. Spoiler: He won't.

---

## ⚖️ Legal Disclaimer

This project is for **educational purposes only**. I am not responsible for:

- ❌ How you use this code
- ❌ Any legal issues you encounter
- ❌ Your browser history
- ❌ Your therapist bills
- ❌ Your hard drive running out of space
- ❌ Explaining this to your significant other
- ❌ Your productivity loss
- ❌ Your sleep schedule

**Use responsibly.** Or don't. I'm a README, not a cop.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
6. Wait for me to review it (ETA: 2-3 business eternities)

**Contribution Guidelines:**
- Write clean code (cleaner than mine, at least)
- Add comments (unlike me)
- Test your changes (I should do this too)
- Don't break existing features (please)

---

## 📜 License

This project is licensed under the **"Don't Sue Me" License**.

More formally: MIT License (because I'm not a monster)

```
MIT License

Copyright (c) 2024 indiser

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...

(You know the rest. It's MIT. It's chill.)
```

---

## 🎯 Final Thoughts

If you've read this far, you either:

1. Are genuinely interested in the project ✨
2. Are a recruiter doing due diligence 👔
3. Have way too much free time ⏰
4. Are me, from the future, wondering what I was thinking 🤔

**To recruiters:** Yes, I can code. Yes, I have a sense of humor. Yes, I'm available for hire. No, I won't build this for your company.

**To developers:** Feel free to steal this code. I stole half of it from Stack Overflow anyway.

**To my mom:** This is a book cataloging system. Don't Google it.

---

## 🙏 Acknowledgments

- **Stack Overflow** - For raising me
- **ChatGPT** - For being my rubber duck
- **Coffee** - For existing
- **My Keyboard** - For surviving my rage
- **Cloudflare** - For making me a better developer (by force)
- **You** - For reading this entire README (seriously, thank you)

---

## 📞 Contact

**Email:** [your.email@example.com]  
**LinkedIn:** [Your LinkedIn]  
**GitHub:** [Your GitHub]  
**Therapy Hotline:** 1-800-WHY-DID-I-BUILD-THIS

---

<div align="center">

### ⭐ If this made you laugh, give it a star!

### 🍕 If this got you hired, buy me a pizza!

**Made with ❤️, ☕, and questionable life choices**

*"It's not a bug, it's a feature"* - Me, probably

</div>

---

## 🎪 Bonus: Easter Eggs

- The code has exactly 3 TODO comments that will never be done
- There's a commented-out `requests` import (RIP, you tried)
- The PDF cleanup thread waits 2 seconds (I tested 1 second, it was too fast)
- The search input placeholder says "Enter ID, Name, or Tags" but accepts your hopes and dreams
- The error messages are more helpful than most documentation
- I used `time.sleep()` in production code (don't tell anyone)

---

**P.S.** If you're a recruiter and you've read this entire README, I'm already impressed. Let's talk. I promise my actual work is more professional than this. Maybe. Probably. We'll see.

**P.P.S.** If you're NOT a recruiter and you've read this entire README, you should be a code reviewer. You have the patience of a saint.

**P.P.P.S.** There is no P.P.P.S. I just wanted to see if you're still reading. You are. Wow. Okay. Bye now. 👋
