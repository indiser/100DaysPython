import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.environ.get("EMAIL")
email_app_pass = os.environ.get("EMAIL_APP_PASS")

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, email_app_pass)
        connection.sendmail(
            from_addr=email,
            to_addrs="ingeneral219@gmail.com",
            msg="Subject:Hello\n\nThis is the body of my email."
        )
        print("Success")
except:
    print("Failed")
