# app/controller/StudentController.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..model.InstrumentModel import Instrument
from app import db
instrument_bp = Blueprint('instrument_bp', __name__)

@instrument_bp.route('/instrument',methods=['GET'])
def instrument():
    instruments = Instrument.query.all()
    return render_template('instrument/instrument.html', instruments=instruments)

@instrument_bp.route('/addInstrument', methods=['GET', 'POST'])
def add_instrument():
    if request.method == 'POST':
        instrument_type = request.form['instrument_type']
        instrument = request.form['instrument']
        case_number = request.form['case_number']
        condition = request.form['condition']
        bar_code = request.form['bar_code']
        current_borrower = request.form.get('current_borrower', None)

        existing_intrument = Instrument.query.filter_by(instrument=instrument,case_number=case_number).first()
        if existing_intrument:
            flash('Instrument with the same case number already exists!', 'danger')
            return redirect(url_for('instrument_bp.add_instrument'))
        new_instrument = Instrument(instrument_type, instrument, case_number, condition, bar_code, current_borrower)
        db.session.add(new_instrument)
        db.session.commit()

        flash('Instrument added successfully!', 'success')
        return redirect(url_for('instrument_bp.add_instrument'))

    return render_template('instrument/add_instrument.html')