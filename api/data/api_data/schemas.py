from pydantic import BaseModel, Field, ConfigDict
from typing import List


class Addition(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)  # запрет на расширение строк

    additional_info: str | None
    additional_number: int


class CreateObjectSchema(BaseModel):
    model_config = ConfigDict(strict=True)  # строгий режим типизации
    # addition: 'CreateObjectSchema.Addition' если в классе

    addition: Addition
    important_numbers: List[int]
    title: str = Field(max_length=100)
    verified: bool


class AdditionResponse(Addition):
    model_config = ConfigDict(extra='forbid', strict=True)

    id: int


class ResponseGetObjectSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int = Field(ge=0)
    addition: AdditionResponse
    important_numbers: List[int]
    title: str | None
    verified: bool
