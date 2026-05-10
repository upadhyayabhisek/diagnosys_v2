from flask import Blueprint, request, jsonify
from database import get_all_faqs, add_faq, update_faq_status, delete_faq_by_id, delete_multiple_faqs, update_faq_details, get_active_faqs

faq_bp = Blueprint('faqs', __name__)

@faq_bp.route("/faqs", methods=["GET"])
def fetch_faqs():
    return jsonify(get_all_faqs())

@faq_bp.route("/api/faqs/active", methods=["GET"])
def fetch_public_faqs():
    return jsonify(get_active_faqs())
 
@faq_bp.route("/faqs", methods=["POST"])
def create_faq():
    data = request.json
    faq_id = add_faq(data['question'], data['answer'], data['category'], 1)
    return jsonify({"status": "success", "id": faq_id}), 201

@faq_bp.route("/faqs/<int:faq_id>/status", methods=["PATCH"])
def toggle_faq(faq_id):
    data = request.json
    update_faq_status(faq_id, data['status'])
    return jsonify({"status": "success"})

@faq_bp.route("/faqs/<int:faq_id>", methods=["PUT"])
def update_faq(faq_id):
    data = request.json
    update_faq_details(
        faq_id, 
        data['question'], 
        data['answer'], 
        data['category']
    )
    return jsonify({"status": "success"})

@faq_bp.route("/faqs/<int:faq_id>", methods=["DELETE"])
def remove_faq(faq_id):
    delete_faq_by_id(faq_id)
    return jsonify({"status": "success"})

@faq_bp.route("/faqs/bulk-delete", methods=["POST"])
def bulk_remove_faqs():
    ids = request.json.get('ids', [])
    delete_multiple_faqs(ids)
    return jsonify({"status": "success"})