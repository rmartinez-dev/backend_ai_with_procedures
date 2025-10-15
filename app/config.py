from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI MVC App"
    app_env: str = "development"
    database_url: str = "sqlite:///./app.db"
    
    db_user: str = "postgres"
    db_password: str = "admin"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "TESTING"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
