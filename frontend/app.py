import streamlit as st
import requests
from pydub import AudioSegment
import os
import subprocess

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except FileNotFoundError:
        st.error("FFmpeg não encontrado. Instale o FFmpeg e adicione ao PATH.")
        st.stop()

def check_service_health(url):
    try:
        response = requests.get(f"{url}/health", timeout=5)
        response.raise_for_status()
        data = response.json()
        return True, f"{data['model']} ({data['device']}) carregado com sucesso"
    except requests.exceptions.RequestException as e:
        return False, f"Erro: {str(e)}"

check_ffmpeg()

st.title("Transcrição de Áudio/Vídeo")

st.subheader("Status dos Modelos")
whisper_ok, whisper_status = check_service_health("http://localhost:8000")
pyannote_ok, pyannote_status = check_service_health("http://localhost:8001")

st.write(f"Whisper: {'Disponível' if whisper_ok else 'Indisponível'} - {whisper_status}")
st.write(f"Pyannote: {'Disponível' if pyannote_ok else 'Indisponível'} - {pyannote_status}")

if whisper_ok and pyannote_ok:
    uploaded_file = st.file_uploader("Escolha um arquivo de áudio ou vídeo", type=["mp3", "wav", "mp4"])
    use_diarization = st.checkbox("Incluir segmentação de falantes", value=True)

    if uploaded_file:
        with st.spinner("Processando o arquivo..."):
            if uploaded_file.type == "video/mp4":
                try:
                    video = AudioSegment.from_file(uploaded_file, format="mp4")
                    audio_path = "audio.wav"
                    video.export(audio_path, format="wav")
                except Exception as e:
                    st.error(f"Erro ao processar o arquivo MP4: {str(e)}")
                    st.stop()
            else:
                audio_path = uploaded_file.name
                with open(audio_path, "wb") as f:
                    f.write(uploaded_file.read())

            if use_diarization:
                try:
                    with open(audio_path, "rb") as f:
                        diarization_response = requests.post(
                            "http://localhost:8001/diarize",
                            files={"file": f},
                            timeout=60
                        )
                        diarization_response.raise_for_status()
                    result = diarization_response.json()
                    segments = result["segments"]
                    num_speakers = result["num_speakers"]
                except requests.exceptions.RequestException as e:
                    st.error(f"Erro na diarização: {str(e)}")
                    st.stop()

                st.write(f"Número de falantes detectados: {num_speakers}")
                st.write("Transcrições por segmento:")

                for segment in segments:
                    #st.write(f"Enviando segmento {segment['speaker']} ({segment['start']:.1f}s - {segment['end']:.1f}s)")
                    with st.spinner(f"Transcrevendo segmento {segment['speaker']} ({segment['start']:.1f}s - {segment['end']:.1f}s)..."):
                        try:
                            with open(audio_path, "rb") as f:
                                transcription_response = requests.post(
                                    "http://localhost:8000/transcribe_segment",
                                    files={"file": (audio_path, f, "audio/wav")},
                                    params={"start": segment["start"], "end": segment["end"]},  # Usar params em vez de data
                                    timeout=120
                                )
                                transcription_response.raise_for_status()
                            transcription = transcription_response.json()["transcription"]
                            st.write(f"Speaker {segment['speaker']} ({segment['start']:.1f}s - {segment['end']:.1f}s): {transcription}")
                        except requests.exceptions.RequestException as e:
                            st.error(f"Erro na transcrição do segmento {segment['speaker']}: {str(e)}")
            else:
                try:
                    with open(audio_path, "rb") as f:
                        transcription_response = requests.post(
                            "http://localhost:8000/transcribe_segment",
                            files={"file": f},
                            timeout=120
                        )
                        transcription_response.raise_for_status()
                    transcription = transcription_response.json()["transcription"]
                    st.write("Transcrição:", transcription)
                except requests.exceptions.RequestException as e:
                    st.error(f"Erro na transcrição: {str(e)}")

            if os.path.exists(audio_path):
                os.remove(audio_path)
else:
    st.warning("Os modelos Whisper e Pyannote precisam estar disponíveis para prosseguir. Inicie os serviços correspondentes.")