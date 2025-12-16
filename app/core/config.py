from pydantic import BaseSettings



class Settings(BaseSettings):
    """Application configuration settings."""

    # Application metadata
    title: str = "Hotel Management API"
    Version: str = "1.0.0"
    env_name: str = "Development"

    # Debug mode
    DEBUG: bool = True

    # Database settings
    DATABASE_URL: str

    # Security settings
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 86400  # Token expiration time in minutes

    
    class Config:
        env_file = ".env"


settings = Settings()