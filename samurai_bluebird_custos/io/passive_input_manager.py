import pytesseract
import cv2
import psutil
import time
from PIL import ImageGrab
from pynput import keyboard
import numpy as np

# Hardcode Tesseract path to avoid PATH issues
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_visual_text():
    """
    Capture visible text on the screen using Tesseract OCR.
    """
    try:
        screenshot = ImageGrab.grab()
        screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        text = pytesseract.image_to_string(screenshot_cv)
        return text.strip()
    except Exception as e:
        print(f"⚠️ OCR failed: {e}")
        return "[OCR unavailable]"

def capture_keystroke_bursts(duration=5):
    """
    Count number of keystrokes over a given duration (seconds).
    Does not log actual keys for privacy.
    """
    count = [0]

    def on_press(key):
        count[0] += 1

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    time.sleep(duration)
    listener.stop()
    return count[0]

def get_active_window_title():
    """
    Return the title of the currently active window.
    """
    try:
        import pygetwindow as gw
        return gw.getActiveWindowTitle()
    except Exception:
        return "[Window title unavailable]"

def get_system_stats():
    """
    Return current CPU and memory usage.
    """
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent
    }

def get_passive_input_snapshot():
    """
    Aggregate all passive inputs into a single structured snapshot.
    Future extensions: audio_context(), emotional_state(), etc.
    """
    snapshot = {
        "active_window": get_active_window_title(),
        "keystrokes": capture_keystroke_bursts(),
        "screenshot_text": capture_visual_text(),
        "system_stats": get_system_stats()
    }
    return snapshot
