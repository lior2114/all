import sqlite3
import os
from datetime import datetime, timedelta

# קביעת נתיב מוחלט לבסיס הנתונים - תמיד בתוך תיקיית Data_Base
current_dir = os.path.dirname(os.path.abspath(__file__))  # תיקיית Models
data_base_dir = os.path.dirname(current_dir)  # תיקיית Data_Base
sql_dir = os.path.join(data_base_dir, "SQL")
path_name = os.path.join(sql_dir, "Mydb.db")

# יצירת תיקיית SQL אם לא קיימת
if not os.path.exists(sql_dir):
    os.makedirs(sql_dir)
    print(f"Created SQL directory at: {sql_dir}")

print(f"Database path: {path_name}")

class Users_Model:

    @staticmethod
    def get_db_connection():
        connection = sqlite3.connect(path_name, timeout=20.0)
        connection.execute("PRAGMA journal_mode=WAL")
        return connection
    
    @staticmethod
    def create_table():
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # יצירת טבלת תפקידים
            sql = '''create table if not exists roles (
                role_id integer primary key autoincrement,
                role_name text not null unique,
                description text
                )'''
            cursor.execute(sql)
            
            # הוספת תפקידים בסיסיים
            try:
                cursor.execute("INSERT INTO roles (role_name, description) VALUES ('admin', 'מנהל מערכת')")
                cursor.execute("INSERT INTO roles (role_name, description) VALUES ('user', 'משתמש רגיל')")
                cursor.execute("INSERT INTO roles (role_name, description) VALUES ('moderator', 'מנחה')")
            except sqlite3.IntegrityError:
                # התפקידים כבר קיימים
                pass
            
            # יצירת טבלת משתמשים
            sql = '''create table if not exists users (
                user_id integer primary key autoincrement,
                first_name text not null,
                last_name text not null,
                user_email text not null unique,
                user_password text not null,
                role_id integer default 2,
                profile_image text,
                is_banned boolean DEFAULT 0,
                ban_reason text,
                ban_until text,
                created_at text DEFAULT CURRENT_TIMESTAMP,
                last_login text,
                FOREIGN KEY (role_id) REFERENCES roles(role_id)
                )'''
            cursor.execute(sql)
            
            # יצירת טבלת התקדמות משתמשים
            sql = '''create table if not exists user_progress (
                progress_id integer primary key autoincrement,
                user_id integer not null,
                total_lessons integer default 0,
                completed_lessons integer default 0,
                total_words_typed integer default 0,
                total_time_spent integer default 0,
                average_wpm real default 0,
                average_accuracy real default 0,
                last_updated text DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
                )'''
            cursor.execute(sql)
            
            # יצירת טבלת שיעורים שהושלמו
            sql = '''create table if not exists lessons_completed (
                completion_id integer primary key autoincrement,
                user_id integer not null,
                lesson_id text not null,
                lesson_type text not null,
                wpm real,
                accuracy real,
                errors integer,
                time_spent integer,
                completed_at text DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
                )'''
            cursor.execute(sql)
            
            # יצירת טבלת היסטוריית הרחקות
            sql = '''create table if not exists ban_history (
                ban_id integer primary key autoincrement,
                user_id integer not null,
                banned_by integer not null,
                ban_reason text not null,
                ban_until text,
                is_permanent boolean default 0,
                created_at text DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (banned_by) REFERENCES users(user_id)
                )'''
            cursor.execute(sql)
            
            connection.commit()
            cursor.close()

    @staticmethod
    def create_user(first_name, last_name, user_email, user_password):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # הצפנת הסיסמה
            hashed_password = user_password # מסירת הצפנה
            
            sql = "insert into users (first_name, last_name, user_email, user_password) values (?, ?, ?, ?)"
            cursor.execute(sql,(first_name, last_name, user_email, hashed_password))
            connection.commit()
            
            user_id = cursor.lastrowid
            
            # יצירת רשומת התקדמות למשתמש החדש
            sql = "insert into user_progress (user_id) values (?)"
            cursor.execute(sql, (user_id,))
            
            connection.commit()
            cursor.close()
            
            return {
                "user_id": user_id,
                "first_name": first_name,
                "last_name": last_name,
                "user_email": user_email,
                "role_id": 2
            }

    @staticmethod
    def get_all_users():
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT users.user_id, users.first_name, users.last_name, users.user_email, 
                    roles.role_name, users.is_banned, users.ban_reason, users.ban_until,
                    users.created_at, users.last_login, user_progress.completed_lessons,
                    user_progress.total_lessons
                    FROM users
                    INNER JOIN roles ON roles.role_id = users.role_id
                    LEFT JOIN user_progress ON user_progress.user_id = users.user_id
                    ORDER BY users.created_at DESC
                    '''
            cursor.execute(sql)
            users = cursor.fetchall()
            if not users:
                cursor.close()
                return {"Message":"No users has been added yet"}
            cursor.close()
            return [
                {
                    "user_id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "user_email": row[3],
                    "role_name": row[4],
                    "is_banned": bool(row[5]) if row[5] else False,
                    "ban_reason": row[6],
                    "ban_until": row[7],
                    "created_at": row[8],
                    "last_login": row[9],
                    "completed_lessons": row[10] or 0,
                    "total_lessons": row[11] or 0
                }
                for row in users
            ]
    

    @staticmethod
    def show_user_by_id(user_id):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT users.*, roles.role_name, user_progress.*
                    FROM users
                    INNER JOIN roles ON roles.role_id = users.role_id
                    LEFT JOIN user_progress ON user_progress.user_id = users.user_id
                    WHERE users.user_id = ?'''
            cursor.execute(sql,(user_id,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Message":"No users with that ID"}
            cursor.close()
            return {
                "user_id": user[0],
                "first_name": user[1],
                "last_name": user[2],
                "user_email": user[3],
                "user_password": user[4],  # הוספת הסיסמה המוצפנת
                "role_name": user[11],
                "profile_image": user[6],
                "is_banned": bool(user[7]) if user[7] else False,
                "ban_reason": user[8],
                "ban_until": user[9],
                "created_at": user[10],
                "last_login": user[11],
                "progress": {
                    "total_lessons": user[16] or 0,
                    "completed_lessons": user[17] or 0,
                    "total_words_typed": user[18] or 0,
                    "total_time_spent": user[19] or 0,
                    "average_wpm": user[20] or 0,
                    "average_accuracy": user[21] or 0
                }
            }
        
    @staticmethod
    def show_user_by_email_and_password(user_email, user_password):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # הצפנת הסיסמה לבדיקה
            hashed_password = user_password # מסירת הצפנה
            
            sql = '''SELECT users.*, roles.role_name
                    FROM users
                    INNER JOIN roles ON roles.role_id = users.role_id
                    WHERE users.user_email = ? AND users.user_password = ?'''
            cursor.execute(sql,(user_email, hashed_password))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Message":"No users with that email and password"}
            
            # עדכון זמן התחברות אחרון
            sql = "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE user_id = ?"
            cursor.execute(sql, (user[0],))
            connection.commit()
            
            cursor.close()
            return {
                "user_id": user[0],
                "first_name": user[1],
                "last_name": user[2],
                "user_email": user[3],
                "user_password": user[4],  # הוספת הסיסמה המוצפנת
                "role_name": user[12],  # role_name נמצא בעמודה 12 (אינדקס 11)
                "profile_image": user[6],
                "is_banned": bool(user[7]) if user[7] else False,
                "ban_reason": user[8],
                "ban_until": user[9],
                "created_at": user[10]
            }
        
    @staticmethod
    def update_user_by_id(user_id, data):
        try:
            print(f"Updating user {user_id} with data: {data}")  # Debug log
            with Users_Model.get_db_connection() as connection:
                cursor = connection.cursor()
                sql = "select * from users where user_id = ?"
                cursor.execute(sql,(user_id,))
                user = cursor.fetchone()
                if not user:
                    cursor.close()
                    return {"Message":"No users with that ID"}
                
                # אם יש סיסמה חדשה, היא כבר מוצפנת מהקונטרולר
                # לא צריך להצפין אותה שוב
                
                set_clauses = []
                values = []
                for key, value in data.items():
                    set_clauses.append(f"{key} = ?")
                    values.append(value)
                values.append(user_id)
                
                sql = f"UPDATE users SET {', '.join(set_clauses)} WHERE user_id = ?"
                print(f"Executing SQL: {sql}")  # Debug log
                print(f"Values: {values}")  # Debug log
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                print(f"User {user_id} updated successfully")  # Debug log
                return {"Message":f"user_id {user_id} has been updated successfully"}
        except Exception as e:
            print(f"Database error: {str(e)}")  # Debug log
            return {"Error": f"Database error: {str(e)}"}
    
    @staticmethod
    def delete_user_by_id(user_id):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Message":"No users with that ID"}
            
            # מחיקת נתונים קשורים
            cursor.execute("DELETE FROM user_progress WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM lessons_completed WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM ban_history WHERE user_id = ?", (user_id,))
            
            sql = "delete from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            connection.commit()
            cursor.close()
            return {"Message":"User deleted successfully"}

    @staticmethod
    def if_mail_exists(user_email):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select user_email from users where user_email = ?"
            cursor.execute(sql,(user_email,))
            exists = cursor.fetchone()
            cursor.close()
            return exists is not None
    
    @staticmethod
    def update_profile_image(user_id, profile_image_url):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return None
            
            if profile_image_url is None:
                sql = "update users set profile_image = NULL where user_id = ?"
                cursor.execute(sql,(user_id,))
            else:
                sql = "update users set profile_image = ? where user_id = ?"
                cursor.execute(sql,(profile_image_url, user_id,))
            
            connection.commit()
            cursor.close()
            return {"Message": f"Profile image updated successfully for user_id {user_id}"}

    @staticmethod
    def ban_user(user_id, ban_reason, ban_until=None, banned_by=None):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # בדיקה שהמשתמש קיים
            sql = "select * from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Message":"No users with that ID"}
            
            # עדכון המשתמש
            if ban_until:
                sql = "UPDATE users SET is_banned = 1, ban_reason = ?, ban_until = ? WHERE user_id = ?"
                cursor.execute(sql, (ban_reason, ban_until, user_id))
            else:
                sql = "UPDATE users SET is_banned = 1, ban_reason = ?, ban_until = NULL WHERE user_id = ?"
                cursor.execute(sql, (ban_reason, user_id))
            
            # הוספה להיסטוריית הרחקות
            sql = "INSERT INTO ban_history (user_id, banned_by, ban_reason, ban_until, is_permanent) VALUES (?, ?, ?, ?, ?)"
            is_permanent = ban_until is None
            cursor.execute(sql, (user_id, banned_by, ban_reason, ban_until, is_permanent))
            
            connection.commit()
            cursor.close()
            return {"Message": f"User {user_id} has been banned successfully", "success": True, "user_id": user_id}

    @staticmethod
    def unban_user(user_id, unbanned_by=None):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # בדיקה שהמשתמש קיים
            sql = "select * from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Message":"No users with that ID"}
            
            # ביטול ההרחקה
            sql = "UPDATE users SET is_banned = 0, ban_reason = NULL, ban_until = NULL WHERE user_id = ?"
            cursor.execute(sql, (user_id,))
            
            connection.commit()
            cursor.close()
            return {"Message": f"User {user_id} has been unbanned successfully"}

    @staticmethod
    def update_user_progress(user_id, lesson_id, lesson_type, wpm, accuracy, errors, time_spent):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # הוספת השיעור שהושלם
            sql = """INSERT INTO lessons_completed 
                    (user_id, lesson_id, lesson_type, wpm, accuracy, errors, time_spent) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(sql, (user_id, lesson_id, lesson_type, wpm, accuracy, errors, time_spent))
            
            # עדכון התקדמות המשתמש
            sql = """UPDATE user_progress SET 
                    completed_lessons = completed_lessons + 1,
                    total_words_typed = total_words_typed + ?,
                    total_time_spent = total_time_spent + ?,
                    last_updated = CURRENT_TIMESTAMP
                    WHERE user_id = ?"""
            cursor.execute(sql, (wpm * time_spent / 60, time_spent, user_id))
            
            # חישוב ממוצעים חדשים
            sql = """SELECT AVG(wpm), AVG(accuracy) FROM lessons_completed WHERE user_id = ?"""
            cursor.execute(sql, (user_id,))
            avg_wpm, avg_accuracy = cursor.fetchone()
            
            if avg_wpm and avg_accuracy:
                sql = """UPDATE user_progress SET 
                        average_wpm = ?, average_accuracy = ? 
                        WHERE user_id = ?"""
                cursor.execute(sql, (avg_wpm, avg_accuracy, user_id))
            
            connection.commit()
            cursor.close()
            return {"Message": "Progress updated successfully"}

    @staticmethod
    def get_user_progress(user_id):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # קבלת התקדמות כללית
            sql = "SELECT * FROM user_progress WHERE user_id = ?"
            cursor.execute(sql, (user_id,))
            progress = cursor.fetchone()
            
            if not progress:
                cursor.close()
                return {"Message": "No progress found for this user"}
            
            # קבלת שיעורים אחרונים שהושלמו
            sql = """SELECT lesson_id, lesson_type, wpm, accuracy, errors, time_spent, completed_at 
                    FROM lessons_completed 
                    WHERE user_id = ? 
                    ORDER BY completed_at DESC 
                    LIMIT 10"""
            cursor.execute(sql, (user_id,))
            recent_lessons = cursor.fetchall()
            
            cursor.close()
            
            return {
                "total_lessons": progress[2] or 0,
                "completed_lessons": progress[3] or 0,
                "total_words_typed": progress[4] or 0,
                "total_time_spent": progress[5] or 0,
                "average_wpm": progress[6] or 0,
                "average_accuracy": progress[7] or 0,
                "last_updated": progress[8],
                "recent_lessons": [
                    {
                        "lesson_id": lesson[0],
                        "lesson_type": lesson[1],
                        "wpm": lesson[2],
                        "accuracy": lesson[3],
                        "errors": lesson[4],
                        "time_spent": lesson[5],
                        "completed_at": lesson[6]
                    }
                    for lesson in recent_lessons
                ]
            }

    @staticmethod
    def get_admin_dashboard_data():
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            
            # סטטיסטיקות כללית
            sql = "SELECT COUNT(*) FROM users"
            cursor.execute(sql)
            total_users = cursor.fetchone()[0]
            
            sql = "SELECT COUNT(*) FROM users WHERE is_banned = 1"
            cursor.execute(sql)
            banned_users = cursor.fetchone()[0]
            
            sql = "SELECT COUNT(*) FROM users WHERE DATE(created_at) = DATE('now')"
            cursor.execute(sql)
            new_users_today = cursor.fetchone()[0]
            
            sql = "SELECT COUNT(*) FROM lessons_completed WHERE DATE(completed_at) = DATE('now')"
            cursor.execute(sql)
            lessons_completed_today = cursor.fetchone()[0]
            
            # משתמשים פעילים (התחברו ב-7 ימים אחרונים)
            sql = "SELECT COUNT(*) FROM users WHERE last_login >= DATE('now', '-7 days')"
            cursor.execute(sql)
            active_users = cursor.fetchone()[0]
            
            cursor.close()
            
            return {
                "total_users": total_users,
                "banned_users": banned_users,
                "new_users_today": new_users_today,
                "lessons_completed_today": lessons_completed_today,
                "active_users": active_users
            }