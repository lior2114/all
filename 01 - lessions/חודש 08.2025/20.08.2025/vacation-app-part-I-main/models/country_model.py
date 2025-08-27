import sqlite3

class Country:
    @staticmethod
    def get_db_connection():
        return sqlite3.connect('my_db.db')

    @staticmethod
    def create_table():
        print("Creating countries table...")
        with Country.get_db_connection() as connection:
            cursor = connection.cursor()
            sql = '''
                CREATE TABLE IF NOT EXISTS countries (
                    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    country_name TEXT NOT NULL UNIQUE
                )
            '''
            cursor.execute(sql)
            cursor.close()

    @staticmethod
    def insert_default_countries():
        countries = [
            'Italy', 'Spain', 'France', 'Greece', 'Japan',
            'Argentina', 'Brazil', 'Mexico', 'Portugal', 'Thailand'
        ]

        with Country.get_db_connection() as connection:
            cursor = connection.cursor()
            for name in countries:
                cursor.execute('SELECT * FROM countries WHERE country_name = ?', (name,))
                if cursor.fetchone() is None:
                    cursor.execute('INSERT INTO countries (country_name) VALUES (?)', (name,))
            connection.commit()
            cursor.close()

    @staticmethod
    def get_all_countries():
        with Country.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM countries')
            rows = cursor.fetchall()
            cursor.close()
            return [{'country_id': row[0], 'country_name': row[1]} for row in rows]
