from flask import Flask, Blueprint
from routes.role_routes import role_bp
from routes.worker_routes import worker_bp
from models.role_model import Role_functions as R
from models.workers_model import WorkersModel as W

app = Flask(__name__)

app.register_blueprint(role_bp)
app.register_blueprint(worker_bp)
R.create_role_table()
W.create_table_workers()

if (__name__== "__main__"):
    app.run (debug = True, host = "0.0.0.0", port = 5000)
