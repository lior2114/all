from flask import jsonify, request
from Models.Users_Models import Users_Model as U
import re 
import hashlib
from datetime import datetime, timedelta

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
        if "Message" in result:
            return jsonify(result), 400
        
        # בדיקה אם המשתמש מוחרם
        if result and "is_banned" in result and result["is_banned"]:
            # בדיקה אם ההרחקה הסתיימה
            ban_until = result.get('ban_until')
            if ban_until:
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
        
        # בדיקת סיסמה נוכחית
        user = U.show_user_by_id(user_id)
        if "Message" in user:
            return jsonify(user), 400
        

        
        # בדיקת סיסמה נוכחית - תמיכה בסיסמאות מוצפנות ורגילות
        current_password = user["user_password"]
        provided_password = data["current_password"]
        
        # בדיקה אם הסיסמה מוצפנת (64 תווים hex)
        is_hashed = len(current_password) == 64 and all(c in '0123456789abcdef' for c in current_password.lower())
        
        if is_hashed:
            # הסיסמה מוצפנת - נצפין את הסיסמה שהוזנה
            hashed_provided = hashlib.sha256(provided_password.encode()).hexdigest()
            password_matches = current_password == hashed_provided
        else:
            # הסיסמה לא מוצפנת - בדיקה רגילה
            password_matches = current_password == provided_password
        
        if not password_matches:
            error_response = {"Error": "הסיסמה הנוכחית שגויה"}
            return jsonify(error_response), 400
        
        # הכנת נתונים לעדכון
        update_data = {}
        
        if "first_name" in data and data["first_name"]:
            if not str(data["first_name"]).isalpha():
                return jsonify({"Error": "first_name must contain only letters"}), 400
            update_data["first_name"] = data["first_name"]
        
        if "last_name" in data and data["last_name"]:
            if not str(data["last_name"]).isalpha():
                return jsonify({"Error": "last_name must contain only letters"}), 400
            update_data["last_name"] = data["last_name"]
        
        if "user_email" in data and data["user_email"]:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", data["user_email"]):
                return jsonify({"Error": "Invalid email format"}), 400
            if U.if_mail_exists(data["user_email"]) and data["user_email"] != user["user_email"]:
                return jsonify({"Error": "Email already exists"}), 400
            update_data["user_email"] = data["user_email"]
        
        if "new_password" in data and data["new_password"]:
            if len(data["new_password"].strip()) < 4:
                return jsonify({"Error": "password need to be more then 4 values"}), 400
            # שמירת הסיסמה החדשה ללא הצפנה
            update_data["user_password"] = data["new_password"]
    
        
        if "role_id" in data and data["role_id"]:
            update_data["role_id"] = data["role_id"]
        
        if not update_data:
            return jsonify({"Error": "No valid data to update"}), 400
        
        result = U.update_user_by_id(user_id, update_data)
        return jsonify(result), 201

    @staticmethod
    def delete_user_by_id(user_id):
        result = U.delete_user_by_id(user_id)
        return jsonify(result), 201

    @staticmethod
    def check_if_email_exists():
        email = request.args.get('email')
        if not email:
            return jsonify({"Error": "Email parameter is required"}), 400
        
        exists = U.if_mail_exists(email)
        return jsonify({"exists": exists}), 200

    @staticmethod
    def update_profile_image(user_id):
        data = request.get_json()
        if not data or "profile_image" not in data:
            return jsonify({"Error": "Profile image URL is required"}), 400
        
        result = U.update_profile_image(user_id, data["profile_image"])
        if not result:
            return jsonify({"Error": "User not found"}), 404
        
        return jsonify(result), 200

    @staticmethod
    def remove_profile_image(user_id):
        result = U.update_profile_image(user_id, None)
        if not result:
            return jsonify({"Error": "User not found"}), 404
        
        return jsonify(result), 200

    @staticmethod
    def ban_user(user_id):
        data = request.get_json()
        
        if not data or "ban_reason" not in data:
            return jsonify({"Error": "Ban reason is required"}), 400
        
        ban_reason = data["ban_reason"]
        ban_until = data.get("ban_until")  # יכול להיות None להרחקה קבועה
        banned_by = data.get("banned_by")
        
        # אם יש תאריך הרחקה, בדוק שהוא תקין
        if ban_until:
            try:
                datetime.fromisoformat(ban_until.replace('Z', '+00:00'))
            except:
                return jsonify({"Error": "Invalid ban date format"}), 400
        
        result = U.ban_user(user_id, ban_reason, ban_until, banned_by)
        return jsonify(result), 200

    @staticmethod
    def unban_user(user_id):
        data = request.get_json()
        unbanned_by = data.get("unbanned_by") if data else None
        
        result = U.unban_user(user_id, unbanned_by)
        return jsonify(result), 200

    @staticmethod
    def update_user_progress():
        data = request.get_json()
        required_fields = ["user_id", "lesson_id", "lesson_type", "wpm", "accuracy", "errors", "time_spent"]
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"Error": "Missing required fields"}), 400
        
        result = U.update_user_progress(
            data["user_id"],
            data["lesson_id"],
            data["lesson_type"],
            data["wpm"],
            data["accuracy"],
            data["errors"],
            data["time_spent"]
        )
        return jsonify(result), 200

    @staticmethod
    def get_user_progress(user_id):
        result = U.get_user_progress(user_id)
        return jsonify(result), 200

    @staticmethod
    def get_admin_dashboard():
        result = U.get_admin_dashboard_data()
        return jsonify(result), 200

    @staticmethod
    def create_admin_user():
        """יצירת משתמש אדמין ראשון"""
        data = request.get_json()
        if not data:
            return jsonify({"Error": "Missing data"}), 400
        
        # בדיקה אם כבר יש אדמין במערכת
        all_users = U.get_all_users()
        if isinstance(all_users, list) and len(all_users) > 0:
            return jsonify({"Error": "Admin user already exists"}), 400
        
        # יצירת משתמש אדמין
        result = U.create_user(
            first_name=data.get("first_name", "Admin"),
            last_name=data.get("last_name", "User"),
            user_email=data["user_email"],
            user_password=data["user_password"]
        )
        
        # עדכון התפקיד לאדמין
        if "user_id" in result:
            U.update_user_by_id(result["user_id"], {"role_id": 1})
            result["role_id"] = 1
        
        return jsonify(result), 201
        
