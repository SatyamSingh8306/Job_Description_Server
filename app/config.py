"""Configuration settings for the Job Description Generator API."""

from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings.
    
    Attributes:
        USE_GROQ: Whether to use Groq as the LLM backend
        MODEL_NAME: Name of the LLM model to use
        API_KEY: API key for Groq
        BASE_URL: Base URL for Ollama
        PORT: Server port
        HOST: Server host
        LOG_LEVEL: Logging level
        ENVIRONMENT: Development environment
    """
    # LLM Configuration
    USE_GROQ: bool = True
    MODEL_NAME: str = "mixtral-8x7b-32768"
    API_KEY: Optional[str] = None
    BASE_URL: str = "http://localhost:11434"
    
    # Server Configuration
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create global settings instance
settings = Settings()