from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.app_v1 import api_v1_router


app = FastAPI(
    title="Job Description Generator",
    description="API for generating job descriptions using LLMs",
    version="1.0.0",
    docs_url="/v1/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",
                   "https://localhost:8000",
                   "https://localhost:8501"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Include v1 API router
app.include_router(api_v1_router, prefix="/v1")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Job Description Generator API is running"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Description Generator API. See /docs for API documentation."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True  # Enable auto-reload in development
    )