import os
import json
from datetime import datetime

BATCH_DIR = "batches"

def ensure_day_folder():
    """
    Ensure today's yyyy-mm-dd folder exists in batches directory.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join(BATCH_DIR, today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def save_batch(feather_input):
    """
    Save the feather_input dict as a JSON batch file.
    """
    folder_path = ensure_day_folder()
    timestamp = datetime.now().strftime("session_%H-%M.json")
    file_path = os.path.join(folder_path, timestamp)
    with open(file_path, "w") as f:
        json.dump(feather_input, f, indent=4)
    print(f"Batch saved: {file_path}")

def get_recent_batches(count=6):
    """
    Retrieve last N batches for meta-pattern processing.
    """
    folder_path = ensure_day_folder()
    all_batches = sorted(os.listdir(folder_path))
    recent_batches = all_batches[-count:]
    batch_data = []
    for batch_file in recent_batches:
        file_path = os.path.join(folder_path, batch_file)
        with open(file_path, "r") as f:
            batch_data.append(json.load(f))
    return batch_data
