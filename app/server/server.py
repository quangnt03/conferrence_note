from fastapi import FastAPI

app = FastAPI(__name__)

@app.get("/test")
async def hello():
    return {
        "message": "Hello"
    }