from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status_code: int
    detail: str
    code_error: str
    title: str
