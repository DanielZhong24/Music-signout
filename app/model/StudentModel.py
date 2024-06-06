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

    __table_args__ = (db.UniqueConstraint('student','student_id', name="unique_student_id"),)
    def __init__(self,student_firstName,student_lastName,student_id,grade):
        self.student_firstName = student_firstName
        self.student_lastName = student_lastName
        self.student_id = student_id
        self.grade = grade
     