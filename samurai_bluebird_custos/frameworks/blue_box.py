# samurai_bluebird_custos/frameworks/blue_box.py

import json
import os

class BlueBox:
    def __init__(self):
        print("🔷 BlueBox initialized.")
        self.sovereignties = self._load_dataset("frameworks/sovereignties_dataset.json")
        self.chakras = self._load_dataset("frameworks/chakra_definitions.json")
        self.context_domains = self._load_dataset("frameworks/context_domains.json")

    def _load_dataset(self, relative_path: str) -> dict:
        """
        Load a dataset JSON from the frameworks directory.
        """
        try:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            dataset_path = os.path.join(project_root, "samurai_bluebird_custos", relative_path)
            with open(dataset_path, "r", encoding="utf-8") as f:
                print(f"📦 Loaded dataset from {dataset_path}")
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️ Dataset not found: {relative_path}")
            return {}

    def process(self, batch_data: dict) -> dict:
        """
        Analyze behavioral patterns in batch_data and map to symbolic frameworks.
        Returns a rich meaning map for AMSCore.
        """
        print("🔷 BlueBox: Analyzing behavioral patterns...")

        # Extract features from batch
        keystroke_burst = batch_data.get("keystroke_burst", 0)
        cpu_usage = batch_data.get("cpu_usage", 0)
        memory_usage = batch_data.get("memory_usage", 0)
        active_window = batch_data.get("active_window", "").lower()
        screenshot_text = batch_data.get("screenshot_text", "").lower()

        # Initialize meaning map
        meaning_map = {
            "sovereignties": {},
            "chakras": {},
            "context_domains": {}
        }

        # --- Sovereignties Reasoning ---
        meaning_map["sovereignties"]["Flow"] = min(1.0, keystroke_burst / 50) if keystroke_burst > 20 and cpu_usage < 60 else 0.2
        meaning_map["sovereignties"]["Struggle"] = min(1.0, cpu_usage / 100) if cpu_usage > 70 else 0.1
        meaning_map["sovereignties"]["Reflection"] = 0.7 if "browser" in active_window or "note" in active_window else 0.3
        meaning_map["sovereignties"]["Distraction"] = 0.6 if keystroke_burst < 5 and "youtube" in active_window else 0.2

        # --- Chakras Reasoning ---
        meaning_map["chakras"]["Heart"] = 0.8 if "love" in screenshot_text or "thank" in screenshot_text else 0.3
        meaning_map["chakras"]["Solar Plexus"] = 0.7 if cpu_usage > 80 else 0.2
        meaning_map["chakras"]["Root"] = 0.9 if memory_usage > 85 else 0.3
        meaning_map["chakras"]["Third Eye"] = 0.6 if "idea" in screenshot_text else 0.2

        # --- Context Domains Reasoning ---
        meaning_map["context_domains"]["Creative"] = 0.8 if keystroke_burst > 30 else 0.3
        meaning_map["context_domains"]["Operational"] = 0.7 if "excel" in active_window or "terminal" in active_window else 0.2
        meaning_map["context_domains"]["Reflective"] = 0.5 if "journal" in active_window or "read" in active_window else 0.2
        meaning_map["context_domains"]["Relational"] = 0.6 if "chat" in active_window or "messenger" in active_window else 0.2

        # Assemble framework output
        framework_output = batch_data.copy()
        framework_output["meaning_map"] = meaning_map

        print(f"🔷 Meaning Map Generated: {json.dumps(meaning_map, indent=2)}")
        return framework_output
