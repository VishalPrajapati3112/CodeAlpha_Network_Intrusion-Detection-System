from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/", methods=["GET"])
def home():
    return "Intrusion Detection API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    required_features = ['dmeansz', 'sloss', 'Sjit', 'Dpkts', 'Sload', 'Djit', 
                         'Sintpkt', 'Spkts', 'ct_state_ttl', 'Dintpkt', 'sbytes', 'tcprtt']
    
    features = np.array([[data[feat] for feat in required_features]])
    features = scaler.transform(features)
    
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
