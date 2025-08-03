# samurai_bluebird_custos/core/resonance_logger.py

import os
import sys

# Fix Windows terminal and file writing for UTF-8
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

LOG_DIR = "logs"

def ensure_log_dir():
    """Ensure that the logs directory exists."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_all(message: str, log_file: str = "input_resonance_log.txt"):
    """
    Write a log message to the specified log file.
    If the logs directory does not exist, create it first.
    """
    ensure_log_dir()
    log_path = os.path.join(LOG_DIR, log_file)
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"{message}\n")
        print(f"📜 Log written to {log_file}")
    except Exception as e:
        print(f"❌ Failed to write log: {e}")