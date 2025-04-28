from pydantic import BaseSettings

class Settings(BaseSettings):
    aimlapi_key: str
    serpapi_key: str
    database_url: str = "sqlite:///./test.db"  # Example default value

    class Config:
        env_file = ".env"

settings = Settings()