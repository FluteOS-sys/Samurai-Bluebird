### main_loop.py

import json
from samurai_bluebird_custos.io.passive_input_manager import PassiveInputManager
from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.agents.tri_agent import reason_over_batch
from samurai_bluebird_custos.core.resonance_logger import log_all


def main_loop():
    # 1. Capture passive input snapshot
    snapshot = PassiveInputManager().capture()

    # 2. Tri-Agent generates narrative and symbolic structure
    enriched = reason_over_batch(snapshot)
    narrative = enriched["narrative"]
    enriched_batch = enriched["enriched_batch"]

    # 3. AMSCore processes symbolic enrichment and updates memory
    ams = AMSCore()
    memory_update = ams.process_batch(enriched_batch)

    # 4. Log the results
    log_all(narrative, "dashboard_log.txt")
    log_all(json.dumps(memory_update, indent=2), "output_resonance_log.txt")
