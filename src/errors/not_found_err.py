from .abstract_err import AbstractErr


class NotFoundError(AbstractErr):
    def __init__(self, message, code_error) -> None:
        status_code = 404
        super().__init__(message, code_error, status_code)
