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
        return render_template("orders.html", orders=getEmployeesOpenOrders())
    return redirect(url_for("session.login"))


@login_required
@bp.route("/create-order", methods=["GET", "POST"])
def createOrder():
    form = CreateOrderForm()
    getFormChoices(form)
    if form.validate_on_submit(): 
        handleCreateOrder(form)
        return redirect(url_for("orders.index"))
    return render_template("forms/form.html", form=form, path=url_for('orders.createOrder'), title='Create Order',)

@login_required
@bp.route("/close-order/<order_id>", methods=["GET", "POST"])
def closeOrder(order_id):
   handleCloseOrder(order_id)
   return redirect(url_for("orders.index"))


@login_required
@bp.route("/add-to-order/<order_id>", methods=["GET", "POST"])
def addToOrder(order_id):
    form = AddOrRemoveItemForm()
    getFormChoices(form)
    if form.validate_on_submit(): 
        handleAddItem(form, order_id)
        return redirect(url_for("orders.index"))
    return render_template("forms/form.html", form=form, path=f'/add-to-order/{order_id}', title='Add Item to Order',)


@login_required
@bp.route("/remove-from-order/<order_id>", methods=["GET", "POST"])
def removeFromOrder(order_id):
    form = AddOrRemoveItemForm()
    getFormChoices(form)
    if form.validate_on_submit(): 
        handleRemoveItem(form, order_id)
        return redirect(url_for("orders.index"))
    return render_template("forms/form.html", form=form, path=f'/remove-from-order/{order_id}', title='Remove Item from Order',)


# ---------------
# EVENT HANDLERS
# ---------------
def handleCreateOrder(form):
    order = Order(employee_id = form.employee.data, table_id= form.table.data, paid = False, ordered_items = [])
    db.session.add(order)
    db.session.commit()

def handleCloseOrder(order_id):
    print('ORDER ID', order_id)
    order = db.session.execute(db.select(Order).where(Order.id == order_id)).scalar()
    order.paid = True
    db.session.commit()

def handleAddItem(form, order_id):
    # find order & item to be added
    order = db.session.execute(db.select(Order).where(Order.id == order_id)).scalar()
    item = db.session.execute(db.select(Item).where(Item.id == form.item.data)).scalar()

    # create new orderedItem
    orderedItem = OrderedItem(order_id= order_id, item = item)
    order.ordered_items.append(orderedItem)
    db.session.commit()

def handleRemoveItem(form, order_id):
    order = db.session.execute(db.select(Order).where(Order.id == order_id)).scalar()
    idToRemove = form.item.data
    order.ordered_items = list(filter(lambda x: int(x.item_id) != int(idToRemove), order.ordered_items ))
    db.session.commit()


# -----------
# HELPERS
# -----------
def getAll(model):
    return db.session.execute(db.select(models[model])).scalars().all()

def getEmployeesOpenOrders():
    return db.session.execute(
        db.select(Order)
        .where(Order.employee_id == current_user.id and Order.paid == False)
        .order_by(Order.paid)
    ).scalars()

def getOpenTables():
    allTables = getAll("table")

    tablesWithUnpaidOrders = db.session.execute(
        db.select(Table)
        .join_from(Table, Order)
        .where(Order.paid == False)
    ).scalars().all()

    openTables = set(filter(lambda x: x not in tablesWithUnpaidOrders, allTables))
    return sorted(openTables, key=lambda x: x.id)


def getFormChoices(form):
    for field in form._fields.keys():
        print('FIELD', field)
        field = form[field].name
        type = form[field].type
        if (type == 'SelectField' or type == 'RadioField'):
            options = []
            if (field == 'table'): 
                options = getOpenTables()
                print('TABLES', options)
            else: options = getAll(field)
            form[field].choices = [(i.id, f"{i.name if hasattr(i, 'name') else str(i.id) }") for i in options]