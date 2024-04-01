from flask import Blueprint
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="")

@bp.route("/")
@login_required
def index():
    return "Order Up!"