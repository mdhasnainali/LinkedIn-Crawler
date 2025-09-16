from typing import Annotated
from fastapi import Depends
from src.app.modules.linkedin.repository import LinkedInRepository
from src.app.core.logger import logger

class LinkedInServices:
    def __init__(self, repository: Annotated[LinkedInRepository, Depends()]):
        self.repository = repository
    
    async def create_linkedin_profile_url(self, url: str):
        return await self.repository.create_linkedin_url(url, "profile")
    
    async def create_linkedin_page_url(self, url: str):
        return await self.repository.create_linkedin_url(url, "page") 
        
