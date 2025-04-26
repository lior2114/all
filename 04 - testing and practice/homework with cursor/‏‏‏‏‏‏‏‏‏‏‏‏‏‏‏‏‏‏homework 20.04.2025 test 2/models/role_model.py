import sqlite3
import os
 
path_name = "./SQL/MyData.db"
if not os.path.exists("SQL"):
    os.makedirs("SQL")

class Tables_Roles:
    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)

#יצירת שולחן 
    @staticmethod
    def create_table_roles():
        with Tables_Roles.get_db_connection() as connection:
            connection.execute('''
            create table if not exists roles(
            role_id integer primary key autoincrement, 
            role_description text not null)
                                        ''')

#יצירת רול
    @staticmethod
    def create_role(role_description):
        with Tables_Roles.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute ('''
                insert into roles (role_description) values (?)
                    ''', (role_description,))
            connection.commit()
            role_id = cursor.lastrowid
        return{"id":role_id, "role_description":role_description}

#הצגת כולם 
    @staticmethod
    def get_all():
        with Tables_Roles.get_db_connection() as connection:
            show = connection.execute(
                '''
                select * from roles
                ''')
            show = show.fetchall()
            if not show:
                return {"message": "have no roles yet"}
            return [{"role_id":row[0], "role_description":row[1]} for row in show]

#הצגה על ידי איי די
    @staticmethod
    def get_by_id(role_id):
        with Tables_Roles.get_db_connection() as connection:
            show = connection.execute(
                '''
                select * from roles where role_id = ?
                ''', (role_id,))
            show = show.fetchone()
            if show is None:
                return {"message": f"No roles found with that ID: {role_id}"}
            return {"role_id": show[0], "role_description": show[1]}

#עדכון רול   
    @staticmethod
    def updating(new_description, role_id):
        with Tables_Roles.get_db_connection() as connection:
            connection.execute(
            '''
            update roles
            set role_description = ? where role_id = ?
            ''', (new_description, role_id))
            connection.commit()
            if role_id is None:
                return {"message": "id not found, please insert correct id"}
            return {"message": f"Role with ID {role_id} Updated successfully"}

#מחיקה  
    @staticmethod
    def deleting(role_id):
        with Tables_Roles.get_db_connection() as connection:
            connection.execute(
            '''
            delete from roles
            where role_id = ?
            ''', (role_id,))
            connection.commit()
            if not role_id:
                return {"massage":"id not found please insert correct id"}
            return {"message": f"Role with ID {role_id} Deleted successfully"}       