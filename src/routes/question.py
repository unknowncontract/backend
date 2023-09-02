from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from dependency_injector.wiring import Provide, inject
from src.core.container import Container
from src.dto.question import QuestionBody, QuestionRes, QuestionType
from src.services.question_service import QuestionService
from src.services import OpenaiService
from json import loads

router = APIRouter(
    prefix="/question",
    tags=["question"],
)


@router.post("/", response_model=QuestionRes)
@inject
async def question(
    question: QuestionBody,
    service: QuestionService = Depends(Provide[Container.question_service]),
):
    data: QuestionRes = None

    match question.type:
        case QuestionType.OWNER:
            data = await service.owner(question.data)
        case QuestionType.BUILDING:
            data = await service.building(question.data)
        case QuestionType.CONTRACT:
            data = await service.contract(question.data)

    return ORJSONResponse(content=data)
