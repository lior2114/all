import sqlite3
import os

path_name = "./SQL/MyData.db"
if not os.path.exists ("./SQL"):
    os.makedirs("./SQL")


class WorkersModel:
    
    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)

    @staticmethod
    def create_table_workers():
        with WorkersModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                create table if not exists workers
                (
                    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    Salary REAL NOT NULL,
                    role_id  INTEGER NOT NULL,
                    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
                    )
                    '''#REAL = Float
            cursor.execute(sql)
            cursor.close()

    @staticmethod
    def create_worker(first_name,last_name,salary, role_id):
        with WorkersModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "insert into workers (first_name,last_name,salary, role_id) values (?,?,?,?)"
            cursor.execute(sql,(first_name,last_name,salary, role_id,))
            connection.commit()
            worker_id = cursor.lastrowid
            return {
                "worker_id":worker_id,
                "first_name": first_name,
                "last_name": last_name,
                "salary": salary,
                "role_id": role_id
            }
        
    @staticmethod
    def get_all():
        with WorkersModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from workers"
            cursor.execute(sql)
            show = cursor.fetchall()
            if not show:
                return {"Error":"no workers has been added yet"}
            cursor.close()
            return [
                {
                    "worker_id": worker[0],
                    "first_name": worker[1],
                    "last_name":worker[2],
                    "salary":worker[3],
                    "role_id":worker[4]
                }
                for worker in show
            ]
        
    @staticmethod 
    def get_by_id(worker_id):
        with WorkersModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from workers where worker_id = ?"
            cursor.execute(sql,(worker_id ,))
            worker = cursor.fetchone()
            if not worker:
                cursor.close()
                return {"Error":"no workers with that ID"}
            cursor.close()
            return {
                    "worker_id": worker[0],
                    "first_name": worker[1],
                    "last_name":worker[2],
                    "salary":worker[3],
                    "role_id":worker[4]
                }

    @staticmethod
    def update_worker_details(worker_id, data):
        with WorkersModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from workers where worker_id = ?"
            cursor.execute(sql,(worker_id ,))
            show_by_id = cursor.fetchone()
            if not show_by_id :
                cursor.close()
                return {"Error":"no workers with that ID"}
            
            pair = ""
            for key,value in data.items():
                pair += key +"="+ "'"+ value + "'" + ","
            pair = pair [:-1] # הורדת הפסיק בשורה האחרונה שלא יהיה בעיה 
            sql = f'''
                update workers
                set {pair} where worker_id = ?
                '''
            cursor.execute(sql,(worker_id,))
            connection.commit()
            cursor.close()
            return {"message":f"info of worker: {worker_id} update successfully"}
        
    @staticmethod
    def delete_worker_by_id(worker_id):
        with WorkersModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from workers where worker_id = ?"
            cursor.execute(sql,(worker_id ,))
            show_by_id = cursor.fetchone()
            if not show_by_id:
                cursor.close()
                return False
            sql = "delete from workers where worker_id = ?"
            cursor.execute(sql,(worker_id,))
            connection.commit()
            return True

