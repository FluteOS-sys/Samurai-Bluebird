# samurai_bluebird_custos/mock_mode/simulated_workday.py

from samurai_bluebird_custos.agents.tri_agent import TriAgent
from samurai_bluebird_custos.ethics.krishna import KrishnaMetaObserver
import time

def run_simulated_workday():
    tri_agent = TriAgent()
    krishna = KrishnaMetaObserver()

    for i in range(3):  # Simulate 3 passive input batches
        print(f"\n🌱 Simulated Batch #{i + 1}")

        dummy_input = {
            "tags": ["Focus", "Trust", "Innovation"],
            "weights": {"Focus": 1.0 + i * 0.1, "Trust": 1.1, "Innovation": 1.2}
        }

        tri_result = tri_agent.reason_over_batch(dummy_input)
        print("🧠 Tri-Agent Output:", tri_result["narrative"])

        krishna_result = krishna.process_lattice_reflection()
        print("👁 Krishna Reflection:", krishna_result["daily_reflection"])

        time.sleep(1)  # Short pause between batches

if __name__ == "__main__":
    run_simulated_workday()
