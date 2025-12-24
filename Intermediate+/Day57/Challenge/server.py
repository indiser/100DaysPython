from flask import Flask, render_template
import requests
import datetime
import random
app=Flask(__name__)

@app.route("/")
def welcome():
    random_num=random.randint(1,10)
    year=datetime.date.today().year
    return render_template("index.html",current_year=year,num=random_num,my_name="God")


@app.route("/guess/<name>")
def guess(name):
    agify_endpoint="https://api.agify.io"
    parameters={
        "name": name.title()
    }
    age_response=requests.get(url=agify_endpoint,params=parameters)
    age_response.raise_for_status()
    age=age_response.json()["age"]

    gender_api_endpoint="https://api.genderize.io"
    gender_response=requests.get(url=gender_api_endpoint,params=parameters,timeout=5)
    gender_response.raise_for_status()
    gender=gender_response.json()["gender"]
    return render_template("guess.html",user_name=name,user_age=age,user_gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response=requests.get(blog_url)
    response.raise_for_status()
    all_posts=response.json()
    return render_template("blog.html",posts=all_posts)
if __name__=='__main__':
    app.run(debug=True)