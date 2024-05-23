from . import db 
from flask_login import UserMixin 
from flask_sqlalchemy import * 
from sqlalchemy.sql import func

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(200))
    tasks = db.relationship('Task')
