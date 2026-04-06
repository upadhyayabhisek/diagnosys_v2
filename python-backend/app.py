from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from chatbot import predict_disease, get_recommendations 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return jsonify({"message": "MediAI Backend running 🚀"})

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

if __name__ == "__main__":
    app.run(debug=True, port=5001)