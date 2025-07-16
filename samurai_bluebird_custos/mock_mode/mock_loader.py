# samurai_bluebird_custos/mock_mode/mock_loader.py

import json
import time
import os

def load_simulated_workday(file_path="samurai_bluebird_custos/mock_mode/simulated_workday.json"):
    """Load simulated workday JSON data."""
    if not os.path.exists(file_path):
        print("⚠️ Simulated workday file not found.")
        return []
    with open(file_path, "r") as f:
        return json.load(f)

def run_simulated_workday():
    """Run through simulated workday inputs with delays."""
    workday = load_simulated_workday()
    if not workday:
        print("⚠️ No simulated data to run.")
        return
    for entry in workday:
        print(f"Simulated Input: {entry}")
        time.sleep(1)  # Delay to simulate time between inputs
