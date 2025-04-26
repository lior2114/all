from flask import Flask, jsonify, request
from models.role_model import Tables_Roles as T

class Controller_Roles:

#יצירת רול
    @staticmethod
    def create_role():
        data = request.get_json()
        # Improved validation
        if not data or 'role_description' not in data or not isinstance(data['role_description'], str) or not data['role_description'].strip():
            return jsonify({"error": "Invalid input: 'role_description' (string) is required"}), 400 # Bad Request
        result = T.create_role(data["role_description"].strip())
        return jsonify(result), 201 # Created

# הצגת כל הרולים
    @staticmethod
    def get_all_roles():
        roles = T.get_all()
        # The model handles the "no roles" case correctly now returning a list or a message
        return jsonify(roles)

#הצגת רול על ידי איי די
    @staticmethod
    def get_role_by_id(role_id):
        try:
            # Convert URL parameter to int
            role_id_int = int(role_id)
        except ValueError:
            return jsonify({"error": f"Invalid role ID: '{role_id}' must be an integer"}), 400 # Bad Request
        result = T.get_by_id(role_id_int)
        if "message" in result: # Check if the model returned an error message (like not found)
             # Check if the message indicates 'not found'
            if "No roles found" in result["message"]:
                 return jsonify(result), 404 # Not Found
            else:
                 return jsonify(result), 400 # Potentially other bad request types if model logic changes
        return jsonify(result)

# עדכון רול
    @staticmethod
    def update_role(role_id): # Get role_id from URL path
        data = request.get_json()
        # Improved validation
        if not data or 'new_description' not in data or not isinstance(data['new_description'], str) or not data['new_description'].strip():
            return jsonify({"error": "Invalid input: 'new_description' (string) is required in the request body"}), 400

        try:
            role_id_int = int(role_id)
        except ValueError:
            return jsonify({"error": f"Invalid role ID: '{role_id}' must be an integer"}), 400

        # Call model method with separate arguments
        result = T.updating(data["new_description"].strip(), role_id_int)
        if "not found" in result.get("message", ""): # Use get for safer access
            return jsonify(result), 404 # Not Found
        return jsonify(result)

#מחיקת רול
    @staticmethod
    def deleting(role_id): # Get role_id from URL path
        try:
             role_id_int = int(role_id)
        except ValueError:
            return jsonify({"error": f"Invalid role ID: '{role_id}' must be an integer"}), 400

        result = T.deleting(role_id_int)
        if "not found" in result.get("message", ""): # Use get for safer access
            return jsonify(result), 404 # Not Found
        return jsonify(result)
    