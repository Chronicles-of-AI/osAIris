import uvicorn

from core_engine.apis.api import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
