from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    db_host: str = ""
    db_port: str = ""
    db_username: str = ""
    db_password: str = ""
    db_name: str = ""
    openai_secret_key: str = ""

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
