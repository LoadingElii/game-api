from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Game API"
    debug: bool = True
    version: str = "1.0.0"
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379

    class Config:
        env_file = ".env"


settings = Settings()