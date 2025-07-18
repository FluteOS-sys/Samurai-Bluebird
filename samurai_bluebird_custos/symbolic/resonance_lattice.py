import json
from typing import Dict, Any, List
from datetime import datetime
import pytz
from samurai_bluebird_custos.utils.planetary_metadata import get_planetary_positions

class ResonanceLattice:
    """
    The Resonance Lattice represents the evolving symbolic memory map of Samurai Bluebird.
    It stores symbolic neurons as nodes with valence, familiarity, novelty, narrative hooks,
    and planetary metadata for temporal orientation.
    """

    def __init__(self, lattice_file: str, timezone: str = "America/Detroit"):
        self.lattice_file = lattice_file
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
        current_timestamp = self._current_time()
        planetary_signature = get_planetary_positions(current_timestamp)

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
                        "planetary_metadata": planetary_signature,
                        "last_updated": current_timestamp
                    }
                else:
                    # Update existing node
                    node = self.lattice[category][neuron_id]
                    node["familiarity"] = round((node["familiarity"] + data.get("familiarity", 0.5)) / 2, 3)
                    node["novelty"] = round((node["novelty"] + data.get("novelty", 0.5)) / 2, 3)
                    node["valence"] = data.get("valence", node["valence"])
                    node["narrative_hooks"] = list(set(node["narrative_hooks"] + data.get("narrative_hooks", [])))
                    node["planetary_metadata"] = planetary_signature
                    node["last_updated"] = current_timestamp

        self._save_lattice()
        print("🌌 Resonance lattice updated.")

    def get_snapshot_json(self) -> Dict[str, Any]:
        return self.lattice

    def get_daily_reflection(self) -> str:
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
        summary += "Reflection: Patterns consolidate in familiar zones while novelty stirs at the edges. The system trends toward balance, remaining vigilant to emerging dynamics.\n"
        return summary

    def _save_lattice(self):
        with open(self.lattice_file, 'w') as f:
            json.dump(self.lattice, f, indent=4)
        print("💾 Resonance lattice saved.")

    def _current_time(self) -> str:
        return datetime.now(self.timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
