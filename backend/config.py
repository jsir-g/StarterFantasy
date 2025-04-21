# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True
    DB_URL = os.getenv("NEON_DB_URL")
    SPORTRADAR_API_KEY = os.getenv("SPORTRADAR_API_KEY")
