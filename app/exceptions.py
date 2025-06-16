"""Custom exceptions for the Job Description Generator API."""

class JobDescriptionGeneratorError(Exception):
    """Base exception for Job Description Generator."""
    def __init__(self, message: str = "An error occurred in the Job Description Generator"):
        self.message = message
        super().__init__(self.message)

class LLMConfigurationError(JobDescriptionGeneratorError):
    """Raised when there are issues with LLM configuration."""
    def __init__(self, message: str = "LLM configuration error"):
        super().__init__(message)

class LLMConnectionError(JobDescriptionGeneratorError):
    """Raised when there are connection issues with the LLM service."""
    def __init__(self, message: str = "Failed to connect to LLM service"):
        super().__init__(message)

class InvalidJobDetailsError(JobDescriptionGeneratorError):
    """Raised when job details are invalid or incomplete."""
    def __init__(self, message: str = "Invalid or incomplete job details provided"):
        super().__init__(message)

class GenerationError(JobDescriptionGeneratorError):
    """Raised when there's an error in generating the job description."""
    def __init__(self, message: str = "Failed to generate job description"):
        super().__init__(message)