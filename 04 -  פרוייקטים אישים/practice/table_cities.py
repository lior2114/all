import sqlite3
import os
path_name = "./SQL/mydata.db"
os.makedirs(os.path.dirname(path_name), exist_ok=True)

# def create_city_table():
#     connection = sqlite3.connect(path_name)
#     print("connected to sqlite")
#     cursor = connection.cursor()
#     sql = '''create table if not exists cities(
#             	"city_id"	INTEGER NOT NULL UNIQUE,
#                 "name"	TEXT NOT NULL,
#                 PRIMARY KEY("city_id" AUTOINCREMENT)
#                 )
#                 '''
#     cursor.execute(sql)
#     cursor.close()
#     connection.close()
# create_city_table()

# def add_cities(names):
#     connection = sqlite3.connect(path_name)
#     print("connected to sqlite")
#     cursor = connection.cursor()
#     sql = '''
#                 insert into cities (name) values (?)
#             '''
#     cursor.executemany(sql,names)
#     connection.commit()
#     cursor.close()
#     connection.close()

# lis_names =[('Tel-Aviv',), ('Holon',),('Rishon-Ltzion',)]
# add_cities(lis_names)
