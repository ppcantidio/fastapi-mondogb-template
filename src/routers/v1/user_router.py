from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.schemas.user_schemas import CreateUserPayload, LoginPayload, LoginResponse, OneUserResponse
from src.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["user"])
service = UserService()


@router.get("/", response_model=OneUserResponse)
async def create_user(payload: CreateUserPayload):
    result = service.create_user(obj_in=payload)

    return result


@router.post("/login", response_model=LoginResponse)
async def user_login(payload: LoginPayload):
    result = service.login()

    return result
