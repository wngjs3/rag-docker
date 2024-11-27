from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DEBUG: bool = False
    AWS_REGION: str
    OPENSEARCH_ENDPOINT: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    INDEX_NAME: str = "rag-embeddings"
    
    class Config:
        env_file = ".env.dev"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings() 