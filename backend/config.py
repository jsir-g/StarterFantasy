import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    # Flask settings
    DEBUG = True

    # Database
    DB_URL = os.getenv("postgresql://neondb_owner:npg_69htXuOzSIPF@ep-gentle-wind-a5aame1u-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")

    # API keys
    SPORTRADAR_API_KEY = os.getenv("SPORTRADAR_API_KEY")

    # Optional future configs (JWT secret, etc.)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
