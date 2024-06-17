# app/controller/StudentController.py
# This code defines all the routes for managing music students 
# It includes displaying all the students and adding new students to the database bascailly the same as the instruments
# Imports
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..model.StudentModel import MusicStudent
from flask_login import login_required, current_user
import time
from app import db
# Create a blueprint for the student routes
student_bp = Blueprint('student_bp', __name__)

# Route to display all the students
@student_bp.route('/student', methods=['GET'])
def students():
    # Query all the students from the database
    students = MusicStudent.query.all()
    # Render the template to display the students passing the students data
    return render_template('student/student.html', students=students)

# Rotue to add a new student 
@student_bp.route('/addStudent', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Get data from the user
        student_firstName = request.form['student_firstName']
        student_lastName = request.form['student_lastName']
        student_id = request.form['student_id']
        grade = request.form['grade']


        # Check if a student with the same first name and student ID already exist
        existing_student = MusicStudent.query.filter_by(student_firstName=student_firstName, student_id=student_id).first()
        if existing_student:
            # If the student already exist flash a mesage and redirect back to the add student page
            flash('Student with the same student number already exists!', 'danger')
            return redirect(url_for('student_bp.add_student'))
        
        # Create a new musicstudent objec t with the form data
        new_student = MusicStudent(student_firstName, student_lastName, student_id, grade)
        # Add the new student to the database
        db.session.add(new_student)
        # save the new student in the database
        db.session.commit()

        # Flash that the student was added successfully and redirect to the students page 
        flash('Student added successfully!', 'success')
        return redirect(url_for('student_bp.students'))

    # If the request method is GET render the add a new student
    return render_template('student/add_student.html')

@student_bp.route('/delete_student/<int:student_id>', methods=['POST'])
@login_required
def delete_student(student_id):
    student_to_delete = MusicStudent.query.get_or_404(student_id)

    try:
        db.session.delete(student_to_delete)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    except:
        db.session.rollback()
        flash('Error deleting student!', 'danger')

    return redirect(url_for('student_bp.student'))

@student_bp.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student_to_edit = MusicStudent.query.get_or_404(student_id)

    if request.method == '[POST]':
        student_to_edit.student_firstName = request.form['student_firstName']
        student_to_edit.student_lastName = request.form['student_lastName']
        student_to_edit.student_id = request.form['student_id']
        student_to_edit.grade = request.form['grade']

        try:
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('student_bp.student'))
        except:
            db.session.rollback()
            flash('Error updating student!', 'danger')

    students = MusicStudent.query.all()
    return render_template('student/edit_student.html', student=student_to_edit, students=students)

