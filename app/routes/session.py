from flask import Blueprint, redirect, url_for, render_template
from app.forms.Login import LoginForm
from app.forms.Signup import SignupForm
from app.models import db, Employee
from flask_login import current_user, login_user, logout_user

bp = Blueprint("session", __name__, url_prefix="/session")

@bp.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("orders.index"))
    form = LoginForm()
    if form.validate_on_submit():
        handleLogin(form)
        return redirect(url_for("session.login"))
    return render_template("forms/form.html", form=form, path=url_for('session.login'), title="Login to view your Orders")


@bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for("orders.index"))

@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        handleSignUp(form)
    return render_template("forms/form.html", form=form, path=url_for('session.signup'), title="Create an Employee Account")

# -----------
# HELPERS
# -----------
def handleLogin(form):
    employee = db.first_or_404(
        db.select(Employee).where(Employee.employee_number == form.employee_number.data))

    if not employee or not employee.check_password(form.password.data):
        return redirect(url_for(".login"))
    
    login_user(employee)
    return redirect(url_for("orders.index"))

def handleSignUp(form):
    employee = Employee(name=form.name.data, employee_number=form.employee_number.data, password=form.password.data)
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for(".login"))
