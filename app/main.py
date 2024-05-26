from fastapi import FastAPI, UploadFile, Request, HTTPException
from fastapi.responses import JSONResponse
from json import JSONDecodeError
import assemblyai as aai
from app.transcription import transcription
from app.llm import chains

app = FastAPI()

@app.post("/transcribe")
async def summarize_transcript(audio_file: UploadFile = None):
    accepted_content_type = 'audio/mp4'
    if not audio_file:
        return HTTPException(400, "No file uploaded")
    if audio_file.content_type != accepted_content_type:
        return HTTPException(400, "Only accept audio data")
    
    aai_client = aai.Transcriber()
    transcript = transcription.process_audio_transcript(aai_client, audio_file)
        
    return JSONResponse(content={
        "content-type": audio_file.content_type,
        "content-size": f"{audio_file.size / 1e6:.2f}mb",
        "transcript": transcript
    }, media_type="application/json")

@app.post('/summarize')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        raise HTTPException(status_code=400, detail='No Content-Type provided')
    elif content_type == 'application/json':
        try:
            payload = await request.json()
            print(payload)
            if not payload or 'transcript' not in payload:
                return HTTPException(400, "Please provide the transcript!", headers={
                    'content-type': 'application/json'
                })
            else:
                summary = chains.summarize_transcript(payload['transcript'])
                return JSONResponse(content={
                    "summary": summary
                })
        except JSONDecodeError:
            raise HTTPException(status_code=400, detail='Invalid JSON data')
    else:
        raise HTTPException(status_code=400, detail='Content-Type not supported')