from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI 0.116.1 App"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()