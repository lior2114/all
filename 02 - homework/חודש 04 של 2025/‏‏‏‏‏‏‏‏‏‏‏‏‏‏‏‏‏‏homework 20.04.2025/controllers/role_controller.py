from flask import Flask, jsonify,request
from models.role_model import Tables_Roles as T

class Controller_Roles:


#יצירת רול
    @staticmethod
    def create_role():
        data = request.get_json()  
        if not data or "role_description" not in data:
            return jsonify({"error": "please enter correct values"})
        elif data is None:
            return jsonify({"error": "please enter correct values"})
        elif isinstance(data, int):
            return jsonify({"error": "data should not be an integer"})
        result = T.create_role(data["role_description"])
        return jsonify(result)

# הצגת כל הרולים 
    @staticmethod
    def get_all_roles():
        roles = T.get_all()
        if not roles:
               return jsonify({"error": "no roles has been added yet"})
        return jsonify(roles)
    
#הצגת רול על ידי איי די
    @staticmethod
    def get_role_by_id(role_id):
        if not isinstance(role_id, int):
            return jsonify({"error": "role_id should be an integer"})
        result = T.get_by_id(role_id)
        return jsonify(result)
    
# עדכון רול
    @staticmethod
    def update_role(role_id):
        data = request.get_json()
        if not data or "new_description" not in data:
            return jsonify({"error": "please enter correct values"})
        elif data is None:
            return jsonify({"error": "please enter correct values"})
        elif isinstance(data["new_description"], int):
            return jsonify({"error": "new_description should not be an integer"})  
        elif isinstance(role_id, str):
            return jsonify({"error": "role_id should not be an str"})  
        T.updating(data["new_description"],role_id)
        return jsonify({f"{role_id} has been updated": f"new description is {data['new_description']}"})
    
#מחיקת רול 
    @staticmethod
    def deleting(role_id):
        if isinstance(role_id, str):
            return jsonify({"error": "role_id should not be a string"})  
        role = T.get_by_id(role_id)
        if "message" in role:
            return jsonify({"error": f"role {role_id} has already been deleted or was not found"})
        T.deleting(role_id)
        return jsonify({"message": f"role {role_id} has been successfully deleted"})

    