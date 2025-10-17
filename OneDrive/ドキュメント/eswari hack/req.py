import requests

url = "https://operator-efficiency-prediction.onrender.com/predict"
data = {
    "operator_id":"OP01",
    "machine_id":"MC01",
    "program_id":"PG01",
    "part_type":"TypeA",
    "shift":"Morning",
    "setup_time_seconds":1200,
    "setup_rework_count":2,
    "offset_stability":0.8,
    "cycle_time_actual_seconds":85,
    "cycle_time_standard_seconds":90,
    "first_pass_yield":0.95,
    "scrap_rate_per_part":0.02,
    "rework_rate_per_part":0.01,
    "alarm_count":3,
    "alarm_duration_seconds":45,
    "downtime_operator_related_seconds":30,
    "PPE_compliance_score":0.9,
    "safe_start_stop_compliance":1.0,
    "incident_count":0,
    "data_completeness_score":0.95,
    "missing_fields_count":1,
    "parameter_adjustments_within_limits":1,
    "stability_after_changes":0.85,
    "improvements_implemented":2,
    "improvement_impact_score":0.8
}

response = requests.post(url, json=data)

try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not JSON. Here is the raw response:")
    print(response.text)
