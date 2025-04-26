from flask import Flask
from models.role_model import Tables_Roles as T
from routes.role_routes import role_bp

app = Flask(__name__)
app.register_blueprint(role_bp)

# Create the table if it doesn't exist when the app starts
T.create_table_roles()

# Remove unnecessary direct calls to model methods
# T.create_role() # Should be called via POST /roles
# T.get_all() # Should be called via GET /roles
# T.get_by_id() # Should be called via GET /roles/<id>

if __name__ == "__main__":
    # Make sure the host and port are suitable for your environment
    # Using 0.0.0.0 makes the server accessible on your network
    app.run(debug=True, host="0.0.0.0", port=5000)
