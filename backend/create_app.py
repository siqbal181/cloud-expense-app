import os
from flask import Flask
from google.cloud import storage

def create_app():
    app = Flask(__name__)

    # Set the service account key file path relative to create_app.py
    key_file_path = os.path.join(os.path.dirname(__file__), 'keys', 'rare-basis-410812-2c7d0a25bc12.json')

    storage_client = storage.Client.from_service_account_json(key_file_path)

    bucket_name = 'expense-app-jan24'

    try:
        bucket = storage_client.get_bucket(bucket_name)
    except storage.exceptions.NotFound:
        bucket = storage_client.create_bucket(bucket_name)

    app.config['STORAGE_CLIENT'] = storage_client
    app.config['BUCKET_NAME'] = bucket_name

    return app
