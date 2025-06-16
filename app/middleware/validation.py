"""Request validation middleware for the Job Description Generator API."""

from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from typing import Callable
from app.exceptions import InvalidJobDetailsError

async def validation_error_handler(request: Request, call_next: Callable):
    """Middleware to handle validation errors globally."""
    try:
        return await call_next(request)
    except ValidationError as exc:
        errors = []
        for error in exc.errors():
            error_msg = {
                'field': error['loc'][-1],
                'message': error['msg'],
                'type': error['type']
            }
            errors.append(error_msg)
        
        return JSONResponse(
            status_code=422,
            content={
                'status': 'error',
                'message': 'Validation error',
                'errors': errors
            }
        )
    except InvalidJobDetailsError as exc:
        return JSONResponse(
            status_code=400,
            content={
                'status': 'error',
                'message': str(exc)
            }
        )