import sqlite3
path_name = './SQL/Mydata.db'

class Workers:
#יצירת שולחן 
    @staticmethod
    def create_workers_table():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            CREATE TABLE IF NOT EXISTS workers (
                "workers_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "first_name"	TEXT NOT NULL,
                "last_name"	TEXT NOT NULL,
                "salary"	INTEGER NOT NULL,
                "city_id"	INTEGER NOT NULL,
                FOREIGN KEY (city_id) REFERENCES cities(city_id)
            )
            '''
        cursor.execute(sql)
        cursor.close()
        connection.close()

#הכנסת עובדים לטבלה
    @staticmethod
    def insert_workers_lis(workers_lis):
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            insert into workers (first_name,last_name,salary,city_id) values (?,?,?,?)
            '''
        cursor.executemany(sql,workers_lis)
        connection.commit()
        cursor.close()
        connection.close()

# מראה את השם של הערים לפי הטבלה של ה cities
    @staticmethod
    def show_cities_names_on_workers():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            select first_name, last_name, salary, name from workers
            inner join cities on workers.city_id = cities.city_id
            '''
        cursor.execute(sql)
        show = cursor.fetchall()
        print(show)
        cursor.close()
        connection.close()


# # Workers.create_workers_table()

#  #אופציה א 
# lis = [
#     ('q1','w1',40000,1),
#     ('q2','w2',30000,2),
#     ('q3','w3',20000,3)
# ]
# Workers.insert_workers_lis(lis)

# אופציה ב 
#ואם עושים פוננקציה עם כל משתנה בנפרד אז צריך לפצל את הליסט ככה 
# for worker in lis:
#     Workers.insert_workers_lis(worker[0], worker[1], worker[2], worker[3])

# Workers.show_cities_names_on_workers()