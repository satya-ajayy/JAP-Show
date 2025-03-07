import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    REDIS_URI: str = os.getenv("REDIS_URI", "")


settings = Settings()