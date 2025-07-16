import os
from datetime import datetime

LOG_DIR = "logs"

def ensure_log_folder():
    """
    Ensure today's yyyy-mm-dd folder exists in logs directory.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join(LOG_DIR, today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def write_log(filename, content):
    """
    Write content to a log file.
    """
    folder_path = ensure_log_folder()
    file_path = os.path.join(folder_path, filename)
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(file_path, "a") as f:
        f.write(f"{timestamp} {content}\n")
    print(f"📜 Log updated: {file_path}")

def log_all(feather_input, meta_notes=""):
    """
    Write all 4 logs (input, dashboard, output, witness) and meta alerts.
    """
    write_log("input_resonance_log.txt", f"Passive Input: {feather_input}")
    write_log("dashboard_log.txt", "Tri-Agent: Narrative reflection placeholder.")
    write_log("output_resonance_log.txt", "12 Pillars: Reasoning alignment check placeholder.")
    write_log("witness_log.txt", f"Krishna: Oversight entry. {meta_notes}")

    if "critical" in meta_notes.lower():
        write_log("meta_alert.txt", "⚠️ Meta Alert: Critical pattern detected.")
