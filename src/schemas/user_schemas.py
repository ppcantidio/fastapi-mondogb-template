from abc import ABC
from datetime import datetime

from pydantic import BaseModel

from .sucess_response import SucessResponse
from .with_id_schema import WithIdSchema


class UserBase(BaseModel, ABC):
    username: str


class UserResponse(UserBase, WithIdSchema):
    pass


class OneUserResponse(SucessResponse):
    data: UserResponse


class CreateUserPayload(UserBase):
    senha: str


class TokenResponse(BaseModel):
    exp: datetime
    groups: list
    user_id: str
    token: str


class LoginResponse(SucessResponse):
    data: TokenResponse


class LoginPayload(BaseModel):
    username: str
    senha: str
