from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from app.models import Order, Item, ItemType, Table, OrderedItem, Order
from app.forms.AddItem import AddItemForm

bp = Blueprint("orders", __name__, url_prefix="")

@bp.route("/")
@login_required
def index():
    items = Item.query.all()
    orders = Order.query.filter_by(employee_id = current_user.id).all()
    form=AddItemForm()
    return render_template("orders.html", orders=orders, items=items, form=form)