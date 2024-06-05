# app/model/StudentModel.py

from .. import db

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True)
    instrument_type = db.Column(db.String(80), nullable=False)
    instrument = db.Column(db.String(80), nullable=False)
    case_number = db.Column(db.String(80), nullable=False)
    condition = db.Column(db.String(80), nullable=False)
    bar_code = db.Column(db.String(80), nullable=False)
    current_borrower = db.Column(db.String(80), nullable=True)
    
    def __repr__(self):
        return f'<MusicStudent {self.name}>'