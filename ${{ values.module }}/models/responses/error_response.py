from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status: int
    detail: str
    code: str
    title: str
