from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee, Menu, Item, ItemType, Table, Order, OrderedItem

with app.app_context():
    db.drop_all()
    db.create_all()

    # ------------
    # Employees
    # ------------
    employee = Employee(name="Margot", employee_number=1234, password="password")

    # ------------
    # Menus
    # ------------
    dinner = Menu(name="Dinner")

    beverages = ItemType(name="Beverages")
    entrees = ItemType(name="Entrees")
    sides = ItemType(name="Sides")

    fries = Item(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = Item(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = Item(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    itemTypes = [beverages, entrees, sides]
    items = [fries, drp, jambalaya]

    # ------------
    # Tables
    # ------------
    tables = []
    for i in range(1,11):
        tables.append(Table(number=i, capacity=(2 if i < 5 else 5)))

    # ------------
    # Orders
    # ------------
    order = Order(employee_id=1, table_id=3, paid=False)
    jambalaya_order = OrderedItem(item=jambalaya, order_id=1)
    fries_order = OrderedItem(item=fries, order_id=1)

    # ------------
    # ALL DATA
    # ------------
    data = [employee, dinner, *items, *itemTypes, *tables, order]

    for i in data:
        db.session.add(i)
    
    db.session.commit()