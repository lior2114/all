from flask import Flask, Blueprint
from controller.vacation_controller import Vacations_Controller as V
from decorators.auth_decorators import admin_required, optional_auth

vacations_bp = Blueprint("/vacations", __name__)

@vacations_bp.route("/vacations", methods = ["POST"])
@admin_required
def create_vacation():
    """Create a new vacation - Admin only"""
    return V.create_vacation()

@vacations_bp.route("/vacations", methods = ["GET"])
@optional_auth
def get_all_vacations():
    """Get all vacations - Public access with optional user context"""
    return V.get_all_vacations()

@vacations_bp.route("/vacations/<int:vacation_id>", methods = ["GET"])
@optional_auth
def show_vacations_by_id(vacation_id):
    """Get vacation by ID - Public access with optional user context"""
    return V.show_vacations_by_id(vacation_id)

@vacations_bp.route("/vacations/update/<int:vacation_id>", methods = ["PUT"])
@admin_required
def update_vacation_by_id(vacation_id):
    """Update vacation by ID - Admin only"""
    return V.update_vacation_by_id(vacation_id)

@vacations_bp.route("/vacations/delete/<int:vacation_id>", methods = ["DELETE"])
@admin_required
def delete_vacation_by_id(vacation_id):
    """Delete vacation by ID - Admin only"""
    return V.delete_vacation_by_id(vacation_id)