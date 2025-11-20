import time
from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.io.passive_input_manager import PassiveInputManager

class Kernel:
    def __init__(self):
        self.ams_core = AMSCore()
        self.feathers = PassiveInputManager()

    def run(self, runtime_minutes=30, interval_seconds=300):
        """
        Run the system for a set duration, processing one snapshot every interval.
        :param runtime_minutes: Total runtime in minutes (default: 30 min).
        :param interval_seconds: Time between snapshots in seconds (default: 5 min).
        """
        print("⚡ Kernel: Starting Resonance Flow runtime...")
        start_time = time.time()
        end_time = start_time + (runtime_minutes * 60)

        while time.time() < end_time:
            try:
                snapshot = self.feathers.capture()
                self.ams_core.process_batch(snapshot)
                print(f"✅ Processed snapshot at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            except Exception as e:
                print(f"❌ Kernel error: {e}")
            time.sleep(interval_seconds)

        print("🛑 Kernel: Resonance Flow completed.")


def assemble_feather_input():
    """Collect a passive input snapshot for quick testing."""

    manager = PassiveInputManager()
    return manager.capture()
