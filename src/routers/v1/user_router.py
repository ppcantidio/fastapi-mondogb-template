from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.payloads.user_payloads import CreateUser, UserLogin
from src.models.responses.user_response import UserResponse
from src.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["examples"])


@router.get("/", response_model=UserResponse)
async def create_user_example(
    payload: CreateUser,
    db: Session = Depends(get_db),
):
    result = UserService().create_example(obj_in=payload)

    return result


@router.post("/login", response_model=UserResponse)
async def user_login(payload: UserLogin):
    result = UserService().login()

    return result
