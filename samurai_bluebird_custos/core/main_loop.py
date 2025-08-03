### main_loop.py

from ..feathers import capture_snapshot
from ..agents.tri_agent import TriAgent
from ..frameworks.blue_box import BlueBox
from ..core.ams_core import AMSCore
from ..core.resonance_logger import write_output_logs, verify_and_log


def main():
    # Step 1: Capture passive input snapshot
    snapshot = capture_snapshot()

    # Step 2: Run Tri-Agent to extract narrative and symbolic hooks
    tri_agent = TriAgent()
    tri_output = tri_agent.reason_over_batch(snapshot)
    narrative = tri_output["narrative"]
    enriched_data = tri_output["raw_enriched"]

    # Step 3: Run BlueBox frameworks to generate symbolic meaning map
    bluebox = BlueBox()
    meaning_map = bluebox.process(narrative)

    # Step 4: Run AMSCore with full enriched batch
    full_batch = {
        "snapshot": snapshot,
        "narrative": narrative,
        "symbolic": enriched_data,
        "meaning_map": meaning_map
    }
    ams_core = AMSCore()
    updated_state = ams_core.process_batch(full_batch)

    # Step 5: Log outputs
    write_output_logs(narrative, enriched_data, meaning_map)
    verify_and_log(updated_state)


if __name__ == "__main__":
    main()
