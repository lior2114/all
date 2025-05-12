from flask import jsonify, request
from models.likes_model import Likes_Model as L

class Likes_Controller:
    def like_vacation():
        data = request.get_json()
        if not data:
            return jsonify({"Error": "No data provided or user_id or vacation_id is missing"}), 400
        result = L.add_like_to_vacation(data["user_id"], data["vacation_id"])
        return jsonify(result), 201
    
    def unlike_vacation():
        data = request.get_json()
        if not data:
            return jsonify({"Error": "No data provided or user_id or vacation_id is missing"}), 400
        result = L.unlike_vacation(data["user_id"], data["vacation_id"])
        return jsonify(result), 201
        
