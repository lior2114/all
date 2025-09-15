from flask import Flask, Blueprint
from controller.countries_controller import Countries_controller as C
from decorators.auth_decorators import admin_required, optional_auth

countries_bp = Blueprint("/countries", __name__)

@countries_bp.route("/countries", methods = ["POST"])
@admin_required
def create_country():
    """Create a new country - Admin only"""
    return C.create_country()

@countries_bp.route("/countries", methods = ["GET"])
@optional_auth
def get_all_countries():
    """Get all countries - Public access with optional user context"""
    return C.get_all_country()

@countries_bp.route("/countries/<int:country_id>", methods = ["GET"])
@optional_auth
def show_country_by_id(country_id):
    """Get country by ID - Public access with optional user context"""
    return C.show_country_by_id(country_id)

@countries_bp.route("/countries/<int:country_id>", methods = ["PUT"])
@admin_required
def update_country_by_id(country_id):
    """Update country by ID - Admin only"""
    return C.update_country_by_id(country_id)

@countries_bp.route("/countries/<int:country_id>", methods = ["DELETE"])
@admin_required
def delete_country_by_id(country_id):
    """Delete country by ID - Admin only"""
    return C.delete_country_by_id(country_id)