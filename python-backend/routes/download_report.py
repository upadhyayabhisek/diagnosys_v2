import os
import json
import sqlite3
from io import BytesIO
from flask import Blueprint, send_file, abort, current_app
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

report_bp = Blueprint('reports', __name__)

def get_db_connection():
    db_path = 'instance/mediai.db'
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@report_bp.route('/download_report/<int:report_id>')
def download_report(report_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT pr.disease_type, pr.record_id, u.name, u.email, u.gender, pr.created_at
            FROM PredictionResults pr
            JOIN users u ON pr.user_email = u.email
            WHERE pr.id = ?
        ''', (report_id,))

        report_meta = cursor.fetchone()
        if not report_meta:
            abort(404, description="Report record not found.")

        table_map = {
            "Kidney": "KidneyRecords",
            "Liver": "LiverRecords",
            "Diabetes": "DiabetesRecords"
        }
        
        disease_type = report_meta['disease_type']
        target_table = table_map.get(disease_type)
        
        if not target_table:
            abort(400, description="Invalid disease type in database.")

        cursor.execute(f'''
            SELECT inputs_json, result, confidence 
            FROM {target_table} 
            WHERE id = ?
        ''', (report_meta['record_id'],))
        
        details = cursor.fetchone()
        if not details:
            abort(404, description="Diagnostic details not found.")

        input_data = json.loads(details['inputs_json'])

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        y = height - 60

        try:
            logo_path = os.path.join(current_app.static_folder, 'images', 'diagn-sys-high-resolution-logo.png')
            #p.drawImage(logo_path, 50, y - 50, width=80, height=80, preserveAspectRatio=True)
        except Exception as e:
            print(f"Logo print error: {e}")

        y -= 80
        p.setFont("Helvetica-Bold", 20)
        p.drawCentredString(width / 2, y, "Clinical Analysis Report")
        y -= 50
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Patient Information")
        y -= 5
        p.line(50, y, width - 50, y)
        
        y -= 25
        p.setFont("Helvetica", 11)
        info_lines = [
            ("Name", report_meta['name']),
            ("Email", report_meta['email']),
            ("Gender", report_meta['gender'] or "N/A"),
            ("Date", report_meta['created_at'])
        ]
        for label, val in info_lines:
            p.setFont("Helvetica-Bold", 10)
            p.drawString(60, y, f"{label}:")
            p.setFont("Helvetica", 10)
            p.drawString(150, y, str(val))
            y -= 18

        y -= 15
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "AI Diagnosis Summary")
        y -= 5
        p.line(50, y, width - 50, y)
        
        y -= 25
        p.setFont("Helvetica-Bold", 11)
        p.drawString(60, y, "Disease Type:")
        p.setFont("Helvetica", 11)
        p.drawString(150, y, f"{disease_type} Analysis")
        y -= 20
        
        res_text = str(details['result'])
        if any(word in res_text.lower() for word in ['positive', 'detected', 'ckd', 'disease']):
            p.setFillColor(colors.red)
        else:
            p.setFillColor(colors.forestgreen)
            
        p.setFont("Helvetica-Bold", 12)
        p.drawString(60, y, "Final Result:")
        p.drawString(150, y, res_text.upper())
        
        p.setFillColor(colors.black)
        y -= 20
        p.setFont("Helvetica-Bold", 11)
        p.drawString(60, y, "Confidence:")
        p.setFont("Helvetica", 11)
        p.drawString(150, y, f"{details['confidence']}%")

        y -= 30
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "Analyzed Bio-Markers")
        y -= 5
        p.line(50, y, width - 50, y)
        y -= 20

        p.setFont("Helvetica", 10)
        for key, value in input_data.items():
            clean_key = key.replace('_', ' ').title()
            p.drawString(60, y, f"• {clean_key}:")
            p.drawRightString(width - 70, y, str(value))
            y -= 16
            if y < 80:
                p.showPage()
                y = height - 60
                p.setFont("Helvetica", 10)

        p.setFont("Helvetica-Oblique", 8)
        p.setFillColor(colors.grey)
        p.drawCentredString(width/2, 40, "Disclaimer: This AI-generated report is for informational purposes only.")
        p.drawCentredString(width/2, 30, "Please consult a medical professional for official diagnosis.")

        p.showPage()
        p.save()
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"Report_{disease_type}_{report_id}.pdf",
            mimetype='application/pdf'
        )

    except Exception as e:
        print(f"PDF Error: {str(e)}")
        abort(500)
    finally:
        conn.close()