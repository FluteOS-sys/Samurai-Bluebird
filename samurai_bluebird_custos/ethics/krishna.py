# samurai_bluebird_custos/ethics/krishna.py

from typing import Dict, Any
from samurai_bluebird_custos.symbolic.resonance_lattice import ResonanceLattice
import os

class KrishnaMetaObserver:
    """Krishna Meta-Observer – Resonance Genesis v0.2.0 with lattice self-reflection."""

    def __init__(self):
        self.lattice = ResonanceLattice("memory/resonance_lattice.json")
        self.logs_dir = "logs/"

    def process_lattice_reflection(self) -> Dict[str, Any]:
        print("👁 Krishna: Observing resonance lattice for ethical and emotional patterns...")

        # Get daily reflection from lattice
        reflection = self.lattice.get_daily_reflection()

        # Write to witness_log.txt
        witness_log_path = os.path.join(self.logs_dir, 'witness_log.txt')
        with open(witness_log_path, 'w') as f:
            f.write(reflection)
        print("📝 witness_log.txt updated.")

        # Trigger meta_alert.txt if unknown zones exceed threshold
        lattice_snapshot = self.lattice.get_snapshot_json()
        unknown_ratio = self._calculate_unknown_ratio(lattice_snapshot)
        if unknown_ratio >= 0.3:  # Example threshold: 30% unknown zones
            meta_alert_path = os.path.join(self.logs_dir, 'meta_alert.txt')
            with open(meta_alert_path, 'w') as f:
                f.write("⚠️ Meta Alert: System detecting high novelty/chaos levels in lattice.")
            print("⚠️ meta_alert.txt triggered.")

        return {"daily_reflection": reflection, "unknown_ratio": unknown_ratio}

    def _calculate_unknown_ratio(self, lattice_snapshot: Dict[str, Any]) -> float:
        known = unknown = 0
        for category, neurons in lattice_snapshot.items():
            for neuron_id, node in neurons.items():
                if node.get('familiarity', 0) >= 0.7:
                    known += 1
                else:
                    unknown += 1
        total = known + unknown if (known + unknown) > 0 else 1
        return round(unknown / total, 3)

if __name__ == "__main__":
    krishna = KrishnaMetaObserver()
    result = krishna.process_lattice_reflection()
    print("Krishna Reflection Result:", result)
