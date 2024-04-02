from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.schema import ForeignKey

db = SQLAlchemy()

# ------------
# Employees
# ------------
class Employee(db.Model, UserMixin):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
# ----------------------------------
# Menus, MenuItems, & MenuItemTypes
# ----------------------------------
class ItemType(db.Model):
    __tablename__ = "item_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)

    type_id = db.Column(db.Integer, ForeignKey("item_types.id"), nullable=False)
    menu_id = db.Column(db.Integer, ForeignKey("menus.id"), nullable=False)

    type = db.relationship("ItemType", cascade="all, delete")
    menu = db.relationship("Menu", cascade="all, delete")

class Menu(db.Model):
    __tablename__ = "menus"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

# ------------
# Tables
# ------------
class Table(db.Model):
    __tablename__ = "tables"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)


# ------------
# Orders
# ------------
ordered_items_per_order = db.Table(
    "ordered_items_per_order",
    db.Model.metadata,
    db.Column("ordered_item_id", db.Integer, db.ForeignKey("ordered_items.id"), primary_key=True),
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
)

class OrderedItem(db.Model):
    __tablename__ = "ordered_items"
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, ForeignKey("orders.id"), nullable=False)
    item_id = db.Column(db.Integer, ForeignKey("items.id"), nullable=False)

    item = db.relationship("Item", cascade="all, delete")
    orders = db.relationship("Order")


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, ForeignKey("employees.id"), nullable=False)
    table_id = db.Column(db.Integer, ForeignKey("tables.id"), nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    ordered_items = db.relationship("OrderedItem", secondary=ordered_items_per_order, back_populates="orders", cascade="all, delete")

orders_per_employee = db.Table(
    "orders_per_employee",
    db.Model.metadata,
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
    db.Column("employee_id", db.Integer, db.ForeignKey("employees.id"), primary_key=True),
)

# Add Employee to Orders Relationship
Employee.orders = db.relationship("Order", primaryjoin=Order.employee_id==Employee.id, cascade="all, delete")
    