from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.errors.forbidden_err import ForbiddenError
from src.models.responses.error_response import ErrorResponse


async def forbidden_error(request: Request, forbidden_err: ForbiddenError):
    error = ErrorResponse(status="403", code="FORBIDDEN_ERROR", detail=forbidden_err.message, title="403: Forbidden")

    content = error.model_dump()

    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=content)
