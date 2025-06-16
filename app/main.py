from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.app_v1 import api_v1_router
from app.exceptions import (
    JobDescriptionGeneratorError,
    LLMConfigurationError,
    LLMConnectionError,
    InvalidJobDetailsError,
    GenerationError
)

app = FastAPI(
    title="Job Description Generator",
    description="API for generating job descriptions using LLMs",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Exception handlers for specific application errors
@app.exception_handler(LLMConfigurationError)
async def llm_configuration_exception_handler(request: Request, exc: LLMConfigurationError):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "error_type": "configuration_error",
            "message": "LLM configuration error",
            "detail": str(exc)
        }
    )

@app.exception_handler(LLMConnectionError)
async def llm_connection_exception_handler(request: Request, exc: LLMConnectionError):
    return JSONResponse(
        status_code=503,  # Service Unavailable
        content={
            "status": "error",
            "error_type": "connection_error",
            "message": "Unable to connect to LLM service",
            "detail": str(exc)
        }
    )

@app.exception_handler(InvalidJobDetailsError)
async def invalid_job_details_exception_handler(request: Request, exc: InvalidJobDetailsError):
    return JSONResponse(
        status_code=400,  # Bad Request
        content={
            "status": "error",
            "error_type": "validation_error",
            "message": "Invalid job details provided",
            "detail": str(exc)
        }
    )

@app.exception_handler(GenerationError)
async def generation_exception_handler(request: Request, exc: GenerationError):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "error_type": "generation_error",
            "message": "Error generating job description",
            "detail": str(exc)
        }
    )

# Generic handler for the base exception class
@app.exception_handler(JobDescriptionGeneratorError)
async def job_description_exception_handler(request: Request, exc: JobDescriptionGeneratorError):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "error_type": "application_error",
            "message": str(exc)
        }
    )

# Handle FastAPI validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,  # Unprocessable Entity
        content={
            "status": "error",
            "error_type": "validation_error",
            "message": "Request validation failed",
            "detail": exc.errors()
        }
    )

# Handle HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "error_type": "http_error",
            "message": exc.detail
        }
    )

# Global exception handler for unexpected errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "error_type": "internal_error",
            "message": "An unexpected error occurred",
            "detail": str(exc) if app.debug else "Internal server error"
        }
    )

# Include v1 API router
app.include_router(api_v1_router, prefix="/api/v1")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Job Description Generator API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True  # Enable auto-reload in development
    )