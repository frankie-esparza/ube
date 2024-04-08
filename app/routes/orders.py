from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import db, Order, Item, Employee, Table
from app.forms.UpdateOrder import UpdateOrderForm
from app.forms.CreateOrder import CreateOrderForm

bp = Blueprint("orders", __name__, url_prefix="")
models = { "employee": Employee, "item": Item, "order": Order, "table": Table }

# -----------
# ROUTES
# -----------
@login_required
@bp.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("orders.html", orders=getEmployeesOrders())
    return redirect(url_for("session.login"))


@login_required
@bp.route("/update-order", methods=["GET"])
def updateOrder():
    form = UpdateOrderForm()
    getFormChoices(form)

    return render_template("forms/form.html", form=form, path='orders.updateOrder', title='Update Order',)


@login_required
@bp.route("/create-order", methods=["GET", "POST"])
def createOrder():
    form = CreateOrderForm()
    getFormChoices(form)

    if form.validate_on_submit():
        handleCreateOrderFormSubmit(form)

    return render_template("forms/form.html", form=form, path='orders.createOrder', title='Create Order',)


# -----------
# HELPERS
# -----------
def handleCreateOrderFormSubmit(form):
    order = Order(employee_id = form.employee.data, table_id= form.table.data, paid = False, ordered_items = [])
    db.session.add(order)
    db.session.commit()

def getAll(model):
    return db.session.execute(db.select(models[model]).order_by(models[model].id)).scalars()

def getEmployeesOrders():
    return db.session.execute(db.select(Order).filter_by(employee_id = current_user.id)).scalars()

def getFormChoices(form):
    for field in form._fields.keys():
        if form[field].type == 'SelectField':
            field = form[field].name
            options = getAll(field)

            for i in options:
                form[field].choices = [(i.id, f"{i.name if hasattr(i, 'name') else field.capitalize() + ' ' + str(i.id) }")]