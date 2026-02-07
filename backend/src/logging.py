import logging
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import traceback


def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )


def log_exception(request: Request, exc: Exception):
    """Log exception details"""
    logging.error(f"Exception in {request.method} {request.url}")
    logging.error(f"Exception type: {type(exc).__name__}")
    logging.error(f"Exception details: {str(exc)}")
    logging.error(f"Traceback: {traceback.format_exc()}")


def exception_handler(request: Request, exc: Exception):
    """Handle exceptions and return appropriate response"""
    log_exception(request, exc)
    
    # Return different responses based on exception type
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    
    # For other exceptions, return a generic 500 error
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )