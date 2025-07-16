# samurai_bluebird_custos/agents/tri_agent.py

from typing import Dict, Any
from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.core.resonance_logger import log_all

class TriAgent:
    """Prototype Tri-Agent Multi-Mind using AMS Core socio-emotional output."""

    def __init__(self):
        self.ams_core = AMSCore()

    def reason_over_batch(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        print("🧠 Tri-Agent: Beginning reasoning cycle with socio-emotional lens...")

        # Step 1: Get processed output from AMS Core
        ams_output = self.ams_core.process_batch(input_data)

        # Step 2: Generate narrative insight
        narrative_insight = self._generate_narrative(ams_output)

        # Step 3: Write to dashboard_log.txt
        with open("logs/dashboard_log.txt", "w") as f:
            f.write(narrative_insight)
        print("📝 dashboard_log.txt updated.")

        # Step 4: Update resonance logger
        log_all({"narrative": narrative_insight}, meta_notes="Tri-Agent reasoning complete.")

        return {"narrative": narrative_insight, "ams_output": ams_output}

    def _generate_narrative(self, ams_output: Dict[str, Any]) -> str:
        se_view = ams_output["combined_data"]["socio_emotional"]
        dominant_chakra = ams_output["combined_data"]["resonance_lattice"]["MetaSummary"]["DominantChakra"]
        dominant_domain = ams_output["combined_data"]["resonance_lattice"]["MetaSummary"]["DominantDomain"]

        return (
            f"Bluebird Narrative Insight:\n"
            f"🌌 Dominant Chakra: {dominant_chakra}\n"
            f"🏛 Dominant Context Domain: {dominant_domain}\n"
            f"💡 Socio-Emotional Lens:\n"
            + "\n".join([f"  - {k}: {v}" for k, v in se_view.items()]) + "\n"
        )

if __name__ == "__main__":
    tri_agent = TriAgent()
    dummy_input = {
        "tags": ["Adaptability", "Resonance", "Trust"],
        "weights": {"Adaptability": 1.3, "Resonance": 0.9, "Trust": 1.1}
    }
    result = tri_agent.reason_over_batch(dummy_input)
    print("Tri-Agent Result:", result)
