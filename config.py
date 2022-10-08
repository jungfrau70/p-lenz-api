from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "REAL_TIME NOTIFICATION API"

    class Config:
        env_file = ".env"