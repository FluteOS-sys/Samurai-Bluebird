# resonance_logger.py

import json
import os
from datetime import datetime
from typing import Any


def _date_directory() -> str:
    """Return the dated log directory and create it if needed."""

    date_dir = os.path.join("logs", datetime.now().strftime("%Y-%m-%d"))
    os.makedirs(date_dir, exist_ok=True)
    return date_dir


def log_all(entry: Any, log_filename: str = "dashboard_log.txt", meta_notes: str | None = None) -> str:
    """Append a timestamped entry to a dated log file.

    Args:
        entry: The content to write. Dicts are JSON-encoded; other values are converted to strings.
        log_filename: The log file name within the dated folder.
        meta_notes: Optional prefix describing the entry.

    Returns:
        The normalized log line written to disk.
    """

    date_dir = _date_directory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    normalized = json.dumps(entry, indent=2) if isinstance(entry, (dict, list)) else str(entry)
    prefix = f"[{timestamp}] "
    if meta_notes:
        prefix += f"{meta_notes} "

    line = f"{prefix}{normalized}\n"
    with open(os.path.join(date_dir, log_filename), "a", encoding="utf-8") as log_file:
        log_file.write(line)
    return line


def write_output_logs(narrative, symbolic_data, meaning_map):
    timestamp = datetime.utcnow().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "narrative": narrative,
        "symbolic": symbolic_data,
        "meaning_map": meaning_map
    }
    log_all(log_entry, "output_resonance_log.txt")


def verify_and_log(system_state):
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "system_state": system_state
    }
    log_all(entry, "dashboard_log.txt")


def tail_log(date_str: str, log_filename: str, limit: int = 100) -> list[str]:
    """Return the last ``limit`` log lines from the dated log file."""

    date_dir = os.path.join("logs", date_str)
    log_path = os.path.join(date_dir, log_filename)
    if not os.path.exists(log_path):
        return []

    with open(log_path, "r", encoding="utf-8") as log_file:
        lines = log_file.readlines()
    return lines[-limit:]
