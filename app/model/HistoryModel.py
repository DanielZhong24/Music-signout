
from .. import db

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(50), db.ForeignKey('music_students.student_id'), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey('instruments.bar_code'), nullable=False)    
    signout_time = db.Column(db.String(100), nullable=False)
    return_time = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'instrument_id', 'signout_time', name='uix_student_instrument_signout'),
    )