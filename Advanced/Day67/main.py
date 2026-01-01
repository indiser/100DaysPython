from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
app.config['CKEDITOR_PKG_TYPE'] = 'full'

# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# with app.app_context():
#     db.create_all()

#WTFform and Ckeditor
class BlogSubmissionForm(FlaskForm):
    blog_post_title=StringField(label="Blog Post Title",validators=[DataRequired()])
    subtitle=StringField(label="Subtitle",validators=[DataRequired()])
    your_name=StringField(label="Your Name",validators=[DataRequired()])
    blog_image_url=StringField(label="Blog Image Url",validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit_post=SubmitField(label="Submit Post")

@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    results=db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    posts=results.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post",methods=["GET","POST"])
def add_new_post():
    blogpostform=BlogSubmissionForm()
    if  blogpostform.validate_on_submit():
        new_post = BlogPost(
            title=blogpostform.blog_post_title.data,
            subtitle=blogpostform.subtitle.data,
            body=blogpostform.body.data,
            img_url=blogpostform.blog_image_url.data,
            author=blogpostform.your_name.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html",form=blogpostform)

# TODO: edit_post() to change an existing blog post
@app.route("/edit_post/<int:post_id>",methods=["GET","POST"])
def edit_post(post_id):
    post=db.get_or_404(BlogPost,post_id)
    edit_form=BlogSubmissionForm(
        blog_post_title=post.title,
        subtitle=post.subtitle,
        body=post.body,
        image_url=post.img_url,
        your_name=post.author,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.blog_post_title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.blog_image_url.data
        post.author = edit_form.your_name.data
        post.body = edit_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html",form=edit_form,is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    blog_to_delete=db.get_or_404(BlogPost,post_id)
    db.session.delete(blog_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
