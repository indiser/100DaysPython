from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def log():
    username=request.form.get("username")
    password=request.form.get("password")
    return f"<h1> Name:{username} Password:{password}</h1>"

if __name__=="__main__":
    app.run(debug=True)