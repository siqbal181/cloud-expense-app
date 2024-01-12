from flask import Blueprint
from ..controllers.budget_controller import save_budget

budget_bp = Blueprint("budget", __name__)

@budget_bp.route("/save-budget", methods=["POST"])
def save_budget_route():
    return save_budget()
