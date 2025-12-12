from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


MY_LONGITUDE=88.363892
MY_LATITUDE=22.572645
api_key=os.environ.get("API_KEY")

parameters={
    "lat":MY_LATITUDE,
    "lon":MY_LONGITUDE,
    "appid":api_key,
    "cnt":4
}


endpoint="https://api.openweathermap.org/data/2.5/forecast"

response=requests.get(url=endpoint,params=parameters)
response.raise_for_status()
will_rain=False
for i in range(0,4):
    data=response.json()["list"][i]["weather"][0]["id"]
    if data<700:
        will_rain=True


if will_rain==True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=os.environ.get("MESSEGING_SERVICE_SID"),
        body="Bring a dam umbralla ☂️",
        to=os.environ.get("MOBILE_NUMBER")
    )
    print(message.status)
else:
    print("No need")
