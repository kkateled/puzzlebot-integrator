import logging
import os

if os.path.isfile(".env"):
    with open(".env") as env_file:
        lines = env_file.read().splitlines()
        for line in lines:
            key, value = line.split('=')
            os.environ[key] = value
else:
    logging.warning("Not found .env")


from fastapi import FastAPI
from api.config.global_config import GlobalConfig
from api.routers import any_message, user_authorization

app = FastAPI()

app.include_router(any_message.router, prefix="/api/v1")
app.include_router(user_authorization.router)
conf = GlobalConfig()


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.get("/config")
async def config():
    return {"conf": conf}
