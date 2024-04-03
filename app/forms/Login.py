from flask_wtf import FlaskForm;
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models import Order, Item

validators = [DataRequired()]

class LoginForm(FlaskForm):
    employee_number = StringField('Employee number', validators)
    password = PasswordField('Password', validators)
    submit = SubmitField('Login', validators)