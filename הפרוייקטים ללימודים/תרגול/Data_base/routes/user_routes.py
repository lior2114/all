from flask import Blueprint
from controllers.user_controller import UserController

# Create blueprint
user_bp = Blueprint('users', __name__)

# Routes
@user_bp.route('/', methods=['GET'])
def get_all_users():
    """Get all users"""
    return UserController.get_all_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    return UserController.get_user_by_id(user_id)

@user_bp.route('/', methods=['POST'])
def create_user():
    """Create a new user"""
    return UserController.create_user()

@user_bp.route('/login', methods=['POST'])
def login():
    """Login user"""
    return UserController.login()

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update user by ID"""
    return UserController.update_user(user_id)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user by ID"""
    return UserController.delete_user(user_id)
