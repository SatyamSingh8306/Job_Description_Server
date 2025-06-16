from pydantic import BaseModel
from typing import List, Optional

class JobDetails(BaseModel):
    title: str
    company: str
    location: str
    required_skills: List[str]
    experience_level: str
    job_type: str
    additional_requirements: Optional[List[str]] = None
    company_description: Optional[str] = None

class JobDescriptionResponse(BaseModel):
    job_description: str
    status: str = "success"
    message: Optional[str] = None 