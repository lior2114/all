from flask import Flask, Blueprint
from routes.countries_routes import countries_bp
from routes.roles_routes import roles_bp
from routes.users_routes import users_bp
from routes.vacations_routes import vacations_bp
from routes.likes_routes import likes_bp
from models.countries_model import Country_Model as c
from models.roles_model import Role_Model as R
from models.users_model import Users_Model as U
from models.vacations_model import Vacations_Model as V
from models.likes_model import Likes_Model as L

app = Flask (__name__)
app.register_blueprint(countries_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(users_bp)
app.register_blueprint(vacations_bp)
app.register_blueprint(likes_bp)

c.create_table()
R.create_table()
U.create_table()
V.create_table()
L.create_table()

if (__name__ == "__main__"):
    app.run (debug=True, host = "0.0.0.0", port = 5000)