from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = Field(...)
    ALGORITHM: str = Field(...)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(...)
    FRONTEND_URL: str = Field(...)
    GOOGLE_API_KEY: str = Field(...)
    HF_TOKEN: str = Field(...)
    DATABASE_URL: str = Field(...)
    ENDPOINT: str = Field(...)
    KEY: str = Field(...)

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
