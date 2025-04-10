import sqlite3
import os
path_name = "./SQL/Mydata.db"
if not os.path.exists(path_name):
    os.makedirs(os.path.dirname(path_name), exist_ok=True)
    if os.path.exists(path_name):
        print("File already exists.")
    else:
        open(path_name, 'w').close()
        print("Made file.")
#קריאה מהטבלה 
# def print_persons():
#     connection =sqlite3.connect('./SQL/mydb_v1.db')
#     print("connected to database")
    
#     cursor = connection.cursor()
#     sql = "select * from Persons"

#     cursor.execute(sql)
#     persons = cursor.fetchall()


#     for p in persons:
#         print(p)
        
#     cursor.close()
#     connection.close()
# print_persons()


#יצירת טבלה חדשה 
def create_table_cities():
    connection = sqlite3.connect(path_name)
    print("connected to database")
    cursor = connection.cursor()
    # אפשר להעתיק מהאסקיואל את מה שרשום למטה כשאנחנו יוצרים טבלה עם משתנים חדשים 
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
create_table_cities()

# #יצירת משתנה בתוך המשתנים בטבלה שיצרנו 
# def insert_city(name):
#     connection = sqlite3.connect('./SQL/mydb_v2.db')
#     print("connected to database mydb_v2")
#     cursur = connection.cursor()

#     sql = f''' 
#             insert into cities (name) values (?)
#             '''
#     cursur.execute(sql, (name,))
#     connection.commit()  # Commit the transaction/save
#     cursur.close()
#     connection.close()

# for i in range(3):
#     city = input("enter city name: ")
#     insert_city(city)

# #יוצר הרבה ערים בגלל שעשינו את השם של העיר יוניק אז לא יתין לנו להפעיל אותה פעם נוספת אלא עם כן נשנה את השמות של העיר 
# def insert_many_city(names):
#     connection = sqlite3.connect('./SQL/mydb_v2.db')
#     print("connected to database mydb_v2")
#     cursur = connection.cursor()

#     sql = f''' 
#             insert into cities (name) values (?)
#             '''
#     cursur.executemany(sql, names) # כאן השתנה להרבה בפקודה
#     connection.commit() 
#     cursur.close()
#     connection.close()

# samples_city=[
#     ('ny',),
#     ('london',),
#     ('tokyo',),
#     ('paris',),
# ]

# insert_many_city (samples_city)

# #בחירת עיר לפי id
# def select_many_cities_by_id(id):
#     connection = sqlite3.connect('./SQL/mydb_v2.db')
#     print("connected to database mydb_v2")
#     cursur = connection.cursor()

#     sql = f''' 
#             select * from cities where city_id = ?
#             '''
#     cursur.execute(sql, (id,) ) # כאן השתנה להרבה בפקודה
#     city = cursur.fetchone() #פאץ אחד  כי בודקים רק משהוא אחד ולא הכל 
#     print(city)
#     cursur.close()
#     connection.close()
# select_many_cities_by_id(1)

# #מחיקת לפי id
# def delete_city_by_id(id):
#     connection = sqlite3.connect('./SQL/mydb_v2.db')
#     print("connected to database mydb_v2")
#     cursor = connection.cursor()

#     sql = ''' 
#             DELETE FROM cities WHERE city_id = ?
#           '''
#     cursor.execute(sql, (id,))
#     connection.commit()  # save
#     print(f"City with id {id} has been deleted.")
#     cursor.close()
#     connection.close()

# #עדכון נתונים בטבלה
# def update_city_by_id(new_name, id):
#     connection = sqlite3.connect('./SQL/mydb_v2.db')
#     print("connected to database mydb_v2")
#     cursor = connection.cursor()

#     sql = ''' 
#             UPDATE cities 
#             SET name = ? 
#             WHERE city_id = ?
#           '''
#     cursor.execute(sql, (new_name, id))
#     connection.commit()  # Save changes
#     print(f"City with id {id} has been updated to {new_name}.")
#     cursor.close()
#     connection.close()