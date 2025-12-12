import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint="https://api.sheety.co"
        self.sheety_config={
            "id":os.environ.get("SHEET_ID"),
            "name":"flightDeals",
            "sheetno":"sheet1"
        }
        self.sheety_config_url=f"{self.sheety_endpoint}/{self.sheety_config['id']}/{self.sheety_config['name']}/{self.sheety_config['sheetno']}"
        self.destination_data=[]

    def get_destination_data(self):
        sheet_response=requests.get(url=self.sheety_config_url,params=self.sheety_config)
        sheet_response.raise_for_status()
        data=sheet_response.json()["sheet1"]
        self.destination_data=data
        return data
