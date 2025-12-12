import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.email=os.environ.get("EMAIL")
        self.password=os.environ.get("EMAIL_APP_PASS")
        self.to_email=os.environ.get("ADDRESS_EMAIL")

    def send_notification(self,price,origin,destination,start_date,end_date):
        with smtplib.SMTP("smtp.gmail.com",587) as connections:
            formatted_msg=f"Subject:Low Price Alert!\n\nOnly ${price} to fly from {origin} to {destination}, from {start_date} to {end_date}"
            connections.starttls()
            connections.login(user=self.email,password=self.password)
            connections.sendmail(
                from_addr=self.email,
                to_addrs=self.to_email,
                msg=formatted_msg
            )