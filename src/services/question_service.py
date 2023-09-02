from src.services.openai_service import OpenaiService
from src.constants.prompt import *
from src.constants.warn import building, owner
from src.dto.question import QuestionRes


class QuestionService:
    openai_service: OpenaiService

    def __init__(self, openai_service: OpenaiService) -> None:
        self.openai_service = openai_service

    async def question(self, message: str) -> str:
        return await self.openai_service.get_message(message=message)

    async def owner(self, data: str):
        parse = await self.openai_service.parse(prompt_owner, data)

        result = []
        self.validate_nested(parse, list(owner.keys()), result)

        return {
            "type": "owner",
            "score": ((len(owner) - len(result)) / len(owner)) * 100,
            "warnings": {key: owner[key] for key in result},
        }

    async def building(self, data: str) -> QuestionRes:
        parse = await self.openai_service.parse(prompt_building, data)

        result = []
        self.validate_nested(parse, list(building.keys()), result)

        return {
            "type": "building",
            "score": ((len(building) - len(result)) / len(building)) * 100,
            "warnings": {key: building[key] for key in result},
        }

    async def contract(self, data: str):
        data = await self.openai_service.message(prompt_contract, data)

        print(data)

    def validate_nested(self, data, warn_list: list[str], result: list[str]):
        if isinstance(data, str):
            if data in warn_list:
                result.append(data)
            return

        if isinstance(data, dict):
            for k, v in data.items():
                self.validate_nested(k, warn_list, result)
                self.validate_nested(v, warn_list, result)

        if isinstance(data, list):
            for v2 in data:
                self.validate_nested(v2, warn_list, result)

    def print_nested(self, data, depth=0):
        if isinstance(data, str):
            print(("-" * depth) + " " + data)
            return

        if isinstance(data, dict):
            for k, v in data.items():
                print(("-" * depth) + " " + k)
                self.print_nested(v, depth=depth + 1)

        if isinstance(data, list):
            for v2 in data:
                self.print_nested(v2, depth=depth)
