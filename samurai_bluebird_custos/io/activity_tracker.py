# samurai_bluebird_custos/io/activity_tracker.py

import psutil
import time

try:
    import win32gui
except ImportError:
    win32gui = None  # Graceful fallback if not on Windows

def get_cpu_usage():
    """Get current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Get current memory usage percentage."""
    return psutil.virtual_memory().percent

def get_active_window_title():
    """Get the title of the current active window (Windows only)."""
    if win32gui:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    return "UnknownWindow"

def get_activity_snapshot():
    """Return a snapshot of system activity."""
    return {
        "active_window": get_active_window_title(),
        "cpu_usage": get_cpu_usage(),
        "memory_usage": get_memory_usage(),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
