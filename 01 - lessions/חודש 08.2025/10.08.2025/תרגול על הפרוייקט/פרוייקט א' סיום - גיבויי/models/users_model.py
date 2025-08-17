import sqlite3
import os
path_name = "./SQL/Mydb.db"
if not os.path.exists("./SQL"):
    os.makedirs("./SQL")

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
            sql = '''create table if not exists users (
                user_id integer primary key autoincrement,
                first_name text not null,
                last_name text not null,
                user_email text not null,
                user_password text not null,
                role_id integer default 2,
                profile_image text,
                FOREIGN KEY (role_id) REFERENCES roles(role_id)
                )'''
            cursor.execute(sql)
            connection.commit()
            
            # הוספת עמודת profile_image אם לא קיימת
            try:
                cursor.execute("ALTER TABLE users ADD COLUMN profile_image text")
                connection.commit()
            except sqlite3.OperationalError:
                # העמודה כבר קיימת
                pass
            
            # הוספת עמודות להרחקת משתמשים אם לא קיימות
            try:
                cursor.execute("ALTER TABLE users ADD COLUMN is_banned boolean DEFAULT 0")
                connection.commit()
            except sqlite3.OperationalError:
                # העמודה כבר קיימת
                pass
            
            try:
                cursor.execute("ALTER TABLE users ADD COLUMN ban_reason text")
                connection.commit()
            except sqlite3.OperationalError:
                # העמודה כבר קיימת
                pass
            
            try:
                cursor.execute("ALTER TABLE users ADD COLUMN ban_until text")
                connection.commit()
            except sqlite3.OperationalError:
                # העמודה כבר קיימת
                pass
            
            cursor.close()

    @staticmethod
    def create_user(first_name, last_name, user_email, user_password):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "insert into users (first_name, last_name, user_email, user_password) values (?, ?, ?, ?)"
            cursor.execute(sql,(first_name, last_name, user_email, user_password))
            connection.commit()
            # השורה הזאת שומרת את ה-id של המשתמש האחרון שנוסף לטבלה (primary key שנוצר אוטומטית)
            user_id = cursor.lastrowid
            cursor.close()
            return {
                "user_id":user_id,
                "first_name": first_name,
                "last_name": last_name,
                "user_email": user_email,
                "user_password": user_password,
                "role_id": 2
            }

    @staticmethod
    def get_all_users():
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT users.user_id, users.first_name, users.last_name, users.user_email, users.user_password, roles.role_name, users.is_banned, users.ban_reason, users.ban_until
            FROM users
            INNER JOIN roles ON roles.role_id = users.role_id
            '''
            cursor.execute(sql)
            users = cursor.fetchall()
            if not users:
                cursor.close()
                return {"Massages":"No users has been added yet"}
            cursor.close()
            return [
                {
                    "user_id":row[0],
                    "first_name":row[1],
                    "last_name":row[2],
                    "user_email":row[3],
                    "user_password":row[4],
                    "role_id":row[5],
                    "is_banned":bool(row[6]) if len(row) > 6 else False,
                    "ban_reason":row[7] if len(row) > 7 else None,
                    "ban_until":row[8] if len(row) > 8 else None
                }
                for row in users
            ]
    

    @staticmethod
    def show_user_by_id(user_id):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_id =?"
            cursor.execute(sql,(user_id ,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Massages":"No users with that ID"}
            cursor.close()
            return {
                    "user_id":user[0],
                    "first_name":user[1],
                    "last_name":user[2],
                    "user_email":user[3],
                    "user_password":user[4],
                    "role_id":user[5],
                    "profile_image":user[6] if len(user) > 6 else None,
                    "is_banned":bool(user[7]) if len(user) > 7 else False,
                    "ban_reason":user[8] if len(user) > 8 else None,
                    "ban_until":user[9] if len(user) > 9 else None
                }
        
    @staticmethod
    def show_user_by_email_and_password(user_email, user_password):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_email =? and user_password =?"
            cursor.execute(sql,(user_email, user_password))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Massages":"No users with that email and password"}
            cursor.close()
            return {
                "user_id":user[0],
                "first_name":user[1],
                "last_name":user[2],
                "user_email":user[3],
                "user_password":user[4],
                "role_id":user[5],
                "profile_image":user[6] if len(user) > 6 else None,
                "is_banned":bool(user[7]) if len(user) > 7 else False,
                "ban_reason":user[8] if len(user) > 8 else None,
                "ban_until":user[9] if len(user) > 9 else None
            }
        
    @staticmethod
    def update_user_by_id(user_id, data):
        try:
            with Users_Model.get_db_connection() as connection:
                cursor = connection.cursor()
                sql = "select * from users where user_id =?"
                cursor.execute(sql,(user_id  ,))
                user = cursor.fetchone()
                if not user:
                    cursor.close()
                    return {"Massages":"No users with that ID"}
                
                # שימוש ב-parameterized queries למניעת SQL injection
                set_clauses = []
                values = []
                for key, value in data.items():
                    set_clauses.append(f"{key} = ?")
                    values.append(value)
                values.append(user_id)
                
                sql = f"UPDATE users SET {', '.join(set_clauses)} WHERE user_id = ?"
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                return {"Message":f"user_id {user_id} has been updated successfully"}
        except Exception as e:
            return {"Error": f"Database error: {str(e)}"}
    
    @staticmethod
    def delete_user_by_id(user_id):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_id =?"
            cursor.execute(sql,(user_id ,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Massages":"No users with that ID"}
            sql = "delete from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            connection.commit()
            cursor.close()
            return {"Message":"User deleted successfully"}

    @staticmethod
    def if_mail_exists(user_email):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select user_email from users where user_email =?"
            cursor.execute(sql,(user_email ,))
            exists = cursor.fetchone()
            cursor.close()
            if not exists:
                return False
            return True
    
    @staticmethod
    def update_profile_image(user_id, profile_image_url):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_id =?"
            cursor.execute(sql,(user_id ,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return None
            
            if profile_image_url is None:
                sql = "update users set profile_image = NULL where user_id = ?"
                cursor.execute(sql,(user_id ,))
            else:
                sql = "update users set profile_image = ? where user_id = ?"
                cursor.execute(sql,(profile_image_url, user_id ,))
            
            connection.commit()
            cursor.close()
            return {"Message": f"Profile image updated successfully for user_id {user_id}"}