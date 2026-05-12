from flask import Flask, jsonify
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.chatbot_routes import chatbot_bp
from routes.user_routes import user_bp
from routes.faq_routes import faq_bp
from routes.hospital_routes import hospital_bp
from routes.doctor_routes import doctor_bp
from routes.fitness_routes import fitness_bp
from routes.diabetes_routes import diabetes_bp
from routes.liver_routes import liver_bp
from routes.kidney_routes import kidney_bp
from routes.report_routes import reports_bp
from routes.admin_dashboard import admin_dashboard_bp
from routes.user_settings_routes import user_settings_bp


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(user_bp)
app.register_blueprint(faq_bp)
app.register_blueprint(hospital_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(fitness_bp)
app.register_blueprint(diabetes_bp)
app.register_blueprint(liver_bp)
app.register_blueprint(kidney_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(admin_dashboard_bp)
app.register_blueprint(user_settings_bp)


@app.route("/")
def home():
    return jsonify({"message": "MediAI Backend running 🚀"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)