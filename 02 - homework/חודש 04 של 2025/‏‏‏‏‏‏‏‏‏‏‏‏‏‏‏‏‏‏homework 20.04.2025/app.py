from flask import Flask
from models.role_model import Tables_Roles as T
from routes.role_routes import role_bp

app = Flask(__name__)
app.register_blueprint(role_bp)
T.create_table_roles()
# T.create_role()
# T.get_all()
# T.get_by_id()
if (__name__ == "__main__"):
    app.run(debug=True, host = "0.0.0.0", port = 5000)
