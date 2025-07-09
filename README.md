🚨 Intrusion Detection System (IDS) 


📌 Project Title:
Machine Learning-Based Network Intrusion Detection System.

💭 Problem Statement:
Today’s networks are highly vulnerable to cyber-attacks. Traditional signature-based IDS often fail to detect new or unknown threats. The goal of this project is to create a machine learning-based IDS that detects both known and unknown malicious activity from network traffic data using supervised learning techniques.

✅ Solution Overview:
Used the UNSW-NB15 dataset which contains real network traffic.

Selected the most important features related to attack patterns.

Trained a machine learning model to classify traffic as normal or intrusion.

Deployed the model using a Flask API, allowing predictions via HTTP requests.

Tested the API using simple scripts with sample input.

🔧 Tools and Technologies Used:
Python – for development

Pandas, NumPy – for data preprocessing

Scikit-learn – for training and evaluating models

XGBoost & Logistic Regression – machine learning algorithms

Flask – to deploy the model as an API

Google Colab & VS Code – for training and development

Joblib/Pickle – to save the trained model and scaler

📈 Project Workflow (Simplified Steps):
Dataset Preparation

Loaded the UNSW-NB15 dataset

Cleaned and selected relevant features

Encoded categorical columns

Scaled the data

Model Training

Trained the model using supervised classification

Achieved high accuracy (~95%)

Saved the model and scaler

API Development

Created a Flask server

Added two endpoints:

One to check if API is running

One to receive data and return prediction

Testing

Sent sample data using test scripts

API responded with prediction: 0 for normal, 1 for attack

Output

Prediction results confirmed

Output screenshot attached (output.png)

📊 Results:
Model Accuracy: 95%

Precision/Recall: High for both normal and intrusion classes

API Response: Real-time prediction of incoming traffic data

🚀 Future Enhancements:
Add a graphical dashboard (e.g., using Streamlit)

Deploy API on cloud (Heroku, AWS)

Implement auto-response to detected threats

Explore deep learning for more accurate results

Integrate with real network traffic monitoring systems

📎 References:
UNSW-NB15 Dataset by University of New South Wales

XGBoost Documentation

Scikit-learn & Flask Documentation
