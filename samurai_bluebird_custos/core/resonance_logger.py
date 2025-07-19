# samurai_bluebird_custos/core/resonance_logger.py

import json
from typing import Dict, Any
import os
from datetime import datetime
import pytz

class ResonanceLogger:
    """
    Resonance Logger – Resonance Genesis v0.2.1
    Centralized logger for all resonance-based outputs.
    """

    def __init__(self, logs_dir: str = "logs", timezone: str = "America/Detroit"):
        self.logs_dir = logs_dir
        self.timezone = pytz.timezone(timezone)

    def log_event(self, log_name: str, content: Dict[str, Any], meta_notes: str = ""):
        """
        Logs a structured event into the specified log file.
        """
        timestamp = self._current_time()
        log_entry = {
            "timestamp": timestamp,
            "meta_notes": meta_notes,
            "content": content
        }

        log_path = os.path.join(self.logs_dir, log_name)
        with open(log_path, 'a') as f:
            f.write(json.dumps(log_entry, indent=4) + "\n")
        print(f"📡 Resonance Logger: Logged event to {log_name}")

    def _current_time(self) -> str:
        return datetime.now(self.timezone).strftime('%Y-%m-%d %H:%M:%S %Z')

def log_all(data: Dict[str, Any], meta_notes: str = ""):
    """
    Convenience function to log to multiple resonance logs.
    """
    logger = ResonanceLogger()
    logger.log_event("input_resonance_log.txt", data, meta_notes=meta_notes)
    logger.log_event("dashboard_log.txt", data, meta_notes=meta_notes)
    logger.log_event("witness_log.txt", data, meta_notes=meta_notes)
