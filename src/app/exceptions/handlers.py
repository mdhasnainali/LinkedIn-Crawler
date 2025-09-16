from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.app.exceptions.errors import NotFoundError, DatabaseError, DuplicateEntryError, ValidationError
from src.app.core.logger import logger
from src.app.exceptions.schemas import ErrorResponse

def register_exception_handlers(application: FastAPI):
    @application.exception_handler(NotFoundError)
    async def not_found_error(request: Request, exc: NotFoundError):
        logger.warning(f"Not found error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="404",
            message="Not found",
            details=exc.detail,
        )
        return JSONResponse(content=payload.model_dump(), status_code=exc.status_code)

    @application.exception_handler(DatabaseError)
    async def database_error(request: Request, exc: DatabaseError):
        logger.error(f"Database error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="500",
            message="Database error occurred",
            details=exc.detail,
        )
        return JSONResponse(content=payload.model_dump(), status_code=exc.status_code)

    @application.exception_handler(DuplicateEntryError)
    async def duplicate_entry_error(request: Request, exc: DuplicateEntryError):
        logger.warning(f"Duplicate entry error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="409",
            message="Duplicate entry",
            details=exc.detail,
        )
        return JSONResponse(content=payload.model_dump(), status_code=exc.status_code)

    @application.exception_handler(ValidationError)
    async def validation_error_handler(request: Request, exc: ValidationError):
        logger.warning(f"Validation error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="422",
            message="Validation error",
            details=exc.detail,
        )
        return JSONResponse(content=payload.model_dump(), status_code=exc.status_code)

    # Handle raw SQLAlchemy exceptions that might slip through
    @application.exception_handler(IntegrityError)
    async def sqlalchemy_integrity_error(request: Request, exc: IntegrityError):
        logger.error(f"SQLAlchemy integrity error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="409",
            message="Database integrity constraint violated",
            details="A unique constraint or foreign key constraint was violated",
        )
        return JSONResponse(content=payload.model_dump(), status_code=409)

    @application.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error(request: Request, exc: SQLAlchemyError):
        logger.error(f"SQLAlchemy error at {request.url}: {exc}")
        payload = ErrorResponse(
            code="500",
            message="Database operation failed",
            details="An unexpected database error occurred",
        )
        return JSONResponse(content=payload.model_dump(), status_code=500)