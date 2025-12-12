import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

load_dotenv()

amadeus_api=os.environ.get("AMADEUS_API_KEY")
amadeus_api_secret=os.environ.get("AMADEUS_API_SECRETS")

amadeus_authentication_endpoint="https://test.api.amadeus.com/v1/security/oauth2/token"
authetication_header={
    "Content-Type": "application/x-www-form-urlencoded"
}
authentication_parameters={
    "grant_type":"client_credentials",
    "client_id":amadeus_api,
    "client_secret":amadeus_api_secret,
}
response=requests.post(url=amadeus_authentication_endpoint,headers=authetication_header,data=authentication_parameters)
response.raise_for_status()

with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day39/Cheap_Flights/auth.json","w") as filp:
    json.dump(response.json(),filp,indent=4)

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
today = datetime.now().strftime("%Y-%m-%d")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day39/Cheap_Flights/auth.json","r") as filp:
            self.data=json.load(filp)
        self.amadeus_header={
            "Authorization":f"{self.data['token_type']} {self.data['access_token']}"
        }
        
    def search_flights(self,origin,destination):
        self.amadeus_endpoint="https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.amadeus_parameters={
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": tomorrow,
            "adults": "1",
            
        }
        with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day39/Cheap_Flights/auth.json","r") as filp:
            self.data=json.load(filp)
        self.amadeus_header={
            "Authorization":f"{self.data['token_type']} {self.data['access_token']}"
        }

        response=requests.get(url=self.amadeus_endpoint,params=self.amadeus_parameters,headers=self.amadeus_header)
        print(f"Status Code: {response.status_code}")
        
