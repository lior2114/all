from flask import jsonify, request
from models.users_model import Users_Model as U
import re #ידוע לי שלא למדנו לקחתי מהצאט כי אין לי מושג איך לרשום את הפונקציה 

class Users_Controller:

    @staticmethod
    def create_user():
        data = request.get_json()
        lis_requimints = ["first_name", "last_name", "user_email", "user_password"]
        if not data or not all(k in data for k in lis_requimints):
            return jsonify ({"Error":"Missing values or data empty"}), 400
        if len(data["user_password"].strip()) < 4:
            return jsonify ({"Error":"password need to be more then 4 values"}), 400
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data["user_email"]): #תנאי בדיקת מיילים 
            return jsonify({"Error": "Invalid email format"}), 400
        if not U.if_mail_exists(data["user_email"]):
            return jsonify ({"Error":"Email already exists"}), 400
        result = U.create_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            user_email=data["user_email"],
            user_password=data["user_password"],
        )
        return jsonify(result) , 201

    @staticmethod
    def get_all_users(): 
        result = U.get_all_users()
        return jsonify(result), 201
    
    @staticmethod
    def show_user_by_id(user_id):
        result = U.show_user_by_id(user_id)
        return jsonify(result), 201
    
    @staticmethod
    def update_user_by_id(user_id):
        data = request.get_json()
        lis_requimints = ["first_name", "last_name", "user_email", "user_password", "role_id"]
        if not data:
            return jsonify ({"Error":"Missing values or data empty"}), 400
        for value in data:
            if value not in lis_requimints:
                return jsonify ({"Error":"invalid key"}), 400
        if "user_password" in data and len(data["user_password"].strip()) < 4: #סטריפ מוריד רווחים 
            return jsonify ({"Error":"password need to be more then 4 values"}), 400
        if "user_email" in data:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", data["user_email"]): #תנאי בדיקת מיילים
                return jsonify({"Error": "Invalid email format"}), 400
            if not U.if_mail_exists(data["user_email"]):
                return jsonify ({"Error":"Email already exists"}), 400
        if "first_name" in data and (not str(data["first_name"]).isalpha()):
            return jsonify({"Error": "first_name must contain only letters"}), 400
        if "last_name" in data and (not str(data["last_name"]).isalpha()):
            return jsonify({"Error": "last_name must contain only letters"}), 400
        result = U.update_user_by_id(user_id, data)
        if result is None:
            return jsonify({"Error": "user not found"}), 400
        return jsonify(result), 201
    
    @staticmethod
    def delete_user_by_id(user_id):
        result = U.delete_user_by_id(user_id)
        return jsonify(result), 201