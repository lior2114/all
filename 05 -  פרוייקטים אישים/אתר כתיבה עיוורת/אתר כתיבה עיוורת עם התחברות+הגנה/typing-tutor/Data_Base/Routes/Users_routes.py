from flask import Flask, Blueprint, request
from controllers.User_Controllers import Users_Controller as U

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
def check_if_email_exists():
    return U.check_if_email_exists()

@users_bp.route("/users/<int:user_id>/profile-image", methods = ["POST"])
def update_profile_image(user_id):
    return U.update_profile_image(user_id)

@users_bp.route("/users/<int:user_id>/profile-image", methods = ["DELETE"])
def remove_profile_image(user_id):
    return U.remove_profile_image(user_id)

@users_bp.route("/users/<int:user_id>/ban", methods = ["POST", "OPTIONS"])
def ban_user(user_id):
    if request.method == "OPTIONS":
        return "", 200
    return U.ban_user(user_id)

@users_bp.route("/users/<int:user_id>/unban", methods = ["POST", "OPTIONS"])
def unban_user(user_id):
    if request.method == "OPTIONS":
        return "", 200
    return U.unban_user(user_id)

# נתיבים חדשים להתקדמות משתמשים
@users_bp.route("/users/progress", methods = ["POST"])
def update_user_progress():
    return U.update_user_progress()

@users_bp.route("/users/<int:user_id>/progress", methods = ["GET"])
def get_user_progress(user_id):
    return U.get_user_progress(user_id)

# נתיבים לפאנל אדמין
@users_bp.route("/admin/dashboard", methods = ["GET"])
def get_admin_dashboard():
    return U.get_admin_dashboard()

@users_bp.route("/admin/create", methods = ["POST"])
def create_admin_user():
    return U.create_admin_user()