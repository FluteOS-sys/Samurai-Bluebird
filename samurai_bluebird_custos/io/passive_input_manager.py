import psutil
import random
from datetime import datetime

class PassiveInputManager:
    def __init__(self):
        print("🪶 PassiveInputManager initialized.")

    def capture(self) -> dict:
        """
        Capture a passive snapshot of the current system state.
        """
        try:
            active_window = self.get_active_window()
        except Exception:
            active_window = "IdleState"

        snapshot = {
            "active_window": active_window,
            "keystroke_burst": self.get_keystroke_burst(),
            "screenshot_text": self.get_screenshot_text(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"📥 Captured snapshot: {snapshot}")
        return snapshot

    def get_active_window(self) -> str:
        # Placeholder for actual active window logic
        return "Samurai-Bluebird – active.py"

    def get_keystroke_burst(self) -> int:
        # Simulated keystroke burst (placeholder)
        return random.randint(0, 50)

    def get_screenshot_text(self) -> str:
        # Placeholder for OCR logic
        return "Sample OCR text from screenshot."
