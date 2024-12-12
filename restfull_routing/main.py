import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
# from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''



app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Form(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    background_img = StringField(label= 'Background image', validators=[DataRequired(), URL()])
    body = CKEditorField('body', validators=[DataRequired()])
    submit = SubmitField()

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post')
def show_post():
    post_id = request.args.get("post_id")
    # TODO: Retrieve a BlogPost from the database based on the post_id
    result = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    requested_post = result.scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = Form()
    if form.validate_on_submit():
        date=datetime.datetime.now()
        form_info = request.form.to_dict()
        new_blog = BlogPost(
            title=form_info["title"],
            subtitle=form_info["subtitle"],
            body=form_info["body"],
            date= date.strftime("%B %d, %Y"),
            author=form_info["author"],
            img_url=form_info["background_img"],
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for("new_post"))
    return render_template("make-post.html", form=form, view="New Post")

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET","POST"])
def edit_post(post_id):
    blog = db.get_or_404(BlogPost, post_id)
    form = Form(
            title=blog.title,
            subtitle=blog.subtitle,
            body=blog.body,
            author=blog.author,
            background_img=blog.img_url
    )
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.body = form.body.data
        blog.author = form.author.data
        blog.background_img = form.background_img.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=blog.id))

    return render_template("make-post.html", form=form, view="Edit post")

# TODO: delete_post() to remove a blog post from the database

@app.route("/delete-post/<post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/")


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
