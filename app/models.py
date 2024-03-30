from flask_sqlalchemy import SQLAlchemy
from flask_login.login_manager import LoginManager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# class Employee(db.Model, UserMixin):
#     __tablename__ = 'employees'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), )
#     employee_something = db.Column(db.Integer, )
#     hashed_password = db.String(255), )

#     @property
#     def password(self):
#         return self.hashed_password

#     @password.setter
#     def password(self, password):
#         self.hashed_password = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password, password)


