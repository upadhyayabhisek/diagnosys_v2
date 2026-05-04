from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

DB_PATH = "instance/mediai.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

#---------------------------------------------------------------------------------

def verify_user(email, provided_password):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    if user:
        if check_password_hash(user['password'], provided_password):
            if user['status'] == 1:
                return user
            else:
                print(f"Login attempt for disabled account: {email}")
                return "account_disabled"
    return None

#---------------------------------------------------------------------------------

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

def get_all_users():
    conn = get_db_connection()
    users = conn.execute("SELECT id, name, email, role, gender, birthday, status, created_at FROM users").fetchall()
    conn.close()
    return [dict(user) for user in users]

def update_user_status(user_id, new_status):
    conn = get_db_connection()
    conn.execute("UPDATE users SET status = ? WHERE id = ?", (new_status, user_id))
    conn.commit()
    conn.close()

def delete_user_by_id(user_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def delete_multiple_users(ids):
    conn = get_db_connection()
    placeholders = ', '.join(['?'] * len(ids))
    conn.execute(f"DELETE FROM users WHERE id IN ({placeholders})", ids)
    conn.commit()
    conn.close()


#---------------------------------------------------------------------------------

def get_all_faqs():
    conn = get_db_connection()
    faqs = conn.execute("SELECT * FROM faqs ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(faq) for faq in faqs]

def get_active_faqs():
    conn = get_db_connection()
    faqs = conn.execute("SELECT * FROM faqs WHERE status = 1 ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(faq) for faq in faqs]

def add_faq(question, answer, category, status=1):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO faqs (question, answer, category, status) VALUES (?, ?, ?, ?)",
        (question, answer, category, status)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def update_faq_status(faq_id, new_status):
    conn = get_db_connection()
    conn.execute("UPDATE faqs SET status = ? WHERE id = ?", (new_status, faq_id))
    conn.commit()
    conn.close()

def update_faq_details(faq_id, question, answer, category):
    """Updates the content of an existing FAQ."""
    conn = get_db_connection()
    conn.execute(
        "UPDATE faqs SET question = ?, answer = ?, category = ? WHERE id = ?",
        (question, answer, category, faq_id)
    )
    conn.commit()
    conn.close()

def delete_faq_by_id(faq_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM faqs WHERE id = ?", (faq_id,))
    conn.commit()
    conn.close()

def delete_multiple_faqs(ids):
    conn = get_db_connection()
    placeholders = ', '.join(['?'] * len(ids))
    conn.execute(f"DELETE FROM faqs WHERE id IN ({placeholders})", ids)
    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------

def get_all_hospitals():
    conn = get_db_connection()
    hospitals = conn.execute("SELECT * FROM hospitals ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(h) for h in hospitals]

def add_hospital(name, address, description, tags, image):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO hospitals (name, address, description, tags, image) VALUES (?, ?, ?, ?, ?)",
        (name, address, description, tags, image)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def update_hospital(h_id, name, address, description, tags, image):
    conn = get_db_connection()
    conn.execute(
        "UPDATE hospitals SET name=?, address=?, description=?, tags=?, image=? WHERE id=?",
        (name, address, description, tags, image, h_id)
    )
    conn.commit()
    conn.close()

def delete_hospital_by_id(h_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM hospitals WHERE id = ?", (h_id,))
    conn.commit()
    conn.close()

def delete_multiple_hospitals(ids):
    conn = get_db_connection()
    placeholders = ', '.join(['?'] * len(ids))
    conn.execute(f"DELETE FROM hospitals WHERE id IN ({placeholders})", ids)
    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------
def get_all_doctors():
    conn = get_db_connection()
    docs = conn.execute("SELECT * FROM doctors ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(row) for row in docs]

def add_new_doctor(name, email, specialty, workplace):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO doctors (name, email, specialty, workplace) VALUES (?, ?, ?, ?)",
        (name, email, specialty, workplace)
    )
    conn.commit()
    conn.close()

def update_doctor_details(doc_id, name, email, specialty, workplace):
    conn = get_db_connection()
    conn.execute(
        "UPDATE doctors SET name = ?, email = ?, specialty = ?, workplace = ? WHERE id = ?",
        (name, email, specialty, workplace, doc_id)
    )
    conn.commit()
    conn.close()

def delete_doctor_record(doc_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM doctors WHERE id = ?", (doc_id,))
    conn.commit()
    conn.close()

def bulk_delete_doctors(ids):
    """Deletes multiple doctors based on a list of IDs."""
    if not ids:
        return
    conn = get_db_connection()
    placeholders = ', '.join(['?'] * len(ids))
    query = f"DELETE FROM doctors WHERE id IN ({placeholders})"
    conn.execute(query, ids)
    conn.commit()
    conn.close()
    