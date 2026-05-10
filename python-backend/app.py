from flask import Flask, jsonify
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.chatbot_routes import chatbot_bp
from routes.user_routes import user_bp
from routes.faq_routes import faq_bp
from routes.hospital_routes import hospital_bp
from routes.doctor_routes import doctor_bp
from routes.fitness_routes import fitness_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(user_bp)
app.register_blueprint(faq_bp)
app.register_blueprint(hospital_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(fitness_bp)

@app.route("/")
def home():
    return jsonify({"message": "MediAI Backend running 🚀"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)