import sys,os

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from wtforms import Form, BooleanField, StringField, PasswordField, validators, DateField

class RegistrationForm(Form):
    firstname = StringField('Firstname', [validators.Length(min=4, max=25)])
    lastname = StringField('Lastname', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    dateOfBirth = DateField('Date of Birth', format='%Y-%m-%d')
    contactno = StringField('Contact Number', [validators.Length(min=11, max=11)])
    

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [validators.DataRequired()])   