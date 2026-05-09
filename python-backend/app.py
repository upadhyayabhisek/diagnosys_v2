from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pickle
import json
import pandas as pd
from fuzzywuzzy import process

from chatbot import predict_disease, get_recommendations 
from database import create_user, verify_user
from database import get_all_faqs, add_faq, update_faq_status, delete_faq_by_id, delete_multiple_faqs,update_faq_details,get_active_faqs
from database import get_all_users, update_user_status, delete_user_by_id, delete_multiple_users
from database import get_all_hospitals, add_hospital, update_hospital, delete_hospital_by_id, delete_multiple_hospitals
from database import get_all_doctors,add_new_doctor,update_doctor_details,delete_doctor_record,bulk_delete_doctors
from database import save_workout_plan,get_latest_workout

# --- 1. Class Definition required for Pickle ---
class FitnessRecommender:
    def __init__(self, df):
        self.df = df.copy()
        self.df["Difficulty Level_Cleaned"] = self.df["Difficulty Level_Cleaned"].str.strip().str.capitalize()
        self.df["Target Muscle Group_Cleaned"] = self.df["Target Muscle Group_Cleaned"].fillna("").str.title().str.strip()

    def fuzzy_match_muscle(self, target):
        all_muscles = self.df["Target Muscle Group_Cleaned"].dropna().unique()
        matches = process.extract(target, all_muscles, limit=3)
        return [m[0] for m in matches if m[1] > 70]

    def recommend(self, difficulty, muscle_group=None, n=5):
        df = self.df[self.df["Difficulty Level_Cleaned"] == difficulty]
        if muscle_group:
            similar = self.fuzzy_match_muscle(muscle_group)
            df = df[df["Target Muscle Group_Cleaned"].isin(similar)]
        if df.empty:
            df = self.df[self.df["Difficulty Level_Cleaned"] == difficulty]
        
        df = df.drop_duplicates(subset="Name of Exercise")
        
        if len(df) < 3:
            return df.head(n)[["Name of Exercise", "Target Muscle Group_Cleaned", "Difficulty Level_Cleaned", "Calories_Burned"]]

        q = df["Calories_Burned"].quantile([0.33, 0.66])
        light = df[df["Calories_Burned"] <= q[0.33]]
        medium = df[(df["Calories_Burned"] > q[0.33]) & (df["Calories_Burned"] <= q[0.66])]
        intense = df[df["Calories_Burned"] > q[0.66]]
        
        result = pd.concat([
            light.sample(n=min(1, len(light)), replace=False),
            medium.sample(n=min(2, len(medium)), replace=False),
            intense.sample(n=min(2, len(intense)), replace=False),
        ])
        return result.sample(frac=1).reset_index(drop=True)[["Name of Exercise", "Target Muscle Group_Cleaned", "Difficulty Level_Cleaned", "Calories_Burned"]]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PKL_PATH = os.path.join(BASE_DIR, "fitness_recommender.pkl")
recommender = None
try:
    with open(PKL_PATH, "rb") as f:
        recommender = pickle.load(f)
    print("✅ Fitness Recommender loaded successfully!")
except FileNotFoundError:
    print(f"❌ Error: Could not find the file at {PKL_PATH}")
except Exception as e:
    print(f"❌ An error occurred loading pickle: {e}")



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


@app.route("/save-workout", methods=["POST"])
def save_workout():
    data = request.json
    email = data.get('email')
    rec = data.get('recommendation')
    if not email or not rec:
        return jsonify({"status": "error", "message": "Missing info"}), 400
    success = save_workout_plan(
        email=email, 
        target=rec['target'], 
        difficulty=data.get('difficulty'), 
        exercises_json=json.dumps(rec['exercises']), 
        expected_burn=rec['expected_burn']
    )
    if success:
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Failed to save to database"}), 500


@app.route("/recommend-workout", methods=["POST"])
def recommend_workout():
    if recommender is None:
        return jsonify({"error": "Recommender system is not initialized"}), 500
    data = request.json
    difficulty = data.get('difficulty', 'Beginner')
    target_muscle = data.get('target_muscle', 'Full Body')
    try:
        user_weight = float(data.get('weight', 70))
    except ValueError:
        user_weight = 70.0
    weight_multiplier = user_weight / 70.0
    try:
        recommendations_df = recommender.recommend(difficulty, target_muscle)
        exercises = []
        running_total = 0
        for _, row in recommendations_df.iterrows():
            base_calories = row['Calories_Burned'] / 100
            adjusted_calories = int(base_calories * weight_multiplier)
            exercises.append({
                "name": row['Name of Exercise'],
                "sets": "3 Sets x 12 Reps",
                "calories": adjusted_calories
            })
            running_total += adjusted_calories
        return jsonify({
            "target": target_muscle,
            "exercises": exercises,
            "expected_burn": running_total
        })
    except Exception as e:
        print(f"Recommendation Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/get-workout-plan", methods=["GET"])
def get_workout_plan():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400
    workout_data = get_latest_workout(email)

    if workout_data:
        return jsonify({
            "status": "success",
            "data": workout_data
        })
    return jsonify({
        "status": "empty", 
        "message": "No workout saved for this user"
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)