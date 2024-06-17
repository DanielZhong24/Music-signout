from app import db

class user(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, priamry_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password