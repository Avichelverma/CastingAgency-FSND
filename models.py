import os
from sqlalchemy import Column, String, Integer, create_engine, Table, ForeignKey, DateTime
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'castingagency'
database_path = "postgres://{}:{}@{}/{}".format(
    'postgres', 'avi_1074', 'localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
-------
Models
-------
'''

# Movies list

movie_list = db.Table('movie_list',
                      db.Column('movie_id', Integer, ForeignKey(
                          'movie.id'), primary_key=True),
                      db.Column('actor_id', Integer, ForeignKey(
                          'actor.id'), primary_key=True))

# Movie Model


class Movie(db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


# Actor Model

class Actor(db.Model):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    movies = db.relationship(
        'Movie', secondary=movie_list, backref=db.backref('actors'), lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
