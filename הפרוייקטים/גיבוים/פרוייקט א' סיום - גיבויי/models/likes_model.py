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
        with Likes_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''create table if not exists likes (
                user_id integer not null,
                vacation_id integer not null,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (vacation_id) REFERENCES vacations(vacation_id)
                )'''
            cursor.execute(sql)
            connection.commit()
            cursor.close()

    @staticmethod
    def add_like_to_vacation(user_id, vacation_id):
        with Likes_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO likes (user_id, vacation_id) VALUES (?, ?)"
            cursor.execute(sql, (user_id, vacation_id))
            connection.commit()
            cursor.close()
            return {"Message":f"user_id {user_id} has been liked vacation_id {vacation_id} successfully"}

    @staticmethod
    def unlike_vacation(user_id, vacation_id):
        with Likes_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "DELETE FROM likes WHERE user_id = ? AND vacation_id = ?"
            cursor.execute(sql, (user_id, vacation_id))
            connection.commit()
            cursor.close()
            return {"Message":f"user_id {user_id} has been unliked vacation_id {vacation_id} successfully"}
        
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