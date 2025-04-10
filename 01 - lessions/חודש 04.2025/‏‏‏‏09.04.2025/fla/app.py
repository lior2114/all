from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)

#יצירת טבלת סיטי
def create_table_cities():
    connection = sqlite3.connect('./SQL/mydb.db')
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''create table if not exists cities(
            	"city_id"	INTEGER NOT NULL UNIQUE,
                "name"	TEXT NOT NULL,
                PRIMARY KEY("city_id" AUTOINCREMENT)
                )
                '''
    cursor.execute(sql)
    cursor.close()
    connection.close()
create_table_cities()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask!"})

@app.route("/details")
def get_details():
    return jsonify({"firstname":"ploni","lastname":"p"})

#לפרסם (לקבל לטבלה נתון שמכניסים מהשרת)
@app.route('/cities', methods = ['post'])
def create_city():
    data = request.get_json()
    print(data)
    connection = sqlite3.connect('./SQL/mydb.db')
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''insert into cities (name) values (?)
                '''
    cursor.execute( sql,     (data['name'],)  )
    connection.commit()
    cursor.close()
    city_id = cursor.lastrowid #מחזיר את הסיטי איי די ומציג אותו גם בפוסטמאן 
    connection.close()
    return jsonify({
        'id':city_id,
        'name':data['name']
    })

#מראה בשרת את הנתונים שיש לנו בטבלת SQL
@app.route('/cities', methods = ['GET'])
def get_cities():
    connection = sqlite3.connect('./SQL/mydb.db')
    print("connected to sqlite")
    cursor = connection.cursor()
    sql = '''select * from cities
                '''
    cursor.execute( sql)
    cities = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify({'cities': [dict(id=city[0], name=city[1]) for city in cities]})

# מחיקת עיר לפי שינוי המספר למעלה בכתובת
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    connection = sqlite3.connect('./SQL/mydb.db')
    print("connected to sqlite")
    cursor = connection.cursor()
    
    # Check if city exists
    cursor.execute('SELECT * FROM cities WHERE city_id = ?', (city_id,))
    city = cursor.fetchone()
    if city is None:
        cursor.close()
        connection.close()
        return jsonify({'error': 'City not found'}), 404
    
    # Delete city
    cursor.execute('DELETE FROM cities WHERE city_id = ?', (city_id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({'message': "City deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)