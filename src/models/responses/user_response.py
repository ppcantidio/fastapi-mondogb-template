from typing import List

from ..bases.user_base import ExampleBase
from .sucess_response import SucessResponse


class UserResponse(SucessResponse):
    data: List[ExampleBase]
