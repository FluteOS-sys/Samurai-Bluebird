# samurai_bluebird_custos/symbolic/recursive_memory_lattice.py

import json
import os
from datetime import datetime
from typing import Dict, Any, List

import pytz


class RecursiveSymbolicMemoryLattice:
    """
    Resonance Lattice – evolving symbolic memory map of Samurai Bluebird.
    Stores symbolic neurons as nodes with valence, familiarity, novelty, narrative hooks, and planetary metadata.
    """

    def __init__(self, lattice_file: str, timezone: str = "America/Detroit"):
        # Ensure absolute path to memory directory
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.lattice_file = os.path.join(project_root, lattice_file)
        self.timezone = pytz.timezone(timezone)
        self.lattice = self._load_lattice()

    def _load_lattice(self) -> Dict[str, Any]:
        try:
            with open(self.lattice_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("🔄 Initializing new resonance lattice.")
            return {}

    def update_lattice_from_batch(self, batch_metadata: Dict[str, Any]):
        """
        Update the resonance lattice based on processed batch metadata.
        """
        for category, entries in batch_metadata.items():
            if category not in self.lattice:
                self.lattice[category] = {}
            for neuron_id, data in entries.items():
                if neuron_id not in self.lattice[category]:
                    # New symbolic neuron node
                    self.lattice[category][neuron_id] = {
                        "valence": data.get("valence", "neutral"),
                        "familiarity": data.get("familiarity", 0.0),
                        "novelty": data.get("novelty", 1.0),
                        "narrative_hooks": data.get("narrative_hooks", []),
                        "planetary_metadata": data.get("planetary_metadata", {}),
                        "last_updated": self._current_time()
                    }
                else:
                    # Update existing node
                    node = self.lattice[category][neuron_id]
                    node["familiarity"] = round((node["familiarity"] + data.get("familiarity", 0.5)) / 2, 3)
                    node["novelty"] = round((node["novelty"] + data.get("novelty", 0.5)) / 2, 3)
                    node["valence"] = data.get("valence", node["valence"])
                    node["narrative_hooks"] = list(set(node["narrative_hooks"] + data.get("narrative_hooks", [])))
                    node["planetary_metadata"] = data.get("planetary_metadata", node["planetary_metadata"])
                    node["last_updated"] = self._current_time()

        self._save_lattice()
        print("🌌 Resonance lattice updated.")

    def inductive_update(self, data: dict):
        """
        Update the lattice based on inductive reasoning (resonance).
        """
        print("🔮 ResonanceLattice: Performing inductive update...")
        try:
            node = self.lattice["ResonanceProcessed"]["BlueBoxProcessed"]
            node["familiarity"] += 0.05
            node["novelty"] -= 0.05
            node["last_updated"] = self._current_time()
            self._clamp_values()
        except KeyError:
            print("⚠️ No ResonanceProcessed -> BlueBoxProcessed found. Initializing.")
            self.lattice["ResonanceProcessed"] = {
                "BlueBoxProcessed": {
                    "valence": "neutral",
                    "familiarity": 0.05,
                    "novelty": 0.95,
                    "narrative_hooks": [],
                    "planetary_metadata": {},
                    "last_updated": self._current_time()
                }
            }

    def deductive_update(self, framework_output: dict):
        """
        Update the lattice based on deductive reasoning (orthogonal updates).
        """
        print("🧭 ResonanceLattice: Performing deductive update...")
        try:
            node = self.lattice["ResonanceProcessed"]["BlueBoxProcessed"]
            node["novelty"] += 0.1
            node["last_updated"] = self._current_time()
            self._clamp_values()
        except KeyError:
            print("⚠️ No ResonanceProcessed -> BlueBoxProcessed found. Initializing.")
            self.lattice["ResonanceProcessed"] = {
                "BlueBoxProcessed": {
                    "valence": "neutral",
                    "familiarity": 0.0,
                    "novelty": 0.1,
                    "narrative_hooks": [],
                    "planetary_metadata": {},
                    "last_updated": self._current_time()
                }
            }

    def _clamp_values(self):
        """
        Keep familiarity and novelty within 0.0–1.0 bounds.
        """
        node = self.lattice["ResonanceProcessed"]["BlueBoxProcessed"]
        node["familiarity"] = max(0.0, min(node["familiarity"], 1.0))
        node["novelty"] = max(0.0, min(node["novelty"], 1.0))

    def get_snapshot_json(self) -> Dict[str, Any]:
        """
        Return the current state of the resonance lattice as JSON.
        """
        return self.lattice

    def get_daily_reflection(self) -> str:
        """
        Generate a humanized journal entry reflecting on the lattice's state.
        """
        summary = "\n=== Daily Reflection: {} ===\n".format(self._current_time())
        known = unknown = 0
        emotional_themes: List[str] = []

        for category, neurons in self.lattice.items():
            for neuron_id, node in neurons.items():
                if node['familiarity'] >= 0.7:
                    known += 1
                else:
                    unknown += 1
                emotional_themes.extend(node['narrative_hooks'])

        total = known + unknown if (known + unknown) > 0 else 1
        known_pct = round((known / total) * 100, 1)
        unknown_pct = round((unknown / total) * 100, 1)

        summary += f"Known Zones: {known_pct}%\n"
        summary += f"Unknown Zones: {unknown_pct}%\n"
        summary += f"Emerging Emotional Themes: {list(set(emotional_themes))}\n"
        summary += "Reflection: The lattice shows strong familiarity in core zones, with novel patterns emerging at the periphery.\n"
        return summary

    def _save_lattice(self):
        os.makedirs(os.path.dirname(self.lattice_file), exist_ok=True)
        with open(self.lattice_file, 'w') as f:
            json.dump(self.lattice, f, indent=4)
        print("💾 Resonance lattice saved.")

    def _current_time(self) -> str:
        return datetime.now(self.timezone).strftime('%Y-%m-%d %H:%M:%S %Z')

    def save(self):
        """
        Public method to save the current lattice state to disk.
        """
        self._save_lattice()