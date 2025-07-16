import json
from typing import Dict, Any

class SymbolicNeurons:
    """Handles symbolic neuron state and updates in Samurai Bluebird."""

    def __init__(self, neuron_file: str):
        self.neuron_file = neuron_file
        self.neurons = self._load_neurons()

    def _load_neurons(self) -> Dict[str, Any]:
        """Load symbolic neuron states from JSON memory file."""
        try:
            with open(self.neuron_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("🔄 Initializing new symbolic neurons.")
            return {}

    def update_neurons(self, resonance_lattice: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update symbolic neurons with the latest resonance lattice data.
        Each resonance dimension subtly shifts neuron states.
        """
        for category, values in resonance_lattice.items():
            if category not in self.neurons:
                self.neurons[category] = {}

            for key, value in values.items():
                if key not in self.neurons[category]:
                    self.neurons[category][key] = value
                else:
                    # Blend previous state with new value (weighted average)
                    prev = self.neurons[category][key]
                    self.neurons[category][key] = round((prev + value) / 2, 3)

        self._save_neurons()
        return self.neurons

    def _save_neurons(self):
        """Persist symbolic neuron states to JSON memory file."""
        with open(self.neuron_file, 'w') as f:
            json.dump(self.neurons, f, indent=4)
        print("💾 Symbolic neurons updated in memory.")

    def get_neuron_state(self) -> Dict[str, Any]:
        """Retrieve the current symbolic neuron state."""
        return self.neurons
