# ✈️ Cheap Flights Finder

> **Automated flight deal finder that monitors prices across 6 months and sends real-time notifications**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Overview

**Cheap Flights Finder** is an intelligent flight monitoring system that:
- 🌍 Automatically detects your location and nearest airport
- 📊 Reads destination lists from Google Sheets
- ✈️ Searches for the cheapest flights over 6 months using Amadeus API
- 📧 Sends email notifications when deals are found
- 💾 Tracks and updates lowest prices in real-time

Perfect for travel enthusiasts who want to find the best flight deals without manual searching!

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          main.py                                 │
│                    (Orchestrator/Controller)                     │
└────────┬────────────────────┬────────────────┬──────────────────┘
         │                    │                │
         ▼                    ▼                ▼
┌────────────────┐   ┌────────────────┐   ┌──────────────────┐
│ DataManager    │   │ FlightSearch   │   │ NotificationMgr  │
│ (Google Sheet) │   │ (Amadeus API)  │   │ (Email Alerts)   │
└────────┬───────┘   └────────┬───────┘   └──────────────────┘
         │                    │
         │                    ▼
         │           ┌────────────────┐
         │           │  FlightData    │
         └──────────►│  (Data Model)  │
                     └────────────────┘
```

---

## 📁 Project Structure

```
Cheap_Flights/
├── main.py                      # Main orchestrator
├── data_manager.py              # Google Sheets interface
├── flight_search.py             # Amadeus API integration
├── flight_data.py               # Flight data model
├── notification_manager.py      # Email notifications
├── NearestAirportsIata.py       # Location detection
├── auth.json                    # API authentication token
├── .env                         # Environment variables
└── README.md                    # This file
```

---

## 🔄 Complete Code Flow

### **Execution Flow Diagram**

```
START
  ↓
[1] Detect User Location
    └─→ Get nearest airport IATA code
  ↓
[2] Load Destinations
    └─→ Read from Google Sheets
  ↓
[3] For Each Destination
    ├─→ Search flights (6 months span)
    ├─→ Find cheapest option
    ├─→ Compare with target price
    └─→ If cheaper:
        ├─→ Create FlightData object
        ├─→ Send email notification
        └─→ Update Google Sheet
  ↓
END
```

---

## 📁 File Responsibilities

### **1. main.py** - 🎯 Orchestrator
**Purpose:** Coordinates all components

**Key Functions:**
- Initialize all classes
- Get user's home airport
- Load destinations from Google Sheet
- Loop through destinations and search flights
- Send notifications for deals
- Update prices in sheet

```python
# Usage
home_iata = NearestAirport().get_iata_code()
destinations = DataManager().get_destination_data()
flight_search = FlightSearch()
notifier = NotificationManager()
```

---

### **2. data_manager.py** - 📊 Google Sheets Interface
**Purpose:** Handle all Google Sheets operations

**Methods:**
- `get_destination_data()` - Fetch destinations from sheet
- `update_destination_codes()` - Update IATA codes
- `update_prices()` - Update lowest prices

**Google Sheet Format:**
```
| City      | IATA Code | Lowest Price |
|-----------|-----------|--------------|
| Paris     | PAR       | 200          |
| Berlin    | BER       | 150          |
| Tokyo     | NRT       | 500          |
```

---

### **3. flight_search.py** - ✈️ Amadeus API
**Purpose:** Search for cheap flights

**Methods:**
- `__init__()` - Load API credentials
- `search_flights(origin, destination)` - Search 6-month span

**Features:**
- Searches 6 months automatically
- Returns cheapest dates
- Supports round trips
- Includes connecting flights

---

### **4. flight_data.py** - 📦 Data Model
**Purpose:** Structure flight information

**Attributes:**
- `price` - Flight cost
- `origin_city` / `origin_airport` - Departure details
- `destination_city` / `destination_airport` - Arrival details
- `out_date` / `return_date` - Travel dates

```python
flight = FlightData(
    price=150,
    origin_city="New York",
    origin_airport="JFK",
    destination_city="Paris",
    destination_airport="CDG",
    out_date="2025-06-01",
    return_date="2025-06-08"
)
```

---

### **5. notification_manager.py** - 📧 Alerts
**Purpose:** Send email notifications

**Methods:**
- `send_notification(price, origin, destination, start_date, end_date)`

**Email Format:**
```
Subject: Low Price Alert! ✈️

Only $150 to fly from NYC to Paris!

Departure: 2025-06-01
Return: 2025-06-08

