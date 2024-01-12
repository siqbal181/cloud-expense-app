from flask import Flask
from backend.routes.budget_route import budget_bp
from backend.create_app import create_app

app = create_app()
app.register_blueprint(budget_bp)

if __name__ == '__main__':
    app.run(debug=True)
