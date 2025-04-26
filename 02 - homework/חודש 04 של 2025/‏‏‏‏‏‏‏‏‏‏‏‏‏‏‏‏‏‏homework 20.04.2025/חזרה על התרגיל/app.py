from flask import Flask, Blueprint
from routes.role_routes import role_bp
from models.role_model import Role_functions as R

app = Flask(__name__)

app.register_blueprint(role_bp)
R.create_role_table()

if (__name__== "__main__"):
    app.run (debug = True, host = "0.0.0.0", port = 5000)
