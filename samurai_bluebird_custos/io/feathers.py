import pytesseract
import cv2
import psutil
import time
from pynput import keyboard
from PIL import ImageGrab
import numpy as np

# Hardcode Tesseract path to avoid PATH issues
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_active_window():
    """Return the title of the currently focused application window."""
    try:
        import win32gui
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        return title
    except ImportError:
        return "UnknownWindow"

def capture_keystroke_bursts(duration=5):
    """Measure typing activity over a period of time (bursts)."""
    count = [0]

    def on_press(key):
        count[0] += 1

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    time.sleep(duration)
    listener.stop()
    return count[0]

def capture_screenshot_text():
    """Take a screenshot and run OCR to extract visible text."""
    try:
        screenshot = ImageGrab.grab()
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        text = pytesseract.image_to_string(screenshot_cv)
        return text.strip()
    except Exception as e:
        print(f"⚠️ Screenshot OCR failed: {e}")
        return "[Screenshot OCR unavailable]"

def get_passive_input_snapshot():
    """Unified passive input snapshot for Kernel."""
    return {
        "active_window": capture_active_window(),
        "keystroke_burst": capture_keystroke_bursts(),
        "screenshot_text": capture_screenshot_text(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

