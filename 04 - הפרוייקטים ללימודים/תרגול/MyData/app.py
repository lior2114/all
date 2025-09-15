from flask import Flask, Blueprint, send_from_directory
import os
from flask_cors import CORS
from routes.countries_routes import countries_bp
from routes.roles_routes import roles_bp
from routes.users_routes import users_bp
from routes.vacations_routes import vacations_bp
from routes.likes_routes import likes_bp
from routes.bans_routes import bans_bp
from models.countries_model import Country_Model as c
from models.roles_model import Role_Model as R
from models.users_model import Users_Model as U
from models.vacations_model import Vacations_Model as V
from models.likes_model import Likes_Model as L
from models.bans_model import Bans_Model as B

app = Flask (__name__)
CORS(app)
app.register_blueprint(countries_bp, url_prefix='/api')
app.register_blueprint(roles_bp, url_prefix='/api')
app.register_blueprint(users_bp, url_prefix='/api')
app.register_blueprint(vacations_bp, url_prefix='/api')
app.register_blueprint(likes_bp, url_prefix='/api')
app.register_blueprint(bans_bp, url_prefix='/api')

# File uploads configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<path:filename>')
def serve_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

c.create_table()
R.create_table()
U.create_table()
V.create_table()
B.create_table()
L.create_table()

# Create default roles if they don't exist
roles = R.get_all_roles()
if not roles or (isinstance(roles, dict) and "Massages" in roles):
    print("No roles found. Creating default roles...")
    try:
        R.create_roles("admin")
        R.create_roles("user")
        print("Default roles created: admin (ID: 1), user (ID: 2)")
    except Exception as e:
        print(f"Failed to create default roles: {e}")

# Create default admin user if no users exist
users = U.get_all_users()
if not users or (isinstance(users, dict) and "Massages" in users):
    print("No users found. Creating default admin user...")
    try:
        U.create_user(
            first_name="Admin",
            last_name="User", 
            user_email="admin@test.com",
            user_password="admin123"
        )
        print("Default admin user created: admin@test.com / admin123")
    except Exception as e:
        print(f"Failed to create default user: {e}")

if (__name__ == "__main__"):
    app.run (debug=True, host = "0.0.0.0", port = 5000)