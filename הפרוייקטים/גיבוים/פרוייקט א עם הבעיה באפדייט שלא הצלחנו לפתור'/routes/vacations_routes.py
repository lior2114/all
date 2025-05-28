from flask import Flask, Blueprint
from controller.vacation_controller import Vacations_Controller as V

vacations_bp = Blueprint("/vacations", __name__)

@vacations_bp.route("/vacations", methods = ["POST"])
def create_vacation():
    return V.create_vacation()

@vacations_bp.route("/vacations", methods = ["GET"])
def get_all_vacations():
    return V.get_all_vacations()

@vacations_bp.route("/vacations/<int:vacation_id>", methods = ["GET"])
def show_vacations_by_id(vacation_id):
    return V.show_vacations_by_id(vacation_id)

@vacations_bp.route("/vacations/update/<int:vacation_id>", methods = ["PUT"])
def update_vacation_by_id(vacation_id):
    return V.update_vacation_by_id(vacation_id)


@vacations_bp.route("/vacations/delete/<int:vacation_id>", methods = ["DELETE"])
def delete_vacation_by_id(vacation_id):
    return V.delete_vacation_by_id(vacation_id)