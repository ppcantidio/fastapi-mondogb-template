from pydantic import BaseModel

from ..bases.user_base import ExampleBase


class CreateUser(ExampleBase):
    password: str


class UpdateUser(CreateUser):
    pass


class UserLogin(BaseModel):
    username: str
    password: str
