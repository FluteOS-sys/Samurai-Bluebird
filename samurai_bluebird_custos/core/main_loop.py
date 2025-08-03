# samurai_bluebird_custos/core/main_loop.py

import time
from samurai_bluebird_custos.core.kernel import Kernel
from samurai_bluebird_custos.agents.tri_agent import TriAgent
from samurai_bluebird_custos.core.resonance_logger import log_all
from samurai_bluebird_custos.ethics.krishna import generate_witness_log, observe_symbolic_drift

if __name__ == "__main__":
    runtime_minutes = 30  # Total run time
    interval_seconds = 300  # 5 min between snapshots

    kernel = Kernel()
    tri_agent = TriAgent()

    print("⚡ Kernel: Starting Resonance Flow runtime...")
    start_time = time.time()
    end_time = start_time + (runtime_minutes * 60)

    while time.time() < end_time:
        try:
            # Capture passive input snapshot
            snapshot = kernel.feathers.capture()

            # Process batch through AMS Core
            filtered_output = kernel.ams_core.process_batch(snapshot)
            print(f"✅ Processed snapshot at {time.strftime('%Y-%m-%d %H:%M:%S')}")

            # Generate narrative insight via Tri-Agent
            tri_output = tri_agent.reason_over_batch(filtered_output)
            narrative = tri_output.get("narrative", "No narrative generated.")

            # Log narrative to dashboard_log
            log_all(narrative, "dashboard_log.txt")

            # Run Krishna meta-observation each cycle
            generate_witness_log()
            observe_symbolic_drift()

            # Log symbolic snapshot to summary
            hooks = filtered_output.get("narrative_hooks", [])
            symbolic_log = f"⏱ {time.strftime('%H:%M:%S')} | Hooks: {', '.join(hooks) or 'None'}"
            log_all(symbolic_log, "symbolic_snapshots.txt")

        except Exception as e:
            print(f"❌ Kernel error: {e}")

        time.sleep(interval_seconds)

    print("🛑 Kernel: Resonance Flow completed.")
