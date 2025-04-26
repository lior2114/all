import sqlite3
path_name = "./SQL/mydata.db"

# def create_table_persons():
#     connection = sqlite3.connect(path_name)
#     print("connected to sqlite")
#     cursor = connection.cursor()

#     sql = '''create table if not exists Persons(
#             	"person_id"	INTEGER NOT NULL UNIQUE,
#                 "Fname"	TEXT NOT NULL,
#                 "Lname"	TEXT NOT NULL,
#                 "city_id"	INTEGER NOT NULL,
#                 PRIMARY KEY("person_id" AUTOINCREMENT),
#                 FOREIGN KEY (city_id) REFERENCES cities(city_id)
#                 )
#                 '''
#     cursor.execute(sql)
#     cursor.close()
#     connection.close()
# create_table_persons()

# def add_Persons(persons_list):
#     connection = sqlite3.connect(path_name)
#     print("connected to sqlite")
#     cursor = connection.cursor()

#     sql = '''
#             insert into Persons (Fname, Lname, city_id) values (?, ?, ?)
#         '''
#     cursor.executemany(sql, persons_list)
#     connection.commit()
#     cursor.close()
#     connection.close()
# lis_Persons = [
#     ('w1', 'w1', 3),
#     ('y2', 'y2', 2),
#     ('r3', 'r3', 1),
# ]
# add_Persons(lis_Persons)

# def represent_cities_names():
#     connection = sqlite3.connect(path_name)
#     print("connected to sqlite")
#     cursor = connection.cursor()
#     sql = '''
#             select Fname,Lname, name from Persons 
#             inner join cities on Persons.city_id = cities.city_id
#         '''
#     cursor.execute(sql)
#     show = cursor.fetchall()
#     print(show)
#     cursor.close()
#     connection.close()

# represent_cities_names()