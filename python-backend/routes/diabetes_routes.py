import os
import json
import joblib 
import sqlite3
from flask import Blueprint, request, jsonify
from .db_utils import get_db_connection

diabetes_bp = Blueprint('diabetes_bp', __name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'diabetes_model.pkl')
diabetes_model = None

def load_diagnostic_model():
    global diabetes_model
    try:
        if os.path.exists(MODEL_PATH):
            diabetes_model = joblib.load(MODEL_PATH)
            print("✅ Diabetes Model loaded successfully with Joblib!")
        else:
            print(f"❌ Model file not found at: {MODEL_PATH}")
    except Exception as e:
        print(f"❌ Error loading model with Joblib: {e}")
        try:
            import pickle
            with open(MODEL_PATH, 'rb') as f:
                diabetes_model = pickle.load(f)
            print("✅ Diabetes Model loaded successfully with Pickle (fallback)!")
        except Exception as e2:
            print(f"❌ Critical: All unpickling methods failed. {e2}")

load_diagnostic_model()


@diabetes_bp.route('/api/predict/diabetes', methods=['POST'])
def predict_diabetes():
    if diabetes_model is None:
        return jsonify({
            "status": "error", 
            "message": "AI Model is currently offline. Please check server logs."
        }), 500

    try:
        data = request.json
        features = [
            float(data.get('pregnancies', 0)),
            float(data.get('glucose', 0)),
            float(data.get('blood_pressure', 0)),
            float(data.get('skin_thickness', 0)),
            float(data.get('insulin', 0)),
            float(data.get('bmi', 0)),
            float(data.get('diabetes_pedigree_function', 0)),
            float(data.get('age', 0))
        ]
        prediction = diabetes_model.predict([features])[0]
        probabilities = diabetes_model.predict_proba([features])[0]
        prob = probabilities[prediction]

        result_text = "Diabetes Detected" if int(prediction) == 1 else "No Diabetes Detected"
        confidence_val = round(float(prob * 100), 2)
        user_email = data.get('user_email', 'Guest')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO DiabetesRecords (inputs_json, result, confidence)
            VALUES (?, ?, ?)
        ''', (json.dumps(data), result_text, confidence_val))
        
        diabetes_record_id = cursor.lastrowid
        cursor.execute('''
            INSERT INTO PredictionResults (user_email, disease_type, record_id)
            VALUES (?, ?, ?)
        ''', (user_email, 'Diabetes', diabetes_record_id))

        conn.commit()
        conn.close()
        return jsonify({
            "status": "success",
            "result": result_text,
            "confidence": confidence_val,
            "report_id": f"DX-{diabetes_record_id}-AI"
        }), 200

    except Exception as e:
        print(f"Prediction Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500




