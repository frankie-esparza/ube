from flask_wtf import FlaskForm;
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

default = [DataRequired()]

class UpdateOrderForm(FlaskForm):
    order = SelectField('Order', validators=default)
    item = SelectField('Item', validators=default)
    submit = SubmitField('Submit')