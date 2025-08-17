from flask import Flask, Blueprint
from controller.user_controller import Users_Controller as U

users_bp = Blueprint("/users", __name__)

@users_bp.route("/users", methods = ["POST"])
def create_user():
    return U.create_user()

@users_bp.route("/users", methods = ["GET"])
def get_all_users():
    return U.get_all_users()

@users_bp.route("/users/login", methods = ["POST"])
def show_user_by_email_and_password():
    return U.show_user_by_email_and_password()

@users_bp.route("/users/<int:user_id>", methods = ["GET"])
def show_user_by_id(user_id):
    return U.show_user_by_id(user_id)

@users_bp.route("/users/<int:user_id>", methods = ["PUT"])
def update_user_by_id(user_id):
    return U.update_user_by_id(user_id)


@users_bp.route("/users/<int:user_id>", methods = ["DELETE"])
def delete_user_by_id(user_id):
    return U.delete_user_by_id(user_id)

@users_bp.route("/users/check_email", methods = ["GET"])
def check_if_mail_exists():
    return U.check_if_email_exists()

@users_bp.route("/users/<int:user_id>/profile-image", methods = ["POST"])
def update_profile_image(user_id):
    return U.update_profile_image(user_id)

@users_bp.route("/users/<int:user_id>/profile-image", methods = ["DELETE"])
def remove_profile_image(user_id):
    return U.remove_profile_image(user_id)

@users_bp.route("/users/<int:user_id>/ban", methods = ["POST"])
def ban_user(user_id):
    return U.ban_user(user_id)

@users_bp.route("/users/<int:user_id>/unban", methods = ["POST"])
def unban_user(user_id):
    return U.unban_user(user_id)