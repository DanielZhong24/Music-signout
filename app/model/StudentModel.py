from app import db

class MusicStudent(db.Model):
    __tablename__ = 'music_students'

    id = db.Column(db.Integer, primary_key=True)
    student_firstName = db.Column(db.String(50))
    student_lastName = db.Column(db.String(50))
    student_id = db.Column(db.String(20), unique=True)
    grade = db.Column(db.String(10))

    def __init__(self, student_firstName, student_lastName, student_id, grade):
        self.student_firstName = student_firstName
        self.student_lastName = student_lastName
        self.student_id = student_id
        self.grade = grade
