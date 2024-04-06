from fastapi import FastAPI

from app.core.logs import logger

# in here we just initialise the fastapi app, without defining
# any endpoints
app = FastAPI()
logger.info("App is ready!")