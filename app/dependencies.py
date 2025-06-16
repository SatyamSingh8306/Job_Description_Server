from functools import lru_cache
from app.services.llm_service import LLMService

@lru_cache()
def get_llm_service() -> LLMService:
    """
    Get or create an instance of LLMService.
    Uses lru_cache to ensure we only create one instance.
    """
    return LLMService() 