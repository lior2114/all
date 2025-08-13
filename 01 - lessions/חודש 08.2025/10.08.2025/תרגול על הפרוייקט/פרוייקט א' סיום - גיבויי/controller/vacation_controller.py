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
        
        # ולידציה של השדות
        if not data["country_id"] or data["country_id"] == "":
            return jsonify({"Error": "Country ID cannot be empty"}), 400
            
        if not data["vacation_description"] or not data["vacation_description"].strip():
            return jsonify({"Error": "Vacation description cannot be empty"}), 400
            
        if not data["vacation_start"]:
            return jsonify({"Error": "Vacation start date cannot be empty"}), 400
            
        if not data["vacation_ends"]:
            return jsonify({"Error": "Vacation end date cannot be empty"}), 400
        
        start_date = datetime.strptime(data["vacation_start"], "%Y-%m-%d")
        end_date = datetime.strptime(data["vacation_ends"], "%Y-%m-%d")
        if start_date > end_date:
            return jsonify({"Error": "cant added vacation beacuse vacation_start are bigger then vacation_end"}), 400
        today = datetime.now().date()
        if start_date.date() < today or end_date.date() < today:
            return jsonify({"Error": "vacation dates cannot be in the past"}), 400

        if data["vacation_price"] > 10000 or data["vacation_price"] <= 0:
            return jsonify({"Error": "vacation_price must be between 0 and 10000"}), 400
        result = V.create_vacation(
            country_id = data["country_id"],
            vacation_description = data["vacation_description"],
            vacation_start = data["vacation_start"],
            vacation_ends = data["vacation_ends"],
            vacation_price = data["vacation_price"],
            vacation_file_name = data["vacation_file_name"]
            )
        return jsonify(result), 201

    

    @staticmethod
    def get_all_vacations():
        result = V.get_all_vacations()
        return jsonify(result),201
    
    @staticmethod
    def show_vacations_by_id(vacation_id):
        result = V.show_vacation_by_id(vacation_id)
        return jsonify(result),201
    
    @staticmethod
    def update_vacation_by_id(vacation_id):
        data = request.get_json()
        allowed_fields = ["country_id", "vacation_description", "vacation_start", "vacation_ends", "vacation_price", "vacation_file_name"]
        
        if not data:
            return jsonify({"Error": "No data provided"}), 400
        
        # בדיקה שכל השדות שנשלחו הם מותרים
        for field in data.keys():
            if field not in allowed_fields:
                return jsonify({"Error": f"Field '{field}' is not allowed for update"}), 400
        
        # ולידציה של השדות
        if "country_id" in data and (not data["country_id"] or data["country_id"] == ""):
            return jsonify({"Error": "Country ID cannot be empty"}), 400
            
        if "vacation_description" in data and (not data["vacation_description"] or not data["vacation_description"].strip()):
            return jsonify({"Error": "Vacation description cannot be empty"}), 400
            
        if "vacation_start" in data and not data["vacation_start"]:
            return jsonify({"Error": "Vacation start date cannot be empty"}), 400
            
        if "vacation_ends" in data and not data["vacation_ends"]:
            return jsonify({"Error": "Vacation end date cannot be empty"}), 400
        
        # בדיקת מחיר אם נשלח
        if "vacation_price" in data:
            try:
                price = float(data["vacation_price"])
                if price > 10000 or price <= 0:
                    return jsonify({"Error": "vacation_price must be between 0 and 10000"}), 400
            except (ValueError, TypeError):
                return jsonify({"Error": "Invalid price format"}), 400
            
        result = V.update_vacation_by_id(vacation_id, data)
        if "Error" in result:
            return jsonify(result), 400
        return jsonify(result), 201
        
    
    @staticmethod
    def delete_vacation_by_id(vacation_id):
        result = V.delete_vacation_by_id(vacation_id)
        return jsonify(result)
        
    @staticmethod
    def upload_vacation_image():
        try:
            if 'image' not in request.files:
                return jsonify({"Error": "No image file provided"}), 400
            
            file = request.files['image']
            if file.filename == '':
                return jsonify({"Error": "No file selected"}), 400
            
            if file:
                # בדיקת סוג הקובץ
                allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
                    return jsonify({"Error": "Invalid file type. Only images are allowed"}), 400
                
                # שמירת הקובץ
                import os
                upload_folder = 'uploads'
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                
                filename = file.filename
                file_path = os.path.join(upload_folder, filename)
                file.save(file_path)
                
                return jsonify({
                    "message": "Image uploaded successfully",
                    "filename": filename,
                    "file_path": file_path
                }), 201
                
        except Exception as e:
            return jsonify({"Error": f"Error uploading file: {str(e)}"}), 500
        