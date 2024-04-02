from flask_sqlalchemy import SQLAlchemy
from flask_login.login_manager import LoginManager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.schema import ForeignKey

db = SQLAlchemy()

class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'
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
    

# class Menu(db.Model):
#     __tablename__ = "menus"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)


# class MenuItemType(db.Model):
#     __tablename__ = 'menu_item_types'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)


# ### TODO - add the table joins between Menu Item & Menu & Menu Item Typep

# class MenuItem(db.Model):
#     __tablename__ = 'menu_items'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     price = db.Column(db.Float, primary_key=True)
#     menu_id = db.Column(db.Integer, ForeignKey("menus.id"), nullable=False)
#     menu_type =db.Column(db.Integer, ForeignKey("menu_item_types.id"), nullable=False)


# class Table(db.Model):
#     __tablename__ = 'tables'
#     id = db.Column(db.Integer, primary_key=True)
#     number = db.Column(db.Integer, unique=True, primary_key=True)
#     capacity = db.Column(db.Integer, nullable=False)





