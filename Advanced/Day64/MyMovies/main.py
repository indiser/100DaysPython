from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, FloatField,TextAreaField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

tmdb_api=os.environ.get("TMDB_API_KEY")
tmdb_access_token=os.environ.get("TMDB_ACCESS_TOKEN")

tmdb_endpoint="https://api.themoviedb.org/3/search/movie"



class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///New_Movies.db"
db.init_app(app)

# CREATE DB
class Movies(db.Model):
    id: Mapped[int]=mapped_column(Integer,primary_key=True,nullable=False)
    title: Mapped[str]=mapped_column(String(250),unique=False,nullable=False)
    year: Mapped[int]=mapped_column(Integer,nullable=False)
    description: Mapped[str]=mapped_column(String(500),nullable=False)
    rating: Mapped[float]=mapped_column(Float,nullable=True)
    ranking: Mapped[int]=mapped_column(Integer,nullable=True)
    review: Mapped[str]=mapped_column(String(250),nullable=True)
    img_url: Mapped[str]=mapped_column(String(250),nullable=False)
    def __repr__(self):
        return f'<Movies {self.title}>'


# with app.app_context():
#     db.create_all()

# CREATE TABLE
class MyForm(FlaskForm):
    rating = FloatField(label="Your Rating out of 10 e.g 7.5",validators=[DataRequired()])
    review=TextAreaField(label="Your Review",validators=[DataRequired()])
    submit=SubmitField(label="Done")


class titleForm(FlaskForm):
    title=StringField(label="Movie Title",validators=[DataRequired()])
    add_movie=SubmitField(label="Add Movies")


headers={
    "accept": "application/json",
    "Authorization": f"Bearer {tmdb_access_token}"
}


@app.route("/")
def home():
    # read
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html",movies=all_movies)


@app.route("/edit",methods=["GET","POST"])
def edit():
    bootstrap_form=MyForm()
    movie_id=request.args.get("id")
    movie_selected=db.get_or_404(Movies,movie_id)
    if bootstrap_form.validate_on_submit():
        if request.method=="POST":
            movie_selected.rating=float(bootstrap_form.rating.data)
            movie_selected.review=bootstrap_form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html",movie=movie_selected,form=bootstrap_form)


@app.route("/delete",methods=["GET","POST"])
def delete():
    movie_id=request.args.get('id')
    movie_to_delete = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    


@app.route('/add',methods=["GET","POST"])
def add():
    titleform=titleForm()
    if titleform.validate_on_submit():
        parameters={
            "query":titleform.title.data,
        }
        response=requests.get(url=tmdb_endpoint,headers=headers,params=parameters)
        all_movies=response.json()["results"]
        return render_template("select.html",results=all_movies)
    return render_template("add.html",form=titleform)



@app.route("/find")
def find_movie():
    movie_id=request.args.get("id")
    if movie_id:
        tmdb_id_endpoint=f"https://api.themoviedb.org/3/movie/{movie_id}"

        response=requests.get(url=tmdb_id_endpoint,headers=headers)
        data=response.json()
        new_movie=Movies(
            title=data["title"],
            year=int(data["release_date"].split("-")[0]),
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit',id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)

