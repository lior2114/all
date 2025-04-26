from flask import Blueprint,jsonify
from controllers.role_controller import Controller_Roles as C

role_bp = Blueprint("role", __name__)  # Removed leading slash from the Blueprint name

@role_bp.route("/roles", methods=["POST"])
def role_create():
    return C.create_role()

@role_bp.route("/roles", methods=["GET"])
def get_all_roles():
    return C.get_all_roles()  # Added return statement for consistency
 
@role_bp.route("/roles/<int:role_id>", methods=["GET"])
def get_role_by_id(role_id):
    return C.get_role_by_id(role_id)

@role_bp.route("/roles/<int:role_id>", methods=["PUT"])
def Update_role(role_id):
    return C.update_role(role_id)

@role_bp.route("/roles/<int:role_id>", methods = ["DELETE"])
def delete_role_by_id(role_id):
    return C.deleting(role_id)