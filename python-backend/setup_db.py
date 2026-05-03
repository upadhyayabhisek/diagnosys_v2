import sqlite3
import os
from werkzeug.security import generate_password_hash

def init_db():
    if not os.path.exists('instance'):
        os.makedirs('instance')
        
    db_path = 'instance/mediai.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            gender TEXT,
            birthday TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    hashed_password = generate_password_hash("admin123")
    
    try:
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            ("Admin User", "admin@mail.com", hashed_password, "admin")
        )
        print("Admin user created successfully.")
    except sqlite3.IntegrityError:
        print("Admin user already exists. If you changed the hashing method, delete the .db file and run this again.")
        
    conn.commit()
    conn.close()
    print(" Database initialized successfully.")

if __name__ == "__main__":
    init_db()