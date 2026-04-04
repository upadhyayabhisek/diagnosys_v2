from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# In your Flask app
CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

@app.route("/")
def home():
    return jsonify({"message": "Flask backend running 🚀"})

@app.route("/print")
def print_api():
    print("Nuxt frontend hit this endpoint!")
    print("---------------------------------")
    return jsonify({"status": "printed in backend"})

if __name__ == "__main__":
        app.run(debug=True, port=5001)