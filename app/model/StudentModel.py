# app/model/StudentModel.py

from .. import db

class MusicStudent(db.Model):
    __tablename__ = 'music_students'
    id = db.Column(db.Integer, primary_key=True)
    student_firstName = db.Column(db.String(80), nullable=False)
    student_lastName = db.Column(db.String(80), nullable=False)
    student_id = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    #make contructor
