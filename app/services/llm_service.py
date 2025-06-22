import os
from typing import Optional, Dict, Any
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain.schema.output import LLMResult
from app import USE_GROQ, MODEL_NAME, API_KEY, BASE_URL
from app.utils.errors.exceptions import (
    LLMConfigurationError,
    LLMConnectionError,
    InvalidJobDetailsError,
    GenerationError
)
from app.utils.logger import logger

class LLMService:
    def __init__(self):
        self.use_groq = USE_GROQ
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        try:
            logger.info(f"Initializing LLM service with backend: {'Groq' if self.use_groq else 'Ollama'}")
            if self.use_groq:
                if not API_KEY:
                    logger.error("API_KEY not found in environment variables")
                    raise LLMConfigurationError("API_KEY not found in environment variables")
                logger.info(f"Initializing Groq with model: {MODEL_NAME}")
                return ChatGroq(
                    api_key=API_KEY,
                    model_name=MODEL_NAME
                )
            else:
                logger.info(f"Initializing Ollama with model: {MODEL_NAME}")
                return ChatOllama(
                    base_url=BASE_URL,
                    model=MODEL_NAME
                )
        except Exception as e:
            logger.error(f"LLM initialization failed: {str(e)}")
            raise LLMConfigurationError(f"Failed to initialize LLM: {str(e)}")

    def _validate_job_details(self, job_details: Dict[str, Any]) -> None:
        logger.info("Validating job details")
        required_fields = ["title", "company", "location", "required_skills", 
                          "experience_level", "job_type"]
        missing_fields = [field for field in required_fields if not job_details.get(field)]
        if missing_fields:
            error_msg = f"Missing required fields: {', '.join(missing_fields)}"
            logger.error(error_msg)
            raise InvalidJobDetailsError(error_msg)
        logger.info("Job details validation successful")

    def generate_job_description(self, job_details: Dict[str, Any]) -> str:
        logger.info(f"Generating job description for position: {job_details.get('title', 'Unknown Title')}")
        try:
            self._validate_job_details(job_details)
            prompt_template = """
                You are an expert HR professional. Create a detailed job description based on the following details:

                Job Title: {title}
                Company: {company}
                Location: {location}
                Required Skills: {required_skills}
                Experience Level: {experience_level}
                Job Type: {job_type}
                Additional Requirements: {additional_requirements}
                Company Description: {company_description}

                Please create a comprehensive job description that includes:
                1. A compelling introduction
                2. Detailed responsibilities
                3. Required qualifications and skills
                4. Preferred qualifications
                5. Company benefits and culture
                6. Call to action

                Format the response in a professional and engaging manner.
            """

            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=[
                    "title", "company", "location", "required_skills",
                    "experience_level", "job_type", "additional_requirements",
                    "company_description"
                ]
            )

            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            # Convert lists to strings for the prompt
            job_details["required_skills"] = ", ".join(job_details["required_skills"])
            if job_details.get("additional_requirements"):
                job_details["additional_requirements"] = ", ".join(job_details["additional_requirements"])
            else:
                job_details["additional_requirements"] = "None specified"

            logger.info("Executing LLM chain for job description generation")
            response = chain.run(**job_details)
            if not response or not isinstance(response, str):
                logger.error("Generated response is invalid or empty")
                raise GenerationError("Generated response is invalid")
            logger.info("Job description generated successfully")
            return response.strip()
            
        except (LLMConfigurationError, InvalidJobDetailsError, GenerationError):
            raise
        except Exception as e:
            logger.error(f"Error during job description generation: {str(e)}")
            raise LLMConnectionError(f"Error during job description generation: {str(e)}")