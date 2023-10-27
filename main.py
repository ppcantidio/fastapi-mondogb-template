from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.errors.bad_request_err import BadRequestError
from src.errors.forbidden_err import ForbiddenError
from src.errors.unauthorized import Unauthorized
from src.infra.handlers import errors_handlers
from src.routers.v1 import user_router


def add_routers_v1(app: FastAPI):
    app.include_router(user_router.router, prefix="/v1")


def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(exc_class_or_status_code=404, handler=errors_handlers.not_found_handler)
    app.add_exception_handler(exc_class_or_status_code=500, handler=errors_handlers.internal_server_error_handler)
    app.add_exception_handler(exc_class_or_status_code=BadRequestError, handler=errors_handlers.abstract_error_handler)
    app.add_exception_handler(exc_class_or_status_code=ForbiddenError, handler=errors_handlers.abstract_error_handler)
    app.add_exception_handler(exc_class_or_status_code=Unauthorized, handler=errors_handlers.abstract_error_handler)


def add_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app():
    app = FastAPI()
    add_routers_v1(app=app)
    add_exception_handlers(app=app)
    add_middlewares(app=app)


create_app()
