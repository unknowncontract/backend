from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from dependency_injector.wiring import Provide, inject
from src.core.container import Container
from src.dto.question import QuestionBody, QuestionRes
from src.services.question_service import QuestionService
from src.services import OpenaiService

router = APIRouter(
    prefix="/question",
    tags=["question"],
)


@router.post("", response_model=QuestionRes)
@inject
async def ask(
    question: QuestionBody,
    service: QuestionService = Depends(Provide[Container.question_service]),
):
    return ORJSONResponse(content={"message": await service.question(question.message)})


@router.post("/parse", response_model=QuestionRes)
@inject
async def parse(
    question: QuestionBody,
    service: OpenaiService = Depends(Provide[Container.openai_service]),
):
    return ORJSONResponse(
        content={"message": await service.parse_data(question.message)}
    )
