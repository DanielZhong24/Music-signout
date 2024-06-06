# app/model/StudentModel.py

from .. import db

class Instrument(db.Model):
    __tablename__ = 'instruments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instrument_type = db.Column(db.String(80), nullable=False)
    instrument = db.Column(db.String(80), nullable=False)
    case_number = db.Column(db.String(80), nullable=False)
    condition = db.Column(db.String(80), nullable=False)
    bar_code = db.Column(db.String(80), nullable=False)
    current_borrower = db.Column(db.String(80), nullable=True)
    
    __table_args__ = (db.UniqueConstraint('instrument','case_number', name="unique_instrument_case"),)
    def __init__(self,instrument_type,instrument,case_number,condition,bar_code,current_borrower=None):
        self.instrument_type = instrument_type
        self.instrument = instrument
        self.case_number = case_number
        self.condition = condition
        self.bar_code = bar_code
        self.current_borrower = current_borrower