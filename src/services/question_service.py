from src.services.openai_service import OpenaiService


class QuestionService:
    openai_service: OpenaiService

    def __init__(self, openai_service: OpenaiService) -> None:
        self.openai_service = openai_service

    async def question(self, message: str) -> str:
        return await self.openai_service.get_message(message=message)
