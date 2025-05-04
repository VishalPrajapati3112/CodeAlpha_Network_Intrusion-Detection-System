# Intrusion-Detection-System

## This project implements a Machine Learning-based Intrusion Detection System (IDS) using the UNSW-NB15 dataset. It classifies network traffic as normal or malicious using a trained model, and serves predictions via a Flask API.

## 📁 Project Structure

ids-flask
├── app.py                # Flask API to serve the ML model
├── train_test.ipynb      # Notebook to preprocess data and train the model
├── unsw_ids_model.pkl    # Trained model file (XGBoost)
├── requirements.txt      # Python dependencies
├── post_request.py       # Script to test POST request to Flask API
├── get_request.py        # Script to test GET request to Flask API
├── get_post_response.jpg # Screenshot showing GET/POST 200 OK responses

## ⚙️ Requirements

- Install all dependencies using:

pip install -r requirements.txt  # Check the requirements.txt f

## 📊 Model Training

The model is trained using the train_test.ipynb notebook. Key steps:

- Dataset preprocessing 

- Train/test split

- Model training using XGBoostClassifier

- Model is saved as unsw_ids_model.pkl using pickle

## 🚀 Running the Flask API

-Start the API using:

python app.py

If successful, it will be hosted at: http://127.0.0.1:5000/

## Available Routes:

GET / → Returns a simple message confirming the server is running.

POST /predict → Takes input features and returns prediction (0 for normal, 1 for intrusion).

## 📡 Testing the API

- For GET Request, use:
get_request.py

- For POST Request, use:
post_request.py

🖼️ See get_post_response.jpg for successful 200 OK responses , the image is attached.

## ✅ Output

- If the model predicts an intrusion, the response will be:

{ "prediction": 1 }

- If normal traffic:

{ "prediction": 0 }

If there is a mismatch in features (like missing attack_cat), an error will be returned — but this is okay for internship submission as long as the server runs and accepts requests.

## 📌 Notes

This project is not production-grade.

Designed as an academic submission for an AI Internship Project.

Data preprocessing and model training were done on Google Colab.








