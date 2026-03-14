from flask import Flask, render_template,url_for,request,redirect
import smtplib
import os
from dotenv import load_dotenv
from string import Template

load_dotenv()

from string import Template

EMAIL_TEMPLATE = Template("""
Portfolio Contact Form Submission

Subject: $subject

Contact Information:
- Name: $name
- Email: $email

Message:
$message

---
Sent via Portfolio Contact Form
""")

def format_portfolio_contact_email(name: str, email: str, subject: str, message: str) -> str:
    # Sanitize inputs
    sanitized = {
        'name': name.replace('\n', ' ').replace('\r', ' ').strip(),
        'email': email.replace('\n', ' ').replace('\r', ' ').strip(),
        'subject': subject.replace('\n', ' ').replace('\r', ' ').strip(),
        'message': message.strip()
    }
    
    return EMAIL_TEMPLATE.substitute(**sanitized)

My_email=os.environ.get("EMAIL")
My_pass=os.environ.get("EMAIL_APP_PASS")

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/messege",methods=["GET","POST"])
def send_msg():
    if request.method=="POST":
        data=request.form
        name=data.get('name')
        email=data.get('email')
        subject=data.get('subject')
        message=data.get('message')
        try:
            formatted_msg = format_portfolio_contact_email(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            email_subject = f"New Portfolio Contact: {subject}"
            full_message = f"Subject: {email_subject}\n\n{formatted_msg}"
            
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=My_email,password=My_pass)
                connection.sendmail(
                    from_addr=My_email,
                    to_addrs=My_email,
                    msg=full_message
                )
            return redirect(url_for('home',success=True))
        except Exception as e:
            print(f"Error: {e}")
            return redirect(url_for('home',success=False))
    return render_template("index.html", success=False)
    


if __name__=="__main__":
    app.run(debug=True)