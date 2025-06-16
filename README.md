# Job Description Generator API

A professional FastAPI-based service that generates detailed job descriptions using LLM technology.

## Features

- Generate detailed job descriptions using LLMs (Groq or Ollama)
- Professional error handling with custom exceptions
- Comprehensive logging system
- Input validation and sanitization
- RESTful API with OpenAPI documentation
- Configurable through environment variables
- Extensive test coverage

## Prerequisites

- Python 3.8 or higher
- Poetry or pip for dependency management
- Groq API key (if using Groq backend)
- Ollama installation (if using Ollama backend)

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
# Development mode with auto-reload
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Usage

### Generate Job Description

```bash
curl -X POST "http://localhost:8000/api/v1/generate" \
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

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run specific test categories
pytest -m unit  # Unit tests
pytest -m integration  # Integration tests
pytest -m api  # API tests
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
│   ├── main.py
│   ├── config.py
│   ├── exceptions.py
│   ├── dependencies.py
│   ├── routers/
│   ├── services/
│   ├── types/
│   ├── utils/
│   └── middleware/
├── tests/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── setup.cfg
└── pytest.ini
```

## Error Handling

The API implements comprehensive error handling with custom exceptions:

- `InvalidJobDetailsError`: Invalid or missing job details
- `LLMConfigurationError`: LLM setup issues
- `LLMConnectionError`: Connection problems with LLM service
- `GenerationError`: Job description generation failures

## Logging

Logs are stored in the `logs` directory with automatic rotation:
- `app.log`: Main application log
- Console output for development

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.