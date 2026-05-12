from flask import Blueprint, request, jsonify
from .db_utils import get_db_connection

user_settings_bp = Blueprint("user_settings_bp", __name__)

@user_settings_bp.route("/api/user/settings/<email>", methods=["GET"])
def get_user_settings(email):

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, email, gender, birthday, role, status, created_at
            FROM users
            WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User not found"}), 404
        cursor.execute("""
            SELECT mobile_no, address, emergency_contact, updated_at
            FROM user_profiles
            WHERE user_email = ?
        """, (email,))

        profile = cursor.fetchone()

        conn.close()

        return jsonify({
            "user": dict(user),
            "profile": dict(profile) if profile else None
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_settings_bp.route("/api/user/settings/<email>", methods=["PUT"])
def update_user_settings(email):

    try:
        data = request.json

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET name = ?, gender = ?, birthday = ?
            WHERE email = ?
        """, (
            data.get("name"),
            data.get("gender"),
            data.get("birthday"),
            email
        ))
        cursor.execute("""
            INSERT INTO user_profiles (user_email, mobile_no, address, emergency_contact, updated_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_email)
            DO UPDATE SET
                mobile_no = excluded.mobile_no,
                address = excluded.address,
                emergency_contact = excluded.emergency_contact,
                updated_at = CURRENT_TIMESTAMP
        """, (
            email,
            data.get("mobile_no"),
            data.get("address"),
            data.get("emergency_contact")
        ))
        conn.commit()
        conn.close()
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500