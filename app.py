from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the full pipeline (preprocessing + model)
PIPELINE_PATH = "cnc_operator_pipeline.pkl"
with open(PIPELINE_PATH, 'rb') as f:
    model_pipeline = pickle.load(f)

@app.route('/')
def home():
    return "CNC Operator ML Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400

        # Convert to DataFrame (single row)
        df = pd.DataFrame([data])

        # Predict
        prediction = model_pipeline.predict(df)[0]  # take first element for single row

        # Predict probability if classifier supports it
        if hasattr(model_pipeline, "predict_proba"):
            proba = model_pipeline.predict_proba(df)[0].max()  # highest class probability
        else:
            proba = None

        # Return simplified JSON
        return jsonify({
            'prediction': prediction,
            'efficiency': proba
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Make accessible externally
    app.run(host='0.0.0.0', port=5000)
