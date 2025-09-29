# scripts/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Add new environment variable assignments after BASE_DIR definition

database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG", "False").lower() == "true"
port = int(os.getenv("PORT", "8000"))

# Data paths
DATA_PATHS = {
    "raw": BASE_DIR / "data" / "raw",
    "processed": BASE_DIR / "data" / "processed",
    "scripts": BASE_DIR / "scripts"
}

# API configuration
API_CONFIG = {
    "base_url": os.getenv("API_BASE_URL", "https://api.example.com"),
    "api_key": os.getenv("API_KEY")
}

# Database configuration
DATABASE_CONFIG = {
    "url": os.getenv("DATABASE_URL"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432"))
}