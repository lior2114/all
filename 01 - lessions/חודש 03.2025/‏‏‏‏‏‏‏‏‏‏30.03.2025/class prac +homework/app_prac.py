import sqlite3
import random
path_name = './SQL_Prac/mydb_v2.db'

# # יצירת טבלה של וורקרס אם לא קיימת אז יוצר 
# def create_workers_table():
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()
#     sql = ''' 
#     CREATE TABLE IF NOT EXISTS workers (
#         "workers_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         "first_name"	TEXT NOT NULL,
#         "last_name"	TEXT NOT NULL,
#         "salary"	INTEGER NOT NULL,
#         "city_id"	INTEGER NOT NULL,
#         FOREIGN KEY (city_id) REFERENCES city(id)
#     )
#     '''
#     cursor.execute(sql)
#     cursor.close()
#     connection.close()
# create_workers_table()

# # מוסיף עובד/עובדים
# def add_worker(first_name,last_name, salary,city_id):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()
#     sql = '''
#         insert into workers (first_name, last_name, salary, city_id) values (?,?,?,?)
#             '''
#     cursor.execute(sql, (first_name, last_name, salary, city_id))
#     connection.commit() #save
#     cursor.close()
#     connection.close()
# for i in range(4):
#     n = random.randint(1000,10000)
#     add_worker(f'W{i+1}',f'y{i+1}',n,i+1)

# # מוחק אנשים לפי ה id
# def delete_worker_by_id(worker_id):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()

#     sql = '''
#             DELETE FROM workers
#             WHERE workers_id = ?
#           '''
#     cursor.execute(sql, (worker_id,))
#     connection.commit()  # Save changes
#     print(f"Worker with id {worker_id} has been deleted.")
#     cursor.close()
#     connection.close()
# delete_worker_by_id(2)

# # מראה את האנשים שמשכרותם גדולה מ - 
# def salary_show_up_from(salary):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()
#     sql = '''
#             select * from workers
#             where salary > ?
#             '''
#     cursor.execute(sql, (salary,))
#     salary_up = cursor.fetchall()
#     for i in salary_up:
#         print(i)
#     cursor.close()
#     connection.close()
# salary_show_up_from(2000)

# # מראה את האנשים שמשכרותם נמוכה מ - 
# def salary_show_low_from(salary):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()
#     sql = '''
#             select * from workers 
#             where salary < ?
#         '''
#     cursor.execute(sql, (salary))
#     salary_down = cursor.fetchall()
#     for i in salary_down:
#         print(i)
#     cursor.close()
#     connection.close()

# #מציג את האנשים שהמשכורת שלהם בין לבין 
# def between(min,max):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()
#     sql = '''
#             select * from workers 
#             where salary > ? or salary < ?
#         '''
#     cursor.execute(sql,(min,max))
#     minmax = cursor.fetchall()
#     for i in minmax:
#         print(i)
#     cursor.close()
#     connection.close()
# between(10,3000)

## פונקציה שמציגה כמה אנשים יש בטבלה 
# def counter_people():
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()
#     sql = '''
#             SELECT COUNT(*) FROM workers
#           '''
#     cursor.execute(sql)
#     count = cursor.fetchone()[0]
#     print(f"Total number of people: {count}")
#     cursor.close()
#     connection.close()
# counter_people()

# # פונקציה שרושמת את המידע לפי השם שבחרנו 
# def get_info_by_name(name):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()

#     sql = '''
#             select * from workers 
#             where first_name = ?
#             '''
#     cursor.execute(sql, (name ,))
#     na = cursor.fetchone()
#     print(na)
#     cursor.close()
#     connection.close()
# get_info_by_name('W1')

# # מצליב בין הטבלאות ורושם את המידע של העובד לפי האיי די שלו כולל מיקום העובד לפי הטבלה השניה של הסיטיס 
# def cross_cities_and_workes_by_id(id):
#     connection = sqlite3.connect(path_name)
#     print("connected to database")
#     cursor = connection.cursor()


#     sql = '''select first_name, last_name, salary, name
#     from workers
#     inner join cities on workers.city_id = cities.city_id
#     where workers.workers_id = ? 
#     '''  
#     cursor.execute(sql, (id ,))
#     by_id = cursor.fetchone()
#     print(by_id)
#     cursor.close()
#     connection.close()
# cross_cities_and_workes_by_id(2)