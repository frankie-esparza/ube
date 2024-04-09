from flask_wtf import FlaskForm;
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

default = [DataRequired()]

class SignupForm(FlaskForm):
    name = StringField('Name', validators=default)
    employee_number = StringField('Employee number', validators=default)
    password = PasswordField('Password', validators=default)
    submit = SubmitField('Submit', validators=default)