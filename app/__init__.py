"""
Job Description Generator Service
"""
import os
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LLM Configuration
USE_GROQ = os.getenv("USE_GROQ", "true").lower() == "true"
MODEL_NAME = os.getenv("MODEL_NAME", "mixtral-8x7b-32768")
API_KEY = os.getenv("GROQ_API_KEY", "")
BASE_URL = os.getenv("BASE_URL", "http://localhost:11434")

# Server Configuration
PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# CORS Configuration
ALLOWED_ORIGINS = ["*"]
ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]

# API Configuration
API_VERSION = "1.0.0"

__version__ = API_VERSION 