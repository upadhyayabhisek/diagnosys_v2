from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from chatbot import predict_disease, get_recommendations 
from database import create_user, verify_user

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return jsonify({"message": "MediAI Backend running 🚀"})

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400
    success = create_user(
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password'),
        gender=data.get('gender'),
        birthday=data.get('birthday')
    )
    if success:
        return jsonify({"status": "success", "message": "User registered"}), 201
    return jsonify({"error": "Email already registered"}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = verify_user(data.get('email'), data.get('password'))
    if user:
        return jsonify({
            "status": "success",
            "user": {
                "name": user['name'],
                "email": user['email'],
                "role": user['role']
            }
        })
    
    return jsonify({"error": "Invalid email or password"}), 401

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

if __name__ == "__main__":
    app.run(debug=True, port=5001)