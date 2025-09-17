from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure CORS with more specific settings
CORS(app, 
     origins=["http://localhost:5173", "http://127.0.0.1:5173"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=True)

# Import and initialize database
from models import init_database
init_database()

# Import routes after app initialization
from routes.user_routes import user_bp

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api/users')

# Handle OPTIONS requests for CORS preflight
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = app.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Users API",
        "status": "running"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "database": "connected"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
