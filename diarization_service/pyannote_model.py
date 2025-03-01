from fastapi import FastAPI, UploadFile, File
from pyannote.audio import Pipeline
import torch
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("Token Hugging Face não fornecido. Defina a variável HF_TOKEN no arquivo .env.")

app = FastAPI()

# Carregar pipeline de diarização com autenticação
try:
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=HF_TOKEN
    )
    if pipeline is None:
        raise ValueError("Falha ao carregar o pipeline. Verifique o token e os termos de uso em https://hf.co/pyannote/speaker-diarization-3.1")
    pipeline.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
except Exception as e:
    print(f"Erro ao carregar o pipeline: {str(e)}")
    raise

@app.get("/health")
async def health_check():
    return {"status": "ok", "model": "pyannote/speaker-diarization-3.1", "device": str(pipeline.device)}

@app.post("/diarize")
async def diarize_audio(file: UploadFile = File(...)):
    temp_path = "temp_audio.wav"
    with open(temp_path, "wb") as f:
        f.write(file.file.read())

    diarization = pipeline(temp_path)
    segments = []
    speakers = set()
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "start": turn.start,
            "end": turn.end,
            "speaker": speaker
        })
        speakers.add(speaker)

    os.remove(temp_path)
    return {
        "segments": segments,
        "num_speakers": len(speakers)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)