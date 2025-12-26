import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.environ.get("EMAIL")
email_app_pass = os.environ.get("EMAIL_APP_PASS")

try:
    with open("C:/Users/ranab/OneDrive/Desktop/100Days Python/Intermediate+/Day32/quotes.txt","r") as filp:
        contents=filp.readlines()
except:
    print("File not found")


monday=dt.datetime.today().weekday()

if monday==0:
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(email,email_app_pass)
            connection.sendmail(
                from_addr=email,
                to_addrs="ingeneral219@gmail.com",
                msg=f"Subject:Monday Motivation\n\n{random.choice(contents)}"
            )
            contents.pop()
            print("Success")
    except:
        print("Failed")
else:
    print(f"Today is:{monday}")