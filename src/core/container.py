from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton, Factory
from src.services import OpenaiService, QuestionService, MoltiService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=["src.routes.question", "src.routes.molti"])

    openai_service = Singleton(OpenaiService)

    question_service = Factory(QuestionService, openai_service=openai_service)

    molti_service = Factory(MoltiService)
