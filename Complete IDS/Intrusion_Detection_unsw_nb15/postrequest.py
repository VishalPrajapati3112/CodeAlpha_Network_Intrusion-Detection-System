import requests

url = 'http://127.0.0.1:5000/predict'

data = {
  "dmeansz": 100.0,
  "sloss": 3,
  "Sjit": 5.2,
  "Dpkts": 12,
  "Sload": 312456.0,
  "Djit": 4.3,
  "Sintpkt": 0.002,
  "Spkts": 18,
  "ct_state_ttl": 31,
  "Dintpkt": 0.003,
  "sbytes": 9500,
  "tcprtt": 0.001
}

response = requests.post(url, json=data)
print("Response:", response.json())
