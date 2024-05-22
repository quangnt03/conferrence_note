from tempfile import NamedTemporaryFile
from fastapi import UploadFile
from assemblyai import Transcriber

def process_audio_transcript(transcriber: Transcriber, audio_file: UploadFile) -> str:
    with NamedTemporaryFile() as tmp_file:
        tmp_file.write(audio_file.file.read())
        tmp_file.seek(0)
        transcription = transcriber.transcribe(tmp_file.name)
        return transcription.text