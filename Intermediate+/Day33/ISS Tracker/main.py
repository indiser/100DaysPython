import requests
from datetime import datetime, timezone
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()

MY_LONGITUDE=88.363892
MY_LATITUDE=22.572645

email = os.environ.get("EMAIL")
email_app_pass = os.environ.get("EMAIL_APP_PASS")


def is_overhead():
    iss_position=requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_position.raise_for_status()
    data=iss_position.json()
    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])
    if MY_LATITUDE-5<=latitude<=MY_LATITUDE+5 and MY_LONGITUDE-5<=longitude<=MY_LONGITUDE+5:
        return True
    return False


def is_dark():
    parameters={
        "lat":MY_LATITUDE,
        "lng":MY_LONGITUDE,
        "formatted":0,
    }

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    today_hour=datetime.now(timezone.utc).hour
    if today_hour >= sunset or today_hour < sunrise:
        return True
    return False

while True:
    if is_overhead() and is_dark():
        try:
            with smtplib.SMTP("smtp.gmail.com",587) as connections:
                connections.starttls()
                connections.login(email,email_app_pass)
                connections.sendmail(
                    to_addrs="ingeneral219@gmail.com",
                    from_addr=email,
                    msg="Subject:LOOK UP!!\n\nISS is above you"
                )
            print("Success")
        except Exception as e:
            print(f"Failed:{e}")
    else:
        print("Not yet")
    time.sleep(60)

