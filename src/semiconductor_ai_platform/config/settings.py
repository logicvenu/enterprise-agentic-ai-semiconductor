from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validated application settings; secrets must be injected at runtime."""

    model_config = SettingsConfigDict(
        env_prefix="SAP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Semiconductor AI Platform"
    environment: Literal["local", "dev", "test", "aws"] = "local"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    api_v1_prefix: str = "/api/v1"
    enable_request_id_middleware: bool = True
    service_version: str = "0.1.0"


@lru_cache
def get_settings() -> Settings:
    """Return cached settings for dependency injection."""
    return Settings()


def clear_settings_cache() -> None:
    """Clear settings cache, primarily for tests."""
    get_settings.cache_clear()
