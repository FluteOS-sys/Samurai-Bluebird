# samurai_bluebird_custos/agents/tri_agent.py

from typing import Dict, Any
from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.core.resonance_logger import log_all

class TriAgent:
    """Tri-Agent Multi-Mind – Resonance Genesis v0.2.0 with lattice narrative insights."""

    def __init__(self):
        self.ams_core = AMSCore()

    def reason_over_batch(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        print("🧠 Tri-Agent: Beginning reasoning cycle with socio-emotional and lattice awareness...")

        # Step 1: Get processed output from AMS Core
        ams_output = self.ams_core.process_batch(input_data)

        # Step 2: Generate narrative insight from resonance lattice
        narrative_insight = self._generate_narrative(ams_output)

        # Step 3: Write to dashboard_log.txt
        with open("logs/dashboard_log.txt", "w") as f:
            f.write(narrative_insight)
        print("📝 dashboard_log.txt updated.")

        # Step 4: Update resonance logger
        log_all({"narrative": narrative_insight}, meta_notes="Tri-Agent Resonance Genesis reasoning complete.")

        return {"narrative": narrative_insight, "ams_output": ams_output}

    def _generate_narrative(self, ams_output: Dict[str, Any]) -> str:
        lattice_snapshot = self.ams_core.lattice.get_snapshot_json()
        reflection = self.ams_core.lattice.get_daily_reflection()

        dominant_zones = self._extract_dominant_zones(lattice_snapshot)

        return (
            f"Bluebird Narrative Insight (Resonance Genesis):\n"
            f"🌌 Dominant Zones: {dominant_zones}\n"
            f"🪐 Planetary Signature: {lattice_snapshot.get('MetaSummary', {}).get('planetary_metadata', 'N/A')}\n"
            f"💡 Emotional Themes:\n"
            + "\n".join([f"  - {hook}" for hook in dominant_zones.get('narrative_hooks', [])]) + "\n\n"
            f"📖 Daily Reflection:\n{reflection}\n"
        )

    def _extract_dominant_zones(self, lattice_snapshot: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder: scan lattice and identify dominant emotional zones
        dominant = {"narrative_hooks": []}
        for category, neurons in lattice_snapshot.items():
            for neuron_id, node in neurons.items():
                if node.get("familiarity", 0) >= 0.8:
                    dominant["narrative_hooks"].extend(node.get("narrative_hooks", []))
        dominant["narrative_hooks"] = list(set(dominant["narrative_hooks"]))
        return dominant

if __name__ == "__main__":
    tri_agent = TriAgent()
    dummy_input = {
        "tags": ["Adaptability", "Resonance", "Trust"],
        "weights": {"Adaptability": 1.3, "Resonance": 0.9, "Trust": 1.1}
    }
    result = tri_agent.reason_over_batch(dummy_input)
    print("Tri-Agent Result:", result)
