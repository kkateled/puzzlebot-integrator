import os


with open(".env") as env_file:
    lines = env_file.read().splitlines()
    for line in lines:
        key, value = line.split('=')
        os.environ[key] = value


from fastapi import FastAPI
from api.config.global_config import GlobalConfig
from api.routers import any_message

app = FastAPI()

app.include_router(any_message.router, prefix="/api/v1")
conf = GlobalConfig()


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.get("/config")
async def config():
    return {"conf": conf}
