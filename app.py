from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the full pipeline (preprocess + model)
with open('cnc_operator_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "CNC Operator ML Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Expecting a dictionary of feature_name: value
        df = pd.DataFrame([data])
        prediction = model.predict(df)

        # For classification, you might also want probabilities
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df).tolist()
        else:
            proba = None

        return jsonify({'prediction': prediction.tolist(), 'probabilities': proba.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
