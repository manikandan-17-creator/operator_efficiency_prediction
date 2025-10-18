import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import pickle

# -----------------------------
# 1. Generate synthetic dataset
# -----------------------------
np.random.seed(42)

n_samples = 300

data = {
    "operator_id": np.random.choice(["OP01", "OP02", "OP03"], n_samples),
    "machine_id": np.random.choice(["MC01", "MC02", "MC03"], n_samples),
    "program_id": np.random.choice(["PG01", "PG02", "PG03"], n_samples),
    "part_type": np.random.choice(["TypeA", "TypeB", "TypeC"], n_samples),
    "shift": np.random.choice(["Morning", "Afternoon", "Night"], n_samples),
    "setup_time_seconds": np.random.randint(500, 5000, n_samples),
    "setup_rework_count": np.random.randint(0, 10, n_samples),
    "offset_stability": np.random.rand(n_samples),
    "cycle_time_actual_seconds": np.random.randint(60, 200, n_samples),
    "cycle_time_standard_seconds": np.random.randint(70, 150, n_samples),
    "first_pass_yield": np.random.rand(n_samples),
    "scrap_rate_per_part": np.random.rand(n_samples),
    "rework_rate_per_part": np.random.rand(n_samples),
    "alarm_count": np.random.randint(0, 20, n_samples),
    "alarm_duration_seconds": np.random.randint(0, 500, n_samples),
    "downtime_operator_related_seconds": np.random.randint(0, 300, n_samples),
    "PPE_compliance_score": np.random.rand(n_samples),
    "safe_start_stop_compliance": np.random.rand(n_samples),
    "incident_count": np.random.randint(0, 5, n_samples),
    "data_completeness_score": np.random.rand(n_samples),
    "missing_fields_count": np.random.randint(0, 5, n_samples),
    "parameter_adjustments_within_limits": np.random.randint(0, 2, n_samples),
    "stability_after_changes": np.random.rand(n_samples),
    "improvements_implemented": np.random.randint(0, 5, n_samples),
    "improvement_impact_score": np.random.rand(n_samples),
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Create synthetic labels
# -----------------------------
# Simple rule: bad quality → low, average → medium, good → high
conditions = []
for i in range(n_samples):
    if df.loc[i, "first_pass_yield"] < 0.4 or df.loc[i, "scrap_rate_per_part"] > 0.4:
        conditions.append("low")
    elif df.loc[i, "first_pass_yield"] > 0.8 and df.loc[i, "scrap_rate_per_part"] < 0.1:
        conditions.append("high")
    else:
        conditions.append("medium")

df["target"] = conditions

# -----------------------------
# 3. Build pipeline
# -----------------------------
categorical = ["operator_id", "machine_id", "program_id", "part_type", "shift"]
numeric = [col for col in df.columns if col not in categorical + ["target"]]

preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ("num", StandardScaler(), numeric),
    ]
)

clf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")

pipeline = Pipeline(steps=[("preprocess", preprocess), ("classifier", clf)])

# -----------------------------
# 4. Train and save
# -----------------------------
X = df.drop("target", axis=1)
y = df["target"]

pipeline.fit(X, y)

with open("cnc_operator_pipeline.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Demo model trained and saved as cnc_operator_pipeline.pkl")
