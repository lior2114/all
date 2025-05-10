import sqlite3
import os
path_name = "./SQL/Mydb.db"
if not os.path.exists("./SQL"):
    os.makedirs("./SQL")

class Vacations_Model:

    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)
    
    @staticmethod
    def create_table():
        with Vacations_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''create table if not exists vacations (
                vacation_id integer primary key autoincrement,
                country_id integer not null,
                vacation_description text not null,
                vacation_start date not null,
                vacation_ends date not null,
                vacation_price float not null,
                vacation_file_name text not null,
                FOREIGN KEY (country_id) REFERENCES countries(country_id)
                )'''
            cursor.execute(sql)
            connection.commit()
            cursor.close()

    @staticmethod
    def create_vacations(country_id, vacation_description, vacation_start, vacation_ends, vacation_price, vacation_file_name):
        with Vacations_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "insert into vacations (country_id, vacation_description, vacation_start, vacation_ends, vacation_price, vacation_file_name) values (?, ?, ?, ?, ?, ?)"
            cursor.execute(sql,(country_id, vacation_description, vacation_start, vacation_ends, vacation_price, vacation_file_name))
            connection.commit()
            vacation_id = cursor.lastrowid
            cursor.close()
            return {
                "vacation_id":vacation_id,
                "country_id": country_id,
                "vacation_description": vacation_description,
                "vacation_start": vacation_start,
                "vacation_ends": vacation_ends,
                "vacation_price": vacation_price,
                "vacation_file_name": vacation_file_name
            }

    @staticmethod
    def get_all():
        with Vacations_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from vacations"
            cursor.execute(sql)
            vacations = cursor.fetchall()
            if not vacations:
                cursor.close()
                return {"Massages":"No vacations has been added yet"}
            cursor.close()
            return [
                {
                    "vacation_id":row[0],
                    "country_id":row[1],
                    "vacation_description":row[2],
                    "vacation_start":row[3],
                    "vacation_ends":row[4],
                    "vacation_price":row[5],
                    "vacation_file_name":row[6]
                }
                for row in vacations
            ]
    

    @staticmethod
    def show_vacation_by_id(vacation_id):
        with Vacations_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from vacations where vacation_id =?"
            cursor.execute(sql,(vacation_id ,))
            vacation = cursor.fetchone()
            if not vacation:
                cursor.close()
                return {"Massages":"No vacations with that ID"}
            cursor.close()
            return {
                    "vacation_id":vacation[0],
                    "country_id":vacation[1],
                    "vacation_description":vacation[2],
                    "vacation_start":vacation[3],
                    "vacation_ends":vacation[4],
                    "vacation_price":vacation[5],
                    "vacation_file_name":vacation[6]
                }
        
    @staticmethod
    def update_vacation(vacation_id, data):
        with Vacations_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from vacations where vacation_id =?"
            cursor.execute(sql,(vacation_id  ,))
            vacation = cursor.fetchone()
            if not vacation:
                cursor.close()
                return {"Massages":"No vacations with that ID"}
            
            pair = ""
            for key,value in data.items():
                pair += key + "=" + "'" + value + "'" + ","
            pair = pair[:-1]
            sql = f'''update vacations 
                    set {pair} where vacation_id = ?'''
            
            cursor.execute(sql,(vacation_id ,))
            connection.commit()
            cursor.close()
            return {"Message":f"vacation_id {vacation_id} has been updated successfully"}
    
    @staticmethod
    def delete_vacation_by_id(vacation_id):
        with Vacations_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from vacations where vacation_id =?"
            cursor.execute(sql,(vacation_id ,))
            vacation = cursor.fetchone()
            if not vacation:
                cursor.close()
                return {"Massages":"No vacations with that ID"}
            sql = "delete from vacations where vacation_id = ?"
            cursor.execute(sql,(vacation_id,))
            connection.commit()
            cursor.close()
            return {"Message":f"vacation_id {vacation_id} has been deleted successfully"}
