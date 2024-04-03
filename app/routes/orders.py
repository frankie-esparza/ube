from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Order, Item, Order, Employee, Table
from app.forms.UpdateOrder import UpdateOrderForm
from app.forms.CreateOrder import CreateOrderForm

bp = Blueprint("orders", __name__, url_prefix="")

@login_required
@bp.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("orders.html", orders=employeesOrders())
    return redirect(url_for("session.login"))



@login_required
@bp.route("/update-order", methods=["GET"])
def updateOrder():
    form = UpdateOrderForm()
    form.item.choices = choices('', allItems())
    form.order.choices = choices('Order ', employeesOrders())
    return render_template("forms/form.html", form=form, path='orders.updateOrder', title='Update Order',)


@login_required
@bp.route("/create-order", methods=["GET"])
def createOrder():
    form = CreateOrderForm()
    form.employee.choices = choices('', allEmployees())
    form.table.choices = choices('Table ', allTables())
    return render_template("forms/form.html", form=form, path='orders.createOrder', title='Create Order',)


# -----------
# HELPERS
# -----------
def allItems():
    return Item.query.order_by(Item.name).all()

def allEmployees():
    return Employee.query.order_by(Employee.name).all()

def allTables():
    return Table.query.order_by(Table.id).all()

def employeesOrders():
    return Order.query.filter_by(employee_id = current_user.id).all()

def choices(textBeforeOption, options):
    return [(i.id, f"{textBeforeOption} {i.name if hasattr(i, 'name') else i.id }") for i in options]