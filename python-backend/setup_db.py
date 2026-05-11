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
    CREATE TABLE IF NOT EXISTS faqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        category TEXT NOT NULL,
        status INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DiabetesRecords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inputs_json TEXT NOT NULL,
        result TEXT NOT NULL,
        confidence REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PredictionResults (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        disease_type TEXT NOT NULL,
        record_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (record_id) REFERENCES DiabetesRecords(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LiverRecords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inputs_json TEXT NOT NULL,
        result TEXT NOT NULL,
        confidence REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospitals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        description TEXT,
        tags TEXT,
        image TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        specialty TEXT NOT NULL,
        workplace TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS saved_workouts (
        user_email TEXT PRIMARY KEY, 
        target_muscle TEXT,
        difficulty TEXT,
        exercises TEXT,
        total_calories INTEGER,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_profiles (
        user_email TEXT PRIMARY KEY,
        mobile_no TEXT,
        address TEXT,
        emergency_contact TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_email) REFERENCES users (email) ON DELETE CASCADE
    )
    ''')

    # Insert test users
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
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()