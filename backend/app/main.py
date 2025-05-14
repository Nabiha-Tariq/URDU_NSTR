from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from app.ocr_engine import recognize_text

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/ocr/")
async def ocr_image(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result_text = recognize_text(file_path)
        os.remove(file_path)

        return JSONResponse(content={"text": result_text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})