# samurai_bluebird_custos/agents/tri_agent.py

from typing import Dict, Any, List
from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.core.resonance_logger import log_all

class TriAgent:
    """
    Tri-Agent Multi-Mind – Resonance Genesis v0.2.1
    Synthesizes narratives from the Resonance Lattice state.
    """

    def __init__(self):
        self.ams_core = AMSCore()

    def reason_over_batch(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        print("🧠 Tri-Agent: Beginning reasoning cycle with resonance awareness...")

        # Step 1: Get processed output from AMS Core
        ams_output = self.ams_core.process_batch(input_data)

        # Step 2: Generate narrative insight from resonance lattice
        narrative_insight = self._generate_narrative(ams_output)

        # Step 3: Write to dashboard_log.txt
        with open("logs/dashboard_log.txt", "w") as f:
            f.write(narrative_insight)
        print("📝 dashboard_log.txt updated.")

        # Step 4: Update resonance logger
        log_all({"narrative": narrative_insight}, meta_notes="Tri-Agent Resonance Genesis narrative synthesized.")

        return {"narrative": narrative_insight, "ams_output": ams_output}

    def _generate_narrative(self, ams_output: Dict[str, Any]) -> str:
        lattice_snapshot = self.ams_core.lattice.get_snapshot_json()
        reflection = self.ams_core.lattice.get_daily_reflection()

        dominant_themes = self._extract_dominant_themes(lattice_snapshot)

        return (
            f"🕊 Bluebird Narrative Insight (Resonance Genesis):\n"
            f"🌌 Dominant Emotional Themes: {', '.join(dominant_themes)}\n"
            f"📖 Reflection:\n{reflection}\n"
        )

    def _extract_dominant_themes(self, lattice_snapshot: Dict[str, Any]) -> List[str]:
        """
        Extract narrative hooks from the lattice for dominant emotional themes.
        """
        hooks = []
        for category, neurons in lattice_snapshot.items():
            for neuron_id, node in neurons.items():
                hooks.extend(node.get('narrative_hooks', []))
        return list(set(hooks))

if __name__ == "__main__":
    tri_agent = TriAgent()
    dummy_input = {
        "tags": ["Adaptability", "Resonance", "Trust"],
        "weights": {"Adaptability": 1.3, "Resonance": 0.9, "Trust": 1.1}
    }
    result = tri_agent.reason_over_batch(dummy_input)
    print("Tri-Agent Result:", result)