Book now: https://www.google.com/flights
```

---

### **6. NearestAirportsIata.py** - 🌍 Location Detection
**Purpose:** Find user's nearest airport

**Methods:**
- `get_location()` - Detect location via IP
- `find_nearest_airport()` - Find closest airport
- `get_iata_code()` - Get airport code
- `get_city()` - Get city name

```python
airport = NearestAirport()
iata = airport.get_iata_code()  # Returns "JFK"
city = airport.get_city()        # Returns "New York"
```

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8+
- Google Sheets account
- Amadeus API account
- Gmail account (for notifications)

### **Installation**

1. **Clone/Download the project**
```bash
cd Cheap_Flights
```

2. **Install dependencies**
```bash
pip install requests python-dotenv pandas airportsdata geocoder
```

3. **Set up environment variables** (`.env` file)
```env
# Amadeus API
AMADEUS_API_KEY=your_key_here
AMADEUS_API_SECRETS=your_secret_here

# Google Sheets (Sheety)
SHEET_ID=your_sheet_id
SHEETY_TOKEN=your_token

# Email
EMAIL=your_email@gmail.com
EMAIL_APP_PASS=your_app_password
ADDRESS_EMAIL=recipient@gmail.com
```

4. **Set up Google Sheet**
Create a sheet with columns:
- City
- IATA Code
- Lowest Price

5. **Run the program**
```bash
python main.py
```

---

## 📊 Data Flow

```
Google Sheet (Sheety API)
         ↓
    [Destinations]
         ↓
   DataManager
         ↓
    main.py ←─────────────────────┐
         ↓                        │
   NearestAirport                 │
    (Get home IATA)               │
         ↓                        │
   FlightSearch                   │
    (Amadeus API)                 │
         ↓                        │
   FlightData                     │
    (Structure info)              │
         ↓                        │
   NotificationManager            │
    (Send email)                  │
         ↓                        │
   Update Google Sheet ───────────┘
```

---

## 🔐 API Credentials

### **Amadeus API**
1. Sign up at [Amadeus for Developers](https://developers.amadeus.com/)
2. Create an app
3. Get `Client ID` and `Client Secret`
4. Add to `.env` file

### **Google Sheets (Sheety)**
1. Create a Google Sheet
2. Sign up at [Sheety](https://sheety.co/)
3. Connect your sheet
4. Get API endpoint and token
5. Add to `.env` file

### **Gmail**
1. Enable 2-factor authentication
2. Generate app password
3. Use app password in `.env` file

---

## 📧 Example Output

```
Your Location: New York, United States
Coordinates: 40.7128, -74.0060
Nearest Airport: John F. Kennedy International Airport
IATA Code: JFK
City: New York
Distance: ~15.2 km

Searching flights to Paris (PAR)...
✓ Found cheap flight: $180
📧 Notification sent!
📊 Updated Google Sheet

Searching flights to Berlin (BER)...
✗ No flights found under $150

Searching flights to Tokyo (NRT)...
✓ Found cheap flight: $450
📧 Notification sent!
📊 Updated Google Sheet

=== Flight search complete ===
```

---

## 🎯 Key Features

✅ **Automatic Location Detection** - Uses IP geolocation  
✅ **6-Month Search Span** - Finds best deals across 6 months  
✅ **Real-Time Notifications** - Email alerts for cheap flights  
✅ **Google Sheets Integration** - Easy destination management  
✅ **Price Tracking** - Updates lowest prices automatically  
✅ **Multi-Destination** - Search multiple cities at once  
✅ **Round Trip Support** - Flexible travel dates  

---

## 🔧 Configuration

### **Search Parameters**
- **Duration**: 1-30 days trip length
- **Round Trip**: Yes (can modify for one-way)
- **Connections**: Allowed (for better prices)
- **Search Span**: 6 months from today

### **Customization**
Edit `flight_search.py` to modify:
- Trip duration
- One-way vs round trip
- Direct flights only
- Currency preference

---

## 📈 Future Enhancements

- [ ] SMS notifications (Twilio)
- [ ] Web dashboard
- [ ] Price history charts
- [ ] Multiple home airports
- [ ] Airline preferences filter
- [ ] Hotel/car rental search
- [ ] Mobile app
- [ ] Scheduled runs (cron jobs)

---

## 🐛 Troubleshooting

**Issue: 404 Error from Amadeus API**
- Check API endpoint URL
- Verify IATA codes are valid
- Ensure token is not expired

**Issue: Email not sending**
- Verify Gmail app password
- Check email credentials in `.env`
- Enable "Less secure apps" if needed

**Issue: Location not detected**
- Check internet connection
- Verify geocoder library installed
- Falls back to default (Delhi) coordinates

---

## 📝 Notes

- API tokens expire after 30 minutes (auto-refreshed)
- Google Sheet must have correct column names
- Email notifications require Gmail account
- Amadeus test environment has limitations

---

## 📄 License

MIT License - Feel free to use and modify!

---

## 👨‍💻 Author

**100 Days of Python - Day 39 Project**

Part of the comprehensive Python learning journey covering:
- API Integration
- Data Management
- Email Automation
- OOP Design Patterns

---

## 🤝 Contributing

Found a bug? Have suggestions? Feel free to improve!

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation
3. Check `.env` file configuration
4. Verify all dependencies installed

---

**Happy Traveling! ✈️🌍**

*Last Updated: 2025*  
*Status: Production Ready*
