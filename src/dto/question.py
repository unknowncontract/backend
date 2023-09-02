from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class QuestionType(str, Enum):
    OWNER = "owner"
    BUILDING = "building"
    CONTRACT = "contract"


class Warning(BaseModel):
    name: str
    description: str


class QuestionBody(BaseModel):
    type: QuestionType
    data: str


class QuestionRes(BaseModel):
    type: QuestionType
    score: int
    warnings: List[Warning]
