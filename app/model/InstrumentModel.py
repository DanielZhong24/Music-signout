# app/models/instrument.py
from app import db

# Defines the instrument model which represnts the instrument table in the database
class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument_type = db.Column(db.String(80), nullable=False)
    instrument = db.Column(db.String(80), nullable=False)
    case_number = db.Column(db.String(80), nullable=False)
    condition = db.Column(db.String(80), nullable=False)
    bar_code = db.Column(db.String(80), nullable=False)
    current_borrower = db.Column(db.String(20), db.ForeignKey('music_students.student_id'), nullable=True)
        
    # Defines a unique constraint on the combination of instrument and case number    
    __table_args__ = (db.UniqueConstraint('instrument', 'case_number', name="unique_instrument_case"),)
    
    # Constructor for initializing instruments
    def __init__(self, instrument_type, instrument, case_number, condition, bar_code, current_borrower=None):
        self.instrument_type = instrument_type
        self.instrument = instrument
        self.case_number = case_number
        self.condition = condition
        self.bar_code = bar_code
        self.current_borrower = current_borrower
