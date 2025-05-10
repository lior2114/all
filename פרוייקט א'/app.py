from flask import Flask, Blueprint
from routes.controllers_routes import countries_bp
from models.countries_model import Country_Model as c

app = Flask (__name__)
app.register_blueprint(countries_bp)
c.create_table()

if (__name__ == "__main__"):
    app.run (debug=True, host = "0.0.0.0", port = 5000)