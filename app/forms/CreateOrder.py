from flask_wtf import FlaskForm;
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

default = [DataRequired()]

class CreateOrderForm(FlaskForm):
    employee = SelectField('Employee', validators=default)
    table = SelectField('Table', validators=default)
    submit = SubmitField('Submit')