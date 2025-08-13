from flask import jsonify, request
from models.likes_model import Likes_Model as L

class Likes_Controller:
    @staticmethod
    def add_like_to_vacation():
        try:
            data = request.get_json()
            print(f"Add like data: {data}")
            
            if not data or "user_id" not in data or "vacation_id" not in data:
                return jsonify({"Error": "No data provided or user_id or vacation_id is missing"}), 400
            
            # המרה למספרים
            user_id = int(data["user_id"])
            vacation_id = int(data["vacation_id"])
            
            print(f"Add like - user_id: {user_id}, vacation_id: {vacation_id}")
            
            result = L.add_like_to_vacation(user_id, vacation_id)
            
            if "Error" in result:
                return jsonify(result), 400
            
            return jsonify(result), 201
        except Exception as e:
            print(f"Add like error: {str(e)}")
            return jsonify({"Error": str(e)}), 500
    
    @staticmethod
    def unlike_vacation():
        try:
            data = request.get_json()
            print(f"Remove like data: {data}")
            
            if not data or "user_id" not in data or "vacation_id" not in data:
                return jsonify({"Error": "No data provided or user_id or vacation_id is missing"}), 400
            
            # המרה למספרים
            user_id = int(data["user_id"])
            vacation_id = int(data["vacation_id"])
            
            print(f"Remove like - user_id: {user_id}, vacation_id: {vacation_id}")
            
            result = L.unlike_vacation(user_id, vacation_id)
            
            if "Error" in result:
                return jsonify(result), 400
            
            return jsonify(result), 200
        except Exception as e:
            print(f"Remove like error: {str(e)}")
            return jsonify({"Error": str(e)}), 500
    
    @staticmethod
    def show_all_likes():
        try:
            result = L.show_likes()
            return jsonify(result)
        except Exception as e:
            print(f"Show likes error: {str(e)}")
            return jsonify({"Error": str(e)}), 500
