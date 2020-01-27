#this defines the table in database
from app.ext import db

#model is about database
#this is database table
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100))