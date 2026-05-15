import os
import json
import joblib
from flask import Blueprint, request, jsonify
from .db_utils import get_db_connection

kidney_bp = Blueprint('kidney_bp', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'kidney_model.pkl')

kidney_model = None

def load_kidney_model():
    global kidney_model

    try:
        if os.path.exists(MODEL_PATH):
            kidney_model = joblib.load(MODEL_PATH)
            print("✅ Kidney model loaded!")
        else:
            print("❌ Kidney model missing!")

    except Exception as e:
        print(f"❌ Kidney model error: {e}")

load_kidney_model()


@kidney_bp.route('/api/predict/kidney', methods=['POST'])
def predict_kidney():

    if kidney_model is None:
        return jsonify({
            "status": "error",
            "message": "Kidney AI model offline."
        }), 500

    try:
        data = request.json
        def encode_category(val, true_condition):
            return 1.0 if str(val).lower() == true_condition.lower() else 0.0
        features = [
            float(data.get('age', 0)),
            float(data.get('blood_pressure', 0)),
            float(data.get('specific_gravity', 1.020)),
            float(data.get('albumin', 0)),
            float(data.get('sugar', 0)),
            encode_category(data.get('red_blood_cells', 'normal'), 'abnormal'),
            encode_category(data.get('pus_cell', 'normal'), 'abnormal'),
            encode_category(data.get('pus_cell_clumps', 'notpresent'), 'present'),
            encode_category(data.get('bacteria', 'notpresent'), 'present'),
            float(data.get('blood_glucose_random', 0)),
            float(data.get('blood_urea', 0)),
            float(data.get('serum_creatinine', 0)),
            float(data.get('sodium', 0)),
            float(data.get('potassium', 0)),
            float(data.get('haemoglobin', 0)),
            float(data.get('packed_cell_volume', 0)),
            float(data.get('white_blood_cell_count', 0)),
            float(data.get('red_blood_cell_count', 0)),
            encode_category(data.get('hypertension', 'no'), 'yes'),
            encode_category(data.get('diabetes_mellitus', 'no'), 'yes'),
            encode_category(data.get('coronary_artery_disease', 'no'), 'yes'),
            encode_category(data.get('appetite', 'good'), 'poor'),
            encode_category(data.get('peda_edema', 'no'), 'yes'),
            encode_category(data.get('aanemia', 'no'), 'yes')
        ]
        prediction = kidney_model.predict([features])[0]
        probabilities = kidney_model.predict_proba([features])[0]
        prob = probabilities[prediction]
        
        result_text = (
            "Kidney Disease Detected"
            if int(prediction) == 1
            else "No Kidney Disease Detected"
        )
        confidence_val = round(float(prob * 100), 2)
        user_email = data.get('user_email', 'Guest')
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO KidneyRecords
            (inputs_json, result, confidence)
            VALUES (?, ?, ?)
        ''', (
            json.dumps(data),
            result_text,
            confidence_val
        ))

        kidney_record_id = cursor.lastrowid
        
        cursor.execute('''
            INSERT INTO PredictionResults
            (user_email, disease_type, record_id)
            VALUES (?, ?, ?)
        ''', (
            user_email,
            'Kidney',
            kidney_record_id
        ))
        prediction_result_id = cursor.lastrowid
        conn.commit()
        conn.close()
    
        return jsonify({
            "status": "success",
            "result": result_text,
            "confidence": confidence_val,
            "report_id": prediction_result_id
        }), 200

    except Exception as e:
        print("Kidney Prediction Error:", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500