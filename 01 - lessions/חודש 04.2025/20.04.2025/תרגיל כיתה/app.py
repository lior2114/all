import sqlite3
from flask import Flask, jsonify, request 
import sqlite3 
import os 

app = Flask(__name__)

if not os.path.exists("SQL"):
    os.makedirs("SQL")
path_name = "./SQL/cities_and_users.db"

#פונקציה עיקבית שכל הפונקציות עוקבות אחריה בפתיחה ובסגירה של הדאטא בייס
def get_db_connetcion():
    with sqlite3.connect(path_name) as connection:
        print(f"connection to {path_name}")
        cursor = connection.cursor()
        return connection,cursor

#print ("=============================================================cities============================================================")
#יצירת השולחן של ערים 
def create_table_cities():
    # Connect to SQLite database
    connection,cursor = get_db_connetcion()
        #create table cities 
    sql = '''create table if not exists cities
                (city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name Text not null)
            '''
    cursor.execute(sql)
    cursor.close()
    print("Database and table created successfully")
create_table_cities()

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Flask server!',
        'status': 'success'
    })

#להוסיף ערים 
@app.route('/cities', methods=['POST'])
def create_city():
    connection,cursor = get_db_connetcion()
    data = request.get_json()
    print(data)
    cursor = connection.cursor()
    sql = 'insert into cities (name) values(?)'  
    cursor.execute(    sql ,  (data['name'],)   )
    city_id = cursor.lastrowid
    connection.commit()# save 
    cursor.close()
    return jsonify({
        'id':city_id,
        'name':data['name']
    })

#הצגת הערים 
@app.route('/cities', methods=['GET'])
def get_cities():
   connection,cursor = get_db_connetcion()
   sql = 'SELECT * FROM CITIES'  
   cursor.execute(sql)
   cities = cursor.fetchall()  
   cursor.close()
   return jsonify({'cities': [dict(id=city[0], name=city[1]) for city in cities]})       

# Delete city
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    connection, cursor = get_db_connetcion()
    
    # Check if city exists
    city = cursor.execute('SELECT * FROM cities WHERE city_id = ?', (city_id,)).fetchone()
    if city is None:
        cursor.close()
        return jsonify({'error': 'City not found'}), 404
    
    cursor.execute('DELETE FROM cities WHERE city_id = ?', (city_id,))
    connection.commit()
 
    return jsonify({'message': f"{city_id} row deleted"})



#print ("=============================================================users============================================================")
#יצירת שולחן משתמשים
def create_table_users():
    connection,cursor = get_db_connetcion()
    sql = '''create table if not exists users
            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT not null,
            last_name TEXT not null,
            email TEXT not null unique,
            password TEXT not null,
            city_id INTEGER not null,
            salary REAL not null,
            is_admin INTEGER default 0,
            FOREIGN KEY (city_id) REFERENCES cities(city_id))
        '''
    #אם לא מכניסים 0 או 1 הדיפולט הוא 0 
    cursor.execute(sql)
    cursor.close()
create_table_users()

#הכנסת המשתמשים לתוך השולחן 
@app.route("/add_users", methods = ["POST"])
def add_users():
    connection,cursor = get_db_connetcion()
    cursor = connection.cursor()
    data = request.get_json()
    sql = '''INSERT INTO users (first_name, last_name, email, password, city_id, salary, is_admin)
        VALUES (?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, (
        data['first_name'],
        data['last_name'],
        data['email'],
        data['password'],
        data['city_id'],
        data['salary'],
        data['is_admin']  # Default to 0 if not provided
    ))
    user_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return jsonify({
        'id': user_id,
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'city_id': data['city_id'],
        'salary': data['salary'],
        'is_admin': data.get('is_admin', 0)
    })


#מראה את כל המשתמשים שיש לי בדאטא בייס 
@app.route("/show_users_in_database", methods = ["GET"])
def show_users():
    connection , cursor = get_db_connetcion()
    sql = "select * from users"
    cursor.execute(sql)
    show = cursor.fetchall()
    cursor.close()
    return jsonify({"users": [dict(user_id=user[0], first_name=user[1], last_name=user[2], email=user[3], password=user[4], city_id=user[5], salary=user[6], is_admin=user[7]) for user in show]})

#מראה את הפרטים של המשתמש לפי האיי די שלו 
@app.route("/get_users_by_id/<user_id>", methods = ["GET"])
def show_user_by_id(user_id):
    connection , cursor = get_db_connetcion()
    sql = "select * from users where user_id = ?"
    cursor.execute(sql, (user_id,))
    show = cursor.fetchone()
    if show is None:
        cursor.close()
        connection.close()
        return jsonify({"error":"user not found"}), 404
    else:
        return jsonify({
            "user_id": show[0],
            "first_name": show[1],
            "last_name": show[2],
            "email": show[3],
            "password": show[4],
            "city_id": show[5],
            "salary": show[6],
            "is_admin": show[7]
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 