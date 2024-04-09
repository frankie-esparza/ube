from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import db, Order, OrderedItem, Item, Employee, Table
from app.forms.AddOrRemoveItem import AddOrRemoveItemForm
from app.forms.CreateOrder import CreateOrderForm

bp = Blueprint("orders", __name__, url_prefix="")
models = { "employee": Employee, "item": Item, "order": Order, "ordered-item": OrderedItem, "table": Table }

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
@bp.route("/create-order", methods=["GET", "POST"])
def createOrder():
    form = CreateOrderForm()
    getFormChoices(form)
    if form.validate_on_submit(): 
        handleCreateOrder(form)
    return render_template("forms/form.html", form=form, path='orders.createOrder', title='Create Order',)

@login_required
@bp.route("/add-to-order", methods=["GET", "POST"])
def addToOrder():
    form = AddOrRemoveItemForm()
    getFormChoices(form)
    if form.validate_on_submit(): 
        handleAddItem(form)
    return render_template("forms/form.html", form=form, path='orders.addToOrder', title='Add Item to Order',)


@login_required
@bp.route("/remove-from-order", methods=["GET", "POST"])
def removeFromOrder():
    form = AddOrRemoveItemForm()
    getFormChoices(form)
    if form.validate_on_submit(): 
        handleRemoveItem(form)
    return render_template("forms/form.html", form=form, path='orders.removeFromOrder', title='Remove Item from Order',)


# ---------------
# EVENT HANDLERS
# ---------------
def handleCreateOrder(form):
    order = Order(employee_id = form.employee.data, table_id= form.table.data, paid = False, ordered_items = [])
    db.session.add(order)
    db.session.commit()

def handleAddItem(form):
    # find order & item to be added
    order = db.session.execute(db.select(Order).where(Order.id == form.order.data)).scalar()
    item = db.session.execute(db.select(Item).where(Item.id == form.item.data)).scalar()

    # create new orderedItem
    orderedItem = OrderedItem(order_id= form.order.data, item = item)
    order.ordered_items.append(orderedItem)
    db.session.commit()

def handleRemoveItem(form):
    order = db.session.execute(db.select(Order).where(Order.id == form.order.data)).scalar()
    idToRemove = form.item.data
    order.ordered_items = list(filter(lambda x: int(x.item_id) != int(idToRemove), order.ordered_items ))
    db.session.commit()


# -----------
# HELPERS
# -----------
def getAll(model):
    return db.session.execute(db.select(models[model])).scalars().all()

def getEmployeesOrders():
    return db.session.execute(db.select(Order).filter_by(employee_id = current_user.id)).scalars()

def getOpenTables():
    paidTables = db.session.execute(
        db.select(Table.id)
        .join_from(Table, Order)
        .where(Order.paid == True)
    ).scalars().all()

    assignedTables = db.session.execute(
        db.select(Table.id)
        .join_from(Table, Order)
    ).scalars().all()

    tablesThatHaveNeverBeenAssigned = filter(lambda x: x.id not in assignedTables, getAll("table"))
    return [*paidTables, *tablesThatHaveNeverBeenAssigned]


def getFormChoices(form):
    for field in form._fields.keys():
        field = form[field].name
        if form[field].type == 'SelectField':
            options = []
            if (field == 'table'): options = getOpenTables()
            else: options = getAll(field)
            form[field].choices = [(i.id, f"{i.name if hasattr(i, 'name') else str(i.id) }") for i in options]