# resonance_logger.py

import json
import os
from datetime import datetime

def write_output_logs(narrative, symbolic_data, meaning_map):
    timestamp = datetime.utcnow().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "narrative": narrative,
        "symbolic": symbolic_data,
        "meaning_map": meaning_map
    }
    os.makedirs("logs", exist_ok=True)
    with open("logs/output_resonance_log.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def verify_and_log(system_state):
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "system_state": system_state
    }
    os.makedirs("logs", exist_ok=True)
    with open("logs/dashboard_log.txt", "a") as f:
        f.write(json.dumps(entry) + "\n")
