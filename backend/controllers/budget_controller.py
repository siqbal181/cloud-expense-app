from flask import current_app, jsonify, request
from ..models.budget import MonthlyBudget

def save_budget():
    spend_data = request.get_json()

    if not spend_data:
        return jsonify({"error": "Invalid spend data"}), 400

    try:
        category = spend_data.get("category", "")
        budget = spend_data.get("budget", "")

        monthly_budget = MonthlyBudget(category=category, budget=budget)
        result = monthly_budget.save_to_gcs()

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
