from app import db
from flask_login import UserMixin


# User is the teacher user and pass
# Defines the user model wich represents the user table in the databse
class User(UserMixin,db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    # Constructor for initializing users
    def __init__(self, username, password):
        self.username = username
        self.password = password