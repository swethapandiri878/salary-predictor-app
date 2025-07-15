from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
from backend.predict import predict_salary
import os

app = Flask(__name__)
CORS(app)

# Serve index.html
@app.route("/")
def home():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return render_template_string(f.read())

# Serve static CSS and JS files
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("frontend", filename)

@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        result = predict_salary(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)