from app.core.logger import logger
from fastapi import FastAPI

app = FastAPI()

logger.info("Application start-up successful!")

