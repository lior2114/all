import sqlite3
from flask import Flask, jsonify, request
import os

path_name = './SQL/MyData.db'
if not os.path.exists('SQL'):
    os.makedirs('SQL')

app = Flask(__name__)
@app.route("/")
def home():
   return jsonify({'massage':'hello'})

#לחסוך שורות 
def con():
   with sqlite3.connect(path_name) as connection:
    print("connected")
    cursor = connection.cursor()
    return connection , cursor

#יצירת שולחן קטגורי
def create_table_categories():
    connection, cursor = con()
    sql = '''
                create table if not exists categories(
                    "category_id"	INTEGER NOT NULL UNIQUE,
                    "name" TEXT NOT NULL,
                    PRIMARY KEY("category_id" AUTOINCREMENT)
                    )
                    '''
    cursor.execute(sql)
    cursor.close()
# create_table_categories()

#יצירת שולחן משימות 
def create_task_table():
   connection,cursor = con()
   sql = '''
        create table if not exists task(
          "task_id"	INTEGER NOT NULL UNIQUE,
          "description" TEXT NOT NULL,
          "is_done"	BOOLEAN NOT NULL CHECK (is_done IN (0, 1)),
          "category_id" INTEGER NOT NULL,
          PRIMARY KEY("task_id" AUTOINCREMENT),
          FOREIGN KEY ("category_id") REFERENCES categories("category_id")
          )
        '''
   cursor.execute(sql)
   cursor.close()
# create_task_table()

#הכנסה של קטגורי
@app.route("/insert_categories", methods=['POST'])
def insert_categories():
    data = request.get_json()
    print(data)
    connection, cursor = con()
    sql = '''
        insert into categories (name) values (?)
        '''
    lis = []
    for d in data:
        cursor.execute(sql, (d['name'],))
        connection.commit()
        lis.append(cursor.lastrowid)
    cursor.close()
    return jsonify({'category id': lis, "message": "Category added successfully"})

#הצגה של כל הקטגוריות 
@app.route("/get_categories", methods=['GET'])
def get_category():
    connection, cursor = con()
    sql = 'select * from categories'
    cursor.execute(sql)
    show = cursor.fetchall()
    cursor.close()
    for s in show:
        return jsonify(dict(category_id = s[0], name = s[1]))



if __name__ == '__main__':
   app.run(debug=True , host = '0.0.0.0', port = 5000)