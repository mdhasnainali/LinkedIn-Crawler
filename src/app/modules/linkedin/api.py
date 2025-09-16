from typing import Annotated
from fastapi import APIRouter
from fastapi_restful.cbv import cbv 
from fastapi import Depends

from src.app.core.logger import logger
from src.app.exceptions.errors import DatabaseError, DuplicateEntryError
from src.app.modules.linkedin.service import LinkedInServices

from .schemas import LinkedInPageRequest, LinkedInProfileRequest, LinkedInPageResponse, LinkedInProfileResponse

linkedin_router = APIRouter(prefix="/linkedin")

@cbv(linkedin_router)
class LinkedInController:
    def __init__(self, service: Annotated[LinkedInServices, Depends()]):
        self.service = service

    @linkedin_router.post("/linkedin_page_url", response_model=LinkedInPageResponse)
    async def post_linkedin_page_url(self, payload: LinkedInPageRequest) -> LinkedInPageResponse:        
        try:
            response = await self.service.create_linkedin_page_url(payload.url)
            return LinkedInPageResponse(id=response.id, url=response.url, user_count=1)
        except DuplicateEntryError:
            raise
        except DatabaseError:
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating LinkedIn page URL: {str(e)}")
            raise DatabaseError(f"Failed to create LinkedIn page URL: {str(e)}")

    @linkedin_router.post("/linkedin_profile_url", response_model=LinkedInProfileResponse)
    async def post_linkedin_profile_url(self, payload: LinkedInProfileRequest) -> LinkedInProfileResponse:
        try:
            response = await self.service.create_linkedin_profile_url(payload.url)
            return LinkedInProfileResponse(id=response.id, url=response.url, user_count=1)
        except DuplicateEntryError:
            raise
        except DatabaseError:
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating LinkedIn profile URL: {str(e)}")
            raise DatabaseError(f"Failed to create LinkedIn profile URL: {str(e)}")