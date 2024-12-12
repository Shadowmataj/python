from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm.exc import UnmappedInstanceError
from random import choice
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):  # This is a dictionary comprehension function created inside the Cafe class definition. It will be used to turn rows into a dictionary before sending it to jsonify.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.get("/all")
def all_cafe():
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        all_cafes = result.scalars().all()
        return jsonify(payload=[cafe.to_dict() for cafe in all_cafes])


@app.get("/random")
def random():
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
        random_cafe = choice(all_cafes)
        return jsonify(cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        })

@app.get("/search")
def search():
    location = request.args.get("loc")
    with app.app_context():
        result = db.session.execute(db.select(Cafe).where(Cafe.location == location.title()))
        all_cafes = result.scalars().all()
        if not all_cafes:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

# HTTP POST - Create Record
@app.post("/add")
def add():
    form = request.form.to_dict()
    with app.app_context():
        new_book = Cafe(name=form["name"],
                        map_url=form["map_url"],
                        img_url=form["img_url"],
                        location=form["location"],
                        seats=form["seats"],
                        has_toilet=bool(form["has_toilet"]),
                        has_wifi=bool(form["has_wifi"]),
                        has_sockets=bool(form["has_sockets"]),
                        can_take_calls=bool(form["can_take_calls"]),
                        coffee_price=form["coffee_price"])
        db.session.add(new_book)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.patch("/update-price/<cafe_id>")
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    with app.app_context():
        result = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
        cafe_to_update = result.scalar()
        try:
            cafe_to_update.coffee_price = new_price
        except AttributeError:
            return jsonify(error={ "Not found": "Sorry a cafe with that id was not found in the database."}),404
        else:
            db.session.commit()
            return jsonify(success="Successfully updated the price"),200

# HTTP DELETE - Delete Record

@app.delete("/report-closed/<cafe_id>")
def report_closed(cafe_id):
    api_key = request.args.get("api_key")
    if api_key != "TopSecretApiKey":
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key.")
    with app.app_context():
        result = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
        cafe_to_delete = result.scalar()
        try:
            db.session.delete(cafe_to_delete)
        except UnmappedInstanceError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}),404
        else:
            db.session.commit()
            return jsonify(success="Successfully deleted the cafe"),200

if __name__ == '__main__':
    app.run(debug=True)
