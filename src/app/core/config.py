from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache

class Config(BaseSettings):
    # general
    project_name: str = "Notepad_App"
    api_prefix: str = Field(default="/api", alias="API_PREFIX")
    
    # environment
    app_env: str = Field(default= "development", alias="APP_ENV")
    
    # postgres credentials
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD")
    postgres_host: str = Field(alias="POSTGRES_HOST")
    postgres_port: str = Field(alias="POSTGRES_PORT")
    postgres_db: str = Field(alias="POSTGRES_DB")
    
    @property
    def db_url(self):
        return (
            f"postgresql+psycopg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
    
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"

@lru_cache
def get_config() -> Config:
    return Config()

