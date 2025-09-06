from flask import Flask, Blueprint
from flask_cors import CORS
import os
from dotenv import load_dotenv, find_dotenv

from Routes.Users_routes import users_bp
from Models.Users_Models import Users_Model as U


_loaded = load_dotenv(find_dotenv())
if not _loaded:
    # Fallback to alternative env file name if .env is not present
    alt_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ENV")
    if os.path.exists(alt_env_path):
        load_dotenv(alt_env_path)

app = Flask (__name__)
# Secret key for JWT signing/verification
app.config["SECRET_KEY"] = os.getenv("JWT_SECRET", "change-this-in-production")
CORS(app, origins=["*"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization", "Accept"], supports_credentials=True)

app.register_blueprint(users_bp)

U.create_table()


if (__name__ == "__main__"):
    app.run (debug=True, host = "0.0.0.0", port = 5000)