from datetime import datetime
import os
import sqlite3
from colorama import Fore
import time

LOG_DIR = "./logs"
LOG_FILE = os.path.join(LOG_DIR, "file.txt")
# Check if running in container or locally
if os.path.exists("/app/mydb.db"):
    DB_FILE = "/app/mydb.db"  # Path in container
else:
    DB_FILE = "./mydb.db"  # Path when running locally

# Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Connect to SQLite database and create/select from cities
try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create cities table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT NOT NULL,
            population INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert some sample data if table is empty
    cursor.execute("SELECT COUNT(*) FROM cities")
    count = cursor.fetchone()[0]
    
    if count == 0:
        sample_cities = [
            ('Tel Aviv', 'Israel', 460000),
            ('Jerusalem', 'Israel', 936000),
            ('Haifa', 'Israel', 285000),
            ('New York', 'USA', 8400000),
            ('London', 'UK', 9000000),
            ('Paris', 'France', 2200000)
        ]
        
        cursor.executemany(
            "INSERT INTO cities (name, country, population) VALUES (?, ?, ?)",
            sample_cities
        )
        conn.commit()
        print(f"{Fore.GREEN}Sample cities data inserted successfully!{Fore.RESET}")
    
    # Select all records from cities table
    cursor.execute("SELECT * FROM cities")
    cities = cursor.fetchall()
    
    print(f"{Fore.CYAN}=== Cities from Database ==={Fore.RESET}")
    for city in cities:
        print(f"{Fore.YELLOW}City: {city}{Fore.RESET}")
    
    conn.close()
    print(f"{Fore.GREEN}Database query completed successfully!{Fore.RESET}")
    
except sqlite3.Error as e:
    print(f"{Fore.RED}Database error: {e}{Fore.RESET}")
except Exception as e:
    print(f"{Fore.RED}Error: {e}{Fore.RESET}")

