from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee, Menu, Item, ItemType, Table, Order, OrderedItem

with app.app_context():
    db.drop_all()
    db.create_all()

    # Employees
    employee = Employee(name="Margot", employee_number=1234, password="password")

    # Menus
    dinner = Menu(name="Dinner")

    # ItemTypes
    beverages = ItemType(name="Beverages")
    entrees = ItemType(name="Entrees")
    sides = ItemType(name="Sides")
    item_types = [beverages, entrees, sides]

    # Items
    fries = Item(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = Item(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = Item(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    items = [fries, drp, jambalaya]

    # Tables
    tables = []
    for i in range(1,11):
        tables.append(Table(number=i, capacity=(2 if i < 5 else 5)))

    # Orders
    order = Order(employee_id=1, table_id=3, paid=False, ordered_items = [])

    # ---------------
    # Seed the Data
    # ---------------
    data = [employee, dinner, *items, *item_types, *tables, order]

    for d in data:
        db.session.add(d)

    db.session.commit()