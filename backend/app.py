from flask import Flask, jsonify
from routes.budget_route import budget_bp
from create_app import create_app

app = create_app()

app.register_blueprint(budget_bp)

@app.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Test route is working!"})


if __name__ == '__main__':
    app.run(debug=True)
