import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class GlobalSettings(BaseSettings):
    DB_HOST: str = os.environ.get("DB_HOST", "db")
    DB_PORT: str = os.environ.get("DB_PORT", "1221")
    DB_NAME: str = os.environ.get("DB_NAME", "postgres")
    DB_USER: str = os.environ.get("DB_USER", "postgres")
    DB_PASS: str = os.environ.get("DB_PASS", "postgres")

    DB_HOST_TEST: str = os.environ.get("DB_HOST_TEST", "db")
    DB_PORT_TEST: str = os.environ.get("DB_PORT_TEST", "6000")
    DB_NAME_TEST: str = os.environ.get("DB_NAME_TEST", "postgres")
    DB_USER_TEST: str = os.environ.get("DB_USER_TEST", "postgres")
    DB_PASS_TEST: str = os.environ.get("DB_PASS_TEST", "postgres")

    DOMAIN_NAME: str = os.environ.get("DOMAIN_NAME", "http://127.0.0.1:8000")

    api_prefix: str = "/api/v1"


settings = GlobalSettings()
