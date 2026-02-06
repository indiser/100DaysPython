from flask import Flask, render_template,redirect,request,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, URLField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5

class CafeForm(FlaskForm):
    name=StringField('name',validators=[DataRequired()])
    locations=StringField('location',validators=[DataRequired()])
    map_url=URLField('map_url')
    sockets=BooleanField('has_sockets')
    toilets=BooleanField('has_toilets')
    wifi=BooleanField('has_wifi')
    calls=BooleanField('can_take_calls')
    seats=StringField('seats',validators=[DataRequired()])
    submit=SubmitField('Submit')

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)
Bootstrap5(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500))
    location = db.Column(db.String(250), nullable=False)
    
    # The Booleans
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    
    # The Stats
    seats = db.Column(db.String(250), nullable=False)

# with app.app_context():
#     db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/styles_listing")
def styleinfo():
    return render_template("styles.html")

@app.route("/listings",methods=["POST","GET"])
def listings():
    results=db.session.execute(db.select(Cafe))
    all_results=results.scalars().all()
    return render_template("list.html",listing=all_results)


@app.route("/add",methods=["POST","GET"])
def addinfo():
    form=CafeForm()
    if form.validate_on_submit():
        new_cafe=Cafe(
            name=form.name.data,
            location=form.locations.data,
            map_url=form.map_url.data,
            has_sockets=form.sockets.data,
            has_toilet=form.toilets.data,
            has_wifi=form.wifi.data,
            can_take_calls=form.calls.data,
            seats=form.seats.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        print("Added Successfully")
        return redirect(url_for('listings'))
    return render_template("add.html",form=form)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_cafe(id):
    cafe_to_delete = db.get_or_404(Cafe, id)
    
    db.session.delete(cafe_to_delete)
    db.session.commit()
    
    flash("Cafe deleted successfully.") 
    
    return redirect(url_for('listings'))


if __name__=="__main__":
    app.run(debug=True)