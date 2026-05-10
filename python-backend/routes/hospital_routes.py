from flask import Blueprint, request, jsonify
from database import get_all_hospitals, add_hospital, update_hospital, delete_hospital_by_id, delete_multiple_hospitals

hospital_bp = Blueprint('hospitals', __name__)

@hospital_bp.route("/hospitals", methods=["GET"])
def fetch_hospitals():
    return jsonify(get_all_hospitals())

@hospital_bp.route("/hospitals", methods=["POST"])
def create_hospital():
    d = request.json
    h_id = add_hospital(d['name'], d['address'], d['description'], d['tags'], d['image'])
    return jsonify({"status": "success", "id": h_id})

@hospital_bp.route("/hospitals/<int:h_id>", methods=["PUT"])
def edit_hospital(h_id):
    d = request.json
    update_hospital(h_id, d['name'], d['address'], d['description'], d['tags'], d['image'])
    return jsonify({"status": "success"})

@hospital_bp.route("/hospitals/<int:h_id>", methods=["DELETE"])
def remove_hospital(h_id):
    delete_hospital_by_id(h_id)
    return jsonify({"status": "success"})

@hospital_bp.route("/hospitals/bulk-delete", methods=["POST"])
def bulk_remove_hospitals():
    ids = request.json.get('ids', [])
    delete_multiple_hospitals(ids)
    return jsonify({"status": "success"})