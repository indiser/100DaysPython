#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData
from NearestAirportsIata import NearestAirport

# Get your home airport
airport=NearestAirport()
home_iata = airport.get_iata_code()
home_city=airport.get_city()
# Get destinations from Google Sheet
data_manager = DataManager()
destinations = data_manager.get_destination_data()

# Initialize flight search and notification manager
flight_search = FlightSearch()
notifier = NotificationManager()

# Loop through each destination
for destination in destinations:
    city = destination["city"]
    iata = destination["iataCode"]
    target_price = destination["lowestPrice"]
    
    print(f"\nSearching flights to {city} ({iata})...")
    
    # Search for flights
    flights = flight_search.search_flights(origin=home_iata, destination=iata)
    
    # Check if flights were found
    if flights and "data" in flights:
        for flight in flights["data"]:
            price = float(flight["price"]["total"])
            
            # If price is lower than target, send notification
            if price < target_price:
                print(f"✓ Found cheap flight: ${price}")
                
                # Get flight details
                departure = flight["itineraries"][0]["segments"][0]["departure"]["at"]
                arrival = flight["itineraries"][0]["segments"][-1]["arrival"]["at"]
                
                # Create FlightData object to structure the information
                flight_data = FlightData(
                    price=price,
                    origin_city=home_city,
                    origin_airport=home_iata,
                    destination_city=city,
                    destination_airport=iata,
                    out_date=departure,
                    return_date=arrival
                )
                
                # Send notification using FlightData
                notifier.send_notification(
                    price=flight_data.price,
                    origin=flight_data.origin_airport,
                    destination=flight_data.destination_airport,
                    start_date=flight_data.out_date,
                    end_date=flight_data.return_date
                )
                break
        else:
            print(f"✗ No flights found under ${target_price}")
    else:
        print(f"✗ No flights available")

print("\n=== Flight search complete ===")