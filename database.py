from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee, Menu, Item, ItemType, Table, Order, OrderedItem

with app.app_context():
    db.drop_all()
    db.create_all()

    # Employees
    employee = Employee(name="Emerenciana", employee_number=1234, password="ube")

    # Menus
    bfast = Menu(name="Breakfast")

    # ItemTypes
    beverages = ItemType(name="Beverages")
    entrees = ItemType(name="Entrees")
    sides = ItemType(name="Sides")
    item_types = [beverages, entrees, sides]

    # Items
    bars = Item(name="Ube Bars", price=9.00, type=entrees, menu=bfast, image_filename = "bars")
    canoli = Item(name="Ube Canoli", price=7.00, type=entrees, menu=bfast, image_filename = "canoli")
    cheescake = Item(name="Ube Cheesecake", price=15.00, type=entrees, menu=bfast, image_filename = "cheescake")
    cookies = Item(name="Ube Cookies", price=9.00, type=entrees, menu=bfast, image_filename = "cookies")
    crinkle = Item(name="Ube Crinkle Cookie", price=9.00, type=entrees, menu=bfast, image_filename = "crinkle")
    flan = Item(name="Ube Flan", price=15.00, type=entrees, menu=bfast, image_filename = "flan")
    monut = Item(name="Ube Monut", price=9.00, type=entrees, menu=bfast, image_filename = "monut")
    poptart = Item(name="Ube Pop Tart", price=9.00, type=entrees, menu=bfast, image_filename = "poptart")
    truffle = Item(name="Ube Cake Truffle", price=9.00, type=entrees, menu=bfast, image_filename = "truffles")
    ubemisu = Item(name="Ubemisu", price=5.00, type=entrees, menu=bfast, image_filename = "ubemisu")

    items = [bars, canoli, cheescake, cookies, crinkle, flan, monut, poptart, truffle, ubemisu]

    # Tables
    tables = []
    for i in range(1,11):
        tables.append(Table(number=i, capacity=(2 if i < 5 else 5)))

    # ---------------
    # Seed the Data
    # ---------------
    data = [employee, bfast, *items, *item_types, *tables]
    for d in data:
        db.session.add(d)
    db.session.commit()