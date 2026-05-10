from flask import Blueprint, request, jsonify
from database import create_user, verify_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
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

@auth_bp.route("/login", methods=["POST"])
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