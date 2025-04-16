from flask import Flask, jsonify, request
from datetime import datetime
import sqlite3
path_name = "./SQL/mydb.db"
app = Flask(__name__)

def create_table_workers():
    connection = sqlite3.connect('./SQL/mydb.db')
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''create table if not exists workers(
            	"worker_id"	INTEGER NOT NULL UNIQUE,
                "Fname" TEXT NOT NULL,
                "Lname"	TEXT NOT NULL,
                "salary" INTEGER NOT NULL,
                PRIMARY KEY("worker_id" AUTOINCREMENT)
                )
                '''
    cursor.execute(sql)
    cursor.close()
    connection.close()
create_table_workers()

@app.route("/")
def home():
    return jsonify({"lori":"klfgd"})


@app.route("/insert_worker", methods=['POST'])
def insert_workers():
    data = request.get_json()
    print(data)
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''insert into workers (Fname, Lname, salary) values (?, ?, ?)'''
    
    worker_ids = []
    for worker in data:
        cursor.execute(sql, (worker['Fname'], worker['Lname'], worker['salary']))
        connection.commit()
        worker_ids.append(cursor.lastrowid) #מציג איזה מספר עובד הוספנו
    
    cursor.close()
    connection.close()
    return jsonify({
        'worker_ids': worker_ids,
        "message": "Worker/s added successfully"
    })
    
    #מה לרשום בפוסטמאן כדי להוסיף 
    '''
    [
  {
    "Fname": "lior",
    "Lname": "mamo",
    "salary": 3000
  }
]

ולשתיים פלוס
[
  {
    "Fname": "lior",
    "Lname": "mamo",
    "salary": 3000
  },
  {
    "Fname": "another",
    "Lname": "worker",
    "salary": 4000
  }
]
    '''
    
@app.route("/show_workers", methods=['GET'])
def show_workers():
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''select * from workers'''
    cursor.execute(sql)
    show = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify({'workers': [dict(id=worker[0], Fname=worker[1], Lname=worker[2], salary=worker[3]) for worker in show]})


@app.route("/delete_worker/<int:worker_id>", methods = ['DELETE'])
def delete_worker_by_id(worker_id):
    connection = sqlite3.connect(path_name)
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''delete from workers 
            where worker_id = ?
    '''
    cursor.execute( sql, (worker_id,) )
    connection.commit()
    cursor.close()
    connection.cloes()
    return jsonify({"message":"worker deleted successfully"})

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=5000)
