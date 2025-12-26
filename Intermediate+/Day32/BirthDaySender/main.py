import datetime as dt
import random
import pandas as pd
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

data = pd.read_csv("birthdays.csv")

email = os.environ.get("EMAIL")
email_app_pass = os.environ.get("EMAIL_APP_PASS")

today = dt.datetime.today()

for index, row in data.iterrows():
    if row["day"] == today.day and row["month"] == today.month:
        try:
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
                letter = file.read().replace("[NAME]", row["name"])
        
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(email, email_app_pass)
                connection.sendmail(
                    from_addr=email,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday!!\n\n{letter}"
                )
            print(f"Birthday email sent to {row['name']}")
        except:
            print("Failed")
