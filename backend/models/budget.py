from google.cloud import storage
from flask import current_app
import json

class MonthlyBudget:
    def __init__(self, category, budget):
        self.category = category
        self.budget = budget

    def save_to_gcs(self):
        try:
            storage_client = current_app.config["STORAGE_CLIENT"]
            bucket_name = current_app.config["BUCKET"]

            blob_name = f"{self.category}_budget.json"
            blob = storage_client.bucket(bucket_name).blob(blob_name)
            blob.upload_from_string(self.to_json(), content_type='application/json')

            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "error": str(e)}

    def to_json(self):
        return json.dumps({"category": self.category, "budget": self.budget})
