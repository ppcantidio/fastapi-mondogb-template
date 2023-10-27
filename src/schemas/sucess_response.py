from typing import Union

from bson import ObjectId
from pydantic import BaseModel


class Pagination(BaseModel):
    current_page: int
    next_page: Union[int, None] = None
    previous_page: Union[int, None] = None
    total_pages: int
    items_per_page: int
    total_items: int


class SucessBaseConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True

        json_encoders = {
            ObjectId: lambda obj: str(obj),  # Converte ObjectId para string
        }


class SucessResponse(SucessBaseConfig):
    detail: str
    data: list
    status_code: int


class SucessPaginationResponse(SucessBaseConfig):
    pagination: Pagination
