# app/controller/StudentController.py

from flask import Blueprint, render_template
from ..model.StudentModel import MusicStudent

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/students')
def students():
    # students = MusicStudent.query.all()
    students = MusicStudent.query.filter_by(student_lastName = "Truong").all()
    return render_template('student/student.html', students=students)
