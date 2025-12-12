import smtplib

# my_outlook_mail = "ranabanerjee2025@outlook.com"
# my_outlook_app = "apfnjfiouljpvtjm"

email = "ranabanerjee3000@gmail.com"
email_app_pass = "yckg miqt gpnt qhuf"
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
