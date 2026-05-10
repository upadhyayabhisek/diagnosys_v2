from flask import Blueprint, request, jsonify
from database import get_all_users, update_user_status, delete_user_by_id, delete_multiple_users

user_bp = Blueprint('users', __name__)

@user_bp.route("/users", methods=["GET"])
def fetch_users():
    return jsonify(get_all_users())

@user_bp.route("/users/<int:user_id>/status", methods=["PATCH"])
def toggle_user_status(user_id):
    data = request.json
    update_user_status(user_id, data['status'])
    return jsonify({"status": "success"})

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    delete_user_by_id(user_id)
    return jsonify({"status": "success"})

@user_bp.route("/users/bulk-delete", methods=["POST"])
def bulk_remove_users():
    ids = request.json.get('ids', [])
    if ids:
        delete_multiple_users(ids)
    return jsonify({"status": "success"})