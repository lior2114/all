import sqlite3
import os 

path_name = "./SQL/MyData.db"
if not os.path.exists ("./SQL"):
    os.makedirs("./SQL")

class UserModel:
    @staticmethod
    def get_db_connection():
        return sqlite3.connect(path_name)
    
    @staticmethod
    def create_user_table():
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                create table if not exists users
                (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                role_id  INTEGER NOT NULL,
                Salary REAL NOT NULL,
                is_admin INTEGER DEFAULT 0, 
                FOREIGN KEY (role_id) REFERENCES Roles(role_id)
                )
                ''' #REAL = FLOAT
            
            cursor.execute(sql)
            cursor.close()


    @staticmethod
    def create(first_name, last_name, email, password, role_id,salary, is_admin =0):
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                INSERT INTO users(first_name, last_name, email, password, role_id, salary, is_admin) VALUES (?,?,?,?,?,?,?)
                '''
            cursor.execute(sql,(first_name, last_name, email, password, role_id, salary, is_admin,))
            connection.commit()
            user_id = cursor.lastrowid
            cursor.close()
            return {
                'user_id': user_id,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'role_id': role_id,
                'salary': salary,
                'is_admin': is_admin
            }


    @staticmethod
    def show_all():
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                SELECT * FROM users
                '''
            cursor.execute(sql)
            users = cursor.fetchall()
            cursor.close()
            return [
                {
                    'user_id': user[0],
                    'first_name': user[1],
                    'last_name': user[2],
                    'email': user[3],
                    'password': user[4],
                    'role_id': user[5],
                    'salary': user[6],
                    'is_admin': user[7]
                }
                for user in users
            ]
        
    @staticmethod
    def get_user(user_id):
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT * FROM users WHERE user_id = ?'''
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            if user: #אם יש את האיי די הזה
                return {
                    'user_id': user[0],
                    'first_name': user[1],
                    'last_name': user[2],
                    'email': user[3],
                    'password': user[4],
                    'role_id': user[5],
                    'salary': user[6],
                    'is_admin': user[7]
                }
        return None # אם אין את האיי די הזה 
    
#אופציה א
    @staticmethod
    def update_A(user_id, **kwargs):
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT * FROM users WHERE user_id = ?'''
            cursor.execute(sql, (user_id,))
            if not cursor.fetchone(): # אם לא קיים 
                cursor.close()
                return None
            update_filds = [] #אם קיים 
            values = []
            for key, value in kwargs.items(): #kwargs.items() = {"first_name":"dd": "password":"123456"}
                update_filds.append(f"{key} = ? ") #[first_name , password]
                values.append(value) #["david","123456"]
            if not update_filds:
                cursor.close()
                return None
            sql = f"UPDATE users set {','.join(update_filds)} where user_id = ? "
            values.append(user_id)
            cursor.execute(sql, values)
            connection.commit()
            cursor.close()
            return {"message":f"user{user_id} update successfully"}

#אופציה ב
    @staticmethod
    def update_B(user_id, data):
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT * FROM users WHERE user_id = ?'''
            cursor.execute(sql, (user_id,))
            if not cursor.fetchone(): # אם לא קיים 
                cursor.close()
                return None
            pair = "" #אם קיים 
            for key, value in data.items(): #kwargs.items() = {"first_name":"dd": "password":"123456"}
                pair += key +"=" +"'" + value +"'" + ","
            pair = pair[:-1] # הורדת הפסיק האחרון 
            print(pair)
            sql = f"update users set {pair} where user_id = ?"
            print(sql)
            cursor.execute(sql,(user_id ,))
            connection.commit()
            cursor.close()
            return {"message":f"user {user_id} updates successfully"}
        

    @staticmethod
    def delete(user_id):
        with UserModel.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''SELECT * FROM users WHERE user_id = ?'''
            cursor.execute(sql, (user_id,))
            if not cursor.fetchone(): # אם לא קיים 
                cursor.close()
                return None
            sql = "delete from users where user_id = ?"
            cursor.execute(sql,(user_id,))
            connection.commit()
            cursor.close()
            return {"message": f"user {user_id} has deleted"}