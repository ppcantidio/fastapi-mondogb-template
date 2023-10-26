from pydantic import BaseModel


class SucessResponse(BaseModel):
    status: int = 200
    message: str
