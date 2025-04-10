import sqlite3
class Workers:
    path_name ='./SQL/Mydata.db'
    def __init__(self, worker_id,Fname, Lname, Age,city_id):
        self.worker_id = worker_id
        self.Fname = Fname
        self.Lname = Lname
        self.Age = Age
        self.city_id = city_id

    def __str__(self):
        return f"Worker_id: {self.worker_id}, Worker: {self.Fname} {self.Lname}, Age: {self.Age}, City ID: {self.city_id}"
    
    #סטטיק מטהוד אומר שלא צריך להריץ את כל הקלאסס שוב פעם 
    # אלא לגשת לפונקציה מתוך הקלאס בלי להריץ את כולה

    @staticmethod
    def create_table_workers():
        connection = sqlite3.connect(Workers.path_name)
        print(f"connected to database {Workers.path_name}")
        cursor = connection.cursor()
        sql = '''
            create table if not exists Workers(
            	"worker_id"	INTEGER NOT NULL,
                "Fname"	TEXT NOT NULL,
                "Lname"	TEXT NOT NULL,
                "Age"	INTEGER NOT NULL,
                "City_id"	INTEGER NOT NULL,
                PRIMARY KEY("worker_id" AUTOINCREMENT)
                FOREIGN KEY(City_id) REFERENCES cities(city_id)
            )
            '''
        cursor.execute(sql)
        cursor.close()
        connection.close()    
    

    def insert_to_table(self):
        connection = sqlite3.connect(Workers.path_name)
        print(f"connected to database {Workers.path_name}")
        cursor = connection.cursor()
        sql = '''
            insert into Workers (Fname, Lname, Age,city_id) values (?,?,?,?)
                '''
        cursor.executemany(sql,self)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def select_id(id):
        connection = sqlite3.connect(Workers.path_name)
        print(f"connected to database {Workers.path_name}")
        cursor = connection.cursor()  
        sql = '''
              select * from Workers where worker_id = ?  
        
            ''' 
        cursor.execute(sql, (id,))
        by_id = cursor.fetchone()
        print(by_id)
        cursor.close()
        connection.close()
    
    @staticmethod
    def delete_by_id (id):
        connection = sqlite3.connect(Workers.path_name)
        print(f"connected to database {Workers.path_name}")
        cursor = connection.cursor()  
        sql = '''
            delete from Workers where worker_id = ?
            '''
        cursor.execute(sql, (id,))
        connection.commit()
        cursor.close()
        connection.close()  

    @staticmethod
    def update_by_id(fname,id):
        connection = sqlite3.connect(Workers.path_name)
        print(f"connected to database {Workers.path_name}")
        cursor = connection.cursor()  
        sql = '''
            update Workers 
            set Fname  = ?
            where workers_id = ?
            '''
        cursor.executemany(sql, (fname ,id,))
        connection.commit()
        cursor.close()
        connection.close()  

    @staticmethod
    def show_cities_over_id_on_workers():
        connection = sqlite3.connect(Workers.path_name)
        print(f"connected to database {Workers.path_name}")
        cursor = connection.cursor()  
        sql = '''
            select Fname, Lname, Age, name from Workers
            inner join cities on Workers.City_id = cities.city_id
            '''
        cursor.execute(sql)
        show = cursor.fetchall()
        for row in show:
            print(row)
        cursor.close()
        connection.close()
