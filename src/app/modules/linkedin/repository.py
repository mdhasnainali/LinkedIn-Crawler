from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.app.core.db import get_db
from src.app.core.logger import logger
from src.app.exceptions.errors import DatabaseError, DuplicateEntryError

from .models import PageUrl, ProfileUrl

class LinkedInRepository:
    def __init__(self, db: Annotated[AsyncSession, Depends(get_db)]):
        self.db = db
    
    async def create_linkedin_url(self, url: str, url_type: str):
        try:
            if url_type == "profile":
                data = ProfileUrl(url=url)
            else:
                data = PageUrl(url=url)

            self.db.add(data)
            await self.db.commit()
            await self.db.refresh(data)
            logger.info(f"Created {url_type} URL: {url}")
            return data
            
        except IntegrityError as e:
            await self.db.rollback()
            logger.warning(f"Duplicate URL attempted: {url}")
            if "unique constraint" in str(e).lower():
                raise DuplicateEntryError(f"URL already exists: {url}")
            else:
                raise DatabaseError(f"Database integrity error: {str(e)}")
                
        except SQLAlchemyError as e:
            await self.db.rollback()
            logger.error(f"Database error creating {url_type} URL: {str(e)}")
            raise DatabaseError(f"Failed to create {url_type} URL: {str(e)}")
        
        except Exception as e:
            await self.db.rollback()
            logger.error(f"Unexpected error creating {url_type} URL: {str(e)}")
            raise DatabaseError(f"Unexpected error occurred: {str(e)}")