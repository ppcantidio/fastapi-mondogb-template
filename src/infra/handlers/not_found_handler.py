from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.errors.not_found_err import NotFoundError
from src.models.responses.error_response import ErrorResponse


async def not_found_handler(request: Request, not_found_err: NotFoundError):
    error = ErrorResponse(status="404", code="NOT_FOUND_ERROR", detail=not_found_err.message, title="404: Not Found")

    content = error.model_dump()

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
