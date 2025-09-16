from pydantic import BaseModel

class LinkedInPageRequest(BaseModel):
    url: str

class LinkedInProfileRequest(BaseModel):
    url: str

class LinkedInPageResponse(BaseModel):
    id: int
    url: str
    user_count: int
    
class LinkedInProfileResponse(BaseModel):
    id: int
    url: str
    user_count: int
