from dotenv import load_dotenv
load_dotenv()

from app import app, db
# from app.models import Employee, Menu, MenuItem, MenuItemType, Table
from app.models import Employee

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
    # dinner = Menu(name="Dinner")

    # beverages = MenuItemType(name="Beverages")
    # entrees = MenuItemType(name="Entrees")
    # sides = MenuItemType(name="Sides")
    # menuItemTypes = [beverages, entrees, sides]

    # fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    # drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    # jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    # menuItems = [fries, drp, jambalaya]

    # ------------
    # Tables
    # ------------
    # tables = []
    # for n in range(1, 11):
    #     c = 2 if n < 5 else 5
    #     tables.append(Table(number=n, capacity=c))

    # data = [employee, dinner, *menuItems, *menuItemTypes, *tables]
    data = [employee]
    # ------------
    # Orders
    # ------------

    for i in data:
        db.session.add(i)
    
    db.session.commit()