from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str

    MODEL_NAME: str = "gemini-2.5-flash"

    LOG_LEVEL: str = "INFO"

    APP_NAME: str = "SHL Assessment Recommendation Agent"

    API_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()