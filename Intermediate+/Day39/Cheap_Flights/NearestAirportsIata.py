# Install: pip install airportsdata geocoder
import airportsdata
import math
import geocoder

class NearestAirport:
    def __init__(self):
        self.airports = airportsdata.load('IATA')
        self.my_lat = None
        self.my_lon = None
        self.nearest_iata = None
        
    def get_location(self):
        """Get current location using IP address"""
        g = geocoder.ip('me')
        if g.ok:
            self.my_lat = g.latlng[0]
            self.my_lon = g.latlng[1]
            print(f"Your Location: {g.city}, {g.country}")
            print(f"Coordinates: {self.my_lat}, {self.my_lon}")
        else:
            print("Could not detect location, using default (Delhi)")
            self.my_lat = 28.7041
            self.my_lon = 77.1025
    
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        """Calculate distance between two coordinates"""
        return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    
    def find_nearest_airport(self):
        """Find nearest airport and return IATA code"""
        if self.my_lat is None:
            self.get_location()
        
        nearest_airport = None
        min_distance = float('inf')
        
        for iata_code, airport_info in self.airports.items():
            if 'lat' in airport_info and 'lon' in airport_info:
                distance = self.calculate_distance(self.my_lat, self.my_lon, airport_info['lat'], airport_info['lon'])
                if distance < min_distance:
                    min_distance = distance
                    nearest_airport = (iata_code, airport_info, distance)
        
        if nearest_airport:
            iata, info, dist = nearest_airport
            self.nearest_iata = iata
            print(f"Nearest Airport: {info['name']}")
            print(f"IATA Code: {iata}")
            print(f"City: {info['city']}")
            print(f"Distance: ~{dist * 111:.1f} km")
            return iata
        else:
            print("No airports found")
            return None
    
    def get_iata_code(self):
        """Simple method to get IATA code"""
        if self.nearest_iata is None:
            return self.find_nearest_airport()
        return self.nearest_iata
    def get_city(self):
        """Get city name of nearest airport"""
        if self.nearest_iata is None:
            self.find_nearest_airport()
        
        if self.nearest_iata and self.nearest_iata in self.airports:
            return self.airports[self.nearest_iata]['city']
        return None
