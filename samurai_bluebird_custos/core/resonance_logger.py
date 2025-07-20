import os

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
