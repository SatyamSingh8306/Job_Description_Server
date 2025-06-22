# Job Description Generator API

A FastAPI-based API for generating professional job descriptions using LLMs (Groq or Ollama), with robust error handling, logging, and a Streamlit app for easy testing.

## Features

- Generate detailed job descriptions using LLMs (Groq or Ollama)
- Professional error handling with custom exceptions
- Comprehensive logging system
- Input validation and sanitization
- RESTful API with OpenAPI documentation
- Configurable through environment variables
- Streamlit app for interactive API testing
- Extensive test coverage

## Prerequisites

- Python 3.8 or higher
- pip for dependency management
- Groq API key (if using Groq backend)
- Ollama installation (if using Ollama backend)
- (Optional) Streamlit for UI testing

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/job-description-generator.git
cd job-description-generator

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
# LLM Configuration
USE_GROQ=true  # Set to false to use Ollama
API_KEY=your_groq_api_key  # Required if USE_GROQ is true
MODEL_NAME=mixtral-8x7b-32768
BASE_URL=http://localhost:11434  # Ollama base URL

# Server Configuration
PORT=8000
HOST=0.0.0.0

# Logging
LOG_LEVEL=INFO
ENVIRONMENT=development
```

## Running the Server

```bash

python -m app
# Development mode with auto-reload
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, access the API documentation at:
- Swagger UI: `http://localhost:8000/v1/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Usage

### Generate Job Description

```bash
curl -X POST "http://localhost:8000/v1/job-description/generate" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Senior Software Engineer",
           "company": "Tech Corp",
           "location": "San Francisco, CA",
           "required_skills": ["Python", "FastAPI", "AWS"],
           "experience_level": "5+ years",
           "job_type": "Full-time",
           "additional_requirements": ["Team leadership"],
           "company_description": "Leading tech company"
         }'
```

## Streamlit App for Testing

You can interactively test the API using the included Streamlit app:

1. (Optional) Uncomment `streamlit` in `requirements.txt` and install it:
   ```bash
   pip install streamlit
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Use the web UI to check API health and generate job descriptions.

## Development

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black .
isort .

# Lint code
flake8

# Type checking
mypy .
```

### Project Structure

```
├── app/
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py
│   ├── app_v1.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── job_description.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── llm_service.py
│   ├── types/
│   │   ├── __init__.py
│   │   └── job_description.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── errors/
│           └── exceptions.py
├── streamlit_app.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── Dockerfile
```

## Error Handling

The API implements comprehensive error handling with custom exceptions (see `app/utils/errors/exceptions.py`).

## Logging

Logs are output to the console for development. You can extend logging in `app/utils/logger.py`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.