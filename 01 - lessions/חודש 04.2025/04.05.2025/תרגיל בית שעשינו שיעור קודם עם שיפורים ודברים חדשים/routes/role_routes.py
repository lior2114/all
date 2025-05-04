from flask import Flask, Blueprint, jsonify
from controller.role_controllers import Role_controller as C

role_bp = Blueprint("role", __name__)

@role_bp.route("/roles", methods = ["POST"])
def add_role_to_table():
    return C.add_role_to_table()

@role_bp.route("/roles", methods = ["GET"])
def show_all_roles_in_table():
    return C.show_all_roles_in_table()

@role_bp.route("/roles/<int:role_id>", methods = ["GET"])
def get_role_by_id(role_id):
    return C.get_role_by_id(role_id)

@role_bp.route("/roles/<int:role_id>", methods = ["PUT"])
def update_role_by_id(role_id):
    return C.update_role_by_id(role_id)


@role_bp.route("/roles/<int:role_id>", methods = ["DELETE"])
def delete_role_by_id(role_id):
    return C.delete_role_by_id(role_id)



