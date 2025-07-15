import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("backend/model.pkl")  # ✅ Update path if needed

# 👉 Utility function: Predict salary category and probability
def predict_salary(data_dict):
    df = pd.DataFrame([data_dict])  # Convert input dictionary to DataFrame

    # Get predicted probability (probability of class 1, i.e., >50K)
    prob = model.predict_proba(df)[0][1]

    # Determine label based on threshold
    label = "Likely to earn > ₹50K" if prob >= 0.5 else "Likely to earn ≤ ₹50K"

    # Return both label and probability %
    return {
        "probability": round(prob * 100, 2),
        "label": label
    }

# 👉 Flask route: Handles POST requests from frontend
@app.route("/predict", methods=["POST"])
def predict_route():
    try:
        data = request.get_json()
        result = predict_salary(data)
        return jsonify(result)
    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)