# 📚 Day 95: Custom API - Doujin API

> **100 Days of Python - Day 95: Professional Portfolio Project**

A high-performance async REST API built with FastAPI that scrapes and serves manga metadata. Features CloudFlare bypass, async session management, and comprehensive data extraction.

## 🎯 Project Overview

Part of the 100 Days of Python challenge, this project demonstrates advanced API development with modern Python async patterns, web scraping techniques, and production-ready architecture.

### Key Features

- ⚡ **FastAPI Framework**: Modern async web framework with automatic documentation
- 🔒 **CloudFlare Bypass**: Uses `curl_cffi` for browser impersonation
- 📊 **Rich Metadata Extraction**: Tags, artists, characters, parodies, and more
- 🖼️ **Direct Image URLs**: Generates links to all pages and cover images
- 🎲 **Recommendations Scraping**: Related content suggestions
- 🧹 **Clean JSON Responses**: Well-structured, easy-to-consume data
- 🔄 **Async Session Management**: Proper lifespan handling with startup/shutdown
- 📖 **Swagger Documentation**: Auto-generated API docs endpoint

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- curl_cffi
- BeautifulSoup4
- Uvicorn

### Installation

1. **Navigate to project directory**
   ```bash
   cd "100Days Python/Professional Portfolio Project/Day95/fastapi"
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn curl-cffi beautifulsoup4
   ```

3. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

   For production with Gunicorn:
   ```bash
   gunicorn main:app -k uvicorn.workers.UvicornWorker
   ```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

### Endpoints

#### `GET /`
**Home endpoint** - Returns a message directing users to the proper endpoints.

**Response:**
```json
{
  "Messege": "Go To The EndPoint Moron"
}
```

---

#### `GET /manga_id={manga_id}`
**Retrieve manga metadata** by ID.

**Parameters:**
- `manga_id` (int): The nHentai gallery ID

**Example Request:**
```bash
curl http://localhost:8000/manga_id=177013
```

**Example Response:**
```json
{
  "id": 177013,
  "title": "Example Title",
  "date": "2023-01-15",
  "media_id": "987654",
  "parodies": ["Original Work"],
  "charecters": ["Character Name"],
  "groups": ["Group Name"],
  "categories": ["Manga"],
  "language": ["English"],
  "favorites": 12345,
  "tags": ["tag1", "tag2"],
  "artists": ["Artist Name"],
  "num_pages": 225,
  "page_urls": [
    "https://i.nhentai.net/galleries/987654/1.jpg",
    "https://i.nhentai.net/galleries/987654/2.jpg"
  ],
  "cover_image": "https://t.nhentai.net/galleries/987654/cover.jpg",
  "recommendations": [
    {"id": 123456, "title": "Related Title 1"},
    {"id": 789012, "title": "Related Title 2"}
  ]
}
```

**Error Response:**
```json
{
  "Error": "Error message here"
}
```

## 🏗️ Architecture

### Tech Stack

- **FastAPI**: Modern async web framework with automatic API documentation
- **curl_cffi**: CloudFlare bypass via browser impersonation
- **BeautifulSoup4**: HTML parsing for scraping recommendations and cover images
- **Uvicorn/Gunicorn**: ASGI server for production deployment

### How It Works

1. **Request Handling**: FastAPI receives the manga ID via path parameter
2. **Session Management**: Async session with Chrome impersonation bypasses CloudFlare
3. **Data Extraction**: 
   - Regex extracts JSON data from `window._gallery` JavaScript variable
   - BeautifulSoup parses HTML for recommendations and cover images
4. **URL Generation**: Constructs direct image URLs using media ID and page extensions
5. **Response**: Returns clean, structured JSON with all metadata

### Lifespan Management

The API implements proper async session lifecycle management:
- Session created on startup using lifespan context manager
- Gracefully closed on shutdown
- Prevents resource leaks and connection issues

## 🔧 Configuration

### Headers
The API uses a standard Chrome User-Agent to avoid detection:
```python
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
```

### Image Extensions
Supports multiple formats with automatic detection:
- `j` → JPG
- `p` → PNG
- `w` → WebP
- `g` → GIF

## 🎓 Learning Outcomes

### Skills Demonstrated

✅ **FastAPI Framework**: Building production-ready REST APIs  
✅ **Async/Await**: Modern Python asynchronous programming  
✅ **Web Scraping**: Data extraction with BeautifulSoup  
✅ **CloudFlare Bypass**: Browser impersonation techniques  
✅ **Session Management**: Proper resource lifecycle handling  
✅ **JSON Processing**: Regex extraction and data parsing  
✅ **URL Generation**: Dynamic image URL construction  
✅ **Error Handling**: Graceful failure management  
✅ **API Design**: RESTful endpoint structure  
✅ **Documentation**: Swagger/OpenAPI integration

## 🚦 Potential Enhancements

- [ ] **Rate Limiting**: Prevent API abuse
- [ ] **Caching**: Redis integration for performance
- [ ] **Error Handling**: More granular HTTP status codes
- [ ] **Search Endpoint**: Query by tags, artists, or titles
- [ ] **Database Integration**: Local metadata storage
- [ ] **Authentication**: API key system

## 🐛 Known Issues

- Error handling could be more specific with HTTP status codes
- No retry logic for failed requests
- Session isn't shared across workers in multi-process deployments

## 📊 Project Context

This project is part of the **100 Days of Python** challenge:
- **Day**: 95/100
- **Level**: Professional Portfolio Projects
- **Category**: API Development & Web Scraping
- **Complexity**: Advanced

### Related Projects in This Challenge
- Day 66: RESTful Cafe API
- Day 96: Manga/Comic API (Enhanced version)
- Day 97: E-Commerce Platform API

## ⚖️ Legal Disclaimer

This project is for **educational purposes only** as part of a coding challenge. Web scraping may violate terms of service. Use responsibly and at your own risk.

## 🙏 Acknowledgments

- **FastAPI**: Modern Python web framework
- **curl_cffi**: CloudFlare bypass solution
- **BeautifulSoup**: HTML parsing library
- **100 Days of Python Challenge**: Project inspiration

---

<div align="center">

**Day 95/100 - Professional Portfolio Project**

*Part of the journey from beginner to professional Python developer*

</div>
