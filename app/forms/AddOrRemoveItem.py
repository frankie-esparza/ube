from flask_wtf import FlaskForm;
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired

default = [DataRequired()]

class AddOrRemoveItemForm(FlaskForm):
    item = RadioField('Item', validators=default)
    submit = SubmitField('Submit')