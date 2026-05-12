import os
import json
import sqlite3
from flask import Blueprint, request, jsonify
from .db_utils import get_db_connection

reports_bp = Blueprint('reports_bp', __name__)

# -----------------------------
# Disease Configuration
# -----------------------------
DISEASE_TABLES = {
    "Diabetes": {
        "table": "DiabetesRecords",
        "prefix": "DIA"
    },
    "Kidney": {
        "table": "KidneyRecords",
        "prefix": "KID"
    },
    "Liver": {
        "table": "LiverRecords",
        "prefix": "LIV"
    }
}


# =====================================================
# GET ALL REPORTS
# =====================================================
@reports_bp.route('/api/reports/<user_email>', methods=['GET'])
def get_user_reports(user_email):

    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 5))
        offset = (page - 1) * limit

        conn = get_db_connection()
        cursor = conn.cursor()

        # Total reports count
        cursor.execute('''
            SELECT COUNT(*) as total
            FROM PredictionResults
            WHERE user_email = ?
        ''', (user_email,))

        total_records = cursor.fetchone()['total']

        # Get all predictions
        cursor.execute('''
            SELECT *
            FROM PredictionResults
            WHERE user_email = ?
            ORDER BY created_at DESC
            LIMIT ? OFFSET ?
        ''', (user_email, limit, offset))

        prediction_rows = cursor.fetchall()

        reports = []

        for pr in prediction_rows:

            disease_type = pr['disease_type']
            record_id = pr['record_id']

            if disease_type not in DISEASE_TABLES:
                continue

            table_name = DISEASE_TABLES[disease_type]['table']
            prefix = DISEASE_TABLES[disease_type]['prefix']

            # Dynamic query
            query = f'''
                SELECT result, confidence, created_at
                FROM {table_name}
                WHERE id = ?
            '''

            cursor.execute(query, (record_id,))
            record = cursor.fetchone()

            if not record:
                continue

            status_str = record['result']

            color = (
                "text-emerald-500"
                if "No" in status_str
                else "text-red-500"
            )

            reports.append({
                "id": f"{prefix}-{record_id}-AI",
                "type": f"{disease_type} Analysis",
                "date": record['created_at'],
                "status": status_str,
                "statusColor": color,
                "summary": f"AI Prediction with {record['confidence']}% confidence based on clinical data."
            })

        conn.close()

        total_pages = (total_records + limit - 1) // limit

        return jsonify({
            "reports": reports,
            "pagination": {
                "total": total_records,
                "page": page,
                "limit": limit,
                "pages": total_pages
            }
        }), 200

    except Exception as e:
        print(f"Error fetching reports: {e}")
        return jsonify({"error": str(e)}), 500


# =====================================================
# GET SINGLE REPORT DETAILS
# =====================================================
@reports_bp.route('/api/report-details/<report_code>', methods=['GET'])
def get_report_details(report_code):

    try:

        # Example:
        # DIA-1-AI
        # KID-5-AI
        # LIV-2-AI

        prefix = report_code.split('-')[0]
        record_id = int(report_code.split('-')[1])

        disease_type = None

        for disease, config in DISEASE_TABLES.items():
            if config['prefix'] == prefix:
                disease_type = disease
                table_name = config['table']
                break

        if not disease_type:
            return jsonify({"error": "Invalid report code"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = f'''
            SELECT
                result,
                confidence,
                created_at,
                inputs_json
            FROM {table_name}
            WHERE id = ?
        '''

        cursor.execute(query, (record_id,))
        row = cursor.fetchone()

        conn.close()

        if not row:
            return jsonify({"error": "Report not found"}), 404

        return jsonify({
            "id": report_code,
            "type": disease_type,
            "result": row['result'],
            "confidence": row['confidence'],
            "date": row['created_at'],
            "formData": json.loads(row['inputs_json'])
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =====================================================
# DISEASE TRENDS
# =====================================================
@reports_bp.route('/api/trends/<disease_type>/<user_email>', methods=['GET'])
def get_disease_trends(disease_type, user_email):

    try:

        disease_type = disease_type.capitalize()

        if disease_type not in DISEASE_TABLES:
            return jsonify({
                "error": "Unsupported disease type"
            }), 400

        table_name = DISEASE_TABLES[disease_type]['table']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = f'''
            SELECT t.inputs_json, t.created_at
            FROM PredictionResults pr
            JOIN {table_name} t
            ON pr.record_id = t.id
            WHERE pr.user_email = ?
            AND pr.disease_type = ?
            ORDER BY t.created_at DESC
            LIMIT 2
        '''

        cursor.execute(query, (user_email, disease_type))
        rows = cursor.fetchall()

        conn.close()

        if len(rows) < 1:
            return jsonify({
                "status": "empty",
                "message": "Not enough data"
            }), 200

        latest = json.loads(rows[0]['inputs_json'])
        previous = (
            json.loads(rows[1]['inputs_json'])
            if len(rows) > 1
            else latest
        )

        markers_map = {

            "Diabetes": [
                {"name": "Glucose", "key": "glucose", "unit": "mg/dL"},
                {"name": "BMI", "key": "bmi", "unit": "kg/m²"},
                {"name": "Blood Pressure", "key": "blood_pressure", "unit": "mmHg"},
                {"name": "Insulin", "key": "insulin", "unit": "mu U/ml"}
            ],

            "Kidney": [
                {"name": "Blood Pressure", "key": "blood_pressure", "unit": "mmHg"},
                {"name": "Blood Urea", "key": "blood_urea", "unit": "mg/dL"},
                {"name": "Serum Creatinine", "key": "serum_creatinine", "unit": "mg/dL"},
                {"name": "Sodium", "key": "sodium", "unit": "mEq/L"},
                {"name": "Potassium", "key": "potassium", "unit": "mEq/L"}
            ],

            "Liver": [
                {"name": "Total Bilirubin", "key": "total_bilirubin", "unit": "mg/dL"},
                {"name": "Direct Bilirubin", "key": "direct_bilirubin", "unit": "mg/dL"},
                {"name": "Alkaline Phosphatase", "key": "alkaline_phosphatase", "unit": "IU/L"},
                {"name": "ALT", "key": "alamine_aminotransferase", "unit": "IU/L"},
                {"name": "AST", "key": "aspartate_aminotransferase", "unit": "IU/L"}
            ]
        }

        markers = markers_map[disease_type]

        trends = []

        for m in markers:

            curr_val = float(latest.get(m['key'], 0))
            prev_val = float(previous.get(m['key'], 0))

            if curr_val < prev_val:
                status = "improved"
            elif curr_val > prev_val:
                status = "increased"
            else:
                status = "stable"

            trends.append({
                "name": m['name'],
                "current": str(curr_val),
                "previous": str(prev_val),
                "unit": m['unit'],
                "status": status
            })

        return jsonify({
            "title": f"{disease_type} Trends",
            "params": trends
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500