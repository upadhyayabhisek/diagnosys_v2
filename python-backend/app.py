from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from chatbot import predict_disease, get_recommendations 
from database import create_user, verify_user
from database import get_all_faqs, add_faq, update_faq_status, delete_faq_by_id, delete_multiple_faqs,update_faq_details,get_active_faqs
from database import get_all_users, update_user_status, delete_user_by_id, delete_multiple_users
from database import get_all_hospitals, add_hospital, update_hospital, delete_hospital_by_id, delete_multiple_hospitals
from database import get_all_doctors,add_new_doctor,update_doctor_details,delete_doctor_record,bulk_delete_doctors

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return jsonify({"message": "MediAI Backend running 🚀"})


#--------------------------------------------------------------------------------------

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400
    
    name = data.get('name')
    email = data.get('email')
    role = 'user' 
    
    success = create_user(
        name=name,
        email=email,
        password=data.get('password'),
        gender=data.get('gender'),
        birthday=data.get('birthday'),
        role=role
    )
    
    if success:
        return jsonify({
            "status": "success", 
            "message": "User registered",
            "user": {
                "name": name,
                "email": email,
                "role": role
            }
        }), 201
        
    return jsonify({"error": "Email already registered"}), 400


#--------------------------------------------------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    result = verify_user(data.get('email'), data.get('password'))
    if result == "account_disabled":
        return jsonify({
            "status": "error",
            "error": "account_disabled"
        }), 403
    if result:
        return jsonify({
            "status": "success",
            "user": {
                "name": result['name'],
                "email": result['email'],
                "role": result['role']
            }
        })
    return jsonify({
        "status": "error", 
        "error": "Invalid email or password"
    }), 401

#--------------------------------------------------------------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        user_msg = data.get("message", "")
        lang = data.get("lang", "en") 
        disease, confidence = predict_disease(user_msg, lang=lang)
        details = get_recommendations(disease, lang=lang)
        
        return jsonify({
            "status": "success",
            "prediction": {
                "disease": disease,
                "confidence": f"{confidence:.2%}",
                "details": details
            }
        })
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

#--------------------------------------------------------------------------------------

@app.route("/users", methods=["GET"])
def fetch_users():
    return jsonify(get_all_users())

@app.route("/users/<int:user_id>/status", methods=["PATCH"])
def toggle_user_status(user_id):
    data = request.json
    update_user_status(user_id, data['status'])
    return jsonify({"status": "success"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    delete_user_by_id(user_id)
    return jsonify({"status": "success"})

@app.route("/users/bulk-delete", methods=["POST"])
def bulk_remove_users():
    ids = request.json.get('ids', [])
    if ids:
        delete_multiple_users(ids)
    return jsonify({"status": "success"})

#--------------------------------------------------------------------------------------

@app.route("/faqs", methods=["GET"])
def fetch_faqs():
    return jsonify(get_all_faqs())

@app.route("/api/faqs/active", methods=["GET"])
def fetch_public_faqs():
    return jsonify(get_active_faqs())
 
@app.route("/faqs", methods=["POST"])
def create_faq():
    data = request.json
    faq_id = add_faq(data['question'], data['answer'], data['category'], 1)
    return jsonify({"status": "success", "id": faq_id}), 201

@app.route("/faqs/<int:faq_id>/status", methods=["PATCH"])
def toggle_faq(faq_id):
    data = request.json
    update_faq_status(faq_id, data['status'])
    return jsonify({"status": "success"})

@app.route("/faqs/<int:faq_id>", methods=["PUT"])
def update_faq(faq_id):
    data = request.json
    update_faq_details(
        faq_id, 
        data['question'], 
        data['answer'], 
        data['category']
    )
    return jsonify({"status": "success"})

@app.route("/faqs/<int:faq_id>", methods=["DELETE"])
def remove_faq(faq_id):
    delete_faq_by_id(faq_id)
    return jsonify({"status": "success"})

@app.route("/faqs/bulk-delete", methods=["POST"])
def bulk_remove_faqs():
    ids = request.json.get('ids', [])
    delete_multiple_faqs(ids)
    return jsonify({"status": "success"})

#--------------------------------------------------------------------------------------

@app.route("/hospitals", methods=["GET"])
def fetch_hospitals():
    return jsonify(get_all_hospitals())

@app.route("/hospitals", methods=["POST"])
def create_hospital():
    d = request.json
    h_id = add_hospital(d['name'], d['address'], d['description'], d['tags'], d['image'])
    return jsonify({"status": "success", "id": h_id})

@app.route("/hospitals/<int:h_id>", methods=["PUT"])
def edit_hospital(h_id):
    d = request.json
    update_hospital(h_id, d['name'], d['address'], d['description'], d['tags'], d['image'])
    return jsonify({"status": "success"})

@app.route("/hospitals/<int:h_id>", methods=["DELETE"])
def remove_hospital(h_id):
    delete_hospital_by_id(h_id)
    return jsonify({"status": "success"})

@app.route("/hospitals/bulk-delete", methods=["POST"])
def bulk_remove_hospitals():
    ids = request.json.get('ids', [])
    delete_multiple_hospitals(ids)
    return jsonify({"status": "success"})

#--------------------------------------------------------------------------------------

@app.route("/doctors", methods=["GET", "POST"])
def handle_doctors():
    if request.method == "GET":
        return jsonify(get_all_doctors())
    
    if request.method == "POST":
        data = request.json
        add_new_doctor(data['name'], data['email'], data['specialty'], data['workplace'])
        return jsonify({"status": "success"}), 201

@app.route("/doctors/<int:doc_id>", methods=["PUT", "DELETE"])
def modify_doctor(doc_id):
    if request.method == "PUT":
        data = request.json
        update_doctor_details(doc_id, data['name'], data['email'], data['specialty'], data['workplace'])
        return jsonify({"status": "success"})
    
    if request.method == "DELETE":
        delete_doctor_record(doc_id)
        return jsonify({"status": "success"})
    
@app.route("/doctors/bulk-delete", methods=["POST"])
def bulk_remove_doctors():
    data = request.json
    ids = data.get('ids', [])
    
    if not ids:
        return jsonify({"status": "error", "message": "No IDs provided"}), 400
    bulk_delete_doctors(ids)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)