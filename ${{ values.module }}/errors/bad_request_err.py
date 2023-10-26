class BadRequestError(Exception):
    def __init__(self, message: str, code_error: str) -> None:
        self.message = message
        self.code_error = code_error

        super().__init__(message)
