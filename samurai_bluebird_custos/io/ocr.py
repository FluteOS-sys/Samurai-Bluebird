# samurai_bluebird_custos/io/ocr.py

import pytesseract
from samurai_bluebird_custos.io.image_analysis import capture_screenshot

# Set Tesseract path (Windows example)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_text_from_screenshot():
    """Run OCR on a screenshot and return extracted text."""
    image = capture_screenshot()
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"⚠️ OCR failed: {e}")
        return "[OCR unavailable]"
