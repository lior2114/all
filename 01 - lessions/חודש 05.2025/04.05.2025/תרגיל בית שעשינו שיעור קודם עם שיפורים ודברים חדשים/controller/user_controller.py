from flask import jsonify,request
from models.user_moodel import UserModel

class UserController:

    @staticmethod
    def create_user():
        data = request.get_json()
        fields = ["first_name", "last_name", "email", "password", "role_id", "salary", "is_admin"]
        if not data or not all(k in data for k in fields):
            return jsonify({"Error":"Missing requried fields"}), 400 
        if not data.get('email'):
            return jsonify({"Error": "Email is required"}), 400
        result = UserModel.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            role_id=data['role_id'],
            salary=data['salary'],
            is_admin=data['is_admin']
        )
        return jsonify({"message": "User created successfully", "user_id": result['user_id']}), 201
    
    @staticmethod
    def show_all_users():
        result = UserModel.show_all()
        return jsonify(result)
    
    @staticmethod
    def get_user(user_id):
        result = UserModel.get_user(user_id)
        return jsonify(result)
    
    @staticmethod
    def update_user(user_id):
        data = request.get_json()
        if not data:
            return jsonify({"Error":"No Data provided"})
        result = UserModel.update_B(user_id, data)
        if result is None:
            return jsonify({"Error": "user not found"})
        return jsonify(result), 201
    
    @staticmethod
    def delete_user(user_id):
        result = UserModel.delete(user_id)
        if result is None:
            return jsonify({"Error": "user not found"})
        return jsonify(result), 201