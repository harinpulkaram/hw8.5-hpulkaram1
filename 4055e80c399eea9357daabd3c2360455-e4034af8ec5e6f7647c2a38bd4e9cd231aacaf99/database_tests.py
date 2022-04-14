import flask
from flask_sqlalchemy import SQLAlchemy
from database import Rating

app = flask.Flask(__name__)
db = SQLAlchemy(app)

class Pnt(Model, Rating):
     __tablename__ = 'pnt'

     id = db.Column(db.Integer, db.Integer, db.String(80), db.Integer)
     ...
     def copy(self):
         return copy