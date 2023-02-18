import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.String)


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class Director(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))


db.create_all()

# with app.app_context():
#     db.create_all()
#     with open('fixtures.json', 'r', encoding='utf-8') as f:
#         json_data = json.load(f)
#
#     for movie in json_data["movies"]:
#         movie_ = Movie(
#             title=movie['title'],
#             description=movie['description'],
#             trailer=movie['trailer'],
#             year=movie['year'],
#             rating=movie['rating'],
#             genre_id=movie['genre_id'],
#             director_id=movie['director_id'],
#             id=movie['pk']
#         )
#         db.session.add(movie_)
#
#     for director in json_data["directors"]:
#         director_ = Director(
#             name=director['name'],
#             id=director['pk']
#         )
#         db.session.add(director_)
#
#     for genre in json_data["genres"]:
#         genre_ = Genre(
#             name=genre['name'],
#             id=genre['pk']
#         )
#         db.session.add(genre_)
#
#     db.session.commit()

if __name__ == "__main__":
    app.run()
