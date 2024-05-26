import uvicorn
from app import main
import os

if __name__ == "__main__":
    env = os.environ.get("ENV") if os.environ.get("ENV") else "dev"
    auto_reload = env == "dev"
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=auto_reload)