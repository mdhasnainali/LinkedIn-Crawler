from fastapi import APIRouter
from src.app.core.config import get_config

from src.app.modules.todo.api import todo_router

config = get_config()

api_v1 = APIRouter(prefix=f"{config.api_prefix}/v1")
api_v1.include_router(todo_router)
