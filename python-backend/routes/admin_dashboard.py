from flask import Blueprint, jsonify
from .db_utils import get_db_connection

admin_dashboard_bp = Blueprint(
    "admin_dashboard_bp",
    __name__
)

@admin_dashboard_bp.route(
    "/api/admin/dashboard",
    methods=["GET"]
)
def get_admin_dashboard():

    try:

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) as total FROM users"
        )
        total_users = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COUNT(*) as total FROM hospitals"
        )
        total_hospitals = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COUNT(*) as total FROM doctors"
        )
        total_doctors = cursor.fetchone()["total"]
        cursor.execute("""
            SELECT
                id,
                name,
                email,
                created_at
            FROM users
            ORDER BY created_at DESC
            LIMIT 3
        """)

        users = cursor.fetchall()
        cursor.execute("""
            SELECT
                user_email,
                disease_type,
                created_at
            FROM PredictionResults
            ORDER BY created_at DESC
            LIMIT 3
        """)

        predictions = cursor.fetchall()
        activity = []
        for user in users:
            activity.append({
                "type": "user_registered",
                "title": "New User Registered",
                "subtitle": user["email"],
                "time": user["created_at"],
                "icon": "lucide:user-plus",
                "color": "text-blue-500"
            })
        for prediction in predictions:
            activity.append({
                "type": "prediction",
                "title": f"{prediction['disease_type']} Prediction",
                "subtitle": prediction["user_email"],
                "time": prediction["created_at"],
                "icon": "lucide:brain-circuit",
                "color": "text-emerald-500"
            })
        activity.sort(
            key=lambda x: x["time"],
            reverse=True
        )

        conn.close()

        return jsonify({
            "metrics": {
                "users": total_users,
                "hospitals": total_hospitals,
                "doctors": total_doctors
            },

            "activity": activity[:8]
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

@admin_dashboard_bp.route(
    "/api/admin/system-analytics",
    methods=["GET"]
)
def get_system_analytics():

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                id,
                user_email,
                disease_type,
                record_id,
                created_at
            FROM PredictionResults
            ORDER BY created_at DESC
        """)

        predictions = cursor.fetchall()

        total_predictions = len(predictions)
        def fetch_confidence(table, record_id):
            try:
                cursor.execute(f"""
                    SELECT confidence
                    FROM {table}
                    WHERE id = ?
                """, (record_id,))
                row = cursor.fetchone()
                return float(row["confidence"]) if row else 0
            except:
                return 0

        diabetes_count = 0
        kidney_count = 0
        liver_count = 0
        confidence_sum = 0
        confidence_count = 0
        activity_map = {}
        confidence_trend = []
        recent_confidence = []

        for p in predictions:

            disease = p["disease_type"]
            record_id = p["record_id"]
            date = p["created_at"]

            if disease == "Diabetes":
                diabetes_count += 1
                table = "DiabetesRecords"
            elif disease == "Kidney":
                kidney_count += 1
                table = "KidneyRecords"
            elif disease == "Liver":
                liver_count += 1
                table = "LiverRecords"
            else:
                continue
            conf = fetch_confidence(table, record_id)

            confidence_sum += conf
            confidence_count += 1
            recent_confidence.append(conf)
            day = str(date).split(" ")[0]
            activity_map[day] = activity_map.get(day, 0) + 1

        conn.close()
        avg_confidence = (
            confidence_sum / confidence_count
            if confidence_count else 0
        )

        confidence_trend = recent_confidence[:6]
        activity = [
            {"date": k, "count": v}
            for k, v in activity_map.items()
        ]
        activity.sort(key=lambda x: x["date"])
        return jsonify({
            "stats": {
                "total_predictions": total_predictions,
                "diabetes": diabetes_count,
                "kidney": kidney_count,
                "liver": liver_count,
                "avg_confidence": round(avg_confidence, 2)
            },

            "charts": {
                "disease_distribution": {
                    "labels": ["Diabetes", "Kidney", "Liver"],
                    "data": [
                        diabetes_count,
                        kidney_count,
                        liver_count
                    ]
                },

                "confidence_trend": confidence_trend,

                "activity": activity
            }
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500