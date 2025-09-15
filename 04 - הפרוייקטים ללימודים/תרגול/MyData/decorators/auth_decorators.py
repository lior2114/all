from functools import wraps
from flask import request, jsonify
from models.users_model import Users_Model as U

def admin_required(f):
    """
    Decorator that requires admin role for access
    Expects admin_user_id in request data (JSON) or form data
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get admin_user_id from different sources
        admin_user_id = None
        
        # Try to get from JSON data first
        if request.is_json:
            data = request.get_json(silent=True) or {}
            admin_user_id = data.get('admin_user_id')
        
        # Try to get from form data
        if not admin_user_id and request.form:
            admin_user_id = request.form.get('admin_user_id')
        
        # Try to get from query parameters
        if not admin_user_id:
            admin_user_id = request.args.get('admin_user_id')
        
        # Check if admin_user_id exists
        if not admin_user_id:
            return jsonify({
                "Error": "Missing admin_user_id",
                "message": "Admin authentication required"
            }), 403
        
        # Validate admin_user_id is a number
        try:
            admin_id = int(admin_user_id)
        except (ValueError, TypeError):
            return jsonify({
                "Error": "Invalid admin_user_id format",
                "message": "Admin user ID must be a valid number"
            }), 400
        
        # Check if user exists and is admin
        admin_user = U.show_user_by_id(admin_id)
        if not admin_user:
            return jsonify({
                "Error": "Admin user not found",
                "message": "Invalid admin user ID"
            }), 404
        
        # Check if user has admin role (role_id = 1)
        user_role = admin_user.get("role_id", 2)  # Default to regular user role if not specified
        if int(user_role) != 1:
            return jsonify({
                "Error": "Insufficient permissions",
                "message": "Only administrators can perform this action"
            }), 403
        
        # Add admin info to request context for use in the function
        request.admin_user = admin_user
        request.admin_id = admin_id
        
        return f(*args, **kwargs)
    
    return decorated_function

def user_required(f):
    """
    Decorator that requires any authenticated user (both admin and regular users)
    Expects user_id in request data (JSON) or form data
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get user_id from different sources
        user_id = None
        
        # Try to get from JSON data first
        if request.is_json:
            data = request.get_json(silent=True) or {}
            user_id = data.get('user_id')
        
        # Try to get from form data
        if not user_id and request.form:
            user_id = request.form.get('user_id')
        
        # Try to get from query parameters
        if not user_id:
            user_id = request.args.get('user_id')
        
        # Check if user_id exists
        if not user_id:
            return jsonify({
                "Error": "Missing user_id",
                "message": "User authentication required"
            }), 403
        
        # Validate user_id is a number
        try:
            user_id_int = int(user_id)
        except (ValueError, TypeError):
            return jsonify({
                "Error": "Invalid user_id format",
                "message": "User ID must be a valid number"
            }), 400
        
        # Check if user exists
        user = U.show_user_by_id(user_id_int)
        if not user:
            return jsonify({
                "Error": "User not found",
                "message": "Invalid user ID"
            }), 404
        
        # Check if user has valid role (1 = admin, 2 = regular user)
        user_role = user.get("role_id", 2)
        if int(user_role) not in [1, 2]:
            return jsonify({
                "Error": "Invalid user role",
                "message": "User has invalid role"
            }), 403
        
        # Add user info to request context
        request.user = user
        request.user_id = user_id_int
        request.is_admin = (int(user_role) == 1)
        
        return f(*args, **kwargs)
    
    return decorated_function

def optional_auth(f):
    """
    Decorator that optionally checks for authentication
    If user_id is provided, validates it, but doesn't require it
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get user_id from different sources
        user_id = None
        
        # Try to get from JSON data first
        if request.is_json:
            data = request.get_json(silent=True) or {}
            user_id = data.get('user_id')
        
        # Try to get from form data
        if not user_id and request.form:
            user_id = request.form.get('user_id')
        
        # Try to get from query parameters
        if not user_id:
            user_id = request.args.get('user_id')
        
        # If user_id is provided, validate it
        if user_id:
            try:
                user_id_int = int(user_id)
                user = U.show_user_by_id(user_id_int)
                if user:
                    user_role = user.get("role_id", 2)
                    # Only accept valid roles (1 = admin, 2 = regular user)
                    if int(user_role) in [1, 2]:
                        request.user = user
                        request.user_id = user_id_int
                        request.is_admin = (int(user_role) == 1)
                    else:
                        request.user = None
                        request.user_id = None
                        request.is_admin = False
                else:
                    request.user = None
                    request.user_id = None
                    request.is_admin = False
            except (ValueError, TypeError):
                request.user = None
                request.user_id = None
                request.is_admin = False
        else:
            request.user = None
            request.user_id = None
            request.is_admin = False
        
        return f(*args, **kwargs)
    
    return decorated_function
