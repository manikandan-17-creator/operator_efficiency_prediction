from flask import Flask, render_template_string
import requests
from sample_data import sample_datasets

app = Flask(__name__)
ML_API_URL = "https://operator-efficiency-prediction.onrender.com/predict"

@app.route("/")
def home():
    results = []
    for dataset in sample_datasets:
        try:
            response = requests.post(ML_API_URL, json=dataset["data"])
            result = response.json()
            results.append({
                "name": dataset["name"],
                "prediction": result.get("prediction", "N/A"),
                "efficiency": result.get("efficiency", "N/A")
            })
        except Exception as e:
            results.append({
                "name": dataset["name"],
                "prediction": "Error",
                "efficiency": str(e)
            })

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Operator Efficiency Predictions</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f9; padding: 40px; }
            h2 { text-align: center; color: #333; }
            .grid { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }
            .card { background: white; padding: 20px; border-radius: 8px;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.2); width: 280px; }
            .name { font-weight: bold; margin-bottom: 10px; }
            .prediction { margin-top: 5px; }
            .efficiency { color: #4CAF50; font-weight: bold; }
        </style>
    </head>
    <body>
        <h2>Operator Efficiency Predictions</h2>
        <div class="grid">
            {% for r in results %}
            <div class="card">
                <div class="name">{{ r.name }}</div>
                <div class="prediction">SKill Level: <b>{{ r.prediction }}</b></div>
                <div class="prediction">Efficiency Score: <span class="efficiency">{{ r.efficiency }}</span></div>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, results=results)

if __name__ == "__main__":
    app.run(debug=True)
