from fastapi import APIRouter
from src.app.core.config import get_config

from src.app.modules.linkedin.api import linkedin_router

config = get_config()

api_v1 = APIRouter(prefix=f"{config.api_prefix}/v1")
api_v1.include_router(linkedin_router)
