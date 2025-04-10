import sqlite3
path_name = './SQL/Mydata.db'

class Projects: 
#יצירת שולחן 
    @staticmethod
    def create_project_table():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()
        sql = '''
                 CREATE TABLE IF NOT EXISTS projects (
                     "ptoject_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     "project_name"	TEXT NOT NULL UNIQUE,
                     "budget"	INTEGER NOT NULL,
                     FOREIGN KEY (ptoject_id) REFERENCES workers(workers_id)
                 )

                '''
        cursor.execute(sql)
        cursor.close()
        connection.close()

#הוספת פרוייקטים 
    @staticmethod
    def insert_projects(from_list):
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()         
        sql = '''
            insert into projects (project_name,budget) values (?,?)
                '''   
        cursor.executemany(sql, from_list)
        connection.commit()
        cursor.close()
        connection.close()

#מראה את הפרוייקט שעליו עובד העובד לפי האיי די 
    @staticmethod
    def show_workers_names_and_projects_by_id(id):
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            select workers.first_name, workers.last_name, workers.salary, projects.project_name from workers
            inner join projects on projects.ptoject_id = workers.workers_id
            where workers.workers_id = ?
            '''
        cursor.execute(sql,(id,))
        show = cursor.fetchall()
        cursor.close()
        connection.close()
        return show


# כל הפרוייקטים מעל 10000 שקל
    @staticmethod
    def projects_over_10000():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            select * from projects 
            where budget > 10000
            '''
        cursor.execute(sql)
        show = cursor.fetchall()
        print(show)
        cursor.close()
        connection.close()


# מוחקת את כל הפרוייטים שמופיעים בסכום שמזינים
    @staticmethod
    def delete_projects_by_budget(budget):
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            delete from projects
            where budget = ?
            '''
        cursor.execute(sql, (budget,))
        connection.commit()
        cursor.close()
        connection.close()

#מראה את הפרטים של האנשים ועל מה שהם עובדים 
    @staticmethod
    def show_workers_names_and_projects():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            select workers.first_name, workers.last_name,projects.project_name from workers
            inner join projects on projects.ptoject_id = workers.workers_id
            '''
        cursor.execute(sql)
        show = cursor.fetchall()
        cursor.close()
        connection.close()
        return show

    @staticmethod
    def return_count_of_projects():
        connection = sqlite3.connect(path_name)
        print("log in database")
        cursor = connection.cursor()   
        sql = ''' 
            select count(*) from projects
            '''
        cursor.execute(sql)
        show = cursor.fetchall()
        cursor.close()
        connection.close()
        return show

#א
# Projects.create_project_table()


# ב
# lis = [
#     ('Tel-Aviv-towers',50000),
#     ('Ranana-towers',40000),
#     ('Tel-Mond-towers',30000)

# ]
# Projects.insert_projects(lis)

#ג
# Projects.show_workers_names_and_projects_by_id(1)
#ד
# Projects.projects_over_10000()

#v
# Projects.delete_projects_by_budget(20)

#u
# Projects.show_workers_names_and_projects()