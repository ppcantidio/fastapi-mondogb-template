from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.errors.abstract_err import AbstractErr
from src.errors.bad_request_err import BadRequestError
from src.errors.not_found_err import NotFoundError
from src.models.responses.error_response import ErrorResponse


async def not_found_handler(request: Request, not_found_err: NotFoundError):
    error = ErrorResponse(status="404", code="NOT_FOUND_ERROR", detail=not_found_err.message, title="404: Not Found")

    content = error.model_dump()

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)


async def bad_request_handler(request: Request, bad_request_err: BadRequestError):
    error = ErrorResponse(
        status="400", code="BAD_REQUEST_ERROR", detail=bad_request_err.message, title="400: Bad Request"
    )

    content = error.model_dump()

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)


async def abstract_error_handler(request: Request, err: AbstractErr):
    status_code = err.status_code
    titles = {
        400: "400: Bad Request",
        401: "401 Unauthorized",
        403: "403: Forbidden",
        404: "404: Not Found",
        405: "405: Method Not Allowed",
        500: "500: Internal Server Error",
    }
    title = titles.get(status_code)
    error = ErrorResponse(status_code=status_code, code_error=err.code_error, detail=err.message, title=title)

    content = error.model_dump()

    return JSONResponse(status_code=status_code, content=content)


async def internal_server_error_handler(request: Request):
    exc_class = AbstractErr(
        message="An error has ocourred, contact the suport.", code_error="INTERNAL_SERVER_ERROR", status_code=500
    )
    return await abstract_error_handler(request=request, err=exc_class)


async def not_found_handler(request: Request):
    exc_class = AbstractErr(message="Url not found.", code_error="URL_NOT_FOUND", status_code=404)
    return await abstract_error_handler(request=request, err=exc_class)
