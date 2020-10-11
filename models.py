import os
from sqlalchemy import Column, String, Integer, create_engine, Date
from flask_sqlalchemy import SQLAlchemy
import json

# Database
# ------------------------------------------------------
database_name = "casting"
database_path = "postgresql://postgres:root@{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

# binds a flask application and a SQLAlchemy service
# ------------------------------------------------------
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# ------------------------------------------------------
# Models
# ------------------------------------------------------

# Movie model
# ------------------------------------------------------
class Movie(db.Model):  
  __tablename__ = 'movies'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)

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
      'release_date': self.release_date,
    }

# Actor model
# ------------------------------------------------------
class Actor(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(Integer)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age

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
        'name': self.name,
        'age': self.age,
        'gender': 'Male' if self.gender else 'Female',
        }