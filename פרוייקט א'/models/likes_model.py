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