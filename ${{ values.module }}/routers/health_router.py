from fastapi import APIRouter

from src.models.responses.health_response import HealthResponse

router = APIRouter(prefix="/health")


@router.get("/")
async def get_health():
    return HealthResponse(status=200, message="The server is running smoothly.", data=[])
