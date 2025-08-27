import sqlite3
import os
path_name = "./SQL/Mydb.db"
if not os.path.exists("./SQL"):
    os.makedirs("./SQL")

class Users_Model:

    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)
    
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
                FOREIGN KEY (role_id) REFERENCES roles(role_id)
                )'''
            cursor.execute(sql)
            connection.commit()
            cursor.close()

    @staticmethod
    def create_user(first_name, last_name, user_email, user_password):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "insert into users (first_name, last_name, user_email, user_password) values (?, ?, ?, ?)"
            cursor.execute(sql,(first_name, last_name, user_email, user_password))
            connection.commit()
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
            sql = '''SELECT users.user_id, users.first_name, users.last_name, users.user_email, users.user_password, roles.role_name
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
                    "role_id":row[5]
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
                    "role_id":user[5]
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
                "role_id":user[5]
            }
        
    @staticmethod
    def update_user_by_id(user_id, data):
        with Users_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from users where user_id =?"
            cursor.execute(sql,(user_id  ,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return {"Massages":"No users with that ID"}
            
            pair = ""
            for key,value in data.items():
                pair += key + "=" + "'" + value + "'" + ","
            pair = pair [:-1]
            sql = f'''update users 
                    set {pair} where user_id = ?'''
            cursor.execute(sql,(user_id ,))
            connection.commit()
            cursor.close()
            return {"Message":f"user_id {user_id} has been updated successfully"}
    
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
                return True
            return False