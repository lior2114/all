from flask import jsonify, request, current_app, g
from Models.Users_Models import Users_Model as U
import re 
import hashlib
from datetime import datetime, timedelta
import jwt


def generate_jwt_token(user_id, role_name, expires_minutes=60*24*7):
    """Generate JWT token with user id and role."""
    payload = {
        "sub": user_id,
        "role": role_name,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes),
    }
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    # PyJWT returns string in v2
    return token


def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"Error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"Error": "Invalid token"}


def auth_required(roles=None):
    """Decorator to require JWT auth. Optionally restrict by roles (list of role names)."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization", "")
            if not auth_header.startswith("Bearer "):
                return jsonify({"Error": "Authorization header missing or invalid"}), 401
            token = auth_header.split(" ", 1)[1].strip()
            payload = decode_jwt_token(token)
            if isinstance(payload, dict) and "Error" in payload:
                return jsonify(payload), 401
            # נרמול מזהה משתמש למספר
            user_id_claim = payload.get("sub")
            try:
                user_id_claim = int(user_id_claim)
            except Exception:
                pass
            g.current_user = {"user_id": user_id_claim, "role_name": payload.get("role")}
            if roles and g.current_user["role_name"] not in roles:
                return jsonify({"Error": "Insufficient permissions"}), 403
            return func(*args, **kwargs)
        
        # Preserve function name and doc
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator

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
        # הוספת טוקן JWT בתגובה
        try:
            token = generate_jwt_token(result["user_id"], "user")
            result["token"] = token
        except Exception:
            pass
        return jsonify(result) , 201

    @staticmethod
    @auth_required(roles=["admin"]) 
    def get_all_users(): 
        result = U.get_all_users()
        return jsonify(result), 201
    
    @staticmethod
    @auth_required()
    def show_user_by_id(user_id):
        # דרוש שהמשתמש המבקש יהיה אותו משתמש או אדמין
        if g.current_user["role_name"] != "admin" and g.current_user["user_id"] != user_id:
            return jsonify({"Error": "Forbidden"}), 403
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
        
        # הוספת טוקן JWT
        try:
            token = generate_jwt_token(result["user_id"], result.get("role_name", "user"))
            result["token"] = token
        except Exception:
            pass
        return jsonify(result), 201

    @staticmethod
    @auth_required()
    def update_user_by_id(user_id):
        data = request.get_json()
        lis_requimints = ["first_name", "last_name", "user_email", "user_password", "password", "current_password", "new_password", "role_id"]
        if not data:
            return jsonify ({"Error":"Missing values or data empty"}), 400
        
        # הרשאות: המשתמש עצמו או אדמין
        if g.current_user["role_name"] != "admin" and g.current_user["user_id"] != user_id:
            return jsonify({"Error": "Forbidden"}), 403
        
        # בדיקה שחובה להזין סיסמה נוכחית
        if "current_password" not in data or not data["current_password"].strip():
            return jsonify ({"Error":"חובה להזין את הסיסמה הנוכחית"}), 400
        
        # בדיקת סיסמה נוכחית
        user = U.show_user_by_id(user_id)
        if "Message" in user:
            return jsonify(user), 400
        

        
        # בדיקת סיסמה נוכחית - שליפה עדכנית מהמסד
        user_auth = U.get_user_auth_by_id(user_id)
        current_password = user_auth["user_password"] if user_auth else ""
        provided_password = data["current_password"]
        
        password_matches = False
        try:
            # תמיכה בסיסמאות בפורמט Werkzeug
            if isinstance(current_password, str) and current_password.startswith("pbkdf2:sha256"):
                from werkzeug.security import check_password_hash
                password_matches = check_password_hash(current_password, provided_password)
            # תמיכה בסיסמאות ישנות בפורמט SHA-256 hex
            elif len(current_password) == 64 and all(c in '0123456789abcdef' for c in current_password.lower()):
                hashed_provided = hashlib.sha256(provided_password.encode()).hexdigest()
                password_matches = current_password == hashed_provided
            else:
                # טקסט רגיל
                password_matches = current_password == provided_password
        except Exception:
            password_matches = False
        
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
            # שמירת הסיסמה החדשה עם הצפנה
            try:
                from werkzeug.security import generate_password_hash
                update_data["user_password"] = generate_password_hash(data["new_password"])
            except Exception:
                update_data["user_password"] = data["new_password"]
    
        
        if "role_id" in data and data["role_id"]:
            # שינוי תפקיד מותר רק לאדמין
            if g.current_user["role_name"] != "admin":
                return jsonify({"Error": "Only admin can change role"}), 403
            update_data["role_id"] = data["role_id"]
        
        if not update_data:
            return jsonify({"Error": "No valid data to update"}), 400
        
        result = U.update_user_by_id(user_id, update_data)
        return jsonify(result), 201

    @staticmethod
    @auth_required(roles=["admin"]) 
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
    @auth_required()
    def update_profile_image(user_id):
        if g.current_user["role_name"] != "admin" and g.current_user["user_id"] != user_id:
            return jsonify({"Error": "Forbidden"}), 403
        data = request.get_json()
        if not data or "profile_image" not in data:
            return jsonify({"Error": "Profile image URL is required"}), 400
        
        result = U.update_profile_image(user_id, data["profile_image"])
        if not result:
            return jsonify({"Error": "User not found"}), 404
        
        return jsonify(result), 200

    @staticmethod
    @auth_required()
    def remove_profile_image(user_id):
        if g.current_user["role_name"] != "admin" and g.current_user["user_id"] != user_id:
            return jsonify({"Error": "Forbidden"}), 403
        result = U.update_profile_image(user_id, None)
        if not result:
            return jsonify({"Error": "User not found"}), 404
        
        return jsonify(result), 200

    @staticmethod
    @auth_required(roles=["admin"]) 
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
    @auth_required(roles=["admin"]) 
    def unban_user(user_id):
        data = request.get_json()
        unbanned_by = data.get("unbanned_by") if data else None
        
        result = U.unban_user(user_id, unbanned_by)
        return jsonify(result), 200

    @staticmethod
    @auth_required()
    def update_user_progress():
        data = request.get_json()
        required_fields = ["user_id", "lesson_id", "lesson_type", "wpm", "accuracy", "errors", "time_spent"]
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"Error": "Missing required fields"}), 400
        if g.current_user["role_name"] != "admin" and g.current_user["user_id"] != data.get("user_id"):
            return jsonify({"Error": "Forbidden"}), 403
        
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
    @auth_required()
    def get_user_progress(user_id):
        if g.current_user["role_name"] != "admin" and g.current_user["user_id"] != user_id:
            return jsonify({"Error": "Forbidden"}), 403
        result = U.get_user_progress(user_id)
        return jsonify(result), 200

    @staticmethod
    @auth_required(roles=["admin"]) 
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
        
