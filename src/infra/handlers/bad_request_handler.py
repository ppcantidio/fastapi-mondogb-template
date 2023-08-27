from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.errors.bad_request_err import BadRequestError
from src.models.responses.error_response import ErrorResponse


async def bad_request_handler(request: Request, bad_request_err: BadRequestError):
    error = ErrorResponse(
        status="400", code="BAD_REQUEST_ERROR", detail=bad_request_err.message, title="400: Bad Request"
    )

    content = error.model_dump()

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)
