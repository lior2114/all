from flask import Flask
from flask_cors import CORS
from models.role_model import Role
from models.user_model import User
from routes.user_routes import auth_bp
from models.country_model import Country
from models.vacation_model import Vacation
from routes.vacation_routes import vacation_bp
from models.like_model import Like
from routes.like_routes import like_bp
from routes.countries_route import country_bp





# from routes.role_routes import role_bp 
app = Flask(__name__)
CORS(app)

# app.register_blueprint(role_bp)

# create database and table  
Role.create_table()
User.create_table()
#load the default roles admin and user
Role.insert_default_roles()
print("Roles table created and initialized with Admin and User roles")

Country.create_table()
Vacation.create_table()
# Country.insert_default_countries() moved to seed_data.py
print("Countries table created")
print("Vacations table created.")
Like.create_table()
print("Likes table created.")




app.register_blueprint(auth_bp)
app.register_blueprint(vacation_bp)
app.register_blueprint(like_bp)
app.register_blueprint(country_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

