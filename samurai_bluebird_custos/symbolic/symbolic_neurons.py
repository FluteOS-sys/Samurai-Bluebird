# samurai_bluebird_custos/symbolic/symbolic_neurons.py

import json
from typing import Dict, Any
from datetime import datetime
import pytz

class SymbolicNeurons:
    """
    Symbolic Neurons – Resonance Genesis v0.2.1
    Manages evolving memory nodes with resonance and orthogonal update awareness.
    """

    def __init__(self, neurons_file: str, timezone: str = "America/Detroit"):
        self.neurons_file = neurons_file
        self.timezone = pytz.timezone(timezone)
        self.neurons = self._load_neurons()

    def _load_neurons(self) -> Dict[str, Any]:
        try:
            with open(self.neurons_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("🔄 Initializing new symbolic neurons.")
            return {}

    def update_neurons(self, updated_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates symbolic neurons with resonance flow logic.
        """
        current_time = self._current_time()
        updates_applied = {}

        for category, entries in updated_data.items():
            if category not in self.neurons:
                self.neurons[category] = {}
            updates_applied[category] = {}
            for neuron_id, data in entries.items():
                if neuron_id not in self.neurons[category]:
                    # Create a new symbolic neuron
                    self.neurons[category][neuron_id] = {
                        "valence": data.get("valence", "neutral"),
                        "familiarity": data.get("familiarity", 0.0),
                        "novelty": data.get("novelty", 1.0),
                        "last_updated": current_time,
                        "resonance_trace": ["Created"]
                    }
                    updates_applied[category][neuron_id] = "Created"
                else:
                    # Update existing neuron
                    neuron = self.neurons[category][neuron_id]
                    prev_fam = neuron.get("familiarity", 0.5)
                    prev_nov = neuron.get("novelty", 0.5)

                    neuron["familiarity"] = round((prev_fam + data.get("familiarity", 0.5)) / 2, 3)
                    neuron["novelty"] = round((prev_nov + data.get("novelty", 0.5)) / 2, 3)
                    neuron["valence"] = data.get("valence", neuron["valence"])
                    neuron["last_updated"] = current_time
                    neuron.setdefault("resonance_trace", []).append("Updated")
                    updates_applied[category][neuron_id] = "Updated"

        self._save_neurons()
        print("🧠 Symbolic neurons updated.")
        return updates_applied

    def get_neuron_snapshot(self) -> Dict[str, Any]:
        """
        Return a snapshot of current symbolic neurons.
        """
        return self.neurons

    def _save_neurons(self):
        with open(self.neurons_file, 'w') as f:
            json.dump(self.neurons, f, indent=4)
        print("💾 Symbolic neurons saved.")

    def _current_time(self) -> str:
        return datetime.now(self.timezone).strftime('%Y-%m-%d %H:%M:%S %Z')

if __name__ == "__main__":
    sn = SymbolicNeurons("memory/symbolic_neurons_v001.json")
    dummy_update = {
        "TestCategory": {
            "Neuron001": {"valence": "positive", "familiarity": 0.8, "novelty": 0.2}
        }
    }
    result = sn.update_neurons(dummy_update)
    print("Symbolic Neurons Update Result:", result)
