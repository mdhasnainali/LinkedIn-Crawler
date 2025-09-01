from fastapi import FastAPI
from src.app.core.config import get_config

from src.app.core.router import api_v1
from src.app.exceptions.handlers import register_exception_handlers

# only expose docs & openapi when not in prod

config = get_config()
IS_PROD = config.app_env == "production"
docs_url = None if IS_PROD else f"{config.api_prefix}/v1/swagger"
openapi_url = None if IS_PROD else f"{config.api_prefix}/v1/openapi.json"

app = FastAPI(
    title=config.project_name,
    docs_url=docs_url,
    redoc_url=None,           # you can similarly gate ReDoc if you use it
    openapi_url=openapi_url   # helps tp get details info in a json schema
)

# Register Exception Handlers
register_exception_handlers(app)

# Add Router
app.include_router(api_v1)
