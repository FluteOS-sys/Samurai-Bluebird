# samurai_bluebird_custos/core/kernel.py

from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.agents.tri_agent import TriAgent
from samurai_bluebird_custos.ethics.krishna import KrishnaMetaObserver
from samurai_bluebird_custos.ethics.ethical_gatekeeper import EthicalGatekeeper
from samurai_bluebird_custos.io.feathers import PassiveInputManager
import time

class Kernel:
    """
    Kernel – Resonance Genesis v0.2.1
    Orchestrates system flow from passive input to symbolic neuron evolution.
    """

    def __init__(self, batch_interval: int = 5):
        self.passive_input_manager = PassiveInputManager()
        self.ams_core = AMSCore()
        self.tri_agent = TriAgent()
        self.ethical_gatekeeper = EthicalGatekeeper()
        self.krishna = KrishnaMetaObserver()
        self.batch_interval = batch_interval  # Interval in seconds for batching

    def run(self, runtime_minutes: int = 1):
        """
        Main runtime loop: runs for specified duration in minutes.
        """
        print("⚡ Kernel: Starting Resonance Flow runtime...")
        end_time = time.time() + runtime_minutes * 60

        while time.time() < end_time:
            # Step 1: Capture passive inputs
            batch_data = self.passive_input_manager.capture_batch()
            print(f"📥 Captured batch: {batch_data}")

            # Step 2: Process batch through AMS Core
            ams_output = self.ams_core.process_batch(batch_data)

            # Step 3: Pass to Tri-Agent for narrative synthesis
            narrative_output = self.tri_agent.reason_over_batch(batch_data)

            # Step 4: Apply Ethical Gatekeeper filter
            filtered_output = self.ethical_gatekeeper.filter_output(ams_output)

            # Step 5: Krishna observes resonance lattice and logs reflections
            krishna_output = self.krishna.process_lattice_reflection()

            # Wait for the next batch cycle
            time.sleep(self.batch_interval)

        print("🏁 Kernel: Resonance Flow runtime completed.")

if __name__ == "__main__":
    kernel = Kernel(batch_interval=5)
    kernel.run(runtime_minutes=0.1)  # Run for 6 seconds for test
