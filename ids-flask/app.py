from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the trained model
with open('unsw_ids_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

# List of features used in training (44 features total)
FEATURES = ['id', 'dur', 'proto', 'service', 'state', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate',
            'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss', 'sinpkt', 'dinpkt', 'sjit', 'djit',
            'swin', 'stcpb', 'dtcpb', 'dwin', 'tcprtt', 'synack', 'ackdat', 'smean', 'dmean',
            'trans_depth', 'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm',
            'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'is_ftp_login', 'ct_ftp_cmd',
            'ct_flw_http_mthd', 'ct_src_ltm', 'ct_srv_dst', 'is_sm_ips_ports']


@app.route('/')
def home():
    return "✅ IDS Flask API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Safely prepare input features, filling missing ones with 0
        input_data = {feature: data.get(feature, 0) for feature in FEATURES}
        input_df = pd.DataFrame([input_data])

        # Reorder columns to ensure correct model input format
        input_df = input_df[FEATURES]

        # Predict
        prediction = model.predict(input_df)[0]

        return jsonify({
            'prediction': int(prediction)  # Convert NumPy int64 to native int
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
