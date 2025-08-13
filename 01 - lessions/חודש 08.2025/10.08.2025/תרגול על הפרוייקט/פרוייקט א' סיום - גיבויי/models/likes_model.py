import sqlite3
import os
path_name = "./SQL/Mydb.db"
if not os.path.exists("./SQL"):
    os.makedirs("./SQL")

class Likes_Model:

    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)
    
    @staticmethod
    def create_table():
        try:
            with Likes_Model.get_db_connection() as connection:
                cursor = connection.cursor()
                
                # בדיקה שהטבלאות users ו-vacations קיימות
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
                users_exists = cursor.fetchone()
                
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='vacations'")
                vacations_exists = cursor.fetchone()
                
                if not users_exists:
                    print("Warning: users table does not exist")
                if not vacations_exists:
                    print("Warning: vacations table does not exist")
                
                sql = '''create table if not exists likes (
                    user_id integer not null,
                    vacation_id integer not null,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (vacation_id) REFERENCES vacations(vacation_id)
                    )'''
                cursor.execute(sql)
                connection.commit()
                cursor.close()
                print("Likes table created successfully")
        except Exception as e:
            print(f"Error creating likes table: {str(e)}")
            raise e

    @staticmethod
    def add_like_to_vacation(user_id, vacation_id):
        try:
            with Likes_Model.get_db_connection() as connection:
                cursor = connection.cursor()
                
                print(f"Adding like - user_id: {user_id}, vacation_id: {vacation_id}")
                
                # בדיקה אם הלייק כבר קיים
                check_sql = "SELECT * FROM likes WHERE user_id = ? AND vacation_id = ?"
                cursor.execute(check_sql, (user_id, vacation_id))
                existing_like = cursor.fetchone()
                
                if existing_like:
                    cursor.close()
                    print("Like already exists")
                    return {"Error": "User has already liked this vacation"}
                
                sql = "INSERT INTO likes (user_id, vacation_id) VALUES (?, ?)"
                cursor.execute(sql, (user_id, vacation_id))
                connection.commit()
                cursor.close()
                print("Like added successfully")
                return {"Message":f"user_id {user_id} has been liked vacation_id {vacation_id} successfully"}
        except Exception as e:
            print(f"Add like error in model: {str(e)}")
            raise e

    @staticmethod
    def unlike_vacation(user_id, vacation_id):
        try:
            with Likes_Model.get_db_connection() as connection:
                cursor = connection.cursor()
                
                print(f"Removing like - user_id: {user_id}, vacation_id: {vacation_id}")
                
                # בדיקה אם הלייק קיים
                check_sql = "SELECT * FROM likes WHERE user_id = ? AND vacation_id = ?"
                cursor.execute(check_sql, (user_id, vacation_id))
                existing_like = cursor.fetchone()
                
                if not existing_like:
                    cursor.close()
                    print("Like does not exist")
                    return {"Error": "User has not liked this vacation"}
                
                sql = "DELETE FROM likes WHERE user_id = ? AND vacation_id = ?"
                cursor.execute(sql, (user_id, vacation_id))
                connection.commit()
                cursor.close()
                print("Like removed successfully")
                return {"Message":f"user_id {user_id} has been unliked vacation_id {vacation_id} successfully"}
        except Exception as e:
            print(f"Remove like error in model: {str(e)}")
            raise e
        
    @staticmethod
    def show_likes():
        with Likes_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT users.user_id, vacations.vacation_id 
                     FROM likes
                     INNER JOIN users ON likes.user_id = users.user_id
                     INNER JOIN vacations ON likes.vacation_id = vacations.vacation_id'''
            cursor.execute(sql)
            results = cursor.fetchall()
            if not results:
                return {"Message":"no user_id or not vacation_id or data is empty"}
            cursor.close()
            return results