import json
from typing import Dict, Any
from samurai_bluebird_custos.symbolic.resonance_lattice import ResonanceLattice
from samurai_bluebird_custos.frameworks.blue_box import BlueBox
from samurai_bluebird_custos.ethics.pillars import SocioEmotionalFilter
from samurai_bluebird_custos.core.resonance_logger import log_all

class AMSCore:
    lattice: ResonanceLattice
    blue_box: BlueBox
    socio_emotional_filter: SocioEmotionalFilter

    def __init__(self):
        self.lattice = ResonanceLattice("memory/resonance_lattice.json")
        self.blue_box = BlueBox()
        self.socio_emotional_filter = SocioEmotionalFilter()

    def process_batch(self, batch_data: Dict[str, Any]) -> Dict[str, Any]:
        print("⚡ AMSCore: Processing new batch with Resonance Flow...")

        # Step 1: Inductive reasoning
        self.lattice.inductive_update(batch_data)
        print("🔄 Inductive reasoning (resonance) completed.")

        # Step 2: Framework processing
        framework_output = self.blue_box.process(batch_data)
        print("📦 BlueBox: Processing input through frameworks...")

        # Step 3: Deductive reasoning
        self.lattice.deductive_update(framework_output)
        print("🧠 Deductive reasoning (orthogonal updates) completed.")

        # Step 4: Apply socio-emotional filter
        filtered_output = self.socio_emotional_filter.apply(framework_output)

        # Step 5: Save lattice
        self.lattice.save()
        print("💾 Resonance lattice saved.")
        print("🌌 Resonance lattice updated.")

        # Step 6: Log the processed batch
        log_entry = {
            "batch": batch_data,
            "framework_output": framework_output,
            "filtered_output": filtered_output
        }
        try:
            log_all(json.dumps(log_entry, indent=2), "input_resonance_log.txt")
        except Exception as e:
            print(f"❌ Log write failed: {e}")

        return filtered_output
