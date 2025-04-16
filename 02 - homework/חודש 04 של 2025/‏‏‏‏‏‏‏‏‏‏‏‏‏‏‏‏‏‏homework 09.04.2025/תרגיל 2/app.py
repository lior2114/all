from flask import Flask, jsonify, request
from datetime import datetime
import sqlite3
path_name = "./SQL/mydb.db"
app = Flask(__name__)

#מסך הבית באתר
@app.route("/")
def home():
    return jsonify({"lori":"klfgd"})

#יוצר שולחן של קטגורי
def create_category_table():
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''create table if not exists category(
            	"category_id"	INTEGER NOT NULL UNIQUE,
                "name" TEXT NOT NULL,
                PRIMARY KEY("category_id" AUTOINCREMENT)
                )
                '''
    cursor.execute(sql)
    cursor.close()
    connection.close()
create_category_table()
#יוצר שולחן טאסק
def create_table_task():
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''create table if not exists task(
          "task_id"	INTEGER NOT NULL UNIQUE,
          "description" TEXT NOT NULL,
          "is_done"	BOOLEAN NOT NULL CHECK (is_done IN (0, 1)),
          "category_id" INTEGER NOT NULL,
          PRIMARY KEY("task_id" AUTOINCREMENT),
          FOREIGN KEY ("category_id") REFERENCES category("category_id")
          )
          '''
    cursor.execute(sql)
    cursor.close()
    connection.close()
create_table_task()


#for category
#מוסיף קטגוריה
@app.route("/insert_category", methods=['POST'])
def insert_categoryies():
    data = request.get_json()
    print(data)
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''insert into  category (name) values (?)'''
    
    category_ids = []
    for category in data:
        cursor.execute(sql, (category['name'],))
        connection.commit()
        category_ids.append(cursor.lastrowid) #מציג איזה מספר עובד הוספנו
    cursor.close()
    connection.close()
    return jsonify({
        'category_ids': category_ids,
        "message": "category/ies added successfully"
    })   
'''
מה לרשום בפוסטמאן כדי להוסיף
  [
{
  "name": "tel-aviv-build"
},
{
  "name":"rishon_tower"
}
]
'''
    
#מוסיף task חדש
@app.route("/insert_task", methods = ["POST"])
def create_task():
    data = request.get_json()
    print(data)  # הדפסה לצורך ניפוי שגיאות כדי לראות את הנתונים שהתקבלו בבקשה.
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''insert into  task (description,is_done,category_id) values (?,?,?)'''
    
    task_ids = []
    for task in data:
        cursor.execute(sql, (task['description'], task['is_done'], task['category_id']))
        connection.commit()
        task_ids.append(cursor.lastrowid) #מציג איזה מספר קטגוריה הוספנו
    cursor.close()
    connection.close()
    return jsonify({
        'task_ids': task_ids,
        "message": "task/s added successfully"
    })
'''
מה לרשום בפוסטמאן כדי להוסיף
[
  {
   "description":"rebuild",
   "is_done":1,
   "category_id":1
  },
  {
  "description":"build",
   "is_done":0,
   "category_id":2
  },
  {
    "description":"jump",
   "is_done":1,
   "category_id":1
   }
]
'''


#הצגת כל הקטגוריות שיש בקטגורי
@app.route("/show_categories", methods=['GET'])
def get_categories():
  connection = sqlite3.connect(path_name)
  print("connected to sqlite")
  cursor = connection.cursor()
  sql = '''select * from category'''
  cursor.execute(sql)
  categories = cursor.fetchall()
  cursor.close()
  connection.close()
  return jsonify({'categories': [dict(category_id=category[0], name=category[1]) for category in categories]})

#מציג הכל ב task
@app.route("/show_task", methods = ['GET'])
def show_all_tasks():
  connection = sqlite3.connect(path_name)
  print("connected to database")
  cursor = connection.cursor()
  sql = 'select * from task'
  cursor.execute(sql)
  show = cursor.fetchall()
  cursor.close()
  connection.close()
  return jsonify({"tasks": [dict(task_id=task[0],description = task[1], is_done = task[2],category_id = task[3])for task in show]})
  
  
  
#משווה בין הטבלאות ומראה את השמות של הקטגוריות לפי האיי די שלהם בטבלה השניה 
@app.route("/show_category_id", methods = ['GET'])
def show_category_id_name():
  connection = sqlite3.connect(path_name)
  print("connected to database")
  cursor = connection.cursor()
  sql = '''SELECT task_id, description, is_done, name 
           FROM task
           INNER JOIN category ON task.category_id = category.category_id'''
  cursor.execute(sql)
  show = cursor.fetchall()
  cursor.close()
  connection.close()
  return jsonify({"tasks": [dict(task_id=task[0], description=task[1], is_done=task[2], category_name=task[3]) for task in show]})



#מחיקת task לפי האיי די בטבלת task
@app.route("/delete_task/<int:task_id>", methods = ['DELETE'])
def delete_task_by_id(task_id):
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''delete from task 
            where task_id = ?
    '''
    cursor.execute( sql, (task_id,) )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message":"task deleted successfully"})
'''
מה רושמי בפוסטמאן
http://127.0.0.1:5000/delete_task/1
'''
if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=5000)
