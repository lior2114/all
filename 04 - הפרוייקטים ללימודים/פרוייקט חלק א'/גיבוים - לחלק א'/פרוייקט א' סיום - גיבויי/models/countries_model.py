import sqlite3
import os
path_name = "./SQL/Mydb.db"
if not os.path.exists("./SQL"):
    os.makedirs("./SQL")

class Country_Model:

    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)
    
    @staticmethod
    def create_table():
        with Country_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''create table if not exists countries (
                country_id integer primary key autoincrement,
                country_name text not null
                )'''
            cursor.execute(sql)
            connection.commit()
            cursor.close()

    @staticmethod
    def create_country(country_name):
        with Country_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "insert into countries (country_name) values (?)"
            cursor.execute(sql,(country_name ,))
            connection.commit()
            country_id = cursor.lastrowid
            cursor.close()
            return [
                {
                    "country_id":country_id,
                    "country_name": country_name
                }
            ]

    @staticmethod
    def get_all_countries():
        with Country_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from countries"
            cursor.execute(sql)
            countries = cursor.fetchall()
            if not countries:
                cursor.close()
                return {"Massages":"No Countries has been added yet"}
            cursor.close()
            return [
                {
                    "country_id":row[0],
                    "country_name":row[1]
                }
                for row in countries
            ]
    

    @staticmethod
    def show_country_by_id(country_id):
        with Country_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from countries where country_id =?"
            cursor.execute(sql,(country_id ,))
            country = cursor.fetchone()
            if not country:
                cursor.close()
                return {"Massages":"No Countries with that ID"}
            cursor.close()
            return [
                {
                    "country_id":country[0],
                    "country_name":country[1]
                }
            ]
        
    @staticmethod
    def update_country(country_id, country_name):
        with Country_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from countries where country_id =?"
            cursor.execute(sql,(country_id ,))
            country = cursor.fetchone()
            if not country:
                cursor.close()
                return {"Massages":"No Countries with that ID"}
            sql = '''update countries 
                    set country_name = ? where country_id = ?''' 
            cursor.execute(sql,(country_name, country_id ,))
            connection.commit()
            cursor.close()
            return {"Message":f"country_id {country_id} has been updated to the name: ({country_name}) successfully"}
    
    @staticmethod
    def delete_country_by_id(country_id):
        with Country_Model.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = "select * from countries where country_id =?"
            cursor.execute(sql,(country_id ,))
            country = cursor.fetchone()
            if not country:
                cursor.close()
                return {"Massages":"No Countries with that ID"}
            sql = "delete from countries where country_id = ?"
            cursor.execute(sql, (country_id ,))
            connection.commit()
            cursor.close()
            return {"Message":"Country has been deleted successfully"}


