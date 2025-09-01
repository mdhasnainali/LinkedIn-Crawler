from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.app.exceptions.errors import NotFoundError

from src.app.core.logger import logger
from src.app.exceptions.schemas import ErrorResponse

# Handle the error using decorator
def register_exception_handlers(application: FastAPI):
    @application.exception_handler(NotFoundError)
    async def not_found_error(request: Request, exc: NotFoundError):
        logger.warning(f"Validation error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="404",
            message="Not found",
            details=exc.detail,
        )
        return JSONResponse(exc.status_code, content=payload.model_dump())
