import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import json

load_dotenv()

ninja_api=os.environ.get("NINJA_API")

today=datetime.now()
current_date=today.strftime("%Y/%m/%d")
current_time=today.strftime("%H:%M:%S")


sheets_api_endpoint="https://api.sheety.co"
ninja_api_endpoint="https://api.api-ninjas.com/v1/caloriesburned"

excercise=input("What did you do for workout??\n").title()
duration=int(input("For How long??\n"))

ninja_config={
    "activity":excercise,
    "duration":duration,
}

ninja_header={
    "X-Api-Key":ninja_api
}

ninja_response=requests.get(url=ninja_api_endpoint,params=ninja_config,headers=ninja_header)
ninja_response.raise_for_status()

calories_burned=ninja_response.json()[0]["total_calories"]



sheets_config={
    "id":os.environ.get("SHEET_ID"),
    "name":"workoutTracker",
    "sheetno":"sheet1",
}

sheets_url=f"{sheets_api_endpoint}/{sheets_config['id']}/{sheets_config['name']}/{sheets_config['sheetno']}"

post_request={
    "sheet1": {
        "date": current_date,
        "time": current_time,
        "excercise": excercise,
        "duration": duration,
        "calories": calories_burned,
    }
}

post_response=requests.post(url=sheets_url,json=post_request)

response=requests.get(url=sheets_url)
response.raise_for_status()
