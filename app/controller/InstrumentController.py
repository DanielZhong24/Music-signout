# app/controller/StudentController.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..model.InstrumentModel import Instrument
from flask_login import login_required, current_user
from ..model.HistoryModel import History
from ..model.StudentModel import MusicStudent
import time
from app import db

instrument_bp = Blueprint('instrument_bp', __name__)

@instrument_bp.route('/instrument',methods=['GET'])
@login_required
def instrument():
    instruments = Instrument.query.all()
    return render_template('instrument/instrument.html', instruments=instruments)

@instrument_bp.route('/addInstrument', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('instrument_bp.instrument'))

    return render_template('instrument/add_instrument.html')

@instrument_bp.route('/delete_instrument/<int:instrument_id>', methods=['POST'])
@login_required
def delete_instrument(instrument_id):
    instrument_to_delete = Instrument.query.get_or_404(instrument_id)

    try:
        db.session.delete(instrument_to_delete)
        db.session.commit()
        flash('Instrument deleted successfully!', 'success')
    except:
        db.session.rollback()
        flash('Error deleting instrument!', 'danger')

    return redirect(url_for('instrument_bp.instrument'))


@instrument_bp.route('/edit_instrument/<int:instrument_id>', methods=['GET', 'POST'])
@login_required
def edit_instrument(instrument_id):
    instrument_to_edit = Instrument.query.get_or_404(instrument_id)

    if request.method == 'POST':
        instrument_to_edit.instrument_type = request.form['instrument_type']
        instrument_to_edit.instrument = request.form['instrument']
        instrument_to_edit.case_number = request.form['case_number']
        instrument_to_edit.condition = request.form['condition']
        instrument_to_edit.bar_code = request.form['bar_code']
        instrument_to_edit.current_borrower = request.form.get('current_borrower', None)

        try:
            db.session.commit()
            flash('Instrument updated successfully!', 'success')
            return redirect(url_for('instrument_bp.instrument'))
        except:
            db.session.rollback()
            flash('Error updating instrument!', 'danger')

    # For GET request to display the edit form
    instruments = Instrument.query.all()  # Or fetch all instruments as needed
    return render_template('instrument/edit_instrument.html', instrument=instrument_to_edit, instruments=instruments)

@instrument_bp.route('/signout', methods=['GET', 'POST'])
def signout_instrument():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        barcode = request.form.get('barcode')
        
        student = MusicStudent.query.filter_by(student_id=student_id).first()
        instrument = Instrument.query.filter_by(bar_code=barcode).first()
        
        if not student or not instrument:
            flash("Invalid student ID or barcode", "danger")
            return render_template('instrument/signout.html')
        
        if instrument.current_borrower:
            flash("Instrument is already borrowed", "danger")
            return render_template('instrument/signout.html')
        
        signout_time = int(time.time())
        
        history_entry = History(
            student_id=student_id,
            instrument_id=barcode,
            signout_time=signout_time,
            notes='Signed out'
        )
        instrument.current_borrower = student_id
        instrument.condition = "In Use"
        
        db.session.add(history_entry)
        db.session.commit()  # Commit the history entry and borrower update
        
        flash("Instrument signed out successfully", "success")
        return redirect(url_for('instrument_bp.signout_instrument'))
    
    return render_template('instrument/signout.html')

@instrument_bp.route('/return', methods=['GET', 'POST'])
def return_instrument():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        barcode = request.form.get('barcode')
        
        student = MusicStudent.query.filter_by(student_id=student_id).first()
        instrument = Instrument.query.filter_by(bar_code=barcode).first()
        
        if not student or not instrument:
            flash("Invalid student ID or barcode", "danger")
            return render_template('instrument/return.html')
        
        if instrument.current_borrower != student_id:
            flash("Instrument not borrowed by this student", "danger")
            return render_template('instrument/return.html')
        
        return_time = int(time.time())
        
        # Find the latest signout entry for this instrument by this student
        history_entry = History.query.filter_by(student_id=student_id, instrument_id=barcode).order_by(History.id.desc()).first()
        
        if history_entry is not None and history_entry.return_time is None:
            history_entry.return_time = return_time
            history_entry.notes = 'Returned'
            instrument.current_borrower = None
            instrument.condition = "Not in Use"
        
            db.session.commit()  # Commit the history entry and borrower update
        
        flash("Instrument returned successfully", "success")
        return redirect(url_for('instrument_bp.return_instrument'))
    
    return render_template('instrument/return.html')

@instrument_bp.route('/history', methods=['GET'])
@login_required
def get_history():
    history = History.query.all()
    result = []
    for entry in history:
        result.append({
            "id": entry.id,
            "student_id": entry.student_id,
            "instrument_id": entry.instrument_id,
            "signout_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(entry.signout_time))) if entry.signout_time else '',
            "return_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(entry.return_time))) if entry.return_time else '',
            "notes": entry.notes
        })
    return render_template('instrument/history.html', history=result)