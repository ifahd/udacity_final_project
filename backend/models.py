import os
from sqlalchemy import Column, String, Integer, create_engine, Date
from flask_sqlalchemy import SQLAlchemy
import json
import datetime

# Database
# ------------------------------------------------------
database_name = "casting"
database_path = "postgresql://postgres:root@{}/{}".format('localhost:5432', database_name)
# database_path = os.environ['DATABASE_URL']

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

# Formatter Date  
# ------------------------------------------------------
def formatter_date(date):
  format_date = None
  try:
    date = datetime.datetime.strptime(date, '%d/%m/%Y')
    format_date = date.strftime('%Y-%m-%d')
  except:
    format_date = date 
  return date 


# Movie model
# ------------------------------------------------------
class Movie(db.Model):  
  __tablename__ = 'movies'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(String)

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
      'release_date': formatter_date(self.release_date),
    }

# Actor model
# ------------------------------------------------------
class Actor(db.Model):
  __tablename__ = 'actors'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  gender = Column(String)
  age = Column(Integer)
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
      return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      }