from fastapi import APIRouter
from app.routers import job_description

api_v1_router = APIRouter()

# Include all v1 routers
api_v1_router.include_router(
    job_description.router,
    prefix="/job-description",
    tags=["job-description"]
)

# Add more v1 routers here as needed 