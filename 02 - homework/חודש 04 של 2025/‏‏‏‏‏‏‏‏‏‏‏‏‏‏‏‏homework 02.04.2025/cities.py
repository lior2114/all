import sqlite3
path_name = './SQL/Mydata.db'

class Cities: 
#יצירת שולחן 
    @staticmethod
    def create_city_table():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()
        sql = '''
                 CREATE TABLE IF NOT EXISTS cities (
                     "city_id"	INTEGER NOT NULL,
                     "name"	TEXT NOT NULL UNIQUE,
                     PRIMARY KEY("city_id" AUTOINCREMENT)
                 )

                '''
        cursor.execute(sql)
        cursor.close()
        connection.close()

#מכניס רשימת ערים 
    @staticmethod
    def insert_cities(name):
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()         
        sql = '''
            insert into cities (name) values (?)
                '''   
        cursor.executemany(sql, name)
        connection.commit()
        cursor.close()
        connection.close()

#מחפש שמות של ערים לפי ה id שלהם 
    @staticmethod
    def search_for_city_by_id(id):
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()     
        sql = '''
            select name from cities where city_id = ?
                '''
        cursor.execute(sql, (id,))
        show = cursor.fetchone()
        cursor.close()
        connection.close()
        return show



# Cities.create_city_table()

# lis = [
#     ('Tel-Aviv',),
#     ('Ranana',),
#     ('Tel-Mond',)

# ]

# Cities.insert_cities(lis)

# Cities.search_for_city_by_id(2)


