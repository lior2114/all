import sqlite3
from city_model import CityModel
import os
path_name = "./SQL/cities.db"
if not os.path.exists("SQL"):
    os.makedirs("SQL")

class CityController:
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect(path_name)
        conn.row_factory = sqlite3.Row
        return conn


    @staticmethod
    def init_db():
        conn = CityController.get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                population INTEGER,
                country TEXT
            )
        ''')

    def add_cities():
        conn = CityController.get_db_connection()
        conn.execute('''
            INSERT INTO cities (name, population, country)
            VALUES 
            ('New York', 8419000, 'USA'),
            ('Los Angeles', 3980000, 'USA'),
            ('London', 8982000, 'UK'),
            ('Manchester', 553230, 'UK'),
            ('Tokyo', 13929286, 'Japan'),
            ('Osaka', 2715000, 'Japan')
        ''')
        conn.commit()
        conn.close()

    def get_by_country(name):
        conn = CityController.get_db_connection()
        cursor = conn.execute('''
            SELECT * FROM cities WHERE country = ?
        ''', (name,))
        results = cursor.fetchall()
        conn.close()
        return [dict(row) for row in results]
