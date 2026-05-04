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
            status INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    hashed_password = generate_password_hash("admin123")
    
    test_users = [
        ("Admin User", "admin@mail.com", "admin", 1),       # Admin (Active)
        ("Active Tester", "mail1@mail.com", "user", 1),     # Normal User (Active)
        ("Disabled Tester", "mail2@mail.com", "user", 0)    # Normal User (Disabled)
    ]
    
    for name, email, role, status in test_users:
        try:
            cursor.execute(
                "INSERT INTO users (name, email, password, role, status) VALUES (?, ?, ?, ?, ?)",
                (name, email, hashed_password, role, status)
            )
            print(f"User {email} created successfully.")
        except sqlite3.IntegrityError:
            print(f"User {email} already exists.")
        
    conn.commit()
    conn.close()
    print(" Database initialized successfully.")

if __name__ == "__main__":
    init_db()