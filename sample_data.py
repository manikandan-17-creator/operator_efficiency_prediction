# sample_data.py

sample_datasets = [
    # Normal case (baseline)
    {
        "name": "Operator A - Normal",
        "data": {
            "operator_id": "OP01",
            "machine_id": "MC01",
            "program_id": "PG01",
            "part_type": "TypeA",
            "shift": "Morning",
            "setup_time_seconds": 1200,
            "setup_rework_count": 2,
            "offset_stability": 0.8,
            "cycle_time_actual_seconds": 85,
            "cycle_time_standard_seconds": 90,
            "first_pass_yield": 0.95,
            "scrap_rate_per_part": 0.02,
            "rework_rate_per_part": 0.01,
            "alarm_count": 3,
            "alarm_duration_seconds": 45,
            "downtime_operator_related_seconds": 30,
            "PPE_compliance_score": 0.9,
            "safe_start_stop_compliance": 1.0,
            "incident_count": 0,
            "data_completeness_score": 0.95,
            "missing_fields_count": 1,
            "parameter_adjustments_within_limits": 1,
            "stability_after_changes": 0.85,
            "improvements_implemented": 2,
            "improvement_impact_score": 0.8
        }
    },

    # 🚨 Worst‑case: terrible quality, high scrap, many alarms
    {
        "name": "Operator B - Worst Case",
        "data": {
            "operator_id": "OP99",
            "machine_id": "MC99",
            "program_id": "PG99",
            "part_type": "TypeZ",
            "shift": "Night",
            "setup_time_seconds": 5000,
            "setup_rework_count": 20,
            "offset_stability": 0.1,
            "cycle_time_actual_seconds": 200,
            "cycle_time_standard_seconds": 80,
            "first_pass_yield": 0.2,
            "scrap_rate_per_part": 0.5,
            "rework_rate_per_part": 0.4,
            "alarm_count": 50,
            "alarm_duration_seconds": 1000,
            "downtime_operator_related_seconds": 800,
            "PPE_compliance_score": 0.2,
            "safe_start_stop_compliance": 0.0,
            "incident_count": 5,
            "data_completeness_score": 0.3,
            "missing_fields_count": 10,
            "parameter_adjustments_within_limits": 0,
            "stability_after_changes": 0.1,
            "improvements_implemented": 0,
            "improvement_impact_score": 0.0
        }
    },

    # 🌟 Best‑case: flawless operator, perfect compliance
    {
        "name": "Operator C - Best Case",
        "data": {
            "operator_id": "OP07",
            "machine_id": "MC07",
            "program_id": "PG07",
            "part_type": "TypeX",
            "shift": "Afternoon",
            "setup_time_seconds": 600,
            "setup_rework_count": 0,
            "offset_stability": 1.0,
            "cycle_time_actual_seconds": 70,
            "cycle_time_standard_seconds": 75,
            "first_pass_yield": 1.0,
            "scrap_rate_per_part": 0.0,
            "rework_rate_per_part": 0.0,
            "alarm_count": 0,
            "alarm_duration_seconds": 0,
            "downtime_operator_related_seconds": 0,
            "PPE_compliance_score": 1.0,
            "safe_start_stop_compliance": 1.0,
            "incident_count": 0,
            "data_completeness_score": 1.0,
            "missing_fields_count": 0,
            "parameter_adjustments_within_limits": 1,
            "stability_after_changes": 1.0,
            "improvements_implemented": 5,
            "improvement_impact_score": 1.0
        }
    }
]
