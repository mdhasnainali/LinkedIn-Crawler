from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


class NotFoundError(HTTPException):
    def __init__(self, detail = None):
        super().__init__(status.HTTP_404_NOT_FOUND, detail)

class DatabaseError(HTTPException):
    def __init__(self, detail = None):
        super().__init__(status.HTTP_500_INTERNAL_SERVER_ERROR, detail)

class DuplicateEntryError(HTTPException):
    def __init__(self, detail = None):
        super().__init__(status.HTTP_409_CONFLICT, detail)

class ValidationError(HTTPException):
    def __init__(self, detail = None):
        super().__init__(status.HTTP_422_UNPROCESSABLE_ENTITY, detail)