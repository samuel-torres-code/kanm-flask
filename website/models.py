from . import db #from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #foreign key, use lowercase bc sql syntax


class User(db.Model, UserMixin): #inherits UserMixin and db.Model
    id = db.Column(db.Integer, primary_key = True) #primary key
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #connects  to children(notes), use python Syntax



