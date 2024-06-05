# app/controller/StudentController.py

from flask import Blueprint, render_template
from ..model.InstrumentModel import Instrument

instrument_bp = Blueprint('instrument_bp', __name__)

@instrument_bp.route('/instrument')
def instruments():
    instruments = Instrument.query.all()
    return render_template('instrument/instrument.html', instruments=instruments)
