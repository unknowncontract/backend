import openai
from src.core.config import config


class OpenaiService:
    async def get_message(self, message: str) -> str:
        response = openai.ChatCompletion.create(
            api_key=config.openai_secret_key,
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 부동산 전문 변호사야. 답은 무조건 목록 형태로 해."},
                {"role": "user", "content": message},
            ],
        )

        return response["choices"][0]["message"]["content"]
