from api.routers.journal_router import router as journal_router
from fastapi import FastAPI
import logging
from dotenv import load_dotenv

load_dotenv(override=True)

console = logging.StreamHandler()
logging.basicConfig(handlers=[console], level=logging.INFO)
logger = logging.getLogger('myLogger')


app = FastAPI(title="Journal API",
              description="A simple journal API for tracking daily work, struggles, and intentions")
app.include_router(journal_router)

logger.info("Test log")
