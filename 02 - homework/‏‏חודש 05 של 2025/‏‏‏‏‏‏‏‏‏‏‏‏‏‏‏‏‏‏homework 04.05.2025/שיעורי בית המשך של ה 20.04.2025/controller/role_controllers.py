from models.role_model import Role_functions as R
from flask import Flask , jsonify, request

class Role_controller:
    @staticmethod
    def add_role_to_table():
        data = request.get_json()
        if not data or "role_description" not in data:
            return jsonify({"massage":"please enter correct value"})
        if data is None:
            return jsonify({"Error":"Please enter values"})
        if isinstance(data["role_description"], int):
            return jsonify({"Error":"data cant be a number"})
        result = R.add_role_to_table(data["role_description"])
        return jsonify(result)
    
    @staticmethod
    def show_all_roles_in_table():
        result = R.show_all_roles_in_table()
        if not result:
            return jsonify({"Error":"No roles has been added yet"})
        return jsonify(result)
    
    @staticmethod
    def get_role_by_id(role_id):
        result = R.get_role_by_id(role_id)
        if not result :
            return jsonify({"Error":"role_id not been found"})
        return jsonify(result)
    
    @staticmethod
    def update_role_by_id(role_id):
        data = request.get_json()
        if not data or "role_description" not in data:
            return jsonify({"massage":"please enter correct value"})
        if data is None:
            return jsonify({"Error":"Please enter values"})
        if not R.get_role_by_id(role_id):
            return jsonify({"massage":"role_id has not been found"})
        if isinstance (data["role_description"], int):
            return jsonify({"Error":"role_description cant be a number"})
        R.update_role_by_id(data["role_description"],role_id)
        return jsonify({"message": f"role id {role_id} has been updated to {data['role_description']}"})

    @staticmethod
    def delete_role_by_id(role_id):
        if not R.get_role_by_id(role_id):
            return jsonify({"massage":"role_id has not been found"})
        if isinstance(role_id,str):
            return jsonify({"Error":"cant be word only number"})
        R.delete_role_by_id(role_id)
        return jsonify({"massage":f"role_id {role_id} has been deleted"})
    