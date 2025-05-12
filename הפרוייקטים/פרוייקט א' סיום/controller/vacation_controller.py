from flask import jsonify, request
from models.vacations_model import Vacations_Model as V
from datetime import datetime

class Vacations_Controller:

    @staticmethod
    def create_vacation():
        data = request.get_json()
        fields = ["country_id", "vacation_description", "vacation_start", "vacation_ends", "vacation_price", "vacation_file_name"]
        if not data or not all(k in fields for k in data):
            return jsonify ({"Error":"Missing values or data empty"}), 400
        
        #לקחתי מהצאט כי לא ידעתי את הפונקציות המתאימות של הבדיקת התאריכים 
        start_date = datetime.strptime(data["vacation_start"], "%Y-%m-%d")
        end_date = datetime.strptime(data["vacation_ends"], "%Y-%m-%d")
        if start_date > end_date:
            return jsonify({"Error": "cant added vacation beacuse vacation_start are bigger then vacation_end"}), 400
        today = datetime.now().date()
        if start_date.date() < today or end_date.date() < today:
            return jsonify({"Error": "vacation dates cannot be in the past"}), 400

        if data["vacation_price"] > 10000 or data["vacation_price"] < 0:
            return jsonify({"Error": "vacation_price cant be lower then 0 or high then 10000"}), 400
        result = V.create_vacation(
            country_id = data["country_id"],
            vacation_description = data["vacation_description"],
            vacation_start = data["vacation_start"],
            vacation_ends = data["vacation_ends"],
            vacation_price = data["vacation_price"],
            vacation_file_name = data["vacation_file_name"]
            )
        return jsonify(result)
    

    @staticmethod
    def get_all_vacations():
        result = V.get_all_vacations()
        return jsonify(result)
    
    @staticmethod
    def show_vacations_by_id(vacation_id):
        result = V.show_vacation_by_id(vacation_id)
        return jsonify(result)
    
    @staticmethod
    def update_vacation_by_id(vacation_id):
        data = request.get_json()
        if not data:
            return jsonify({"Error": "No data provided"}), 400
        result = V.update_vacation_by_id(vacation_id, data)
        if "Error" in result:
            return jsonify(result), 400
        return jsonify(result)
    
    @staticmethod
    def delete_vacation_by_id(vacation_id):
        result = V.delete_vacation_by_id(vacation_id)
        return jsonify(result)
        