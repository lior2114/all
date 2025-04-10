import sqlite3
path_name = './SQL/Mydata.db'
class City:
    def __init__(self, city_id, name):
        self.city_id = city_id
        self.name = name 

    def __str__(self):
        return (f"city_id:{self.city_id}, name:{self.name}" )
    

#סטטיק מטהוד אומר שלא צריך להריץ את כל הקלאסס שוב פעם 
# אלא לגשת לפונקציה מתוך הקלאס בלי להריץ את כולה
    @staticmethod
    def create_table_cities():
        # התחברות למסד הנתונים ויצירת טבלה אם לא קיימת
        connection = sqlite3.connect(path_name)
        print(f"Connected to database {path_name}")
        cursor = connection.cursor()
        # יצירת טבלה בשם cities
        sql = '''create table if not exists cities
                (city_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 name Text not null)
            '''
        cursor.execute(sql)
        cursor.close()
        connection.close() 
        print("Database and table created successfully")

    @staticmethod
    def insert(name):
        # הוספת עיר חדשה לטבלה
        connection = sqlite3.connect(path_name)
        print(f"Connected to database {path_name}")

        cursor = connection.cursor()
        sql = 'insert into cities (name) values(?)'  
        cursor.executemany(sql, name)
        connection.commit()  # שמירת השינויים
        cursor.close()
        connection.close()

    @staticmethod
    def select_by_id(id):
        # שליפת עיר לפי מזהה
        connection = sqlite3.connect(path_name)
        print(f"Connected to database {path_name}")
        cursor = connection.cursor()
        sql = 'select * from cities where city_id = ?'  
        cursor.execute(sql, (id,))
        city = cursor.fetchone()
        print(city)
        cursor.close()
        connection.close()

    @staticmethod
    def delete_by_id( id):
        # מחיקת עיר לפי מזהה
        connection = sqlite3.connect(path_name)
        print(f"Connected to database {path_name}")
        cursor = connection.cursor()
        sql = 'delete from cities where city_id = ?'  
        cursor.execute(sql, (id,))
        connection.commit()  # שמירת השינויים
        cursor.close()
        connection.close()

    @staticmethod
    def update_by_id(id, new_name):
        # עדכון שם של עיר לפי מזהה
        connection = sqlite3.connect(path_name)
        print(f"Connected to database {path_name}")
        cursor = connection.cursor()
        sql = 'update cities set name = ? where city_id = ?'  
        cursor.execute(sql, (new_name, id))
        connection.commit()  # שמירת השינויים
        cursor.close()
        connection.close()
