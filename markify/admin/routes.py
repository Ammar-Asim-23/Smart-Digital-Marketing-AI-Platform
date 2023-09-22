import os
import sys

from flask import flash, redirect, render_template, request, session, url_for

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)
from markify import app, bcrypt, db

from .forms import RegistrationForm, LoginForm
from .models import User


@app.route('/', methods=['GET'])
def index():
    return render_template("admin/index.html", title="Admin Page")

@app.route('/admin')
def admin():
    if 'email' not in session:
        flash('Please login first', 'danger')
        return(redirect(url_for('login')))
    return render_template("admin/index.html", title="Admin Page")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
                    password=hash_password, dateOfBirth=form.dateOfBirth.data, contactno=form.contactno.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.firstname.data}! Thank you for registering', "success")
        return redirect(url_for('index'))
    return render_template('admin/register.html', form=form, title="Registration page")


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {user.firstname}! You are logged in now', "success")
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Wrong password! Please try again', "danger")                
    return render_template('admin/login.html', form=form, title="Login page")