"""Test suite for the Job Description Generator API."""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.llm_service import LLMService
from app.exceptions import (
    InvalidJobDetailsError,
    LLMConfigurationError,
    GenerationError
)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_job_details():
    return {
        "title": "Senior Software Engineer",
        "company": "Tech Corp",
        "location": "San Francisco, CA",
        "required_skills": ["Python", "FastAPI", "AWS"],
        "experience_level": "5+ years",
        "job_type": "Full-time",
        "additional_requirements": ["Team leadership"],
        "company_description": "Leading tech company"
    }

@pytest.mark.api
def test_root_endpoint(client):
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert "message" in response.json()

@pytest.mark.api
def test_test_endpoint(client):
    response = client.get("/api/v1/test")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

@pytest.mark.api
def test_generate_job_description_success(client, valid_job_details):
    response = client.post("/api/v1/generate", json=valid_job_details)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "job_description" in response.json()

@pytest.mark.api
def test_generate_job_description_missing_fields(client):
    invalid_details = {
        "title": "Senior Engineer"
    }
    response = client.post("/api/v1/generate", json=invalid_details)
    assert response.status_code == 422  # Validation error

@pytest.mark.unit
def test_llm_service_validation():
    service = LLMService()
    with pytest.raises(InvalidJobDetailsError):
        service.generate_job_description({"title": "Incomplete Job"})

@pytest.mark.integration
def test_generate_job_description_integration(valid_job_details):
    service = LLMService()
    result = service.generate_job_description(valid_job_details)
    assert isinstance(result, str)
    assert len(result) > 0