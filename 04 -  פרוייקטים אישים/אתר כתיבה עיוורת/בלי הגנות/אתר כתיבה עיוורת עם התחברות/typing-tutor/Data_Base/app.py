from flask import Flask, Blueprint
from flask_cors import CORS

from Routes.Users_routes import users_bp
from Models.Users_Models import Users_Model as U


app = Flask (__name__)
CORS(app, origins=["*"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization", "Accept"], supports_credentials=True)

app.register_blueprint(users_bp)

U.create_table()


if (__name__ == "__main__"):
    app.run (debug=True, host = "0.0.0.0", port = 5000)