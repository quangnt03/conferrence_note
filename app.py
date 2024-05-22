import uvicorn
import app
import os

if __name__ == "__main__":
    evn = os.getenv("env") | "dev"
    auto_reload = evn == "dev"
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=auto_reload)