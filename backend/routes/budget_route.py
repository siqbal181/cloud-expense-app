from flask import Blueprint, current_app, jsonify, request
from ..controllers.budget_controller import save_budget

budget_bp = Blueprint("budget", __name__)

@budget_bp.route("/save-budget", methods=["POST"])
def save_budget_route():
    result, status_code = save_budget()
    
    if status_code != 200:
        return jsonify({"error": result}), status_code
    
    return jsonify({"message": "Budget saved successfully"}), status_code
