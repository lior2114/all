from flask import Blueprint
from controller.user_controller import UserController as U

user_bp = Blueprint('user', __name__)
@user_bp.route('/users', methods = ['POST'])
def create_user():
    return U.create_user()

@user_bp.route('/users', methods = ['GET'])
def show_all_users():
    return U.show_all_users()

@user_bp.route('/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    return U.get_user(user_id)

@user_bp.route('/users/<int:user_id>', methods = ['PUT'])
def update_B(user_id):
    return U.update_user(user_id)

@user_bp.route('/users/<int:user_id>', methods = ['DELETE'])
def delete_user(user_id):
    return U.delete_user(user_id)