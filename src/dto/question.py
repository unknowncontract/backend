from pydantic import BaseModel, Field


class QuestionBody(BaseModel):
    message: str


class QuestionRes(BaseModel):
    message: str
