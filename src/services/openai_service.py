import openai
from src.core.config import config
from src.constants.prompt import prompt_contract
import json


class OpenaiService:
    async def get_message(self, message: str) -> str:
        response = openai.ChatCompletion.create(
            api_key=config.openai_secret_key,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "너는 부동산 전문 변호사야. 답은 무조건 목록 형태로 해."},
                {"role": "user", "content": message},
            ],
        )

        return response["choices"][0]["message"]["content"]

    async def parse_data(self, text: str) -> str:
        response = openai.ChatCompletion.create(
            api_key=config.openai_secret_key,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_contract},
                {"role": "user", "content": text},
            ],
        )

        return response["choices"][0]["message"]["content"]

    async def message(self, prompt: str, text: str) -> str:
        response = openai.ChatCompletion.create(
            api_key=config.openai_secret_key,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text},
            ],
        )

        return response["choices"][0]["message"]["content"]

    async def parse(self, prompt: str, data: str) -> dict:
        response = openai.ChatCompletion.create(
            api_key=config.openai_secret_key,
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly assistant. Your answers are JSON only.",
                },
                {
                    "role": "assistant",
                    "content": '{"message": "Understood. I will output my answers in JSON format." }',
                },
                {"role": "system", "content": prompt},
                {"role": "user", "content": data},
            ],
        )

        message = response["choices"][0]["message"]["content"]

        return json.loads(message)
