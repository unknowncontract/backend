import openai
from src.core.config import config


openai.api_key = config.openai_secret_key


class OpenaiService:
    async def get_message(self, message: str) -> str:
        return message
