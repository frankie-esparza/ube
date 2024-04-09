from flask_wtf import FlaskForm;
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired

default = [DataRequired()]

class AddOrRemoveItemForm(FlaskForm):
    item = SelectField('Item', validators=default)
    submit = SubmitField('Submit')