import os
import json
import joblib 
import sqlite3
from flask import Blueprint, request, jsonify
from .db_utils import get_db_connection

reports_bp = Blueprint('reports_bp', __name__)




@reports_bp.route('/api/reports/<user_email>', methods=['GET'])
def get_user_reports(user_email):
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 5))
        offset = (page - 1) * limit

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT COUNT(*) as total
            FROM PredictionResults
            WHERE user_email = ?
        ''', (user_email,))
        total_records = cursor.fetchone()['total']
        query = '''
            SELECT 
                pr.record_id as id,
                pr.disease_type as type,
                dr.result as status,
                dr.confidence,
                dr.created_at as date,
                dr.inputs_json
            FROM PredictionResults pr
            JOIN DiabetesRecords dr ON pr.record_id = dr.id
            WHERE pr.user_email = ?
            ORDER BY dr.created_at DESC
            LIMIT ? OFFSET ?
        '''
        
        cursor.execute(query, (user_email, limit, offset))
        rows = cursor.fetchall()
        conn.close()

        reports = []
        for row in rows:
            status_str = row['status']
            color = "text-emerald-500" if "No Diabetes" in status_str else "text-red-500"
            
            reports.append({
                "id": f"DX-{row['id']}-AI",
                "type": f"{row['type']} Analysis",
                "date": row['date'],
                "status": status_str,
                "statusColor": color,
                "summary": f"AI Prediction with {row['confidence']}% confidence based on clinical data."
            })
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


@reports_bp.route('/api/report-details/<int:report_id>', methods=['GET'])
def get_report_details(report_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = '''
            SELECT 
                pr.disease_type,
                dr.result,
                dr.confidence,
                dr.created_at,
                dr.inputs_json
            FROM PredictionResults pr
            JOIN DiabetesRecords dr ON pr.record_id = dr.id
            WHERE dr.id = ?
        '''
        cursor.execute(query, (report_id,))
        row = cursor.fetchone()
        conn.close()

        if not row:
            return jsonify({"error": "Report not found"}), 404
        return jsonify({
            "id": f"DX-{report_id}-AI",
            "type": row['disease_type'],
            "result": row['result'],
            "confidence": row['confidence'],
            "date": row['created_at'],
            "formData": json.loads(row['inputs_json'])
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@reports_bp.route('/api/trends/diabetes/<user_email>', methods=['GET'])
def get_diabetes_trends(user_email):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT dr.inputs_json, dr.created_at
            FROM PredictionResults pr
            JOIN DiabetesRecords dr ON pr.record_id = dr.id
            WHERE pr.user_email = ? AND pr.disease_type = 'Diabetes'
            ORDER BY dr.created_at DESC
            LIMIT 2
        '''
        cursor.execute(query, (user_email,))
        rows = cursor.fetchall()
        conn.close()

        if len(rows) < 1:
            return jsonify({"status": "empty", "message": "Not enough data"}), 200
        latest = json.loads(rows[0]['inputs_json'])
        previous = json.loads(rows[1]['inputs_json']) if len(rows) > 1 else latest
        markers = [
            {"name": "Glucose", "key": "glucose", "unit": "mg/dL"},
            {"name": "BMI", "key": "bmi", "unit": "kg/m²"},
            {"name": "Blood Pressure", "key": "blood_pressure", "unit": "mmHg"},
            {"name": "Insulin", "key": "insulin", "unit": "mu U/ml"}
        ]
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
            "title": "Diabetes Control",
            "icon": "ph:drop-bold",
            "params": trends
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500