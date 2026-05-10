from flask import Blueprint, request, jsonify
from database import get_all_doctors, add_new_doctor, update_doctor_details, delete_doctor_record, bulk_delete_doctors

doctor_bp = Blueprint('doctors', __name__)

@doctor_bp.route("/doctors", methods=["GET", "POST"])
def handle_doctors():
    if request.method == "GET":
        return jsonify(get_all_doctors())
    
    if request.method == "POST":
        data = request.json
        add_new_doctor(data['name'], data['email'], data['specialty'], data['workplace'])
        return jsonify({"status": "success"}), 201

@doctor_bp.route("/doctors/<int:doc_id>", methods=["PUT", "DELETE"])
def modify_doctor(doc_id):
    if request.method == "PUT":
        data = request.json
        update_doctor_details(doc_id, data['name'], data['email'], data['specialty'], data['workplace'])
        return jsonify({"status": "success"})
    
    if request.method == "DELETE":
        delete_doctor_record(doc_id)
        return jsonify({"status": "success"})
    
@doctor_bp.route("/doctors/bulk-delete", methods=["POST"])
def bulk_remove_doctors():
    data = request.json
    ids = data.get('ids', [])
    
    if not ids:
        return jsonify({"status": "error", "message": "No IDs provided"}), 400
    bulk_delete_doctors(ids)
    return jsonify({"status": "success"})