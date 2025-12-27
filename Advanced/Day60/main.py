from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email=os.environ.get("EMAIL")
email_pass=os.environ.get("EMAIL_APP_PASS")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="GET":
        return render_template("contact.html",contact_us="Contact Me")
    elif request.method=="POST":
        data=request.form
        nm=data["name"]
        em=data["email"]
        ph=data["phone"]
        ms=data["message"]
        try:
            with smtplib.SMTP("smtp.gmail.com",587) as connections:
                formatted_msg=f"Subject:Form\n\nName:{nm}\nEmail:{em}\nPhone:{ph}\nmessage:{ms}"
                connections.starttls()
                connections.login(user=email,password=email_pass)
                connections.sendmail(
                    from_addr=email,
                    to_addrs="ingeneral219@gmail.com",
                    msg=formatted_msg
                )
            return render_template("contact.html",contact_us="Successfully Sent")
        except:
            return render_template("contact.html",contact_us="Not Sent")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
