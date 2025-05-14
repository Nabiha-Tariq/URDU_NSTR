import easyocr
import os

reader = easyocr.Reader(['ur'], gpu=False)

def recognize_text(image_path: str) -> str:
    results = reader.readtext(image_path, detail=0)
    return '\n'.join(results)