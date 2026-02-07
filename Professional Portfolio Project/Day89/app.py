from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

app=Flask(__name__)
db = SQLAlchemy(model_class=Base)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db.init_app(app)

class TODOLIST(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  task=db.Column(db.String(250),unique=True)
  status=db.Column(db.String(250))

# with app.app_context():
#   db.create_all()

@app.route("/")
def home():
    results=db.session.execute(db.select(TODOLIST))
    tasks=results.scalars().all()
    return render_template("index.html",tasks=tasks)


@app.route("/add",methods=["POST"])
def addTask():
  if request.method=="POST":
    new_task=TODOLIST(
      task=request.form.get('form1'),
      status="In Progress"
    )
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/finish",methods=["GET","POST"])
def finishTask():
   id=request.args.get("task_id")
   task_by_id=db.get_or_404(TODOLIST,id)
   task_by_id.status="Finished"
   db.session.commit()
   return redirect(url_for('home'))

@app.route("/delete",methods=["GET","POST"])
def deleteTask():
   id=request.args.get("task_id")
   task_by_id=db.get_or_404(TODOLIST,id)
   db.session.delete(task_by_id)
   db.session.commit()
   return redirect(url_for('home'))
   

if __name__=="__main__":
    app.run(debug=True)