from flask import Flask, jsonify, request  # Added 'request' here
from flask_cors import CORS
import os
# This line connects your chatbot.py functions to the API
from chatbot import predict_disease, get_recommendations 

app = Flask(__name__)

# Standardize CORS to allow your Nuxt app to talk to Flask
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
        
        # Call the functions from chatbot.py
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
    # Ensure this matches the port your Nuxt app is calling (5001)
    app.run(debug=True, port=5001)