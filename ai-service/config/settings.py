from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REVIEW_API: str = "http://localhost:5083/api/Reviews"

    class Config:
        env_file = ".env"


settings = Settings()