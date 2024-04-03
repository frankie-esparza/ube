from flask_wtf import FlaskForm;
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models import Order, Item

default = [DataRequired()]

class AddItemForm(FlaskForm):
#     with app.app_context():
#         items = Item.query.all()
#         orders = Order.query.all()

#     item_choices = map(lambda x: x.name, items)
#     order_choices = map(lambda x: x.name, orders)

    # order_id = SelectField('Order Id', validators=default, choices = order_choices)
    # item = SelectField('Item', validators=default, choices=item_choices)

    order_id = StringField('Order Id', validators=default)
    item = StringField('Item', validators=default)
    submit = SubmitField('Submit')