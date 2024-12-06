from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
import os

TOKEN = os.environ.get("TOKEN")

class Form(FlaskForm):
    rating = StringField(label='New Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField()

class MovieForm(FlaskForm):
    movie_name = StringField(label='Movie', validators=[DataRequired()])
    submit = SubmitField(label="Add movie")

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(400), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String, nullable=True)
    img_url: Mapped[str] = mapped_column(String, nullable=False)




with app.app_context():
    db.create_all()
def create_record(movie_info):
    with app.app_context():
        new_movie = Movie(
        title=movie_info["original_title"],
        year=movie_info["release_date"].split("-")[0],
        description=movie_info["overview"],
        rating=0,
        ranking=0,
        review="None",
        img_url=f"https://media.themoviedb.org/t/p/w220_and_h330_face{movie_info["poster_path"]}")
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.id


def read_all_records():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        movies = result.scalars().all()
        return movies

def read_specific_record(movie_id):
    with app.app_context():
        result = db.session.execute(db.select(Movie).where(Movie.id == movie_id))
        movie = result.scalar()
        return movie

def update_record(movie_id, rating, review):
    with app.app_context():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie_to_update.rating = rating
        movie_to_update.review = review
        db.session.commit()

def update_record_ranking(movie_id, ranking):
    with app.app_context():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie_to_update.ranking = ranking
        db.session.commit()

def delete_record(movie_id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()

@app.route("/")
def home():
    movies = read_all_records()[::-1]
    for position in range(len(movies)):
        ranking = position+1
        update_record_ranking(movie_id=movies[position].id, ranking=ranking)
        movies[position].ranking = position+1

    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    movie_form = MovieForm()
    url="https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {TOKEN}"
    }
    if movie_form.validate_on_submit():
        parameters = {
        "query": movie_form.movie_name.data
        }
        response = requests.get(url=url, params=parameters, headers=headers).json()
        print(response["results"])
        return render_template("select.html", options=response["results"])
    return render_template("add.html", form=movie_form)

@app.route("/add_movie")
def add_movie():
    movie_id = request.args.get("id")
    url="https://api.themoviedb.org/3/movie"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url=f"{url}/{movie_id}", headers=headers).json()
    new_movie_id = create_record(response)
    return redirect(f"/update?id={new_movie_id}")


@app.route("/update", methods=["GET", "POST"])
def update():
    movie_id = request.args.get("id")
    movie = read_specific_record(movie_id=movie_id)
    form = Form()
    if form.validate_on_submit():
        update_record(movie_id=movie_id, rating=float(form.rating.data), review=form.review.data)
        return redirect("/")
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    delete_record(movie_id)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
