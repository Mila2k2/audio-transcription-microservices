from fastapi import FastAPI, UploadFile, File, HTTPException
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torch
import librosa
import os
from pydub import AudioSegment
from dotenv import load_dotenv
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("Token Hugging Face não fornecido. Defina HF_TOKEN no .env.")

app = FastAPI()

model_name = "openai/whisper-large-v3"
model = WhisperForConditionalGeneration.from_pretrained(model_name, token=HF_TOKEN)
processor = WhisperProcessor.from_pretrained(model_name, token=HF_TOKEN)
model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

@app.get("/health")
async def health_check():
    return {"status": "ok", "model": model_name, "device": str(model.device)}

@app.post("/transcribe_segment")
async def transcribe_segment(file: UploadFile = File(...), start: float = 0.0, end: float = None):
    start_time = time.time()
    logger.info(f"Recebido pedido para transcrever segmento {start}s - {end}s")

    temp_path = "temp_audio.wav"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    audio = AudioSegment.from_file(temp_path)
    total_duration = len(audio) / 1000.0
    if end is None or end > total_duration:
        end = total_duration
    if start >= end:
        raise HTTPException(status_code=400, detail="O tempo de início deve ser menor que o tempo de fim")

    start_ms = int(start * 1000)
    end_ms = int(end * 1000)
    logger.info(f"Cortando áudio: {start_ms}ms - {end_ms}ms (duração: {end_ms - start_ms}ms)")
    
    segment_audio = audio[start_ms:end_ms]
    segment_path = "temp_segment.wav"
    segment_audio.export(segment_path, format="wav")

    segment_duration = (end_ms - start_ms) / 1000.0
    logger.info(f"Segmento exportado com duração de {segment_duration:.2f}s")

    audio_data, sample_rate = librosa.load(segment_path, sr=16000)
    input_features = processor(
        audio_data,
        sampling_rate=sample_rate,
        return_tensors="pt",
        language="pt",
        return_attention_mask=True
    ).to(model.device)

    with torch.no_grad():
        predicted_ids = model.generate(
            input_features["input_features"],
            attention_mask=input_features["attention_mask"]
        )
    transcription = processor.decode(predicted_ids[0], skip_special_tokens=True)

    os.remove(temp_path)
    os.remove(segment_path)

    end_time = time.time()
    logger.info(f"Transcrição concluída em {end_time - start_time:.2f}s: {transcription}")
    return {"transcription": transcription}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)