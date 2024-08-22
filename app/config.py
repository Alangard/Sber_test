import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class GlobalSettings(BaseSettings):
    DB_HOST: str = os.environ.get("DB_HOST", 'db')
    DB_PORT: str = os.environ.get("DB_PORT", '1221')
    DB_NAME: str = os.environ.get("DB_NAME", 'postgres')
    DB_USER: str = os.environ.get("DB_USER", 'postgres')
    DB_PASS: str = os.environ.get("DB_PASS", 'postgres')

    api_prefix: str = "/api/v1"


settings = GlobalSettings()