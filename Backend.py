import shutil
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import whisper
import tempfile

app = FastAPI()

# Obsługa CORS, aby frontend mógł komunikować się z backendem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Zadanie 2.1: Ładowanie modelu Whisper (globalnie)
# "base" to dobry balans między szybkością a dokładnością
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Zadanie 2.3: Implementacja funkcji przetwarzania
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".webm")
    
    try:
        # Zapisywanie przesłanego Bloba do pliku tymczasowego
        with open(temp_file.name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Transkrypcja przez model Whisper
        result = model.transcribe(temp_file.name)
        
        return {"text": result["text"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Usunięcie pliku tymczasowego po zakończeniu
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)