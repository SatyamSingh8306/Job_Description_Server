from fastapi import APIRouter, HTTPException, Depends, status
from app.types.job_description import JobDetails, JobDescriptionResponse
from app.services.llm_service import LLMService
from app.dependencies import get_llm_service
from app.utils.logger import logger
from app.utils.errors.exceptions import (
    LLMConfigurationError,
    LLMConnectionError,
    InvalidJobDetailsError,
    GenerationError,
    JobDescriptionGeneratorError
)

router = APIRouter()

@router.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {
        "message": "Job Description Generator API",
        "endpoints": {
            "generate": "/generate (POST) - Generate job description",
            "test": "/test (GET) - Test endpoint"
        }
    }

@router.get("/test")
async def test_endpoint():
    logger.info("Test endpoint accessed")
    return {
        "status": "success",
        "message": "API is working!"
    }

@router.post("/generate", response_model=JobDescriptionResponse)
async def generate_job_description(
    job_details: JobDetails,
    llm_service: LLMService = Depends(get_llm_service)
):
    logger.info(f"Received job description generation request for position: {job_details.title}")
    try:
        job_description = llm_service.generate_job_description(job_details.dict())
        logger.info("Successfully generated job description")
        return JobDescriptionResponse(
            job_description=job_description,
            status="success",
            message="Job description generated successfully"
        )
    except InvalidJobDetailsError as e:
        logger.error(f"Invalid job details: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except LLMConfigurationError as e:
        logger.error(f"LLM configuration error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e)
        )
    except LLMConnectionError as e:
        logger.error(f"LLM connection error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )
    except GenerationError as e:
        logger.error(f"Generation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    except JobDescriptionGeneratorError as e:
        logger.error(f"Job description generator error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )