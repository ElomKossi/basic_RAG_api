from fastapi import FastAPI

from app import version
from app.core.logs import logger
from app.chats.api import router as chat_router
from app.core.api import router as core_router

app = FastAPI(version=version)

app.include_router(core_router)
app.include_router(chat_router)

logger.info("App is ready!")
