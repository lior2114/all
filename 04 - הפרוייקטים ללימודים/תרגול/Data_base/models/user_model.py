import sqlite3
import hashlib
from datetime import datetime

class UserModel:
    DATABASE = 'users.db'
    
    @staticmethod
    def init_db():
        """Initialize the database and create tables"""
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def get_db_connection():
        """Get database connection"""
        conn = sqlite3.connect(UserModel.DATABASE)
        conn.row_factory = sqlite3.Row  # This enables column access by name
        return conn
    
    @staticmethod
    def create_user(username, email, password):
        """Create a new user"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            hashed_password = UserModel.hash_password(password)
            
            cursor.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (username, email, hashed_password))
            
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return user_id
        except sqlite3.IntegrityError:
            conn.close()
            raise Exception("Username or email already exists")
        except Exception as e:
            conn.close()
            raise e
    
    @staticmethod
    def get_all_users():
        """Get all users"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
            users = cursor.fetchall()
            
            conn.close()
            
            return [dict(user) for user in users]
        except Exception as e:
            conn.close()
            raise e
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            user = cursor.fetchone()
            
            conn.close()
            
            return dict(user) if user else None
        except Exception as e:
            conn.close()
            raise e
    
    @staticmethod
    def get_user_by_username(username):
        """Get user by username"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            
            conn.close()
            
            return dict(user) if user else None
        except Exception as e:
            conn.close()
            raise e
    
    @staticmethod
    def get_user_by_email(email):
        """Get user by email"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = cursor.fetchone()
            
            conn.close()
            
            return dict(user) if user else None
        except Exception as e:
            conn.close()
            raise e
    
    @staticmethod
    def update_user(user_id, **kwargs):
        """Update user by ID"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            # Build update query dynamically
            update_fields = []
            values = []
            
            for field, value in kwargs.items():
                if field in ['username', 'email', 'password']:
                    update_fields.append(f"{field} = ?")
                    if field == 'password':
                        values.append(UserModel.hash_password(value))
                    else:
                        values.append(value)
            
            if not update_fields:
                conn.close()
                return False
            
            values.append(user_id)
            query = f"UPDATE users SET {', '.join(update_fields)} WHERE id = ?"
            
            cursor.execute(query, values)
            
            if cursor.rowcount == 0:
                conn.close()
                return False
            
            conn.commit()
            conn.close()
            
            return True
        except sqlite3.IntegrityError:
            conn.close()
            raise Exception("Username or email already exists")
        except Exception as e:
            conn.close()
            raise e
    
    @staticmethod
    def delete_user(user_id):
        """Delete user by ID"""
        try:
            conn = UserModel.get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            
            if cursor.rowcount == 0:
                conn.close()
                return False
            
            conn.commit()
            conn.close()
            
            return True
        except Exception as e:
            conn.close()
            raise e
