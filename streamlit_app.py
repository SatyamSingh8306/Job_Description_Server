import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"
API_DOCS_URL = f"{API_BASE_URL}/v1/docs"
HEALTH_URL = f"{API_BASE_URL}/health"
GENERATE_URL = f"{API_BASE_URL}/v1/job-description/generate"

# Default data for testing
default_job_details = {
    "title": "Senior Software Engineer",
    "company": "Tech Corp",
    "location": "San Francisco, CA",
    "required_skills": ["Python", "FastAPI", "AWS"],
    "experience_level": "5+ years",
    "job_type": "Full-time",
    "additional_requirements": ["Team leadership"],
    "company_description": "Leading tech company"
}

st.title("Job Description Generator API Checker")

# Health check
st.header("API Health Check")
try:
    health_resp = requests.get(HEALTH_URL, timeout=3)
    if health_resp.status_code == 200:
        st.success(f"API is healthy: {health_resp.json()}")
    else:
        st.error(f"API health check failed: {health_resp.status_code} {health_resp.text}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

# Docs link
st.markdown(f"[Open API Docs]({API_DOCS_URL})")

# Job Description Generation Test
st.header("Test Job Description Generation")
with st.form("generate_form"):
    title = st.text_input("Job Title", default_job_details["title"])
    company = st.text_input("Company", default_job_details["company"])
    location = st.text_input("Location", default_job_details["location"])
    required_skills = st.text_area("Required Skills (comma separated)", ", ".join(default_job_details["required_skills"]))
    experience_level = st.text_input("Experience Level", default_job_details["experience_level"])
    job_type = st.text_input("Job Type", default_job_details["job_type"])
    additional_requirements = st.text_area("Additional Requirements (comma separated)", ", ".join(default_job_details["additional_requirements"]))
    company_description = st.text_area("Company Description", default_job_details["company_description"])
    submit = st.form_submit_button("Generate Job Description")

    if submit:
        payload = {
            "title": title,
            "company": company,
            "location": location,
            "required_skills": [s.strip() for s in required_skills.split(",") if s.strip()],
            "experience_level": experience_level,
            "job_type": job_type,
            "additional_requirements": [s.strip() for s in additional_requirements.split(",") if s.strip()],
            "company_description": company_description
        }
        try:
            resp = requests.post(GENERATE_URL, json=payload, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                st.success("Job Description Generated Successfully!")
                st.write(data)
                st.markdown(f"**Job Description:**\n\n{data.get('job_description', '')}")
            else:
                st.error(f"Error: {resp.status_code} {resp.text}")
        except Exception as e:
            st.error(f"Request failed: {e}") 