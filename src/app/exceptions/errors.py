from fastapi import HTTPException, status

class NotFoundError(HTTPException):
    def __init__(self, detail = None):
        super().__init__(status.HTTP_404_NOT_FOUND, detail)
        