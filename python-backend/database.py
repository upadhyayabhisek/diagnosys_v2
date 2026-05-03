from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

DB_PATH = "instance/mediai.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def verify_user(email, provided_password):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    
    if user and check_password_hash(user['password'], provided_password):
        return user
    return None

def create_user(name, email, password, role='user', gender=None, birthday=None):
    hashed_password = generate_password_hash(password)
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO users (name, email, password, role, gender, birthday) VALUES (?, ?, ?, ?, ?, ?)",
            (name, email, hashed_password, role, gender, birthday)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()