import datetime
from typing import Literal
from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class Status(BaseModel):
    status: Literal["success"]


class CreateAdvRequest(BaseModel):
    title: str
    description: str
    price: int
    author: int
    creation_date: datetime.datetime


class CreateAdvResponse(IdResponse):
    pass


class GetAdvResponse(BaseModel):
    id: int
    title: str
    description: str
    price: int
    author: int
    creation_date: datetime.datetime
    recent_changes: datetime.datetime | None = None


class UpdateAdvRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None
    author: str | None = None
    recent_changes: datetime.datetime


class UpdateAdvResponse(IdResponse):
    pass


class DeleteAdvResponse(Status):
    pass
