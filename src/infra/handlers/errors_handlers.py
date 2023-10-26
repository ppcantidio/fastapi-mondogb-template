from fastapi import Request
from fastapi.responses import JSONResponse

from src.errors.abstract_err import AbstractErr
from src.schemas.error_response import ErrorResponse


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
