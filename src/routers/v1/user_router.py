from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.payloads.user_payloads import CreateUser, UserLogin
from src.models.responses.user_response import UserResponse
from src.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["user"])
service = UserService()


@router.get("/", response_model=UserResponse)
async def create_user(payload: CreateUser):
    result = service.create_user(obj_in=payload)

    return result


@router.post("/login", response_model=UserResponse)
async def user_login(payload: UserLogin):
    result = service.login()

    return result
