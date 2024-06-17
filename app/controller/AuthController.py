from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.model.UserModel import User
from app.forms import LoginForm, RoleSelectForm
from app import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return redirect(url_for('auth_bp.role_select'))

@auth_bp.route('/role_select', methods=['GET', 'POST'])
def role_select():
    form = RoleSelectForm()
    if form.validate_on_submit():
        if form.role.data == 'teacher':
            return redirect(url_for('auth_bp.login'))
        else:
            return redirect(url_for('instrument_bp.signout_instrument'))
    return render_template('auth/role_select.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('auth_bp.home'))  # Update this to redirect to a suitable page after login
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.role_select'))
