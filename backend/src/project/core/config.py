import os

from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "d966aeeb45d5a75e2c2267522d572e1e1d3bbbee3b56098190064e57555bfc25")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ORIGINS: str = "*"
    ROOT_PATH: str = ""
    ENV: str = "DEV"
    LOG_LEVEL: str = "DEBUG"

    POSTGRES_SCHEMA: str = "university"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_DB: str = "university"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: SecretStr = "postgres"
    POSTGRES_PASSWORD: SecretStr = "postgres"
    POSTGRES_RECONNECT_INTERVAL_SEC: int = 1

    @property
    def postgres_url(self) -> str:
        creds = f"{self.POSTGRES_USER.get_secret_value()}:{self.POSTGRES_PASSWORD.get_secret_value()}"
        return f"postgresql+asyncpg://{creds}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
