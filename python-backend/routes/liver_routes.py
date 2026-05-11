
import os
import json
import joblib
from flask import Blueprint, request, jsonify
from .db_utils import get_db_connection

liver_bp = Blueprint('liver_bp', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'liver_model.pkl')

liver_model = None


def load_liver_model():
    global liver_model

    try:
        if os.path.exists(MODEL_PATH):
            liver_model = joblib.load(MODEL_PATH)
            print("✅ Liver model loaded!")
        else:
            print("❌ Liver model missing!")

    except Exception as e:
        print(f"❌ Liver model error: {e}")

load_liver_model()


@liver_bp.route('/api/predict/liver', methods=['POST'])
def predict_liver():

    if liver_model is None:
        return jsonify({
            "status": "error",
            "message": "Liver AI model offline."
        }), 500

    try:
        data = request.json
        features = [
            float(data.get('age', 0)),
            float(data.get('gender', 0)),
            float(data.get('total_bilirubin', 0)),
            float(data.get('direct_bilirubin', 0)),
            float(data.get('alkaline_phosphatase', 0)),
            float(data.get('alamine_aminotransferase', 0)),
            float(data.get('aspartate_aminotransferase', 0)),
            float(data.get('total_proteins', 0)),
            float(data.get('albumin', 0)),
            float(data.get('albumin_and_globulin_ratio', 0))
        ]

        prediction = liver_model.predict([features])[0]
        probabilities = liver_model.predict_proba([features])[0]
        prob = probabilities[prediction]
        result_text = (
            "Liver Disease Detected"
            if int(prediction) == 1
            else "No Liver Disease Detected"
        )

        confidence_val = round(float(prob * 100), 2)

        user_email = data.get('user_email', 'Guest')

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO LiverRecords
            (inputs_json, result, confidence)
            VALUES (?, ?, ?)
        ''', (
            json.dumps(data),
            result_text,
            confidence_val
        ))

        liver_record_id = cursor.lastrowid

        cursor.execute('''
            INSERT INTO PredictionResults
            (user_email, disease_type, record_id)
            VALUES (?, ?, ?)
        ''', (
            user_email,
            'Liver',
            liver_record_id
        ))

        conn.commit()
        conn.close()

        return jsonify({
            "status": "success",
            "result": result_text,
            "confidence": confidence_val,
            "report_id": f"LIV-{liver_record_id}-AI"
        }), 200

    except Exception as e:
        print("Liver Prediction Error:", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500