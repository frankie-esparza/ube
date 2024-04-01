from flask_wtf import FlaskForm;
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    validators = [DataRequired()]
    employee_number = StringField('Employee number', validators)
    password = PasswordField('Password', validators)
    submit = SubmitField('Login', validators)