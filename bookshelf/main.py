from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'{self.title} - {self.author} - {self.rating}'

with app.app_context():
    db.create_all()
def create_new_record(title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author = author, rating = rating)
        db.session.add(new_book)
        db.session.commit()

def read_all_records():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        books = result.scalars().all()
    return books

def read_specific_record(book_id):
    with app.app_context():
        result = db.session.execute(db.select(Book).where(Book.id == book_id))
        book = result.scalar()
    return book

def update_record(book_id, rating):
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.rating = rating
        db.session.commit()

def delete_record(book_id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()


@app.route('/', methods=["GET", "DELETE"])
def home():
    all_books = read_all_records()
    if request.method == "DELETE":
        delete_record()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_dict = request.form.to_dict()
        create_new_record(title=book_dict["title"], author=book_dict["author"], rating=float(book_dict["rating"]))

    return render_template("add.html")

@app.route("/edit", methods=["GET","POST"])
def edit():
    book_id = int(request.args.get("id"))
    book = read_specific_record(book_id=book_id)
    if request.method == "POST":
        response = request.form.to_dict()
        update_record(book_id=book_id, rating=float(response["rating"]))
        book = read_specific_record(book_id=book_id)
        return render_template("edit.html", book=book)
    return render_template("edit.html", book= book)

@app.route("/delete")
def delete():
    book_id = int(request.args.get("id"))
    delete_record(book_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)



