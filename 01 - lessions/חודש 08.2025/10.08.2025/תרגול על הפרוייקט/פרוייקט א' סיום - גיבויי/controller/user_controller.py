from flask import jsonify, request
from models.users_model import Users_Model as U
import re 

class Users_Controller:

    @staticmethod
    def create_user():
        data = request.get_json()
        print("Received data:", data)  # Debug log
        lis_requimints = ["first_name", "last_name", "user_email", "user_password"]
        if not data or not all(k in data for k in lis_requimints):
            return jsonify ({"Error":"Missing values or data empty"}), 400
        if len(data["user_password"].strip()) < 4:
            return jsonify ({"Error":"password need to be more then 4 values"}), 400
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data["user_email"]): #תנאי בדיקת מיילים 
            return jsonify({"Error": "Invalid email format"}), 400
        if U.if_mail_exists(data["user_email"]):
            return jsonify ({"Error":"Email already exists"}), 400
        if not str(data["first_name"]).isalpha():
            return jsonify({"Error": "first_name must contain only letters"}), 400
        if not str(data["last_name"]).isalpha():
            return jsonify({"Error": "last_name must contain only letters"}), 400
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
    def show_user_by_email_and_password():
        data = request.get_json()
        if not data:
            return jsonify ({"Error":"Missing values or data empty"}), 400
        if "user_email" not in data or "user_password" not in data:
            return jsonify ({"Error":"Missing values or data empty"}), 400
        
        result = U.show_user_by_email_and_password(data["user_email"], data["user_password"])
        
        # בדיקה אם יש שגיאה בהתחברות
        if "Massages" in result:
            return jsonify(result), 400
        
        # בדיקה אם המשתמש מוחרם
        if result and "is_banned" in result and result["is_banned"]:
            # בדיקה אם ההרחקה הסתיימה
            ban_until = result.get('ban_until')
            if ban_until:
                from datetime import datetime
                try:
                    ban_date = datetime.fromisoformat(ban_until.replace('Z', '+00:00'))
                    current_date = datetime.now()
                    if current_date > ban_date:
                        # ההרחקה הסתיימה - ביטול ההרחקה
                        U.update_user_by_id(result["user_id"], {
                            "is_banned": False,
                            "ban_reason": None,
                            "ban_until": None
                        })
                    else:
                        # המשתמש עדיין מוחרם
                        return jsonify({
                            "Error": "המשתמש הורחק מהמערכת. אנא פנה למנהל המערכת לפרטים נוספים."
                        }), 403
                except:
                    # אם יש בעיה עם התאריך, המשתמש נשאר מוחרם
                    return jsonify({
                        "Error": "המשתמש הורחק מהמערכת. אנא פנה למנהל המערכת לפרטים נוספים."
                    }), 403
            else:
                # הרחקה קבועה (ללא תאריך סיום)
                return jsonify({
                    "Error": "המשתמש הורחק מהמערכת לצמיתות. אנא פנה למנהל המערכת לפרטים נוספים."
                }), 403
        
        return jsonify(result), 201

    @staticmethod
    def update_user_by_id(user_id):
        data = request.get_json()
        lis_requimints = ["first_name", "last_name", "user_email", "user_password", "password", "current_password", "new_password", "role_id"]
        if not data:
            return jsonify ({"Error":"Missing values or data empty"}), 400
        
        # בדיקה שחובה להזין סיסמה נוכחית
        if "current_password" not in data or not data["current_password"].strip():
            return jsonify ({"Error":"חובה להזין את הסיסמה הנוכחית"}), 400
        
        # בדיקת הסיסמה הנוכחית
        current_user = U.show_user_by_id(user_id)
        if not current_user or "Massages" in current_user:
            return jsonify ({"Error":"משתמש לא נמצא"}), 400
        
        if current_user["user_password"] != data["current_password"]:
            return jsonify ({"Error":"הסיסמה הנוכחית שגויה"}), 400
        
        # הכנת הנתונים לעדכון
        update_data = {}
        
        # המרת new_password ל-user_password אם נשלח
        if "new_password" in data and data["new_password"].strip():
            if len(data["new_password"].strip()) < 4:
                return jsonify ({"Error":"סיסמה חדשה חייבת להיות לפחות 4 תווים"}), 400
            update_data["user_password"] = data["new_password"]
        
        # הוספת שדות אחרים לעדכון
        for field in ["first_name", "last_name", "user_email"]:
            if field in data:
                update_data[field] = data[field]
        
        # בדיקות תקינות
        if "user_email" in update_data:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", update_data["user_email"]):
                return jsonify({"Error": "פורמט אימייל לא תקין"}), 400
            
            # בדיקה שהאימייל לא קיים אצל משתמש אחר
            if current_user.get("user_email") != update_data["user_email"]:
                if U.if_mail_exists(update_data["user_email"]):
                    return jsonify ({"Error":"האימייל כבר קיים במערכת"}), 400
        
        if "first_name" in update_data and (not str(update_data["first_name"]).isalpha()):
            return jsonify({"Error": "שם פרטי חייב להכיל רק אותיות"}), 400
        if "last_name" in update_data and (not str(update_data["last_name"]).isalpha()):
            return jsonify({"Error": "שם משפחה חייב להכיל רק אותיות"}), 400
        
        if "role_id" in data:
            return jsonify({"error":"לא ניתן לעדכן role_id (ניתן לעדכן רק במסד הנתונים)"})
        
        result = U.update_user_by_id(user_id, update_data)
        if result is None or "Massages" in result:
            return jsonify({"Error": "משתמש לא נמצא"}), 400
        return jsonify(result), 201
    
    @staticmethod
    def delete_user_by_id(user_id):
        result = U.delete_user_by_id(user_id)
        return jsonify(result), 201
    
    @staticmethod
    def check_if_email_exists():
        data = request.get_json()
        if not data:
            return jsonify ({"Error":"Missing values or data empty"}), 400
        if not "user_email" in data:
            return jsonify ({"error":"wrong value"})
        if U.if_mail_exists(data["user_email"]):
            return jsonify({"Message":"email alredy exists in system"})
        else:
            return jsonify({"Message":"email not exists"})
    
    @staticmethod
    def update_profile_image(user_id):
        try:
            if 'profile_image' not in request.files:
                return jsonify({"error": "No image file provided"}), 400
            
            file = request.files['profile_image']
            if file.filename == '':
                return jsonify({"error": "No file selected"}), 400
            
            if file:
                # בדיקת סוג הקובץ
                allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
                    return jsonify({"error": "Invalid file type. Only images are allowed"}), 400
                
                # מחיקת תמונה ישנה אם קיימת
                current_user = U.show_user_by_id(user_id)
                if current_user and current_user.get('profile_image'):
                    import os
                    old_file_path = os.path.join('uploads/profile_images', current_user['profile_image'].split('/')[-1])
                    if os.path.exists(old_file_path):
                        os.remove(old_file_path)
                
                # שמירת הקובץ
                import os
                upload_folder = 'uploads/profile_images'
                if not os.path.exists(upload_folder):
                    os.makedirs(upload_folder)
                
                # יצירת שם קובץ ייחודי
                import uuid
                file_extension = file.filename.rsplit('.', 1)[1].lower()
                unique_filename = f"profile_{user_id}_{uuid.uuid4().hex}.{file_extension}"
                file_path = os.path.join(upload_folder, unique_filename)
                
                file.save(file_path)
                
                # עדכון מסד הנתונים עם הנתיב החדש
                profile_image_url = f"/uploads/profile_images/{unique_filename}"
                result = U.update_profile_image(user_id, profile_image_url)
                
                if result is None:
                    return jsonify({"error": "User not found"}), 404
                
                return jsonify({
                    "message": "Profile image updated successfully",
                    "profile_image_url": profile_image_url
                }), 200
                
        except Exception as e:
            return jsonify({"error": f"Error updating profile image: {str(e)}"}), 500
    
    @staticmethod
    def remove_profile_image(user_id):
        try:
            # קבלת פרטי המשתמש הנוכחי
            user = U.show_user_by_id(user_id)
            if not user or 'error' in user:
                return jsonify({"error": "User not found"}), 404
            
            # מחיקת הקובץ מהדיסק אם קיים
            if user.get('profile_image'):
                import os
                file_path = os.path.join('uploads/profile_images', user['profile_image'].split('/')[-1])
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # עדכון מסד הנתונים - הסרת תמונת הפרופיל
            result = U.update_profile_image(user_id, None)
            
            if result is None:
                return jsonify({"error": "User not found"}), 404
            
            return jsonify({
                "message": "Profile image removed successfully"
            }), 200
            
        except Exception as e:
            return jsonify({"error": f"Error removing profile image: {str(e)}"}), 500
    
    @staticmethod
    def ban_user(user_id):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data provided"}), 400
            
            # בדיקה שהמשתמש קיים
            current_user = U.show_user_by_id(user_id)
            if not current_user or "Massages" in current_user:
                return jsonify({"error": "משתמש לא נמצא"}), 404
            
            # הכנת נתוני ההרחקה
            ban_data = {
                "is_banned": True,
                "ban_reason": data.get("ban_reason", ""),
                "ban_until": data.get("ban_until", None)
            }
            
            # עדכון המשתמש במסד הנתונים
            result = U.update_user_by_id(user_id, ban_data)
            if result is None or "Massages" in result:
                return jsonify({"error": "שגיאה בעדכון המשתמש"}), 500
            
            return jsonify({
                "message": f"המשתמש {current_user.get('first_name', '')} {current_user.get('last_name', '')} הורחק בהצלחה",
                "ban_reason": ban_data["ban_reason"],
                "ban_until": ban_data["ban_until"]
            }), 200
            
        except Exception as e:
            return jsonify({"error": f"שגיאה בהרחקת המשתמש: {str(e)}"}), 500
    
    @staticmethod
    def unban_user(user_id):
        try:
            # בדיקה שהמשתמש קיים
            current_user = U.show_user_by_id(user_id)
            if not current_user or "Massages" in current_user:
                return jsonify({"error": "משתמש לא נמצא"}), 404
            
            # ביטול ההרחקה
            unban_data = {
                "is_banned": False,
                "ban_reason": None,
                "ban_until": None
            }
            
            # עדכון המשתמש במסד הנתונים
            result = U.update_user_by_id(user_id, unban_data)
            if result is None or "Massages" in result:
                return jsonify({"error": "שגיאה בעדכון המשתמש"}), 500
            
            return jsonify({
                "message": f"הרחקת המשתמש {current_user.get('first_name', '')} {current_user.get('last_name', '')} בוטלה בהצלחה"
            }), 200
            
        except Exception as e:
            return jsonify({"error": f"שגיאה בביטול הרחקת המשתמש: {str(e)}"}), 500
        
