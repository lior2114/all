import os
import time
import mysql.connector

def connect_to_mysql():
    max_retries = 30
    retry_count = 0
    while retry_count < max_retries:
        try:
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST", 'localhost'),
                database=os.getenv("DB_DATABASE", 'mydb'),
                password=os.getenv("DB_PASSWORD", '123456'),
                user=os.getenv("DB_USER", 'root'),
            )
            print("Connected to MySQL")
            return conn
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            retry_count += 1
            time.sleep(2)
    raise Exception("Failed to connect to MySQL")

conn = connect_to_mysql()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
""")
conn.commit()

cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("John Doe", "john.doe@example.com"))
conn.commit()

cursor.execute("select * from users")
users = cursor.fetchall()
for user in users:
    print(user)

cursor.close()
conn.close()
