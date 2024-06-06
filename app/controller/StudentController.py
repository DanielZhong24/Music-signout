# app/controller/StudentController.py

from flask import Blueprint, render_template
from ..model.StudentModel import MusicStudent

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/student')
def students():
    students = MusicStudent.query.all()
    # students = MusicStudent.query.filter_by(student_lastName = "Truong").all()
    return render_template('student/student.html', students=students)

@student_bp.route('/addStudent', methods=['GET', 'POST'])
def add_instrument():
    if request.method == 'POST':
        student_firstName = request.form['student_firstName']
        student_lastName = request.form['student_lastName']
        student_id = request.form['student_id']
        grade = request.form['grade']
        
        existing_student = students.query.filter_by(students=students,student_id=student_id).first()
        if existing_student:
            flash('Student with the same student number already exists!', 'danger')
            return redirect(url_for('student_bp.add_student'))
        new_student = Student(student_firstName, student_lastName, student_id, grade)
        db.session.add(new_student)
        db.session.commit()

        flash('Student added successfully!', 'success')
        return redirect(url_for('student_bp.add_student'))

    return render_template('student/add_student.html')