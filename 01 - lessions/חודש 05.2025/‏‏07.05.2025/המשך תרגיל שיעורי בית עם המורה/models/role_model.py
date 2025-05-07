import sqlite3
import os

path_name = "./SQL/MyData.db"
if not os.path.exists ("./SQL"):
    os.makedirs("./SQL")


class Role_functions:
    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)
    
    @staticmethod
    def create_role_table():
        with Role_functions.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        create table if not exists Roles
                           (
                            role_id integer primary key autoincrement, 
                            role_description text not null
                           )
                           ''')
            cursor.close()

    @staticmethod
    def add_role_to_table(role_description):
        with Role_functions.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into Roles (role_description) values (?)", (role_description,))
            connection.commit()
            role_id = cursor.lastrowid
            cursor.close
            return {"message": f"role_id {role_id}, role_description '{role_description}' has been added successfully."}

    @staticmethod
    def show_all_roles_in_table():
       with Role_functions.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("select * from Roles")
            show_all = cursor.fetchall()
            if not show_all:
                return {"massage":"no roles has been added yet"}
            cursor.close()
            return [{"role_id": role[0],"role_description": role[1]} for role in show_all]


    @staticmethod      
    def get_role_by_id(role_id):
       with Role_functions.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("select * from Roles where role_id = ?", (role_id,))
            show = cursor.fetchone()
            if not show:
                return {"massage":"role_id has not been found"}
            cursor.close()
            return {"role_id":show[0], "role_description": show[1]} #בוחר רק את מה שמופיע ומופיע רק את מה שתואם לרול איי די אז לא יהיה משהוא אחר להציג חוץ מזה בגלל זה לא צריך את הלולאה
            
    @staticmethod
    def update_role_by_id(role_description,role_id):
        with Role_functions.get_db_connection() as connection:
            cursor = connection.cursor()   
            cursor.execute("update Roles set role_description = ? where role_id = ?",(role_description,role_id,))
            if not Role_functions.get_role_by_id(role_id):
                return {"error":"role_id has not been found"}
            connection.commit()
            cursor.close()
            return {"massage":f"role id {role_id} has been update to {role_description}"}
        
    @staticmethod
    def delete_role_by_id(role_id):
        with Role_functions.get_db_connection() as connection:
            cursor = connection.cursor()       
            cursor.execute("delete from Roles where role_id = ?", (role_id,))    
            connection.commit()
            if not Role_functions.get_role_by_id(role_id):
                return {"error":"role_id has not been found"}
            cursor.close()
            return {"massage":f"role id {role_id} has been deleted"}
    






