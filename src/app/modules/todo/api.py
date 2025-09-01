from fastapi import APIRouter
from fastapi_restful.cbv import cbv 
from src.app.core.logger import logger
from src.app.exceptions.errors import NotFoundError

todo_router = APIRouter(prefix="/todo")

@cbv(todo_router)
class ToDoController:
    def __init__(self):
        pass
    
    @todo_router.get("/")
    def get_hello(self):
        logger.info("Test Logging")    
        raise NotFoundError("No Found: API")

        return {"test": "hello"}
    